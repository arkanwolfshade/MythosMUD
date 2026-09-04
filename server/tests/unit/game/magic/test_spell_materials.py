"""Unit tests for spell material checking and consumption."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.magic.spell_materials import SpellMaterialsService
from server.models.spell import Spell, SpellEffectType, SpellMaterial, SpellRangeType, SpellSchool, SpellTargetType


def _spell(*materials: SpellMaterial) -> Spell:
    return Spell(
        spell_id="test_spell",
        name="Test Spell",
        description="A test spell",
        school=SpellSchool.MYTHOS,
        mp_cost=5,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
        materials=list(materials),
    )


@pytest.fixture
def player_service():
    service = MagicMock()
    service.persistence = MagicMock()
    return service


@pytest.fixture
def materials_service(player_service):
    return SpellMaterialsService(player_service)


@pytest.mark.asyncio
async def test_check_materials_empty_spell(materials_service):
    missing = await materials_service.check_materials(uuid.uuid4(), _spell())
    assert missing == []


@pytest.mark.asyncio
async def test_check_materials_missing_player(materials_service, player_service):
    player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    spell = _spell(SpellMaterial(item_id="herb_1"))
    missing = await materials_service.check_materials(uuid.uuid4(), spell)
    assert missing == ["herb_1"]


@pytest.mark.asyncio
async def test_check_materials_all_present(materials_service, player_service):
    player = MagicMock()
    player.get_inventory.return_value = [{"item_id": "herb_1", "quantity": 2}]
    player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    spell = _spell(SpellMaterial(item_id="herb_1"))
    missing = await materials_service.check_materials(uuid.uuid4(), spell)
    assert missing == []


@pytest.mark.asyncio
async def test_check_materials_reports_missing(materials_service, player_service):
    player = MagicMock()
    player.get_inventory.return_value = [{"prototype_id": "other_item"}]
    player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    spell = _spell(SpellMaterial(item_id="herb_1"))
    missing = await materials_service.check_materials(uuid.uuid4(), spell)
    assert missing == ["herb_1"]


@pytest.mark.asyncio
async def test_consume_materials_no_materials(materials_service):
    result = await materials_service.consume_materials(uuid.uuid4(), _spell())
    assert result["success"] is True


@pytest.mark.asyncio
async def test_consume_materials_player_not_found(materials_service, player_service):
    player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    spell = _spell(SpellMaterial(item_id="herb_1"))
    result = await materials_service.consume_materials(uuid.uuid4(), spell)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_consume_materials_decrements_quantity(materials_service, player_service):
    player = MagicMock()
    player.get_inventory.return_value = [{"item_id": "herb_1", "quantity": 2}]
    player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    player_service.persistence.save_player = AsyncMock()
    spell = _spell(SpellMaterial(item_id="herb_1", consumed=True))
    result = await materials_service.consume_materials(uuid.uuid4(), spell)
    assert result["success"] is True
    assert result["consumed"] == ["herb_1"]
    saved_inventory = player.set_inventory.call_args[0][0]
    assert saved_inventory[0]["quantity"] == 1
    player_service.persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_consume_materials_non_consumed_keeps_item(materials_service, player_service):
    player = MagicMock()
    player.get_inventory.return_value = [{"item_id": "focus_1", "quantity": 1}]
    player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    player_service.persistence.save_player = AsyncMock()
    spell = _spell(SpellMaterial(item_id="focus_1", consumed=False))
    result = await materials_service.consume_materials(uuid.uuid4(), spell)
    assert result["success"] is True
    assert result.get("consumed", []) == []


def test_process_material_requirement_skips_processed_index(materials_service):
    material = SpellMaterial(item_id="herb_1")
    inventory = [{"item_id": "herb_1"}]
    found, index, consume = materials_service._process_material_requirement(material, inventory, {0})
    assert found is False
    assert index is None
    assert consume is False
