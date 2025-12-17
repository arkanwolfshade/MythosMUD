"""
Tests for spell materials service.

This module tests the SpellMaterialsService class which handles
checking and consuming spell materials from player inventory.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.game.magic.spell_materials import SpellMaterialsService
from server.models.spell import Spell, SpellEffectType, SpellMaterial, SpellRangeType, SpellSchool, SpellTargetType


class TestSpellMaterialsService:
    """Test SpellMaterialsService class."""

    @pytest.fixture
    def mock_player_service(self):
        """Create a mock PlayerService."""
        mock_service = MagicMock()
        mock_service.persistence = AsyncMock()
        return mock_service

    @pytest.fixture
    def service(self, mock_player_service):
        """Create a SpellMaterialsService instance."""
        return SpellMaterialsService(mock_player_service)

    @pytest.fixture
    def mock_player(self):
        """Create a mock player."""
        player = MagicMock()
        player.player_id = uuid4()
        player.get_inventory.return_value = []
        player.set_inventory = MagicMock()
        return player

    @pytest.fixture
    def basic_spell(self):
        """Create a basic spell with no materials."""
        return Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[],
        )

    @pytest.mark.asyncio
    async def test_init(self, mock_player_service):
        """Test SpellMaterialsService initialization."""
        service = SpellMaterialsService(mock_player_service)
        assert service.player_service == mock_player_service

    @pytest.mark.asyncio
    async def test_check_materials_no_materials(self, service, mock_player, basic_spell):
        """Test checking materials when spell has no materials."""
        result = await service.check_materials(mock_player.player_id, basic_spell)
        assert result == []
        mock_player.get_inventory.assert_not_called()

    @pytest.mark.asyncio
    async def test_check_materials_player_not_found(self, service, mock_player_service, basic_spell):
        """Test checking materials when player is not found."""
        player_id = uuid4()
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[SpellMaterial(item_id="material1", consumed=True)],
        )

        result = await service.check_materials(player_id, spell)
        assert result == ["material1"]

    @pytest.mark.asyncio
    async def test_check_materials_all_present(self, service, mock_player_service, mock_player, basic_spell):
        """Test checking materials when all materials are present."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player.get_inventory.return_value = [
            {"item_id": "material1", "quantity": 1},
            {"item_id": "material2", "quantity": 1},
        ]

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[
                SpellMaterial(item_id="material1", consumed=True),
                SpellMaterial(item_id="material2", consumed=False),
            ],
        )

        result = await service.check_materials(mock_player.player_id, spell)
        assert result == []

    @pytest.mark.asyncio
    async def test_check_materials_some_missing(self, service, mock_player_service, mock_player, basic_spell):
        """Test checking materials when some materials are missing."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player.get_inventory.return_value = [{"item_id": "material1", "quantity": 1}]

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[
                SpellMaterial(item_id="material1", consumed=True),
                SpellMaterial(item_id="material2", consumed=False),
            ],
        )

        result = await service.check_materials(mock_player.player_id, spell)
        assert result == ["material2"]

    @pytest.mark.asyncio
    async def test_check_materials_match_by_prototype_id(self, service, mock_player_service, mock_player, basic_spell):
        """Test checking materials when items match by prototype_id."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player.get_inventory.return_value = [{"prototype_id": "material1", "quantity": 1}]

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[SpellMaterial(item_id="material1", consumed=True)],
        )

        result = await service.check_materials(mock_player.player_id, spell)
        assert result == []

    @pytest.mark.asyncio
    async def test_consume_materials_no_materials(self, service, basic_spell):
        """Test consuming materials when spell has no materials."""
        result = await service.consume_materials(uuid4(), basic_spell)
        assert result == {"success": True, "message": ""}

    @pytest.mark.asyncio
    async def test_consume_materials_player_not_found(self, service, mock_player_service, basic_spell):
        """Test consuming materials when player is not found."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[SpellMaterial(item_id="material1", consumed=True)],
        )

        result = await service.consume_materials(uuid4(), spell)
        assert result == {"success": False, "message": "Player not found."}

    @pytest.mark.asyncio
    async def test_consume_materials_missing_material(self, service, mock_player_service, mock_player, basic_spell):
        """Test consuming materials when a required material is missing."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player.get_inventory.return_value = []

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[SpellMaterial(item_id="material1", consumed=True)],
        )

        result = await service.consume_materials(mock_player.player_id, spell)
        assert result == {"success": False, "message": "Missing required material: material1."}
        mock_player.set_inventory.assert_not_called()

    @pytest.mark.asyncio
    async def test_consume_materials_consumed_single_quantity(
        self, service, mock_player_service, mock_player, basic_spell
    ):
        """Test consuming materials when material is consumed and quantity is 1."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player_service.persistence.save_player = AsyncMock()
        mock_player.get_inventory.return_value = [{"item_id": "material1", "quantity": 1}]

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[SpellMaterial(item_id="material1", consumed=True)],
        )

        with patch("server.game.magic.spell_materials.logger"):
            result = await service.consume_materials(mock_player.player_id, spell)

            assert result == {"success": True, "message": "", "consumed": ["material1"]}
            mock_player.set_inventory.assert_called_once()
            # Item should be removed (not in final_inventory)
            final_inventory = mock_player.set_inventory.call_args[0][0]
            assert len(final_inventory) == 0
            mock_player_service.persistence.save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_consume_materials_consumed_multiple_quantity(
        self, service, mock_player_service, mock_player, basic_spell
    ):
        """Test consuming materials when material is consumed and quantity > 1."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player_service.persistence.save_player = AsyncMock()
        mock_player.get_inventory.return_value = [
            {"item_id": "material1", "quantity": 3},
            {"item_id": "other_item", "quantity": 1},
        ]

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[SpellMaterial(item_id="material1", consumed=True)],
        )

        with patch("server.game.magic.spell_materials.logger"):
            result = await service.consume_materials(mock_player.player_id, spell)

            assert result == {"success": True, "message": "", "consumed": ["material1"]}
            mock_player.set_inventory.assert_called_once()
            # Item quantity should be reduced
            final_inventory = mock_player.set_inventory.call_args[0][0]
            assert len(final_inventory) == 2
            material_item = next((item for item in final_inventory if item.get("item_id") == "material1"), None)
            assert material_item is not None
            assert material_item["quantity"] == 2
            # Other item should remain
            other_item = next((item for item in final_inventory if item.get("item_id") == "other_item"), None)
            assert other_item is not None
            mock_player_service.persistence.save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_consume_materials_not_consumed(self, service, mock_player_service, mock_player, basic_spell):
        """Test consuming materials when material is not consumed (reusable)."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player_service.persistence.save_player = AsyncMock()
        mock_player.get_inventory.return_value = [{"item_id": "material1", "quantity": 1}]

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[SpellMaterial(item_id="material1", consumed=False)],
        )

        with patch("server.game.magic.spell_materials.logger"):
            result = await service.consume_materials(mock_player.player_id, spell)

            assert result == {"success": True, "message": "", "consumed": []}
            mock_player.set_inventory.assert_called_once()
            # Item should remain in inventory
            final_inventory = mock_player.set_inventory.call_args[0][0]
            assert len(final_inventory) == 1
            assert final_inventory[0]["item_id"] == "material1"
            assert final_inventory[0]["quantity"] == 1
            mock_player_service.persistence.save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_consume_materials_multiple_materials(self, service, mock_player_service, mock_player, basic_spell):
        """Test consuming multiple materials."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player_service.persistence.save_player = AsyncMock()
        mock_player.get_inventory.return_value = [
            {"item_id": "material1", "quantity": 1},
            {"item_id": "material2", "quantity": 2},
            {"item_id": "other_item", "quantity": 1},
        ]

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[
                SpellMaterial(item_id="material1", consumed=True),
                SpellMaterial(item_id="material2", consumed=False),
            ],
        )

        with patch("server.game.magic.spell_materials.logger"):
            result = await service.consume_materials(mock_player.player_id, spell)

            assert result == {"success": True, "message": "", "consumed": ["material1"]}
            mock_player.set_inventory.assert_called_once()
            final_inventory = mock_player.set_inventory.call_args[0][0]
            # material1 should be removed (consumed, quantity 1)
            # material2 should remain (not consumed)
            # other_item should remain
            assert len(final_inventory) == 2
            material1 = next((item for item in final_inventory if item.get("item_id") == "material1"), None)
            assert material1 is None
            material2 = next((item for item in final_inventory if item.get("item_id") == "material2"), None)
            assert material2 is not None
            assert material2["quantity"] == 2
            mock_player_service.persistence.save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_consume_materials_match_by_prototype_id(
        self, service, mock_player_service, mock_player, basic_spell
    ):
        """Test consuming materials when items match by prototype_id."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player_service.persistence.save_player = AsyncMock()
        mock_player.get_inventory.return_value = [{"prototype_id": "material1", "quantity": 1}]

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[SpellMaterial(item_id="material1", consumed=True)],
        )

        with patch("server.game.magic.spell_materials.logger"):
            result = await service.consume_materials(mock_player.player_id, spell)

            assert result == {"success": True, "message": "", "consumed": ["material1"]}
            mock_player_service.persistence.save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_consume_materials_no_quantity_field(self, service, mock_player_service, mock_player, basic_spell):
        """Test consuming materials when item has no quantity field (defaults to 1)."""
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player_service.persistence.save_player = AsyncMock()
        mock_player.get_inventory.return_value = [{"item_id": "material1"}]

        spell = Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            materials=[SpellMaterial(item_id="material1", consumed=True)],
        )

        with patch("server.game.magic.spell_materials.logger"):
            result = await service.consume_materials(mock_player.player_id, spell)

            assert result == {"success": True, "message": "", "consumed": ["material1"]}
            # Item should be removed (quantity defaults to 1, so consumed)
            final_inventory = mock_player.set_inventory.call_args[0][0]
            assert len(final_inventory) == 0
