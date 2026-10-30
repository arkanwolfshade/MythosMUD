"""
The quests part of a PlayerAggregate: the player's ``quest_instances`` rows (ADR-029 §3.2, step 5a).

Loaded with the rest of the aggregate (``list_quest_instances_by_player``, every state) and keyed by quest id, since
a player has at most one instance of each quest. Every change is synchronous, progress counters included (the user's
choice for 5a): a sync commit upserts every instance the player holds (``upsert_quest_instance``). A player holds a
handful, and writing them all means a retried write never needs to know which one changed.
"""

from __future__ import annotations

import json
import uuid
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field, replace
from datetime import UTC, datetime
from typing import cast, override

from sqlalchemy import text

from .part import DbSession, Part, PartWrite
from .player_row import as_json_object

LIST_QUEST_INSTANCES_SQL = text(
    "SELECT id, quest_id, state, progress, accepted_at, completed_at FROM list_quest_instances_by_player(:id)"
)

UPSERT_QUEST_INSTANCE_SQL = text(
    "CALL upsert_quest_instance(:id, :player_id, :quest_id, :state, CAST(:progress AS jsonb), :accepted_at,"
    + " :completed_at)"
)

_EPOCH = datetime.min.replace(tzinfo=UTC)


@dataclass(frozen=True, slots=True)
class QuestInstanceData:
    """One quest instance, as the aggregate holds it. Change it through ``PlayerQuestsPart.set``."""

    instance_id: uuid.UUID
    quest_id: str
    state: str
    progress: Mapping[str, object] = field(default_factory=dict[str, object])
    accepted_at: datetime | None = None
    completed_at: datetime | None = None

    @classmethod
    def from_row(cls, row: Mapping[str, object]) -> QuestInstanceData:
        """Build from a ``list_quest_instances_by_player`` row."""
        return cls(
            instance_id=uuid.UUID(str(row["id"])),
            quest_id=str(row["quest_id"]),
            state=str(row["state"]),
            progress=as_json_object(row.get("progress")),
            accepted_at=cast(datetime | None, row.get("accepted_at")),
            completed_at=cast(datetime | None, row.get("completed_at")),
        )


class PlayerQuestsPart(Part):
    """The player's quest instances by quest id, with read access and synchronous mutators."""

    __slots__: tuple[str, ...] = ("_instances", "_player_id")

    _player_id: uuid.UUID
    _instances: dict[str, QuestInstanceData]

    def __init__(self, player_id: uuid.UUID, instances: Sequence[QuestInstanceData] = ()) -> None:
        super().__init__()
        self._player_id = player_id
        self._instances = {instance.quest_id: instance for instance in instances}

    @classmethod
    def from_rows(cls, player_id: uuid.UUID, rows: Sequence[Mapping[str, object]]) -> PlayerQuestsPart:
        """Build from ``list_quest_instances_by_player`` rows."""
        return cls(player_id, [QuestInstanceData.from_row(row) for row in rows])

    # ---- reads ----

    def get(self, quest_id: str) -> QuestInstanceData | None:
        """The player's instance of this quest, in any state, or None."""
        return self._instances.get(quest_id)

    def active(self) -> list[QuestInstanceData]:
        """Active instances, oldest accepted first."""
        found = [instance for instance in self._instances.values() if instance.state == "active"]
        return sorted(found, key=lambda instance: instance.accepted_at or _EPOCH)

    def completed(self) -> list[QuestInstanceData]:
        """Completed instances, most recently completed first."""
        found = [instance for instance in self._instances.values() if instance.state == "completed"]
        return sorted(found, key=lambda instance: instance.completed_at or _EPOCH, reverse=True)

    # ---- mutators ----

    def set(
        self,
        quest_id: str,
        *,
        state: str | None = None,
        progress: Mapping[str, object] | None = None,
        completed_at: datetime | None = None,
    ) -> QuestInstanceData:
        """Change the instance of ``quest_id`` (creating it, accepted now, if the player has none); returns it.

        Only the fields given change. A new instance needs a ``state``.
        """
        current = self._instances.get(quest_id)
        if current is None:
            if state is None:
                raise ValueError(f"a new quest instance needs a state: {quest_id}")
            updated = QuestInstanceData(uuid.uuid4(), quest_id, state, dict(progress or {}), datetime.now(UTC))
        else:
            updated = replace(
                current,
                state=state if state is not None else current.state,
                progress=dict(progress) if progress is not None else current.progress,
                completed_at=completed_at if completed_at is not None else current.completed_at,
            )
        if updated != current:
            self._instances[quest_id] = updated
            self.mark_dirty(sync=True)
        return updated

    def write_params(self) -> list[dict[str, object]]:
        """``upsert_quest_instance`` parameters for every instance."""
        return [
            {
                "id": str(instance.instance_id),
                "player_id": str(self._player_id),
                "quest_id": instance.quest_id,
                "state": instance.state,
                "progress": json.dumps(dict(instance.progress)),
                "accepted_at": instance.accepted_at,
                "completed_at": instance.completed_at,
            }
            for instance in self._instances.values()
        ]

    # ---- Part protocol ----

    @override
    def _copy_state(self) -> object:
        return dict(self._instances)  # the instances are frozen, so a shallow copy is a snapshot

    @override
    def _restore_state(self, state: object) -> None:
        if isinstance(state, dict):
            self._instances = cast(dict[str, QuestInstanceData], state)

    @override
    def capture_write(self) -> PartWrite:
        rows = self.write_params()

        async def write(session: DbSession) -> None:
            for params in rows:
                _ = await session.execute(UPSERT_QUEST_INSTANCE_SQL, params)

        return write
