"""
Invariant: every server event that puts player-visible text on the client carries a valid semantic category.

``INVENTORY`` lists each text-bearing emitter. A driver runs the real builder or emitter (only the connection
manager, NATS transport and WebSocket are stubbed) and returns the events it produced. The tests then assert,
for every emitter, that each event carrying text also carries ``data.category`` set to a ``MessageCategory``.

A second test cross-checks the inventory against the client projector: every event type whose handler appends
text to the log must be covered here (or be on the explicit client-authored list), so a new emitter cannot
reach players without a category and without this file noticing.

Categories are assigned in shared builders only; see ``server/constants/message_category.py``.
"""

# pyright: reportPrivateUsage=false
# Reason: the chat, room-message and set-stat builders are exercised through their underscore-prefixed helpers,
# which have no public wrapper that avoids the full NATS / FastAPI stack.

from __future__ import annotations

import asyncio
import re
import uuid
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
from typing import cast, override
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocket

from server.api.game import broadcast_message
from server.commands.admin_setstat_command import _maybe_attach_dp_posture_message
from server.commands.admin_setstat_support import SetStatConnectionManager, SetStatTargetPlayer
from server.commands.admin_shutdown_command import _broadcast_shutdown_cancellation, broadcast_shutdown_notification
from server.commands.admin_teleport_utils import broadcast_teleport_effects, notify_player_of_teleport
from server.commands.rest_countdown_task import create_rest_countdown_task
from server.constants.message_category import MessageCategory
from server.constants.message_segments import npc_name_segment
from server.constants.npc_disposition import NpcDisposition, NpcOccupant
from server.events.combat_events import (
    CombatEndedEvent,
    NPCAttackedEvent,
    NPCTookDamageEvent,
    PlayerAttackedEvent,
)
from server.events.event_types import (
    PlayerDeliriumRespawnedEvent,
    PlayerEnteredRoom,
    PlayerLeftRoom,
    PlayerRespawnedEvent,
)
from server.models.user import User
from server.realtime.connection_manager import ConnectionManager
from server.realtime.event_handlers import EventHandler
from server.realtime.message_builders import MessageBuilder
from server.realtime.message_formatters import format_message_content
from server.realtime.nats_message_handler import NATSMessageHandler
from server.realtime.npc_event_handlers import NPCEventHandler
from server.realtime.player_event_handlers_respawn import PlayerRespawnEventHandler
from server.realtime.player_event_handlers_utils import PlayerEventHandlerUtils
from server.realtime.posture_notify import emit_posture_change
from server.realtime.websocket_handler import send_system_message
from server.realtime.websocket_handler_commands import handle_game_command
from server.services.combat_event_publisher import CombatEventPublisher
from server.services.combat_messaging import CombatMessagingIntegration
from server.services.lucidity_event_dispatcher import send_rescue_update_event
from server.services.nats_service import NATSService
from server.services.nats_subject_manager import NATSSubjectManager

Emitted = tuple[str, dict[str, object]]
Driver = Callable[[], Awaitable[list[Emitted]]]

_REPO_ROOT = Path(__file__).resolve().parents[4]
_PROJECTOR_DIR = _REPO_ROOT / "client" / "src" / "components" / "ui-v2" / "eventLog"
_VALID_CATEGORIES = frozenset(member.value for member in MessageCategory)

PLAYER_ID = uuid.UUID("11111111-1111-1111-1111-111111111111")
ROOM_ID = "room_001"

# Payload keys whose value is text the client appends to the log.
_TEXT_KEYS = ("message", "posture_message", "result", "reason", "messages")

# Handlers the client builds with a fixed category of its own, not from a server payload (the projector
# reads no data.category for these). They are the only text events allowed to lack a server emitter below.
CLIENT_AUTHORED_EVENT_TYPES = frozenset(
    {"client_message", "mythos_time_update", "game_tick", "player_entered_game", "player_left_game"}
)

# Lower-case spellings the client also accepts; they alias an event type that is in the inventory.
CLIENT_ALIASES = {
    "playerrespawned": "player_respawned",
    "playerdeliriumrespawned": "player_delirium_respawned",
    "playerdpupdated": "player_dp_updated",
    "combat_death": "npc_died",  # no server emitter sends this name; NPC deaths arrive as npc_died
}


def _as[T](_kind: type[T], fake: object) -> T:
    """View a test double as the production type the emitter is annotated with."""
    return cast(T, fake)


class _Transport:
    """Stands in for the connection manager, WebSocket and NATS: records every event it is handed."""

    def __init__(self) -> None:
        self.events: list[Emitted] = []
        self.sequence_counter: int = 0
        self.resting_players: dict[uuid.UUID, object] = {}
        self.player_websockets: dict[uuid.UUID, object] = {PLAYER_ID: object()}
        self.room_manager: _Transport = self
        self.event_bus: MagicMock = MagicMock()

    def _record(self, event: Mapping[str, object]) -> None:
        self.events.append((str(event["event_type"]), cast(dict[str, object], event["data"])))

    async def send_personal_message(self, _player_id: uuid.UUID | str, event: Mapping[str, object]) -> dict[str, int]:
        self._record(event)
        return {"success": 1, "websocket_delivered": 1, "active_connections": 1}

    async def send_json(self, event: Mapping[str, object]) -> None:
        self._record(event)

    async def broadcast_to_room(
        self, _room_id: str, event: Mapping[str, object], exclude_player: object = None
    ) -> dict[str, int]:
        _ = exclude_player  # the emitters pass it by keyword, so the name must stay
        self._record(event)
        return {"successful_deliveries": 1, "failed_deliveries": 0}

    async def broadcast_room_event(
        self, event_type: str, _room_id: str, data: dict[str, object], *_args: object
    ) -> dict[str, int]:
        self.events.append((event_type, data))
        return {"successful_deliveries": 1}

    async def broadcast_global_event(self, event_type: str, data: dict[str, object]) -> dict[str, int]:
        self.events.append((event_type, data))
        return {"successful_deliveries": 1}

    async def refresh_room_occupants(self, *_args: object, **_kwargs: object) -> None:
        return None

    async def get_room_subscribers(self, _room_id: str) -> list[str]:
        return [str(PLAYER_ID)]

    async def get_player(self, _player_id: uuid.UUID | str) -> object:
        return _StatsPlayer()

    def get_online_player_by_display_name(self, _name: str) -> dict[str, object]:
        return {"player_id": PLAYER_ID}


class _StatsPlayer:
    """A standing player in the test room; posture drivers drop DP to lying."""

    name: str = "Ada"
    current_room_id: str = ROOM_ID
    player_id: uuid.UUID = PLAYER_ID

    def get_stats(self) -> dict[str, object]:
        return {"position": "standing", "current_dp": 5, "max_dp": 10}

    def set_stats(self, stats: dict[str, object]) -> None:
        _ = stats

    def apply_dp_change(self, new_dp: int) -> tuple[int, bool, bool]:
        return new_dp, False, False


# --- drivers --------------------------------------------------------------------------------------------


async def _drive_command_chokepoint() -> list[Emitted]:
    """handle_game_command: the single chokepoint every command handler's result passes through."""
    transport = _Transport()
    with patch(
        "server.realtime.websocket_handler_commands.process_websocket_command",
        AsyncMock(return_value={"result": "You wave."}),
    ):
        await handle_game_command(
            _as(WebSocket, transport), str(PLAYER_ID), "wave", None, _as(ConnectionManager, transport)
        )
    return transport.events


async def _drive_direct_command_response() -> list[Emitted]:
    """send_game_event: follow / party / spell / catch-up notices that bypass the command chokepoint."""
    transport = _Transport()
    with patch("server.realtime.connection_manager_api._require_manager", return_value=transport):
        from server.realtime.connection_manager_api import send_game_event

        await send_game_event(PLAYER_ID, "command_response", {"result": "You begin to follow Armitage."})
    return transport.events


async def _drive_rest_countdown() -> list[Emitted]:
    """The /rest countdown lines, then the intentional_disconnect notice."""
    transport = _Transport()
    transport.resting_players[PLAYER_ID] = object()
    disconnect = AsyncMock()
    with (
        patch("server.commands.rest_countdown_task.rest_countdown_seconds", return_value=1),
        patch("server.commands.rest_countdown_task.sleep", AsyncMock()),
    ):
        task = create_rest_countdown_task(PLAYER_ID, "Ada", transport, MagicMock(), disconnect)
        await task
    return transport.events


def _chat_driver(channel: str) -> Driver:
    async def drive() -> list[Emitted]:
        handler = NATSMessageHandler(connection_manager=_as(ConnectionManager, _Transport()))
        payload: dict[str, object] = {
            "channel": channel,
            "room_id": ROOM_ID,
            "sender_id": str(uuid.uuid4()),
            "sender_name": "Morgan",
            "content": "Hello",
            "message_id": "msg_001",
            "timestamp": "2024-01-01T00:00:00Z",
        }
        fields = handler._extract_chat_message_fields(payload)
        validated = handler._validate_chat_message_fields(fields, payload)
        event = handler._build_chat_event(validated, "formatted")
        return [("chat_message", cast(dict[str, object], event["data"]))]

    return drive


async def _drive_chat_segments() -> list[Emitted]:
    """#1036: an NPC speaker's name and a narration line's inner spans, built the way the NATS handler builds them."""
    handler = NATSMessageHandler(connection_manager=_as(ConnectionManager, _Transport()))
    events: list[Emitted] = []
    for extra in (
        {"speaker_kind": "npc", "speaker_disposition": "aggressive_mob"},
        {
            "channel": "system",
            "content": "A Shadow materializes",
            "content_segments": [
                {"text": "A "},
                {"text": "Shadow", "category": "npc.aggressive_mob"},
                {"text": " materializes"},
            ],
        },
    ):
        payload: dict[str, object] = {
            "channel": "say",
            "room_id": ROOM_ID,
            "sender_id": str(uuid.uuid4()),
            "sender_name": "Ghoul",
            "content": "Hello",
            "message_id": "msg_001",
            "timestamp": "2024-01-01T00:00:00Z",
            **extra,
        }
        validated = handler._validate_chat_message_fields(handler._extract_chat_message_fields(payload), payload)
        formatted = format_message_content(validated["channel"], validated["sender_name"], validated["content"])
        events.append(
            ("chat_message", cast(dict[str, object], handler._build_chat_event(validated, formatted)["data"]))
        )
    return events


async def _drive_npc_room_messages() -> list[Emitted]:
    transport = _Transport()

    class _Registry:
        def register_task(self, coro: object, _name: str, _task_type: str) -> None:
            _ = asyncio.ensure_future(cast("asyncio.Future[None]", coro))

    handler = NPCEventHandler(
        connection_manager=transport,
        task_registry=_Registry(),
        message_builder=MessageBuilder(lambda: 1),
        send_occupants_update=None,
    )
    await handler._send_room_message(ROOM_ID, "Rat left north.", message_type="system")
    await handler._send_room_message(ROOM_ID, "A rat scurries in.")
    # #1025: the same movement line with the NPC's name as a styled segment.
    await handler._send_room_line(
        ROOM_ID,
        handler.message_builder.create_npc_movement_parts(
            npc_name_segment("Rat", NpcDisposition.AGGRESSIVE_MOB), "north", "left"
        ),
        message_type="system",
    )
    await asyncio.sleep(0)
    return transport.events


async def _drive_player_enter_leave() -> list[Emitted]:
    builder = MessageBuilder(lambda: 1)
    entered = builder.create_player_entered_message(PlayerEnteredRoom(player_id="p1", room_id="room_a"), "Armitage")
    left = builder.create_player_left_message(PlayerLeftRoom(player_id="p1", room_id="room_a"), "Ward")
    return [("player_entered", entered["data"]), ("player_left", left["data"])]


async def _drive_system_events() -> list[Emitted]:
    transport = _Transport()
    for message_type in ("info", "warning", "error"):
        await send_system_message(_as(WebSocket, transport), "Hello", message_type)
    await broadcast_teleport_effects(transport, "Alice", "room-a", "room-b", "teleport")
    await notify_player_of_teleport(transport, "Bob", "Admin", "teleported_to")
    return transport.events


async def _drive_posture() -> list[Emitted]:
    """Posture change: room line (player_posture_change) and the personal self-line (player_update)."""
    transport = _Transport()
    _ = await emit_posture_change(
        transport,
        player_id=PLAYER_ID,
        display_name="Ada",
        room_id=ROOM_ID,
        previous_position="standing",
        new_position="sitting",
    )
    return transport.events


async def _drive_setstat_posture() -> list[Emitted]:
    transport = _Transport()
    payload: dict[str, object] = {"player_id": str(PLAYER_ID)}
    await _maybe_attach_dp_posture_message(
        cast(SetStatConnectionManager, cast(object, transport)),
        cast(SetStatTargetPlayer, cast(object, _StatsPlayer())),
        PLAYER_ID,
        payload,
        stat_key="current_dp",
        previous_position="standing",
        updated_stats={"position": "lying"},
    )
    return [("player_update", payload)]


class _OfflineRespawnHandler(PlayerRespawnEventHandler):
    """The real respawn event builders, with the database and room lookups replaced by canned data."""

    sent: list[Emitted]

    def __init__(self) -> None:
        super().__init__(None, _as(PlayerEventHandlerUtils, MagicMock()), MagicMock())
        self.sent = []

    @override
    async def _resolve_player_data_for_respawn_event(
        self, player_id_str: str, player_id_uuid: uuid.UUID, event: PlayerRespawnedEvent
    ) -> None:
        return None

    @override
    async def get_player_data_for_delirium_respawn(self, player_id_str: str, default_lucidity: int) -> tuple[None, str]:
        return None, "standing"

    @override
    async def _prepare_room_data_for_respawn(
        self, room_id: str, respawned_player_name: str
    ) -> tuple[None, list[NpcOccupant], list[str], list[str]]:
        return None, [], [], []

    @override
    async def send_respawn_event_with_retry(
        self, player_id_uuid: uuid.UUID, respawn_event: dict[str, object], max_wait_time: float = 2.0
    ) -> None:
        self.sent.append((str(respawn_event["event_type"]), cast(dict[str, object], respawn_event["data"])))

    @override
    async def _send_room_occupants_after_respawn(
        self,
        player_id_str: str,
        player_id_uuid: uuid.UUID,
        respawn_room_id: str,
        room_data: dict[str, object] | None,
        occupant_names: list[str],
    ) -> None:
        return None

    @override
    async def _emit_respawn_room_posture(self, *, player_id: uuid.UUID, player_name: str, room_id: str | None) -> None:
        return None


async def _drive_respawn() -> list[Emitted]:
    handler = _OfflineRespawnHandler()
    await handler.handle_player_respawned(
        PlayerRespawnedEvent(player_id=PLAYER_ID, player_name="Ada", respawn_room_id=ROOM_ID, old_dp=-10, new_dp=10)
    )
    await handler.handle_player_delirium_respawned(
        PlayerDeliriumRespawnedEvent(
            player_id=PLAYER_ID, player_name="Ada", respawn_room_id=ROOM_ID, old_lucidity=0, new_lucidity=20
        )
    )
    return handler.sent


async def _drive_combat_messaging() -> list[Emitted]:
    transport = _Transport()
    integration = CombatMessagingIntegration(connection_manager=transport)
    _ = await integration.broadcast_combat_attack(ROOM_ID, "Alice", "Ghoul", 4, "punch", "c1", "alice-id")
    _ = await integration.broadcast_combat_target_switch(ROOM_ID, "c1", "Ghoul", "Bob")
    _ = await integration.broadcast_npc_disengage(ROOM_ID, "c1", "Ghoul", "withdraws.")
    _ = await integration.broadcast_player_joined_combat(ROOM_ID, "c1", "Bob", "Ghoul", "bob-id")
    _ = await integration.broadcast_taunt_result(ROOM_ID, "c1", "Bob taunts the Ghoul.")
    _ = await integration.broadcast_protect_result(ROOM_ID, "c1", "Bob shields Alice.")
    return transport.events


async def _drive_dp_decay() -> list[Emitted]:
    """Bleed-out: one 'Your lifeforce ebbs away' line per second while mortally wounded (#1059)."""
    transport = _Transport()
    integration = CombatMessagingIntegration(connection_manager=transport)
    _ = await integration.send_dp_decay_message(str(PLAYER_ID), -3)
    return transport.events


async def _drive_mortally_wounded() -> list[Emitted]:
    """Defeat: the personal collapse line and the room's 'verge of death' line (#1057)."""
    transport = _Transport()
    integration = CombatMessagingIntegration(connection_manager=transport)
    _ = await integration.broadcast_player_mortally_wounded(str(PLAYER_ID), "Ada", "Ghoul", ROOM_ID)
    return transport.events


async def _drive_npc_died() -> list[Emitted]:
    transport = _Transport()
    await EventHandler(connection_manager=_as(ConnectionManager, transport)).handle_npc_died_event(
        {"room_id": ROOM_ID, "npc_id": "npc-1", "npc_name": "Shoggoth"}
    )
    # #1025: the publisher tells us the NPC's disposition, so the name becomes a styled segment.
    await EventHandler(connection_manager=_as(ConnectionManager, transport)).handle_npc_died_event(
        {"room_id": ROOM_ID, "npc_id": "npc-2", "npc_name": "Shoggoth", "npc_disposition": "aggressive_mob"}
    )
    return transport.events


async def _drive_combat_publisher() -> list[Emitted]:
    """The structured combat events, as published to NATS before the connection manager fans them out."""
    published: list[dict[str, object]] = []

    class _Nats:
        def is_connected(self) -> bool:
            return True

        async def publish(self, _subject: str, message: dict[str, object]) -> bool:
            published.append(message)
            return True

    class _Subjects:
        def build_subject(self, *_args: object, **_kwargs: object) -> str:
            return "combat.subject"

    publisher = CombatEventPublisher(_as(NATSService, _Nats()), _as(NATSSubjectManager, _Subjects()))
    combat_id, attacker, target = uuid.uuid4(), uuid.uuid4(), uuid.uuid4()
    assert await publisher.publish_player_attacked(
        PlayerAttackedEvent(
            combat_id=combat_id,
            room_id=ROOM_ID,
            attacker_id=attacker,
            attacker_name="Ghoul",
            target_id=target,
            target_name="Bob",
            damage=3,
            action_type="auto_attack",
            target_current_dp=7,
            target_max_dp=10,
        )
    )
    assert await publisher.publish_npc_attacked(
        NPCAttackedEvent(
            combat_id=combat_id,
            room_id=ROOM_ID,
            attacker_id=target,
            attacker_name="Bob",
            npc_id=attacker,
            npc_name="Ghoul",
            damage=3,
            action_type="auto_attack",
            target_current_dp=7,
            target_max_dp=10,
        )
    )
    assert await publisher.publish_npc_took_damage(
        NPCTookDamageEvent(
            combat_id=combat_id, room_id=ROOM_ID, npc_id=attacker, npc_name="Ghoul", damage=3, current_dp=7, max_dp=10
        )
    )
    assert await publisher.publish_combat_ended(
        CombatEndedEvent(combat_id=combat_id, room_id=ROOM_ID, reason="victory", duration_seconds=5, participants={})
    )
    names = ["player_attacked", "npc_attacked", "npc_took_damage", "combat_ended"]
    return [
        (name, cast(dict[str, object], message["event_data"])) for name, message in zip(names, published, strict=True)
    ]


async def _drive_rescue_update() -> list[Emitted]:
    send = AsyncMock()
    with patch("server.realtime.connection_manager_api.send_game_event", send):
        await send_rescue_update_event(PLAYER_ID, status="channeling", message="Hold on.")
    return [("rescue_update", cast(dict[str, object], send.await_args_list[0].args[2]))]


async def _drive_admin_broadcasts() -> list[Emitted]:
    """Shutdown countdown, shutdown cancellation and the superuser /game/broadcast (#1028)."""
    transport = _Transport()
    assert await broadcast_shutdown_notification(transport, 10)
    await _broadcast_shutdown_cancellation(transport)
    admin = _as(User, SimpleNamespace(id=uuid.uuid4(), username="admin"))
    _ = await broadcast_message("Hello all", admin, _as(ConnectionManager, transport))
    return transport.events


@dataclass(frozen=True)
class Emitter:
    """One text-bearing server emitter: the event types it must produce, and how to run it."""

    name: str
    event_types: frozenset[str]
    drive: Driver


_CHAT_CHANNELS = ("say", "local", "global", "party", "whisper", "shout", "emote", "pose", "admin", "system")

INVENTORY: tuple[Emitter, ...] = (
    Emitter("command chokepoint", frozenset({"command_response"}), _drive_command_chokepoint),
    Emitter("direct command_response", frozenset({"command_response"}), _drive_direct_command_response),
    Emitter("rest countdown", frozenset({"command_response", "intentional_disconnect"}), _drive_rest_countdown),
    *(Emitter(f"chat {channel}", frozenset({"chat_message"}), _chat_driver(channel)) for channel in _CHAT_CHANNELS),
    Emitter("npc room messages", frozenset({"room_message"}), _drive_npc_room_messages),
    Emitter("chat segments", frozenset({"chat_message"}), _drive_chat_segments),
    Emitter("player enter/leave", frozenset({"player_entered", "player_left"}), _drive_player_enter_leave),
    Emitter("system events", frozenset({"system"}), _drive_system_events),
    Emitter("posture change", frozenset({"player_posture_change", "player_update"}), _drive_posture),
    Emitter("admin set-stat posture", frozenset({"player_update"}), _drive_setstat_posture),
    Emitter("respawn", frozenset({"player_respawned", "player_delirium_respawned"}), _drive_respawn),
    Emitter(
        "combat messaging",
        frozenset(
            {
                "combat_attack",
                "combat_target_switch",
                "combat_npc_disengage",
                "combat_participant_joined",
                "combat_taunt",
                "combat_protect",
            }
        ),
        _drive_combat_messaging,
    ),
    Emitter("dp decay", frozenset({"player_dp_decay"}), _drive_dp_decay),
    Emitter(
        "mortally wounded",
        frozenset({"player_mortally_wounded", "player_mortally_wounded_room"}),
        _drive_mortally_wounded,
    ),
    Emitter("npc died", frozenset({"npc_died"}), _drive_npc_died),
    Emitter(
        "combat publisher",
        frozenset({"player_attacked", "npc_attacked", "npc_took_damage", "combat_ended"}),
        _drive_combat_publisher,
    ),
    Emitter("rescue update", frozenset({"rescue_update"}), _drive_rescue_update),
    Emitter(
        "admin broadcasts",
        frozenset({"shutdown_notification", "shutdown_cancelled", "system_broadcast"}),
        _drive_admin_broadcasts,
    ),
)


def _has_text(data: Mapping[str, object]) -> bool:
    return any(data.get(key) for key in _TEXT_KEYS)


def _assert_valid_category(label: str, value: object) -> None:
    assert isinstance(value, str), f"{label}: category must be a string, got {value!r}"
    assert value in _VALID_CATEGORIES, f"{label}: {value!r} is not a MessageCategory value"


@pytest.mark.asyncio
@pytest.mark.parametrize("emitter", INVENTORY, ids=[e.name for e in INVENTORY])
async def test_every_text_event_carries_a_valid_category(emitter: Emitter) -> None:
    """Each event an emitter produces that carries text is tagged; combat_attack tags each perspective line."""
    emitted = await emitter.drive()

    produced = {event_type for event_type, _ in emitted}
    assert emitter.event_types <= produced, f"driver did not produce {sorted(emitter.event_types - produced)}"

    for event_type, data in emitted:
        if event_type not in emitter.event_types or not _has_text(data):
            continue
        label = f"{emitter.name} / {event_type}"
        if event_type == "combat_attack":
            messages = cast(dict[str, str], data["messages"])
            categories = cast(dict[str, object], data["categories"])
            assert set(categories) == set(messages), f"{label}: categories must be keyed like messages"
            for key, value in categories.items():
                _assert_valid_category(f"{label}[{key}]", value)
        else:
            assert "category" in data, f"{label}: text event has no data.category"
            _assert_valid_category(label, data["category"])


# The category each emitter chose, for the cases where the choice is a decision rather than a lookup.
EXPECTED_CATEGORIES = (
    ("direct command_response", "command_response", MessageCategory.COMMAND_OUTPUT),
    ("rest countdown", "command_response", MessageCategory.SYSTEM_INFO),
    ("rest countdown", "intentional_disconnect", MessageCategory.SYSTEM_INFO),
    ("respawn", "player_respawned", MessageCategory.SYSTEM_INFO),
    ("respawn", "player_delirium_respawned", MessageCategory.SYSTEM_INFO),
    ("posture change", "player_posture_change", MessageCategory.ROOM_MOVEMENT),
    ("posture change", "player_update", MessageCategory.ROOM_MOVEMENT),  # the second-person self-line
    ("admin set-stat posture", "player_update", MessageCategory.ROOM_MOVEMENT),
    ("dp decay", "player_dp_decay", MessageCategory.STATUS_HEALTH),
    ("mortally wounded", "player_mortally_wounded", MessageCategory.COMBAT_STATUS),
    ("mortally wounded", "player_mortally_wounded_room", MessageCategory.COMBAT_STATUS),
    ("rescue update", "rescue_update", MessageCategory.STATUS_RESCUE),
    ("npc died", "npc_died", MessageCategory.COMBAT_DEATH),
    ("admin broadcasts", "shutdown_notification", MessageCategory.SYSTEM_WARNING),
    ("admin broadcasts", "shutdown_cancelled", MessageCategory.SYSTEM_INFO),
    ("admin broadcasts", "system_broadcast", MessageCategory.SYSTEM_INFO),
)


@pytest.mark.asyncio
@pytest.mark.parametrize(("emitter_name", "event_type", "expected"), EXPECTED_CATEGORIES)
async def test_emitter_chooses_the_documented_category(
    emitter_name: str, event_type: str, expected: MessageCategory
) -> None:
    emitter = next(e for e in INVENTORY if e.name == emitter_name)
    categories = [
        data.get("category") for kind, data in await emitter.drive() if kind == event_type and _has_text(data)
    ]
    assert categories
    assert set(categories) == {expected}


@pytest.mark.asyncio
@pytest.mark.parametrize("emitter", INVENTORY, ids=[e.name for e in INVENTORY])
async def test_segments_always_join_back_to_the_message(emitter: Emitter) -> None:
    """#1025: wherever an emitter attaches ``segments``, they concatenate to exactly ``message``."""
    for event_type, data in await emitter.drive():
        if "segments" not in data:
            continue
        label = f"{emitter.name} / {event_type}"
        segments = cast(list[dict[str, str]], data["segments"])
        assert "".join(segment["text"] for segment in segments) == data["message"], f"{label}: segments != message"
        for segment in segments:
            if "category" in segment:
                _assert_valid_category(label, segment["category"])


@pytest.mark.asyncio
async def test_inventory_exercises_segments() -> None:
    """Guard the guard: if no driver emits ``segments``, the join test above is passing vacuously."""
    produced: set[str] = set()
    for emitter in INVENTORY:
        produced |= {event_type for event_type, data in await emitter.drive() if "segments" in data}
    assert {"room_message", "npc_died", "chat_message"} <= produced


# --- inventory vs the client projector ------------------------------------------------------------------

_HANDLER_RE = re.compile(r"^  (\w+)\(prevState", re.MULTILINE)
_DELEGATE_RE = re.compile(r"(?:messageHandlers|stateHandlers)\.(\w+)!")
_TEXT_CALLS = ("buildChatMessage(", "appendPostureGameInfoMessage(", "mergePostureMessageIntoState(")


def _handler_bodies(source: str) -> dict[str, str]:
    starts = [(m.group(1), m.start()) for m in _HANDLER_RE.finditer(source)]
    ends = [start for _, start in starts[1:]] + [len(source)]
    return {name: source[start:end] for (name, start), end in zip(starts, ends, strict=True)}


def _newly_delegating(bodies: dict[str, str], text_types: set[str]) -> set[str]:
    """Handlers not yet known to render text that delegate to one that does."""
    return {
        name
        for name, body in bodies.items()
        if name not in text_types
        and any(target in text_types for target in cast(list[str], _DELEGATE_RE.findall(body)))
    }


def _client_text_event_types() -> set[str]:
    """Event types whose projector handler appends text to the message log, following delegating handlers."""
    bodies: dict[str, str] = {}
    for name in ("projectorHandlersMessages.ts", "projectorHandlersState.ts"):
        bodies.update(_handler_bodies((_PROJECTOR_DIR / name).read_text(encoding="utf-8")))
    text_types = {name for name, body in bodies.items() if any(call in body for call in _TEXT_CALLS)}
    while newly := _newly_delegating(bodies, text_types):
        text_types |= newly
    return text_types


def test_scanner_finds_the_known_client_text_handlers() -> None:
    """Guard the scanner itself: if the projector is restructured and this empties, fail loudly."""
    found = _client_text_event_types()
    assert {"command_response", "chat_message", "room_message", "player_update", "player_dp_decay"} <= found


def test_inventory_covers_every_client_text_event() -> None:
    """A text event the client renders needs a server emitter in INVENTORY, unless the client authors it."""
    covered = {event_type for emitter in INVENTORY for event_type in emitter.event_types}
    client_types = {CLIENT_ALIASES.get(name, name) for name in _client_text_event_types()}
    missing = client_types - covered - CLIENT_AUTHORED_EVENT_TYPES
    assert not missing, f"client renders text for {sorted(missing)} but INVENTORY has no emitter for them"
