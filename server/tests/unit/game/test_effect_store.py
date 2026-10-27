"""Unit tests for the content effect dict <-> player_effects row mapping (ADR-029 step 3b-i)."""

from __future__ import annotations

import uuid
from collections.abc import Iterator

import pytest

from server.game import effect_store
from server.models.player_effect import PlayerEffect
from server.persistence.repositories.player_effect_repository import AddEffectInput


class FakeRepository:
    """Records add_effect inputs and instance-scoped clears instead of reaching the database."""

    added: list[tuple[uuid.UUID, AddEffectInput]] = []
    cleared: list[uuid.UUID] = []

    async def add_effect(self, player_id: uuid.UUID, effect: AddEffectInput) -> str:
        self.added.append((player_id, effect))
        return "effect-1"

    async def delete_instance_scoped_effects(self, player_id: uuid.UUID) -> int:
        self.cleared.append(player_id)
        return 3


@pytest.fixture(autouse=True)
def _fake_repository(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    FakeRepository.added = []
    FakeRepository.cleared = []
    monkeypatch.setattr(effect_store, "PlayerEffectRepository", FakeRepository)
    yield None


@pytest.mark.asyncio
async def test_a_timed_effect_stores_its_duration_as_remaining_seconds() -> None:
    pid = uuid.uuid4()
    effect: dict[str, object] = {"type": "heal_over_time", "healing": 5, "duration": 15}

    assert await effect_store.add_content_effect(pid, effect) == "effect-1"

    [(player_id, stored)] = FakeRepository.added
    assert player_id == pid
    assert (stored["effect_type"], stored["category"], stored.get("remaining_seconds")) == (
        "heal_over_time",
        "scripted",
        15,
    )
    assert stored.get("payload") == {"healing": 5, "duration": 15}
    assert stored.get("instance_scoped") is False


@pytest.mark.asyncio
async def test_an_untimed_instance_scoped_effect_lasts_until_removed() -> None:
    effect: dict[str, object] = {"type": "lucidity_drain_over_time", "rate": 1, "instance_scoped": True}

    _ = await effect_store.add_content_effect(uuid.uuid4(), effect)

    [(_pid, stored)] = FakeRepository.added
    assert stored.get("remaining_seconds") is None
    assert stored.get("instance_scoped") is True
    assert stored.get("payload") == {"rate": 1}


def test_a_stored_effect_reads_back_as_the_dict_content_wrote() -> None:
    effect: dict[str, object] = {"type": "lucidity_drain_over_time", "rate": 1, "instance_scoped": True}
    row = PlayerEffect(
        effect_type="lucidity_drain_over_time",
        payload=effect_store.effect_payload(effect),
        instance_scoped=True,
    )

    assert effect_store.effect_dict(row) == effect


@pytest.mark.asyncio
async def test_clearing_instance_scoped_effects_returns_the_count() -> None:
    pid = uuid.uuid4()

    assert await effect_store.clear_instance_scoped_effects(pid) == 3
    assert FakeRepository.cleared == [pid]
