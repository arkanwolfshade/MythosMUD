"""Skipping First Exposure at creation (#1081, ADR-028 D22/D24): who may, and what the skip leaves them with."""

from __future__ import annotations

import uuid
from collections.abc import AsyncIterator, Mapping, Sequence
from dataclasses import dataclass, field
from typing import cast

import pytest

from server.game import first_exposure as module
from server.game.first_exposure import (
    COMPLETION_QUEST_ID,
    FINISH_ACTIONS,
    RESTORED_LCD,
    FinishPersistence,
    account_completed_first_exposure,
    skip_first_exposure,
)
from server.game.scripted_actions import ScriptedActionContext
from server.models.player import Player
from server.schemas.scripted_actions import ScriptedAction
from server.services.lucidity_service import resolve_tier


def _character() -> Player:
    return Player(player_id=str(uuid.uuid4()), name="Tester")


class FakeQuestLog:
    """Quest logs per character id."""

    _logs: dict[uuid.UUID, list[dict[str, object]]]

    def __init__(self, logs: dict[uuid.UUID, list[dict[str, object]]]) -> None:
        self._logs = logs

    async def get_quest_log(
        self, player_id: uuid.UUID, include_completed: bool = True
    ) -> Sequence[Mapping[str, object]]:
        assert include_completed  # completion is the whole question
        return self._logs.get(player_id, [])


def _id(player: Player) -> uuid.UUID:
    return uuid.UUID(str(player.player_id))


@pytest.mark.asyncio
async def test_an_account_whose_character_finished_the_tutorial_may_skip() -> None:
    newcomer, veteran = _character(), _character()
    quests = FakeQuestLog({_id(veteran): [{"quest_id": COMPLETION_QUEST_ID, "state": "completed"}]})

    assert await account_completed_first_exposure([newcomer, veteran], quests) is True


@pytest.mark.asyncio
async def test_an_unfinished_or_partly_played_tutorial_does_not_earn_the_skip() -> None:
    midway, other = _character(), _character()
    quests = FakeQuestLog(
        {
            _id(midway): [
                {"quest_id": "first_exposure_dusk", "state": "completed"},
                {"quest_id": COMPLETION_QUEST_ID, "state": "active"},  # still in the Below act
            ],
            _id(other): [{"quest_id": "some_other_quest", "state": "completed"}],
        }
    )

    assert await account_completed_first_exposure([midway, other], quests) is False


@pytest.mark.asyncio
async def test_an_account_with_no_characters_may_not_skip() -> None:
    assert await account_completed_first_exposure([], FakeQuestLog({})) is False


@dataclass
class FakeLucidity:
    current_lcd: int = 100
    current_tier: str = "lucid"


@dataclass
class SkipRig:
    player: Player
    lucidity: FakeLucidity = field(default_factory=FakeLucidity)
    debriefs_marked: list[uuid.UUID] = field(default_factory=lambda: cast(list[uuid.UUID], []))
    commits: int = 0
    ran: list[tuple[tuple[ScriptedAction, ...], Player]] = field(
        default_factory=lambda: cast(list[tuple[tuple[ScriptedAction, ...], Player]], [])
    )


class FakePersistence:
    _player: Player | None

    def __init__(self, player: Player | None) -> None:
        self._player = player

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        _ = player_id
        return self._player

    async def save_player(self, player: object) -> None:  # pragma: no cover - the finish actions are faked here
        _ = player


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> SkipRig:
    rig = SkipRig(player=_character())

    class FakeSession:
        async def commit(self) -> None:
            rig.commits += 1

    async def fake_sessions() -> AsyncIterator[FakeSession]:
        yield FakeSession()

    class FakeRepository:
        def __init__(self, session: object) -> None:
            _ = session

        async def get_or_create_player_lucidity(self, player_id: uuid.UUID) -> FakeLucidity:
            _ = player_id
            return rig.lucidity

    async def fake_mark(lucidity_service: object, player_id: uuid.UUID) -> None:
        _ = lucidity_service
        rig.debriefs_marked.append(player_id)

    async def fake_run(actions: Sequence[ScriptedAction], ctx: ScriptedActionContext) -> None:
        rig.ran.append((tuple(actions), ctx.player))

    monkeypatch.setattr("server.database.get_async_session", fake_sessions)
    monkeypatch.setattr("server.services.lucidity_repository.LucidityRepository", FakeRepository)
    monkeypatch.setattr("server.services.debrief_service.mark_debrief_pending", fake_mark)
    monkeypatch.setattr(module, "run_scripted_actions", fake_run)
    return rig


def _persistence(player: Player | None) -> FinishPersistence:
    return cast(FinishPersistence, cast(object, FakePersistence(player)))


@pytest.mark.asyncio
async def test_a_skipped_character_gets_the_end_state_of_a_finished_run(rig: SkipRig) -> None:
    player_id = _id(rig.player)

    await skip_first_exposure(player_id, _persistence(rig.player), None)

    assert rig.lucidity.current_lcd == RESTORED_LCD
    assert rig.lucidity.current_tier == resolve_tier(RESTORED_LCD)
    assert rig.debriefs_marked == [player_id]  # Dr. Morgan's debrief waits for them
    assert rig.commits == 1
    # The same finish actions as the ending: the corruption floor, then the epilogue quest.
    assert rig.ran == [(FINISH_ACTIONS, rig.player)]


@pytest.mark.asyncio
async def test_a_character_that_cannot_be_loaded_still_gets_its_lucidity_and_debrief(rig: SkipRig) -> None:
    await skip_first_exposure(_id(rig.player), _persistence(None), None)

    assert rig.lucidity.current_lcd == RESTORED_LCD
    assert rig.debriefs_marked == [_id(rig.player)]
    assert rig.ran == []
