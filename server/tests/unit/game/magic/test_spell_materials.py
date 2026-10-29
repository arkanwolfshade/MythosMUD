"""Unit tests for spell material checking and consumption."""

import json
import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.magic.spell_materials import SpellMaterialsService
from server.game.player_registry import DbSession, PlayerAggregate, PlayerRegistry
from server.models.spell import Spell, SpellEffectType, SpellMaterial, SpellRangeType, SpellSchool, SpellTargetType
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, raw_row


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


def _herb(item_id: str, quantity: int) -> dict[str, object]:
    return {"item_id": item_id, "item_name": item_id.title(), "slot_type": "inventory", "quantity": quantity}


def _registered(carried: list[dict[str, object]] | None) -> tuple[SpellMaterialsService, FakeDatabase, uuid.UUID]:
    """A materials service over a real registry; ``carried=None`` means there is no such player."""
    db = FakeDatabase()
    player_id = uuid.uuid4()

    async def load(_session: DbSession, pid: uuid.UUID) -> PlayerAggregate | None:
        return None if carried is None else aggregate(raw_row(pid, inventory=json.dumps(carried)))

    return SpellMaterialsService(MagicMock(), PlayerRegistry(db.session, loader=load)), db, player_id


def _committed_carried(db: FakeDatabase) -> list[dict[str, object]]:
    write = db.last_inventory_write()
    assert write is not None, "nothing was committed"
    return cast(list[dict[str, object]], json.loads(str(write["inventory_json"])))


@pytest.mark.asyncio
async def test_consume_materials_player_not_found() -> None:
    service, db, player_id = _registered(None)

    result = await service.consume_materials(player_id, _spell(SpellMaterial(item_id="herb_1")))

    assert result == {"success": False, "message": "Player not found."}
    assert db.executed == []


@pytest.mark.asyncio
async def test_consume_materials_decrements_quantity_and_commits_it() -> None:
    """ADR-029 step 4c-i: the live inventory, one registry unit, no full-row save."""
    service, db, player_id = _registered([_herb("herb_1", 2), _herb("candle", 1)])

    result = await service.consume_materials(player_id, _spell(SpellMaterial(item_id="herb_1", consumed=True)))

    assert result["success"] is True
    assert result["consumed"] == ["herb_1"]
    assert [(stack["item_id"], stack["quantity"]) for stack in _committed_carried(db)] == [
        ("herb_1", 1),
        ("candle", 1),
    ]
    assert db.commits == 1


@pytest.mark.asyncio
async def test_consume_materials_non_consumed_keeps_item_and_writes_nothing() -> None:
    service, db, player_id = _registered([_herb("focus_1", 1)])

    result = await service.consume_materials(player_id, _spell(SpellMaterial(item_id="focus_1", consumed=False)))

    assert result["success"] is True
    assert result.get("consumed", []) == []
    assert db.executed == []


@pytest.mark.asyncio
async def test_consume_materials_missing_one_takes_none() -> None:
    service, db, player_id = _registered([_herb("herb_1", 1)])
    spell = _spell(SpellMaterial(item_id="herb_1", consumed=True), SpellMaterial(item_id="bone", consumed=True))

    result = await service.consume_materials(player_id, spell)

    assert result == {"success": False, "message": "Missing required material: bone."}
    assert db.executed == []


def test_process_material_requirement_skips_processed_index(materials_service):
    material = SpellMaterial(item_id="herb_1")
    inventory = [{"item_id": "herb_1"}]
    found, index, consume = materials_service._process_material_requirement(material, inventory, {0})
    assert found is False
    assert index is None
    assert consume is False
