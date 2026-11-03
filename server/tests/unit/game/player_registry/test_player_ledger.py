"""Unit tests for the append-only ledger part (ADR-029 §3.2; corruption_adjustment_log since step 5c)."""

from __future__ import annotations

import uuid

from server.game.player_registry import PlayerLedgerPart
from server.game.player_registry.player_ledger import ADD_CORRUPTION_ADJUSTMENT_LOG_SQL

from .fakes import FakeDatabase


async def _write(part: PlayerLedgerPart) -> list[dict[str, object]]:
    """Take the part's write and run it; the rows it inserted."""
    write = part.take_write()
    assert write is not None
    db = FakeDatabase()
    async with db.session() as session:
        await write(session)
    return [dict(params) for params in db.executed if params is not None]


def test_a_logged_row_dirties_the_part_and_sync_is_the_callers_choice() -> None:
    lazy, eager = PlayerLedgerPart(uuid.uuid4()), PlayerLedgerPart(uuid.uuid4())

    lazy.log(2, "room_flux", "{}", None)
    eager.log(5, "spell_cast", "{}", "room-1", sync=True)

    assert lazy.dirty and not lazy.sync_required
    assert eager.dirty and eager.sync_required


async def test_the_write_inserts_every_queued_row_in_order() -> None:
    player_id = uuid.uuid4()
    part = PlayerLedgerPart(player_id)
    part.log(5, "spell_cast", '{"spell_id": "x"}', "room-1")
    part.log(-8, "ritual_cleanse", "{}", None)

    rows = await _write(part)

    assert [(row["delta"], row["reason_code"], row["location_id"]) for row in rows] == [
        (5, "spell_cast", "room-1"),
        (-8, "ritual_cleanse", None),
    ]
    assert {row["player_id"] for row in rows} == {str(player_id)}
    assert not part.dirty and part.take_write() is None  # nothing left queued
    assert "add_corruption_adjustment_log" in str(ADD_CORRUPTION_ADJUSTMENT_LOG_SQL)


def test_rollback_drops_the_rows_the_unit_queued() -> None:
    part = PlayerLedgerPart(uuid.uuid4())
    part.log(1, "earlier", "{}", None)
    part.begin()
    part.log(5, "spell_cast", "{}", None)
    part.rollback()

    write = part.take_write()
    assert write is not None  # the earlier row is still queued
    assert part.take_write() is None


async def test_a_failed_lazy_flush_puts_its_rows_back_ahead_of_newer_ones() -> None:
    part = PlayerLedgerPart(uuid.uuid4())
    part.log(1, "first", "{}", None)
    assert part.take_write() is not None  # captured; its flush fails below
    part.log(2, "second", "{}", None)

    part.write_failed()

    assert part.dirty
    assert [row["reason_code"] for row in await _write(part)] == ["first", "second"]
