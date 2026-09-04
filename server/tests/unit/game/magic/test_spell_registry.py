"""Unit tests for SpellRegistry."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.magic.spell_registry import SpellRegistry
from server.models.spell import Spell, SpellEffectType, SpellRangeType, SpellSchool, SpellTargetType


def _spell(spell_id: str, name: str, school: SpellSchool = SpellSchool.ELEMENTAL) -> Spell:
    return Spell(
        spell_id=spell_id,
        name=name,
        description="Test",
        school=school,
        mp_cost=1,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
    )


@pytest.fixture
def repo():
    mock = MagicMock()
    mock.get_all_spells = AsyncMock(return_value=[])
    return mock


@pytest.fixture
def registry(repo):
    return SpellRegistry(spell_repository=repo)


def test_init_not_loaded(registry):
    assert registry.is_loaded() is False
    assert registry.get_spell("x") is None
    assert registry.list_spells() == []
    assert registry.search_spells("x") == []


@pytest.mark.asyncio
async def test_load_spells_skips_when_already_loaded(registry, repo):
    registry._loaded = True
    await registry.load_spells()
    repo.get_all_spells.assert_not_called()


@pytest.mark.asyncio
async def test_load_spells_populates_and_lookup(registry, repo):
    repo.get_all_spells.return_value = [
        _spell("s1", "Fireball").model_dump(),
        _spell("s2", "Cold Snap").model_dump(),
        {"spell_id": "bad", "name": "Broken"},  # invalid row skipped
    ]
    await registry.load_spells()
    assert registry.is_loaded()
    assert registry.get_spell("s1") is not None
    assert registry.get_spell_by_name("fireball").spell_id == "s1"
    assert registry.get_spell_by_name("cold").spell_id == "s2"
    assert registry.get_spell_by_name("nap").spell_id == "s2"
    assert registry.get_spell_by_name("") is None
    assert registry.get_spell_by_name("missing") is None
    assert len(registry.list_spells()) == 2
    assert len(registry.search_spells("fire")) == 1
    assert registry.get_all_spell_ids() == ["s1", "s2"]


@pytest.mark.asyncio
async def test_load_spells_converts_materials_dict(registry, repo):
    repo.get_all_spells.return_value = [
        {
            **_spell("s1", "Rite").model_dump(),
            "materials": [{"item_id": "herb", "consumed": True}],
        }
    ]
    await registry.load_spells()
    spell = registry.get_spell("s1")
    assert spell is not None
    assert spell.materials[0].item_id == "herb"


@pytest.mark.asyncio
async def test_load_spells_filters_by_school(registry, repo):
    repo.get_all_spells.return_value = [
        _spell("a", "Arc", SpellSchool.ELEMENTAL).model_dump(),
        _spell("m", "Myth", SpellSchool.MYTHOS).model_dump(),
    ]
    await registry.load_spells()
    mythos = registry.list_spells(school=SpellSchool.MYTHOS)
    assert len(mythos) == 1
    assert mythos[0].spell_id == "m"


@pytest.mark.asyncio
async def test_load_spells_raises_on_repo_failure(registry, repo):
    repo.get_all_spells.side_effect = OSError("db down")
    with pytest.raises(OSError):
        await registry.load_spells()
