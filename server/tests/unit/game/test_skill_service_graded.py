"""Unit tests for graded d100 skill checks (#833): SuccessLevel, grade_d100 and roll_best_skill_check."""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.skill_service import SkillService, SuccessLevel, grade_d100

_RANDINT = "server.game.skill_service.random.randint"
E, H, R, F, X = (
    SuccessLevel.EXTREME,
    SuccessLevel.HARD,
    SuccessLevel.REGULAR,
    SuccessLevel.FAILURE,
    SuccessLevel.FUMBLE,
)


@pytest.mark.parametrize(
    ("roll", "value", "expected"),
    [
        # value 60: extreme <= 12, hard <= 30, regular <= 60
        (1, 60, E),
        (12, 60, E),
        (13, 60, H),
        (30, 60, H),
        (31, 60, R),
        (60, 60, R),
        (61, 60, F),
        (99, 60, F),  # skill >= 50: only a 100 fumbles
        (100, 60, X),
        # value 49 / 50 is the fumble-range boundary
        (95, 49, F),
        (96, 49, X),
        (96, 50, F),
        (100, 40, X),
        # 01 is always an extreme success, even at skill 0
        (1, 0, E),
        (2, 0, F),
        # a high skill still succeeds on 96-99
        (96, 99, R),
        (100, 99, X),
    ],
)
def test_grade_d100(roll: int, value: int, expected: SuccessLevel) -> None:
    assert grade_d100(roll, value) is expected


def test_only_regular_hard_and_extreme_count_as_success() -> None:
    assert {level for level in SuccessLevel if level.is_success} == {R, H, E}


@dataclass
class _Skill:
    key: str


@dataclass
class _Row:
    skill_id: int
    value: int
    skill: _Skill


def _service(rows: list[_Row], *, player_level: int | None = None) -> tuple[SkillService, AsyncMock, AsyncMock]:
    """A SkillService over fakes; returns (service, record_use mock, get_player_by_id mock)."""
    record_use: AsyncMock = AsyncMock()
    get_player: AsyncMock = AsyncMock(return_value=None if player_level is None else MagicMock(level=player_level))
    player_skill_repo: MagicMock = MagicMock()
    player_skill_repo.get_by_player_id = AsyncMock(return_value=rows)
    use_log_repo: MagicMock = MagicMock()
    use_log_repo.record_use = record_use
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_id = get_player
    service = SkillService(
        skill_repository=MagicMock(),
        player_skill_repository=player_skill_repo,
        skill_use_log_repository=use_log_repo,
        persistence=persistence,
    )
    return service, record_use, get_player


_INTIMIDATE = _Row(skill_id=7, value=30, skill=_Skill("intimidate"))
_FIGHTING = _Row(skill_id=8, value=55, skill=_Skill("fighting"))
_DODGE = _Row(skill_id=9, value=90, skill=_Skill("dodge"))


@pytest.mark.asyncio
async def test_best_skill_check_uses_the_higher_of_the_two_skills() -> None:
    """A 40 fails on Intimidate (30) alone but is a Regular success on Fighting (55): the best skill is rolled."""
    player_id = uuid.uuid4()
    service, record_use, _ = _service([_INTIMIDATE, _FIGHTING, _DODGE])

    with patch(_RANDINT, return_value=40):
        result = await service.roll_best_skill_check(player_id, ["intimidate", "fighting"], character_level=3)

    assert result is R
    record_use.assert_awaited_once_with(player_id=player_id, skill_id=8, character_level_at_use=3)


@pytest.mark.asyncio
async def test_best_skill_check_ignores_skills_that_were_not_asked_for() -> None:
    """Dodge 90 is not in the key list, so it neither helps the roll nor gets a use recorded."""
    service, record_use, _ = _service([_DODGE])
    randint: MagicMock = MagicMock(return_value=1)

    with patch(_RANDINT, new=randint):
        result = await service.roll_best_skill_check(uuid.uuid4(), ["intimidate", "fighting"], character_level=1)

    assert result is F
    randint.assert_not_called()  # nothing to roll against
    record_use.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize(("roll", "expected"), [(10, E), (25, H), (80, F), (100, X)])
async def test_best_skill_check_grades_the_roll_and_records_only_successes(roll: int, expected: SuccessLevel) -> None:
    service, record_use, _ = _service([_FIGHTING])  # value 55: extreme <= 11, hard <= 27

    with patch(_RANDINT, return_value=roll):
        result = await service.roll_best_skill_check(uuid.uuid4(), ["fighting"], character_level=2)

    assert result is expected
    assert record_use.await_count == (1 if expected.is_success else 0)


@pytest.mark.asyncio
async def test_best_skill_check_defaults_to_the_players_current_level() -> None:
    player_id = uuid.uuid4()
    service, record_use, get_player = _service([_FIGHTING], player_level=4)

    with patch(_RANDINT, return_value=20):
        _ = await service.roll_best_skill_check(player_id, ["fighting"])

    get_player.assert_awaited_once_with(player_id)
    record_use.assert_awaited_once_with(player_id=player_id, skill_id=8, character_level_at_use=4)


@pytest.mark.asyncio
async def test_best_skill_check_falls_back_to_level_one_when_the_player_is_missing() -> None:
    player_id = uuid.uuid4()
    service, record_use, _ = _service([_FIGHTING], player_level=None)

    with patch(_RANDINT, return_value=20):
        _ = await service.roll_best_skill_check(player_id, ["fighting"])

    record_use.assert_awaited_once_with(player_id=player_id, skill_id=8, character_level_at_use=1)


@pytest.mark.asyncio
async def test_roll_skill_check_shares_the_graded_rule_a_roll_of_one_always_succeeds() -> None:
    """roll_skill_check delegates to grade_d100, so 01 succeeds even against a skill of 0."""
    player_id = uuid.uuid4()
    service, record_use, _ = _service([_Row(skill_id=5, value=0, skill=_Skill("dodge"))])

    with patch(_RANDINT, return_value=1):
        assert await service.roll_skill_check(player_id, skill_id=5, character_level=1) is True
    with patch(_RANDINT, return_value=2):
        assert await service.roll_skill_check(player_id, skill_id=5, character_level=1) is False

    assert record_use.await_count == 1
