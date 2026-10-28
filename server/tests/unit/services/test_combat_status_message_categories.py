"""
Semantic message categories on combat and status emitters (slice B).

Each test drives the real payload builder and asserts on the ``category`` that reaches the wire. The
perspective rule: a category describes the line from the recipient's point of view.
"""

# pyright: reportPrivateUsage=false
# Reason: the phantom parity test drives CombatEventHandler._publish_attack_events, which has no public wrapper.

import ast
import uuid
from collections.abc import Awaitable
from pathlib import Path
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.constants.message_category import MessageCategory
from server.events.combat_events import (
    CombatEndedEvent,
    NPCAttackedEvent,
    NPCTookDamageEvent,
    PlayerAttackedEvent,
)
from server.models.combat import CombatParticipant, CombatParticipantType
from server.realtime.event_handlers import EventHandler
from server.services.combat_event_handler import CombatEventHandler
from server.services.combat_event_publisher import CombatEventPublisher
from server.services.combat_messaging import CombatMessagingIntegration
from server.services.lucidity_event_dispatcher import (
    send_catatonia_event,
    send_lucidity_change_event,
    send_rescue_update_event,
)


def _first_awaited_args(mock: AsyncMock, call: int = 0) -> tuple[object, ...]:
    """Positional args of the nth await of an AsyncMock (fails the test if it was never awaited)."""
    assert mock.await_args_list, "expected the mock to have been awaited"
    return cast(tuple[object, ...], mock.await_args_list[call].args)


def _data(event: object) -> dict[str, object]:
    """The ``data`` payload of a built event envelope."""
    return cast(dict[str, object], cast(dict[str, object], event)["data"])


@pytest.fixture(name="connection_manager")
def connection_manager_fixture() -> MagicMock:
    """Connection manager double: the transport boundary only."""
    manager = MagicMock()
    manager.broadcast_to_room = AsyncMock(return_value={"successful_deliveries": 1, "failed_deliveries": 0})
    manager.send_personal_message = AsyncMock(return_value={"success": True})
    return manager


@pytest.fixture(name="integration")
def integration_fixture(connection_manager: MagicMock) -> CombatMessagingIntegration:
    return CombatMessagingIntegration(connection_manager=connection_manager)


def _sent_personal(connection_manager: MagicMock) -> dict[str, object]:
    return _data(_first_awaited_args(cast(AsyncMock, connection_manager.send_personal_message))[1])


def _sent_room(connection_manager: MagicMock) -> dict[str, object]:
    return _data(_first_awaited_args(cast(AsyncMock, connection_manager.broadcast_to_room))[1])


# --- combat_broadcasts / player_broadcasts ---------------------------------------------------------------


@pytest.mark.asyncio
async def test_combat_attack_categories_follow_each_recipients_perspective(
    integration: CombatMessagingIntegration, connection_manager: MagicMock
) -> None:
    """The attacker deals a hit; the defender is hurt; a bystander observes a hit."""
    _ = await integration.broadcast_combat_attack("r1", "Alice", "Ghoul", 4, "punch", "c1", "alice-id")

    personal = _sent_personal(connection_manager)
    assert personal["category"] == MessageCategory.COMBAT_HIT
    room = _sent_room(connection_manager)
    assert room["categories"] == {
        "attack_attacker": MessageCategory.COMBAT_HIT,
        "attack_defender": MessageCategory.COMBAT_HURT,
        "attack_other": MessageCategory.COMBAT_HIT,
    }
    # One category per perspective line, so the client can tag whichever line it renders.
    assert set(cast(dict[str, str], room["categories"])) == set(cast(dict[str, str], room["messages"]))


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("send", "expected"),
    [
        ("broadcast_combat_target_switch", MessageCategory.COMBAT_STATUS),
        ("broadcast_npc_disengage", MessageCategory.COMBAT_STATUS),
        ("broadcast_player_joined_combat", MessageCategory.COMBAT_STATUS),
        ("broadcast_taunt_result", MessageCategory.COMBAT_STATUS),
        ("broadcast_protect_result", MessageCategory.COMBAT_STATUS),
    ],
)
async def test_combat_state_notices_are_combat_status(
    integration: CombatMessagingIntegration,
    connection_manager: MagicMock,
    send: str,
    expected: MessageCategory,
) -> None:
    calls = {
        "broadcast_combat_target_switch": lambda: integration.broadcast_combat_target_switch(
            "r1", "c1", "Ghoul", "Bob"
        ),
        "broadcast_npc_disengage": lambda: integration.broadcast_npc_disengage("r1", "c1", "Ghoul", "withdraws."),
        "broadcast_player_joined_combat": lambda: integration.broadcast_player_joined_combat(
            "r1", "c1", "Bob", "Ghoul", "bob-id"
        ),
        "broadcast_taunt_result": lambda: integration.broadcast_taunt_result("r1", "c1", "Bob taunts the Ghoul."),
        "broadcast_protect_result": lambda: integration.broadcast_protect_result("r1", "c1", "Bob shields Alice."),
    }
    _ = await calls[send]()

    room = _sent_room(connection_manager)
    assert room["category"] == expected
    assert room["message"]  # the original payload fields survive the tagging


@pytest.mark.asyncio
async def test_mortally_wounded_lines_are_combat_status_for_both_recipients(
    integration: CombatMessagingIntegration, connection_manager: MagicMock
) -> None:
    _ = await integration.broadcast_player_mortally_wounded("p1", "Bob", "Ghoul", "r1")

    assert _sent_personal(connection_manager)["category"] == MessageCategory.COMBAT_STATUS
    assert _sent_room(connection_manager)["category"] == MessageCategory.COMBAT_STATUS


@pytest.mark.asyncio
async def test_player_death_lines_are_combat_death_for_both_recipients(
    integration: CombatMessagingIntegration, connection_manager: MagicMock
) -> None:
    _ = await integration.broadcast_player_death("p1", "Bob", "r1", "Dockside")

    assert _sent_personal(connection_manager)["category"] == MessageCategory.COMBAT_DEATH
    assert _sent_room(connection_manager)["category"] == MessageCategory.COMBAT_DEATH


@pytest.mark.asyncio
async def test_dp_decay_is_status_health(
    integration: CombatMessagingIntegration, connection_manager: MagicMock
) -> None:
    _ = await integration.send_dp_decay_message("p1", -3)

    assert _sent_personal(connection_manager)["category"] == MessageCategory.STATUS_HEALTH


@pytest.mark.asyncio
async def test_npc_death_line_is_combat_death() -> None:
    manager = MagicMock()
    manager.broadcast_room_event = AsyncMock()
    manager.event_bus = MagicMock()
    manager.refresh_room_occupants = AsyncMock()

    await EventHandler(connection_manager=manager).handle_npc_died_event(
        {"room_id": "r1", "npc_id": "npc-1", "npc_name": "Shoggoth"}
    )

    payload = cast(dict[str, object], _first_awaited_args(cast(AsyncMock, manager.broadcast_room_event))[2])
    assert payload["message"] == "The Shoggoth has been slain."
    assert payload["category"] == MessageCategory.COMBAT_DEATH


# --- combat_event_publisher (structured events) ----------------------------------------------------------


@pytest.fixture(name="nats")
def nats_fixture() -> MagicMock:
    service = MagicMock()
    service.is_connected = MagicMock(return_value=True)
    service.publish = AsyncMock(return_value=True)
    return service


@pytest.fixture(name="publisher")
def publisher_fixture(nats: MagicMock) -> CombatEventPublisher:
    subjects = MagicMock()
    subjects.build_subject = MagicMock(return_value="combat.subject")
    return CombatEventPublisher(nats, subjects)


def _published_data(nats: MagicMock) -> dict[str, object]:
    message = cast(dict[str, object], _first_awaited_args(cast(AsyncMock, nats.publish))[1])
    return cast(dict[str, object], message["event_data"])


@pytest.mark.asyncio
async def test_player_attacked_is_combat_hurt(publisher: CombatEventPublisher, nats: MagicMock) -> None:
    """The client words this event as 'X attacks you': the recipient is the one taking damage."""
    event = PlayerAttackedEvent(
        combat_id=uuid.uuid4(),
        room_id="r1",
        attacker_id=uuid.uuid4(),
        attacker_name="Ghoul",
        target_id=uuid.uuid4(),
        target_name="Bob",
        damage=3,
        action_type="auto_attack",
        target_current_dp=7,
        target_max_dp=10,
    )
    assert await publisher.publish_player_attacked(event)
    assert _published_data(nats)["category"] == MessageCategory.COMBAT_HURT


@pytest.mark.asyncio
async def test_npc_attacked_and_took_damage_are_combat_hit(publisher: CombatEventPublisher, nats: MagicMock) -> None:
    """The client words these as 'You attack X' / 'Dealt N damage to X': the recipient deals damage."""
    attacked = NPCAttackedEvent(
        combat_id=uuid.uuid4(),
        room_id="r1",
        attacker_id=uuid.uuid4(),
        attacker_name="Bob",
        npc_id=uuid.uuid4(),
        npc_name="Ghoul",
        damage=3,
        action_type="auto_attack",
        target_current_dp=7,
        target_max_dp=10,
    )
    assert await publisher.publish_npc_attacked(attacked)
    assert _published_data(nats)["category"] == MessageCategory.COMBAT_HIT

    took_damage = NPCTookDamageEvent(
        combat_id=uuid.uuid4(), room_id="r1", npc_id=uuid.uuid4(), npc_name="Ghoul", damage=3, current_dp=7, max_dp=10
    )
    assert await publisher.publish_npc_took_damage(took_damage)
    assert _published_data(nats)["category"] == MessageCategory.COMBAT_HIT


@pytest.mark.asyncio
async def test_combat_ended_is_combat_status(publisher: CombatEventPublisher, nats: MagicMock) -> None:
    event = CombatEndedEvent(
        combat_id=uuid.uuid4(), room_id="r1", reason="victory", duration_seconds=5, participants={}
    )
    assert await publisher.publish_combat_ended(event)
    assert _published_data(nats)["category"] == MessageCategory.COMBAT_STATUS


# --- phantom hostiles (#625 / ADR-024) -------------------------------------------------------------------


def _participant(kind: CombatParticipantType, name: str) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(), participant_type=kind, name=name, current_dp=10, max_dp=10, dexterity=10
    )


@pytest.mark.asyncio
async def test_phantom_combat_line_matches_real_npc_category_and_never_mints_its_own() -> None:
    """
    A real aggressive NPC's hit on a player is published tagged COMBAT_HURT through the shared publisher.

    A phantom's hit goes through the same CombatEventHandler but publishes nothing room-visible (#625), so
    there is no second code path that could choose a different category for it.
    """
    publish_player_attacked = AsyncMock(return_value=True)
    publisher = MagicMock(
        publish_player_attacked=publish_player_attacked,
        publish_npc_attacked=AsyncMock(return_value=True),
        publish_npc_took_damage=AsyncMock(return_value=True),
    )
    service = MagicMock()
    service._combat_event_publisher = publisher
    handler = CombatEventHandler(service)
    combat = MagicMock(combat_id=uuid.uuid4(), room_id="r1")
    player = _participant(CombatParticipantType.PLAYER, "Bob")

    await handler._publish_attack_events(_participant(CombatParticipantType.PHANTOM, "Ghoul"), player, 3, combat)
    publish_player_attacked.assert_not_awaited()

    await handler._publish_attack_events(_participant(CombatParticipantType.NPC, "Ghoul"), player, 3, combat)
    publish_player_attacked.assert_awaited_once()

    # Drive the real publisher with exactly the event the handler built for the real NPC.
    built = cast(PlayerAttackedEvent, _first_awaited_args(publish_player_attacked)[0])
    nats = MagicMock()
    nats.is_connected = MagicMock(return_value=True)
    nats.publish = AsyncMock(return_value=True)
    real = CombatEventPublisher(nats, MagicMock(build_subject=MagicMock(return_value="s")))
    assert await real.publish_player_attacked(built)
    assert _published_data(nats)["category"] == MessageCategory.COMBAT_HURT


def test_phantom_hostile_service_does_not_import_message_category() -> None:
    """ADR-024: hallucination code never chooses a category."""
    import server.services.phantom_hostile_service as phantom_module

    tree = ast.parse(Path(phantom_module.__file__ or "").read_text(encoding="utf-8"))
    imported = {
        alias.name for node in ast.walk(tree) if isinstance(node, ast.ImportFrom | ast.Import) for alias in node.names
    } | {node.module or "" for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    assert "MessageCategory" not in imported
    assert not any("message_category" in name for name in imported)


# --- lucidity / rescue dispatcher ------------------------------------------------------------------------


async def _dispatched(dispatch: Awaitable[None]) -> dict[str, object]:
    """Await the dispatcher coroutine with the transport patched; return the payload it sent."""
    send = AsyncMock()
    with patch("server.realtime.connection_manager_api.send_game_event", send):
        await dispatch
    return cast(dict[str, object], _first_awaited_args(send)[2])


@pytest.mark.asyncio
async def test_lucidity_change_is_status_lucidity() -> None:
    payload = await _dispatched(send_lucidity_change_event(uuid.uuid4(), current_lcd=40, delta=-5, tier="uneasy"))
    assert payload["category"] == MessageCategory.STATUS_LUCIDITY


@pytest.mark.asyncio
async def test_catatonia_is_status_lucidity() -> None:
    payload = await _dispatched(send_catatonia_event(uuid.uuid4(), message="Your mind goes dark."))
    assert payload["category"] == MessageCategory.STATUS_LUCIDITY


@pytest.mark.asyncio
async def test_rescue_update_is_status_rescue() -> None:
    payload = await _dispatched(send_rescue_update_event(uuid.uuid4(), status="channeling", message="Hold on."))
    assert payload["category"] == MessageCategory.STATUS_RESCUE
