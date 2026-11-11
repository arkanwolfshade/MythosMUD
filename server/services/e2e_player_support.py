"""
E2E test support: reset, place and read E2E characters through the player registry (ADR-029 step 8b).

Playwright specs used to reset characters with scripts that wrote Postgres directly (``scripts/e2e_reset_players.py``,
``e2e_place_player.py``) and read them back with another (``e2e_player_state.py``). With the registry owning every
player's state, an out-of-band write is exactly the kind the registry cannot see, so the harness goes through the
server instead: every change here is one synchronous registry unit, and ``state`` reads the registry's aggregate.

Like the scripts, a reset or placement does not refuse a character who is online: the caller (the spec) logs them out
first, because a logged-in player's live session would carry on from the old state.

The routes that expose this live in ``server/api/admin/e2e_test_support.py`` and exist only on the e2e server.
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping, Sequence
from typing import Protocol, cast

from pydantic import BaseModel

from ..constants.instance_rooms import PENDING_INSTANCE_ID
from ..constants.spawn_defaults import DEFAULT_RESPAWN_ROOM
from ..game.player_registry import PlayerRegistry, PlayerView
from ..models.lucidity import LucidityActionCode

SHARED_PLAYERS = ("ArkanWolfshade", "Ithaqua")
FOLK_TONIC_COOLDOWN = "folk_tonic"
TUTORIAL_ITEM_PROTOTYPE = "pack_dark_ages.weapon.sling"
SHARED_PLAYER_DP = 50
LOST_AND_FOUND_ROLE = "lost_and_found"
# The login ward is kept: the server clears its in-memory grace only when that effect expires, and logging out does
# not end the grace, so deleting a running ward left the next login warded for good (NPC attacks blocked forever).
KEPT_EFFECT = "login_warded"


class UnknownPlayerError(LookupError):
    """There is no character with this name."""


class UnknownRoomError(LookupError):
    """There is no room with this stable id."""


class E2ePlayerState(BaseModel):
    """What ``GET /admin/test/players/{name}/state`` returns (client/tests/e2e/runtime/fixtures/tutorial.ts)."""

    current_room_id: str
    respawn_room_id: str | None
    tutorial_instance_id: str | None
    bank_items: list[str]
    current_dp: int | None
    corruption: int | None
    magic_points: int | None
    max_magic_points: int | None
    intelligence: int | None
    current_lcd: int
    inventory_items: list[str]
    quests: dict[str, str]
    debrief_pending: bool


class _NamedPlayer(Protocol):
    @property
    def player_id(self) -> object:
        """The character's id."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class _Persistence(Protocol):
    """The slice of the persistence layer the harness uses: a name lookup, and the containers outside the aggregate."""

    async def get_player_by_name(self, name: str) -> _NamedPlayer | None:
        """The character with this name, or None."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    async def get_bank_container(self, owner_id: uuid.UUID) -> Mapping[str, object] | None:
        """The character's bank deposit box, or None if they have never opened one."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    async def get_containers_by_room_id(self, room_id: str) -> Sequence[Mapping[str, object]]:
        """Every container in a room."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    async def update_container(
        self, container_id: uuid.UUID, items_json: list[dict[str, object]] | None = None
    ) -> object:
        """Replace a container's items."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class _Rooms(Protocol):
    async def get_room(self, room_id: str) -> Mapping[str, object] | None:
        """The room with this stable id, or None."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


def _int_stat(view: PlayerView, key: str) -> int | None:
    value = view.row.stats.get(key)
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _as_mapping(raw: object) -> Mapping[str, object]:
    return cast(Mapping[str, object], raw) if isinstance(raw, Mapping) else {}


def _stack_names(stacks: Sequence[Mapping[str, object]]) -> list[str]:
    return [str(stack.get("item_name", stack.get("item_id"))) for stack in stacks]


def _as_stacks(raw: object) -> list[Mapping[str, object]]:
    return [_as_mapping(stack) for stack in cast(list[object], raw)] if isinstance(raw, list) else []


class E2ePlayerSupport:
    """Resets, places and reads E2E characters, one registry unit each."""

    _registry: PlayerRegistry
    _persistence: _Persistence
    _rooms: _Rooms

    def __init__(self, registry: PlayerRegistry, persistence: _Persistence, rooms: _Rooms) -> None:
        self._registry = registry
        self._persistence = persistence
        self._rooms = rooms

    async def _player_id(self, name: str) -> uuid.UUID:
        player = await self._persistence.get_player_by_name(name)
        if player is None:
            raise UnknownPlayerError(name)
        return uuid.UUID(str(player.player_id))

    async def reset_shared_players(self) -> None:
        """Put ArkanWolfshade and Ithaqua back in the default room, standing, at 50 DP, with no folk tonic cooldown."""
        for name in SHARED_PLAYERS:
            async with self._registry.mutate(await self._player_id(name), sync=True) as player:
                player.row.set_current_room_id(DEFAULT_RESPAWN_ROOM, sync=True)
                player.row.set_stat("current_dp", SHARED_PLAYER_DP, sync=True)
                player.row.set_stat("position", "standing", sync=True)
                _ = player.cooldowns.clear(FOLK_TONIC_COOLDOWN)

    async def reset_tutorial_character(self, name: str) -> None:
        """Put a character back at the very start of First Exposure, as one who has not met it yet.

        Saved in the Main Foyer with the pending-instance marker, so the next login goes through the server's
        tutorial connect path and builds a brand new instance. DP, lucidity and corruption are reset, the character
        holds one Sling (the generic instance-flush-to-bank tests drop it), status effects (but the login ward) and
        cooldowns are emptied, quests deleted (the first quest starts again on spawn). The shared lost-and-found
        chest and the character's own deposit box are emptied too, so nothing carries over into the next test.
        """
        player_id = await self._player_id(name)
        sling: dict[str, object] = {
            "item_id": TUTORIAL_ITEM_PROTOTYPE,
            "prototype_id": TUTORIAL_ITEM_PROTOTYPE,
            "item_instance_id": f"e2e-tutorial-sling-{uuid.uuid4().hex[:12]}",
            "item_name": "Sling",
            "slot_type": "backpack",
            "quantity": 1,
        }
        async with self._registry.mutate(player_id, sync=True) as player:
            player.row.set_current_room_id(DEFAULT_RESPAWN_ROOM, sync=True)
            player.row.set_respawn_room_id(DEFAULT_RESPAWN_ROOM, sync=True)
            player.row.set_tutorial_instance_id(PENDING_INSTANCE_ID)
            max_dp = player.row.stats.get("max_dp")
            player.row.set_stat("current_dp", max_dp if isinstance(max_dp, int) else 100, sync=True)
            player.row.set_stat("corruption", 0, sync=True)
            player.row.set_stat("position", "standing", sync=True)
            player.inventory.replace([sling], {})
            _ = player.quests.clear()
            for effect in player.effects.effects:
                if effect.effect_type != KEPT_EFFECT:
                    _ = player.effects.remove(effect.id)
            _ = player.lucidity.set(lcd=100, tier="lucid", liabilities="[]")
            _ = player.cooldowns.clear_prefix("")
        await self._empty_lost_and_found()
        await self._empty_bank(player_id)

    async def _empty_lost_and_found(self) -> None:
        # shortcut: looks in the default room only (where the one chest is), not every room, upgrade if chests spread.
        for container in await self._persistence.get_containers_by_room_id(DEFAULT_RESPAWN_ROOM):
            if _as_mapping(container.get("metadata_json")).get("role") == LOST_AND_FOUND_ROLE:
                _ = await self._persistence.update_container(uuid.UUID(str(container["container_id"])), items_json=[])

    async def _empty_bank(self, player_id: uuid.UUID) -> None:
        bank = await self._persistence.get_bank_container(player_id)
        if bank is not None:
            _ = await self._persistence.update_container(uuid.UUID(str(bank["container_id"])), items_json=[])

    async def place(self, name: str, room_id: str) -> None:
        """Move a character to a room. Placing them in the ordinary world also takes them out of the tutorial.

        Clearing the tutorial instance matters: otherwise the server would put them back in a fresh tutorial instance
        on login. A room that does not exist is refused, so a typo fails loudly instead of stranding the character.
        """
        player_id = await self._player_id(name)
        if await self._rooms.get_room(room_id) is None:
            raise UnknownRoomError(room_id)
        async with self._registry.mutate(player_id, sync=True) as player:
            player.row.set_current_room_id(room_id, sync=True)
            player.row.set_tutorial_instance_id(None)

    async def state(self, name: str) -> E2ePlayerState:
        """One character's state as the registry holds it (the bank deposit box is read from its container)."""
        player_id = await self._player_id(name)
        view = await self._registry.get(player_id)
        if view is None:
            raise UnknownPlayerError(name)
        bank = await self._persistence.get_bank_container(player_id)
        return E2ePlayerState(
            current_room_id=view.row.current_room_id,
            respawn_room_id=view.row.respawn_room_id,
            tutorial_instance_id=view.row.tutorial_instance_id,
            bank_items=_stack_names(_as_stacks(bank.get("items_json"))) if bank is not None else [],
            current_dp=_int_stat(view, "current_dp"),
            corruption=_int_stat(view, "corruption"),
            magic_points=_int_stat(view, "magic_points"),
            max_magic_points=_int_stat(view, "max_magic_points"),
            intelligence=_int_stat(view, "intelligence"),
            current_lcd=view.lucidity.lcd,
            inventory_items=_stack_names(view.inventory.carried),
            quests={instance.quest_id: instance.state for instance in view.quests.all()},
            debrief_pending=view.cooldowns.expires_at(LucidityActionCode.DEBRIEF_PENDING) is not None,
        )
