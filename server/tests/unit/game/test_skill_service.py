"""
Unit tests for SkillService (get_skills_catalog, set_player_skills, get_player_skills).

Character creation revamp 4.3, 4.4: occupation/personal allocation, profession modifiers,
Own Language = EDU when not allocated, Cthulhu Mythos rejected.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.skill_service import SkillService
from server.models.skill import Skill

# pylint: disable=protected-access  # Reason: Test file - accessing protected members for validation tests
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names match fixture names


@pytest.fixture
def catalog_with_own_language_and_mythos():
    """Minimal catalog: accounting, library_use, own_language, cthulhu_mythos (for coverage)."""
    return [
        Skill(
            id=1,
            key="accounting",
            name="Accounting",
            description="Ledgers",
            base_value=5,
            allow_at_creation=True,
            category="knowledge",
        ),
        Skill(
            id=2,
            key="library_use",
            name="Library Use",
            description="Research",
            base_value=5,
            allow_at_creation=True,
            category="knowledge",
        ),
        Skill(
            id=3,
            key="own_language",
            name="Own Language",
            description="Native language",
            base_value=0,
            allow_at_creation=True,
            category="knowledge",
        ),
        Skill(
            id=4,
            key="cthulhu_mythos",
            name="Cthulhu Mythos",
            description="Forbidden",
            base_value=0,
            allow_at_creation=False,
            category="knowledge",
        ),
        Skill(
            id=5,
            key="spot_hidden",
            name="Spot Hidden",
            description="Notice clues",
            base_value=25,
            allow_at_creation=True,
            category="physical",
        ),
        Skill(id=6, key="skill_6", name="Skill 6", description="", base_value=0, allow_at_creation=True, category=""),
        Skill(id=7, key="skill_7", name="Skill 7", description="", base_value=0, allow_at_creation=True, category=""),
        Skill(id=8, key="skill_8", name="Skill 8", description="", base_value=0, allow_at_creation=True, category=""),
        Skill(id=9, key="skill_9", name="Skill 9", description="", base_value=0, allow_at_creation=True, category=""),
        Skill(
            id=10, key="skill_10", name="Skill 10", description="", base_value=0, allow_at_creation=True, category=""
        ),
        Skill(
            id=11, key="skill_11", name="Skill 11", description="", base_value=0, allow_at_creation=True, category=""
        ),
        Skill(
            id=12, key="skill_12", name="Skill 12", description="", base_value=0, allow_at_creation=True, category=""
        ),
        Skill(
            id=13, key="skill_13", name="Skill 13", description="", base_value=0, allow_at_creation=True, category=""
        ),
        Skill(
            id=14, key="skill_14", name="Skill 14", description="", base_value=0, allow_at_creation=True, category=""
        ),
        Skill(
            id=15, key="skill_15", name="Skill 15", description="", base_value=0, allow_at_creation=True, category=""
        ),
    ]


@pytest.fixture
def mock_skill_repo(catalog_with_own_language_and_mythos):
    """Mock SkillRepository returning catalog."""
    repo = MagicMock()
    repo.get_all_skills = AsyncMock(return_value=catalog_with_own_language_and_mythos)
    return repo


@pytest.fixture
def mock_player_skill_repo():
    """Mock PlayerSkillRepository."""
    repo = MagicMock()
    repo.delete_for_player = AsyncMock()
    repo.insert_many = AsyncMock()
    repo.get_by_player_id = AsyncMock(return_value=[])
    repo.update_value = AsyncMock()
    return repo


@pytest.fixture
def mock_persistence():
    """Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id)."""
    return AsyncMock()


@pytest.fixture
def mock_skill_use_log_repo():
    """Mock SkillUseLogRepository for use logging and improvement (plan 10.4)."""
    repo = MagicMock()
    repo.record_use = AsyncMock()
    repo.get_skill_ids_used_at_level = AsyncMock(return_value=[])
    return repo


@pytest.fixture
def skill_service(mock_skill_repo, mock_player_skill_repo, mock_skill_use_log_repo, mock_persistence):
    """SkillService with mocks."""
    return SkillService(
        mock_skill_repo,
        mock_player_skill_repo,
        mock_skill_use_log_repo,
        mock_persistence,
    )


def _occupation_slots_9():
    """Valid 9 slots: one 70, two 60, three 50, three 40; 9 distinct skill_ids (no overlap with personal)."""
    return [
        {"skill_id": 1, "value": 70},
        {"skill_id": 2, "value": 60},
        {"skill_id": 5, "value": 60},
        {"skill_id": 6, "value": 50},
        {"skill_id": 7, "value": 50},
        {"skill_id": 8, "value": 50},
        {"skill_id": 9, "value": 40},
        {"skill_id": 10, "value": 40},
        {"skill_id": 11, "value": 40},
    ]


def _personal_interest_4():
    """Four personal interest (skill_ids only); distinct and no overlap with occupation. Exclude own_language for EDU."""
    return [{"skill_id": 12}, {"skill_id": 13}, {"skill_id": 14}, {"skill_id": 15}]


@pytest.mark.asyncio
async def test_get_skills_catalog_returns_list(skill_service, mock_skill_repo):
    """get_skills_catalog returns list of skill dicts."""
    result = await skill_service.get_skills_catalog()
    assert isinstance(result, list)
    assert len(result) == 15
    assert result[0]["id"] == 1
    assert result[0]["key"] == "accounting"
    assert result[0]["base_value"] == 5
    assert result[0]["allow_at_creation"] is True
    mock_skill_repo.get_all_skills.assert_awaited_once()


@pytest.mark.asyncio
async def test_set_player_skills_valid_creates_rows(
    skill_service,
    mock_persistence,
    mock_player_skill_repo,
):
    """set_player_skills with valid occupation and personal calls delete then insert_many."""
    mock_profession = MagicMock()
    mock_profession.get_skill_modifiers = MagicMock(return_value=[])
    mock_profession.get_stat_modifiers = MagicMock(return_value=[])
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    player_id = uuid.uuid4()
    await skill_service.set_player_skills(
        player_id=player_id,
        occupation_slots=_occupation_slots_9(),
        personal_interest=_personal_interest_4(),
        profession_id=1,
        stats_for_edu=65,
    )

    mock_player_skill_repo.delete_for_player.assert_awaited_once_with(player_id)
    mock_player_skill_repo.insert_many.assert_awaited_once()
    call_args = mock_player_skill_repo.insert_many.call_args
    assert call_args[0][0] == player_id
    rows = call_args[0][1]
    assert isinstance(rows, list)
    assert len(rows) == 15
    skill_ids = {r[0] for r in rows}
    assert 3 in skill_ids
    for row in rows:
        if row[0] == 3:
            assert row[1] == 65


@pytest.mark.asyncio
async def test_set_player_skills_own_language_not_allocated_equals_edu(
    skill_service,
    mock_persistence,
    mock_player_skill_repo,
):
    """When Own Language is not in occupation or personal, its value is stats_for_edu."""
    mock_profession = MagicMock()
    mock_profession.get_skill_modifiers = MagicMock(return_value=[])
    mock_profession.get_stat_modifiers = MagicMock(return_value=[])
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    player_id = uuid.uuid4()
    await skill_service.set_player_skills(
        player_id=player_id,
        occupation_slots=_occupation_slots_9(),
        personal_interest=_personal_interest_4(),
        profession_id=1,
        stats_for_edu=72,
    )

    call_args = mock_player_skill_repo.insert_many.call_args
    rows = call_args[0][1]
    own_lang_row = next((r for r in rows if r[0] == 3), None)
    assert own_lang_row is not None
    assert own_lang_row[1] == 72


@pytest.mark.asyncio
async def test_set_player_skills_cthulhu_mythos_in_occupation_rejected(
    skill_service,
    mock_persistence,
):
    """Occupation slot with Cthulhu Mythos (allow_at_creation=False) raises ValueError."""
    mock_profession = MagicMock()
    mock_profession.get_skill_modifiers = MagicMock(return_value=[])
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    slots = _occupation_slots_9()
    slots[0] = {"skill_id": 4, "value": 70}

    with pytest.raises(ValueError, match="cannot be chosen in occupation"):
        await skill_service.set_player_skills(
            player_id=uuid.uuid4(),
            occupation_slots=slots,
            personal_interest=_personal_interest_4(),
            profession_id=1,
            stats_for_edu=65,
        )


@pytest.mark.asyncio
async def test_set_player_skills_cthulhu_mythos_in_personal_rejected(
    skill_service,
    mock_persistence,
):
    """Personal interest with Cthulhu Mythos raises ValueError."""
    mock_profession = MagicMock()
    mock_profession.get_skill_modifiers = MagicMock(return_value=[])
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    personal = [{"skill_id": 12}, {"skill_id": 13}, {"skill_id": 14}, {"skill_id": 4}]

    with pytest.raises(ValueError, match="cannot be chosen in personal interest"):
        await skill_service.set_player_skills(
            player_id=uuid.uuid4(),
            occupation_slots=_occupation_slots_9(),
            personal_interest=personal,
            profession_id=1,
            stats_for_edu=65,
        )


@pytest.mark.asyncio
async def test_set_player_skills_wrong_occupation_count_raises(skill_service, mock_persistence):
    """occupation_slots not length 9 raises ValueError."""
    mock_profession = MagicMock()
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    with pytest.raises(ValueError, match="exactly 9 entries"):
        await skill_service.set_player_skills(
            player_id=uuid.uuid4(),
            occupation_slots=[{"skill_id": 1, "value": 70}],
            personal_interest=_personal_interest_4(),
            profession_id=1,
            stats_for_edu=65,
        )


@pytest.mark.asyncio
async def test_set_player_skills_wrong_occupation_values_raises(skill_service, mock_persistence):
    """occupation_slots with wrong value set (e.g. two 70s) raises ValueError."""
    mock_profession = MagicMock()
    mock_profession.get_skill_modifiers = MagicMock(return_value=[])
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    slots = _occupation_slots_9()
    slots[1]["value"] = 70

    with pytest.raises(ValueError, match="one 70, two 60, three 50, three 40"):
        await skill_service.set_player_skills(
            player_id=uuid.uuid4(),
            occupation_slots=slots,
            personal_interest=_personal_interest_4(),
            profession_id=1,
            stats_for_edu=65,
        )


@pytest.mark.asyncio
async def test_set_player_skills_personal_interest_not_four_raises(skill_service, mock_persistence):
    """personal_interest must have exactly 4 entries."""
    mock_profession = MagicMock()
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    with pytest.raises(ValueError, match="exactly 4 entries"):
        await skill_service.set_player_skills(
            player_id=uuid.uuid4(),
            occupation_slots=_occupation_slots_9(),
            personal_interest=[{"skill_id": 1}],
            profession_id=1,
            stats_for_edu=65,
        )


@pytest.mark.asyncio
async def test_set_player_skills_duplicate_occupation_skill_ids_raises(skill_service, mock_persistence):
    """occupation_slots with duplicate skill_id raises ValueError."""
    mock_profession = MagicMock()
    mock_profession.get_skill_modifiers = MagicMock(return_value=[])
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    slots = _occupation_slots_9()
    slots[1] = {"skill_id": 1, "value": 60}

    with pytest.raises(ValueError, match="unique skill_id per slot"):
        await skill_service.set_player_skills(
            player_id=uuid.uuid4(),
            occupation_slots=slots,
            personal_interest=_personal_interest_4(),
            profession_id=1,
            stats_for_edu=65,
        )


@pytest.mark.asyncio
async def test_set_player_skills_duplicate_personal_skill_ids_raises(skill_service, mock_persistence):
    """personal_interest with duplicate skill_id raises ValueError."""
    mock_profession = MagicMock()
    mock_profession.get_skill_modifiers = MagicMock(return_value=[])
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    personal = [{"skill_id": 12}, {"skill_id": 13}, {"skill_id": 14}, {"skill_id": 12}]

    with pytest.raises(ValueError, match="unique skill_id per slot"):
        await skill_service.set_player_skills(
            player_id=uuid.uuid4(),
            occupation_slots=_occupation_slots_9(),
            personal_interest=personal,
            profession_id=1,
            stats_for_edu=65,
        )


@pytest.mark.asyncio
async def test_set_player_skills_overlap_occupation_and_personal_raises(skill_service, mock_persistence):
    """Occupation and personal interest sharing a skill_id raises ValueError."""
    mock_profession = MagicMock()
    mock_profession.get_skill_modifiers = MagicMock(return_value=[])
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    personal_with_overlap = [{"skill_id": 12}, {"skill_id": 13}, {"skill_id": 14}, {"skill_id": 1}]

    with pytest.raises(ValueError, match="must not share any skill"):
        await skill_service.set_player_skills(
            player_id=uuid.uuid4(),
            occupation_slots=_occupation_slots_9(),
            personal_interest=personal_with_overlap,
            profession_id=1,
            stats_for_edu=65,
        )


@pytest.mark.asyncio
async def test_get_player_skills_owner_returns_list(
    skill_service,
    mock_persistence,
    mock_player_skill_repo,
):
    """get_player_skills for owned player returns list of skill dicts."""
    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.user_id = user_id
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

    ps1 = MagicMock()
    ps1.skill_id = 1
    ps1.skill = MagicMock()
    ps1.skill.key = "accounting"
    ps1.skill.name = "Accounting"
    ps1.value = 70
    mock_player_skill_repo.get_by_player_id = AsyncMock(return_value=[ps1])

    result = await skill_service.get_player_skills(player_id, user_id)

    assert result is not None
    assert len(result) == 1
    assert result[0]["skill_id"] == 1
    assert result[0]["skill_key"] == "accounting"
    assert result[0]["skill_name"] == "Accounting"
    assert result[0]["value"] == 70


@pytest.mark.asyncio
async def test_get_player_skills_non_owner_returns_none(skill_service, mock_persistence):
    """get_player_skills for another user's player returns None."""
    player_id = uuid.uuid4()
    owner_id = uuid.uuid4()
    other_user_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.user_id = owner_id
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

    result = await skill_service.get_player_skills(player_id, other_user_id)

    assert result is None


# --- Plan 10.4 T2–T5: skill use logging and improvement ---


@pytest.mark.asyncio
async def test_record_successful_skill_use_calls_repo(skill_service, mock_skill_use_log_repo):
    """record_successful_skill_use delegates to repo.record_use with correct args."""
    player_id = uuid.uuid4()
    await skill_service.record_successful_skill_use(
        player_id=player_id,
        skill_id=2,
        character_level_at_use=3,
    )
    mock_skill_use_log_repo.record_use.assert_awaited_once_with(
        player_id=player_id,
        skill_id=2,
        character_level_at_use=3,
    )


@pytest.mark.asyncio
async def test_get_skills_used_this_level_returns_repo_result(skill_service, mock_skill_use_log_repo):
    """get_skills_used_this_level returns distinct skill_ids from repo."""
    player_id = uuid.uuid4()
    mock_skill_use_log_repo.get_skill_ids_used_at_level.return_value = [1, 2, 5]
    result = await skill_service.get_skills_used_this_level(
        player_id=player_id,
        character_level=2,
    )
    assert result == [1, 2, 5]
    mock_skill_use_log_repo.get_skill_ids_used_at_level.assert_awaited_once_with(
        player_id=player_id,
        character_level=2,
    )


@pytest.mark.asyncio
async def test_run_improvement_rolls_previous_level_under_1_no_op(
    skill_service, mock_skill_use_log_repo, mock_player_skill_repo
):
    """run_improvement_rolls with new_level 1 does nothing (previous level 0)."""
    player_id = uuid.uuid4()
    await skill_service.run_improvement_rolls(player_id, new_level=1)
    mock_skill_use_log_repo.get_skill_ids_used_at_level.assert_not_called()
    mock_player_skill_repo.update_value.assert_not_called()


@pytest.mark.asyncio
async def test_run_improvement_rolls_no_skills_used_no_updates(
    skill_service, mock_skill_use_log_repo, mock_player_skill_repo
):
    """run_improvement_rolls when no skills used at previous level does not update."""
    player_id = uuid.uuid4()
    mock_skill_use_log_repo.get_skill_ids_used_at_level.return_value = []
    await skill_service.run_improvement_rolls(player_id, new_level=3)
    mock_skill_use_log_repo.get_skill_ids_used_at_level.assert_awaited_once_with(
        player_id=player_id,
        character_level=2,
    )
    mock_player_skill_repo.get_by_player_id.assert_not_called()
    mock_player_skill_repo.update_value.assert_not_called()


@pytest.mark.asyncio
async def test_run_improvement_rolls_improvement_applied_when_roll_exceeds_value(
    skill_service, mock_skill_use_log_repo, mock_player_skill_repo
):
    """When roll > current value, update_value called with new value (gain 1 or 1d10)."""
    player_id = uuid.uuid4()
    mock_skill_use_log_repo.get_skill_ids_used_at_level.return_value = [1]
    ps = MagicMock()
    ps.skill_id = 1
    ps.value = 50
    mock_player_skill_repo.get_by_player_id = AsyncMock(return_value=[ps])
    # Force roll > 50 so improvement happens; gain is 1d10 so 1-10
    with patch(
        "server.game.skill_service.random.randint",
        side_effect=[99, 5],
    ):  # roll=99 (>50), gain=5
        await skill_service.run_improvement_rolls(player_id, new_level=2)
    mock_player_skill_repo.update_value.assert_awaited_once_with(player_id, 1, 55)  # 50 + 5


@pytest.mark.asyncio
async def test_run_improvement_rolls_high_skill_gains_one(
    skill_service, mock_skill_use_log_repo, mock_player_skill_repo
):
    """When current >= 90, successful improvement adds 1 (cap 99)."""
    player_id = uuid.uuid4()
    mock_skill_use_log_repo.get_skill_ids_used_at_level.return_value = [2]
    ps = MagicMock()
    ps.skill_id = 2
    ps.value = 92
    mock_player_skill_repo.get_by_player_id = AsyncMock(return_value=[ps])
    with patch(
        "server.game.skill_service.random.randint",
        return_value=99,
    ):  # roll 99 > 92 -> gain 1
        await skill_service.run_improvement_rolls(player_id, new_level=2)
    mock_player_skill_repo.update_value.assert_awaited_once_with(player_id, 2, 93)


@pytest.mark.asyncio
async def test_run_improvement_rolls_roll_under_current_no_change(
    skill_service, mock_skill_use_log_repo, mock_player_skill_repo
):
    """When roll <= current value, no update_value call."""
    player_id = uuid.uuid4()
    mock_skill_use_log_repo.get_skill_ids_used_at_level.return_value = [1]
    ps = MagicMock()
    ps.skill_id = 1
    ps.value = 70
    mock_player_skill_repo.get_by_player_id = AsyncMock(return_value=[ps])
    with patch(
        "server.game.skill_service.random.randint",
        return_value=50,
    ):  # 50 <= 70, no improvement
        await skill_service.run_improvement_rolls(player_id, new_level=2)
    mock_player_skill_repo.update_value.assert_not_called()


@pytest.mark.asyncio
async def test_roll_skill_check_unknown_skill_returns_false(
    skill_service, mock_player_skill_repo, mock_skill_use_log_repo
):
    """roll_skill_check when player has no value for skill_id returns False."""
    player_id = uuid.uuid4()
    mock_player_skill_repo.get_by_player_id = AsyncMock(return_value=[])
    result = await skill_service.roll_skill_check(
        player_id=player_id,
        skill_id=99,
        character_level=1,
    )
    assert result is False
    mock_skill_use_log_repo.record_use.assert_not_called()


@pytest.mark.asyncio
async def test_roll_skill_check_success_records_use_and_returns_true(
    skill_service, mock_player_skill_repo, mock_skill_use_log_repo
):
    """When roll <= skill value, record_use is called and returns True."""
    player_id = uuid.uuid4()
    ps = MagicMock()
    ps.skill_id = 2
    ps.value = 60
    mock_player_skill_repo.get_by_player_id = AsyncMock(return_value=[ps])
    with patch(
        "server.game.skill_service.random.randint",
        return_value=40,
    ):  # 40 <= 60 success
        result = await skill_service.roll_skill_check(
            player_id=player_id,
            skill_id=2,
            character_level=2,
        )
    assert result is True
    mock_skill_use_log_repo.record_use.assert_awaited_once_with(
        player_id=player_id,
        skill_id=2,
        character_level_at_use=2,
    )


@pytest.mark.asyncio
async def test_roll_skill_check_failure_does_not_record(skill_service, mock_player_skill_repo, mock_skill_use_log_repo):
    """When roll > skill value, record_use is not called and returns False."""
    player_id = uuid.uuid4()
    ps = MagicMock()
    ps.skill_id = 2
    ps.value = 30
    mock_player_skill_repo.get_by_player_id = AsyncMock(return_value=[ps])
    with patch(
        "server.game.skill_service.random.randint",
        return_value=80,
    ):  # 80 > 30 failure
        result = await skill_service.roll_skill_check(
            player_id=player_id,
            skill_id=2,
            character_level=1,
        )
    assert result is False
    mock_skill_use_log_repo.record_use.assert_not_called()
