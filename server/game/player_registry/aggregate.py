"""
PlayerAggregate: everything the server knows about one player, held once in memory (ADR-029 §3.2).

The aggregate is a set of parts. Today that is the ``players`` row, the inventory and the quests; later ADR-029
steps add lucidity, effects and the rest as their subsystems move onto the registry. Callers only ever reach it through
PlayerRegistry: ``mutate()`` hands out the aggregate itself, ``peek()`` hands out a PlayerView.
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping, Sequence
from typing import Protocol

from ...events.event_types import BaseEvent
from .part import Part, PartWrite
from .player_inventory import PlayerInventoryPart
from .player_quests import PlayerQuestsPart, QuestInstanceData
from .player_row import PlayerRowPart


class PlayerRowView(Protocol):
    """Read-only access to the ``players`` row part. There are no setters, so the type checker blocks mutation."""

    @property
    def player_id(self) -> uuid.UUID:
        """The player's id."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def user_id(self) -> str:
        """The owning account's id."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def name(self) -> str:
        """The character name."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def current_room_id(self) -> str:
        """The room the player is in."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def respawn_room_id(self) -> str | None:
        """Where the player respawns."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def experience_points(self) -> int:
        """Total XP."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def level(self) -> int:
        """Character level."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def is_admin(self) -> bool:
        """True for an admin character."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def profession_id(self) -> int | None:
        """The profession, if any."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def tutorial_instance_id(self) -> str | None:
        """The tutorial instance the player is in (or the pending marker), else None."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def is_deleted(self) -> bool:
        """True for a soft-deleted character."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def stats(self) -> Mapping[str, object]:
        """The stats jsonb (DP, MP, corruption, ...)."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class PlayerInventoryView(Protocol):
    """Read-only access to the inventory part. There are no setters, so the type checker blocks mutation."""

    @property
    def carried(self) -> Sequence[Mapping[str, object]]:
        """Carried stacks."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def equipped(self) -> Mapping[str, object]:
        """Equipped stacks by slot."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class PlayerQuestsView(Protocol):
    """Read-only access to the quests part."""

    def get(self, quest_id: str) -> QuestInstanceData | None:
        """The player's instance of this quest, in any state, or None."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    def active(self) -> list[QuestInstanceData]:
        """Active instances, oldest accepted first."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    def completed(self) -> list[QuestInstanceData]:
        """Completed instances, most recently completed first."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class PlayerView(Protocol):
    """What ``PlayerRegistry.peek()`` returns: the live aggregate, typed read-only."""

    @property
    def player_id(self) -> uuid.UUID:
        """The player's id."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def row(self) -> PlayerRowView:
        """The ``players`` row."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def inventory(self) -> PlayerInventoryView:
        """Carried and equipped stacks."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    @property
    def quests(self) -> PlayerQuestsView:
        """Quest instances."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class PlayerAggregate:
    """One player's in-memory state: its parts and the domain events its current unit of work has queued."""

    __slots__: tuple[str, ...] = ("_events", "_inventory", "_quests", "_row")

    _row: PlayerRowPart
    _inventory: PlayerInventoryPart
    _quests: PlayerQuestsPart
    _events: list[BaseEvent]

    def __init__(
        self, row: PlayerRowPart, inventory: PlayerInventoryPart, quests: PlayerQuestsPart | None = None
    ) -> None:
        self._row = row
        self._inventory = inventory
        self._quests = quests if quests is not None else PlayerQuestsPart(row.player_id)
        self._events = []

    @property
    def player_id(self) -> uuid.UUID:
        """The player's id."""
        return self._row.player_id

    @property
    def row(self) -> PlayerRowPart:
        """The ``players`` row."""
        return self._row

    @property
    def inventory(self) -> PlayerInventoryPart:
        """Carried and equipped stacks."""
        return self._inventory

    @property
    def quests(self) -> PlayerQuestsPart:
        """Quest instances."""
        return self._quests

    def parts(self) -> tuple[Part, ...]:
        """Every part, in write order."""
        return (self._row, self._inventory, self._quests)

    def emit(self, event: BaseEvent) -> None:
        """Queue a domain event; it is published only if the unit of work commits."""
        self._events.append(event)

    @property
    def dirty(self) -> bool:
        """True if any part has changes the database does not have yet."""
        return any(part.dirty for part in self.parts())

    @property
    def sync_required(self) -> bool:
        """True if any part's pending changes must be committed before the command returns."""
        return any(part.sync_required for part in self.parts())

    def begin(self) -> None:
        """Checkpoint every part at the start of a unit of work."""
        for part in self.parts():
            part.begin()
        self._events.clear()

    def rollback(self) -> None:
        """Undo the unit of work: restore every part and drop its events."""
        for part in self.parts():
            part.rollback()
        self._events.clear()

    def end(self) -> list[BaseEvent]:
        """Finish the unit of work: drop the checkpoints and hand back the queued events."""
        for part in self.parts():
            part.end()
        events, self._events = self._events, []
        return events

    def take_writes(self) -> list[tuple[Part, PartWrite]]:
        """Capture a write for every dirty part (clearing its flags), paired with the part for retry marking."""
        writes: list[tuple[Part, PartWrite]] = []
        for part in self.parts():
            write = part.take_write()
            if write is not None:
                writes.append((part, write))
        return writes
