"""
Tests for spell learning service.

This module tests the SpellLearningService class which handles
spell acquisition from various sources including spellbooks, NPCs, and quests.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.game.magic.spell_learning_service import SpellLearningService
from server.game.player_service import PlayerService
from server.models.spell import Spell, SpellEffectType, SpellRangeType, SpellSchool, SpellTargetType


class TestSpellLearningService:
    """Test SpellLearningService functionality."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock()
        mock_persistence.save_player = AsyncMock()
        return mock_persistence

    @pytest.fixture
    def mock_player_service(self, mock_persistence):
        """Create a mock player service."""
        player_service = MagicMock(spec=PlayerService)
        player_service.persistence = mock_persistence
        return player_service

    @pytest.fixture
    def mock_spell_registry(self):
        """Create a mock spell registry."""
        registry = MagicMock()
        registry.get_spell = MagicMock()
        registry.get_spell_by_name = MagicMock()
        return registry

    @pytest.fixture
    def mock_player_spell_repository(self):
        """Create a mock player spell repository."""
        repo = MagicMock()
        repo.get_player_spell = AsyncMock(return_value=None)
        repo.get_player_spells = AsyncMock(return_value=[])
        repo.learn_spell = AsyncMock()
        repo.update_mastery = AsyncMock()
        return repo

    @pytest.fixture
    def spell_learning_service(self, mock_spell_registry, mock_player_service, mock_player_spell_repository):
        """Create spell learning service instance."""
        return SpellLearningService(
            spell_registry=mock_spell_registry,
            player_service=mock_player_service,
            player_spell_repository=mock_player_spell_repository,
        )

    @pytest.fixture
    def sample_spell(self):
        """Create a sample spell."""
        return Spell(
            spell_id="spell-1",
            name="Fireball",
            description="A ball of fire",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.ENTITY,
            range_type=SpellRangeType.SAME_ROOM,
            effect_type=SpellEffectType.DAMAGE,
            effect_data={},
        )

    @pytest.fixture
    def mythos_spell(self):
        """Create a Mythos spell with corruption."""
        return Spell(
            spell_id="spell-mythos-1",
            name="Call of Cthulhu",
            description="Forbidden knowledge",
            school=SpellSchool.MYTHOS,
            mp_cost=50,
            corruption_on_learn=5,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.CORRUPTION_ADJUST,
            effect_data={},
        )

    @pytest.fixture
    def sample_player(self):
        """Create a sample player with stats."""
        player = MagicMock()
        player.player_id = uuid4()
        player.get_stats.return_value = {
            "power": 50,
            "intelligence": 50,
            "corruption": 0,
        }
        return player

    @pytest.mark.asyncio
    async def test_learn_spell_success(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_spell,
        sample_player,
    ):
        """Test successful spell learning."""
        player_id = sample_player.player_id
        mock_spell_registry.get_spell.return_value = sample_spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.spell_learning_service.logger"):
            result = await spell_learning_service.learn_spell(player_id, "spell-1", source="spellbook")

            assert result["success"] is True
            assert "learned" in result["message"].lower()
            assert result["spell_name"] == "Fireball"
            assert result["corruption_applied"] == 0
            mock_player_spell_repository.learn_spell.assert_called_once()

    @pytest.mark.asyncio
    async def test_learn_spell_not_found_by_id(self, spell_learning_service, mock_spell_registry):
        """Test learning spell when spell is not found by ID."""
        player_id = uuid4()
        mock_spell_registry.get_spell.return_value = None
        mock_spell_registry.get_spell_by_name.return_value = None

        result = await spell_learning_service.learn_spell(player_id, "nonexistent", source="spellbook")

        assert result["success"] is False
        assert "not found" in result["message"]

    @pytest.mark.asyncio
    async def test_learn_spell_found_by_name(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_spell,
        sample_player,
    ):
        """Test learning spell found by name when not found by ID."""
        player_id = sample_player.player_id
        mock_spell_registry.get_spell.return_value = None
        mock_spell_registry.get_spell_by_name.return_value = sample_spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.spell_learning_service.logger"):
            result = await spell_learning_service.learn_spell(player_id, "Fireball", source="spellbook")

            assert result["success"] is True
            mock_spell_registry.get_spell_by_name.assert_called_once_with("Fireball")

    @pytest.mark.asyncio
    async def test_learn_spell_player_not_found(
        self, spell_learning_service, mock_spell_registry, mock_player_service, sample_spell
    ):
        """Test learning spell when player is not found."""
        player_id = uuid4()
        mock_spell_registry.get_spell.return_value = sample_spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=None)

        result = await spell_learning_service.learn_spell(player_id, "spell-1", source="spellbook")

        assert result["success"] is False
        assert "not recognized" in result["message"]

    @pytest.mark.asyncio
    async def test_learn_spell_already_known(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_spell,
        sample_player,
    ):
        """Test learning spell that is already known."""
        player_id = sample_player.player_id
        mock_spell_registry.get_spell.return_value = sample_spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        # Mock existing spell
        existing_spell = MagicMock()
        existing_spell.spell_id = "spell-1"
        mock_player_spell_repository.get_player_spell = AsyncMock(return_value=existing_spell)

        result = await spell_learning_service.learn_spell(player_id, "spell-1", source="spellbook")

        assert result["success"] is False
        assert "already know" in result["message"]
        assert result["already_known"] is True
        mock_player_spell_repository.learn_spell.assert_not_called()

    @pytest.mark.asyncio
    async def test_learn_spell_with_corruption(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        mythos_spell,
        sample_player,
    ):
        """Test learning Mythos spell applies corruption."""
        player_id = sample_player.player_id
        mock_spell_registry.get_spell.return_value = mythos_spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.spell_learning_service.logger"):
            result = await spell_learning_service.learn_spell(player_id, "spell-mythos-1", source="spellbook")

            assert result["success"] is True
            assert result["corruption_applied"] == 5
            assert sample_player.get_stats()["corruption"] == 5
            mock_player_service.persistence.save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_learn_spell_prerequisite_power_failed(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_player,
    ):
        """Test learning spell fails when power prerequisite is not met."""
        player_id = sample_player.player_id
        spell = Spell(
            spell_id="spell-1",
            name="Powerful Spell",
            description="Requires high power",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            effect_data={"required_power": 100},
        )
        mock_spell_registry.get_spell.return_value = spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await spell_learning_service.learn_spell(player_id, "spell-1", source="spellbook")

        assert result["success"] is False
        assert "requires Power" in result["message"]
        assert result["prerequisite_failed"] is True

    @pytest.mark.asyncio
    async def test_learn_spell_prerequisite_intelligence_failed(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_player,
    ):
        """Test learning spell fails when intelligence prerequisite is not met."""
        player_id = sample_player.player_id
        spell = Spell(
            spell_id="spell-1",
            name="Complex Spell",
            description="Requires high intelligence",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            effect_data={"required_intelligence": 100},
        )
        mock_spell_registry.get_spell.return_value = spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await spell_learning_service.learn_spell(player_id, "spell-1", source="spellbook")

        assert result["success"] is False
        assert "requires Intelligence" in result["message"]
        assert result["prerequisite_failed"] is True

    @pytest.mark.asyncio
    async def test_learn_spell_prerequisite_spells_failed(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_spell,
        sample_player,
    ):
        """Test learning spell fails when required spells are not known."""
        player_id = sample_player.player_id
        spell = Spell(
            spell_id="spell-2",
            name="Advanced Spell",
            description="Requires prerequisite spells",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            effect_data={"required_spells": ["spell-prereq-1", "spell-prereq-2"]},
        )
        mock_spell_registry.get_spell.return_value = spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        # Mock prerequisite spell lookup
        prereq_spell = MagicMock()
        prereq_spell.name = "Prerequisite Spell"
        mock_spell_registry.get_spell.return_value = spell
        mock_spell_registry.get_spell.side_effect = [spell, prereq_spell, None]  # spell, prereq1, prereq2 (not found)

        result = await spell_learning_service.learn_spell(player_id, "spell-2", source="spellbook")

        assert result["success"] is False
        assert "requires knowledge of" in result["message"]
        assert result["prerequisite_failed"] is True

    @pytest.mark.asyncio
    async def test_learn_spell_repository_error(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_spell,
        sample_player,
    ):
        """Test learning spell handles repository errors."""
        player_id = sample_player.player_id
        mock_spell_registry.get_spell.return_value = sample_spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)
        mock_player_spell_repository.learn_spell = AsyncMock(side_effect=OSError("Database error"))

        with patch("server.game.magic.spell_learning_service.logger") as mock_logger:
            result = await spell_learning_service.learn_spell(player_id, "spell-1", source="spellbook")

            assert result["success"] is False
            assert "Failed to learn spell" in result["message"]
            mock_logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_learn_spell_from_book_no_spell_id(self, spell_learning_service):
        """Test learning spell from book without specifying spell ID."""
        player_id = uuid4()
        result = await spell_learning_service.learn_spell_from_book(player_id, "book-123", spell_id=None)

        assert result["success"] is False
        assert "No spell specified" in result["message"]

    @pytest.mark.asyncio
    async def test_learn_spell_from_book_with_spell_id(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_spell,
        sample_player,
    ):
        """Test learning spell from book with spell ID."""
        player_id = sample_player.player_id
        mock_spell_registry.get_spell.return_value = sample_spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.spell_learning_service.logger"):
            result = await spell_learning_service.learn_spell_from_book(player_id, "book-123", spell_id="spell-1")

            assert result["success"] is True
            assert result["source"] == "spellbook"

    @pytest.mark.asyncio
    async def test_learn_spell_from_npc(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_spell,
        sample_player,
    ):
        """Test learning spell from NPC teacher."""
        player_id = sample_player.player_id
        mock_spell_registry.get_spell.return_value = sample_spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.spell_learning_service.logger"):
            result = await spell_learning_service.learn_spell_from_npc(player_id, "npc-123", "spell-1")

            assert result["success"] is True
            assert "npc_teacher:npc-123" in result["source"]

    @pytest.mark.asyncio
    async def test_learn_spell_from_quest(
        self,
        spell_learning_service,
        mock_spell_registry,
        mock_player_service,
        mock_player_spell_repository,
        sample_spell,
        sample_player,
    ):
        """Test learning spell from quest reward."""
        player_id = sample_player.player_id
        mock_spell_registry.get_spell.return_value = sample_spell
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.spell_learning_service.logger"):
            result = await spell_learning_service.learn_spell_from_quest(player_id, "quest-123", "spell-1")

            assert result["success"] is True
            assert "quest_reward:quest-123" in result["source"]

    @pytest.mark.asyncio
    async def test_increase_mastery_on_cast_success(
        self, spell_learning_service, mock_player_spell_repository, sample_player
    ):
        """Test increasing mastery on successful cast."""
        player_id = sample_player.player_id
        player_spell = MagicMock()
        player_spell.mastery = 50
        mock_player_spell_repository.get_player_spell = AsyncMock(return_value=player_spell)

        with patch("server.game.magic.spell_learning_service.logger"):
            await spell_learning_service.increase_mastery_on_cast(player_id, "spell-1", cast_success=True)

            mock_player_spell_repository.update_mastery.assert_called_once()
            call_args = mock_player_spell_repository.update_mastery.call_args
            assert call_args[0][0] == player_id
            assert call_args[0][1] == "spell-1"
            assert call_args[0][2] > 50  # Mastery increased

    @pytest.mark.asyncio
    async def test_increase_mastery_on_cast_failure(
        self, spell_learning_service, mock_player_spell_repository, sample_player
    ):
        """Test mastery not increased on failed cast."""
        player_id = sample_player.player_id
        player_spell = MagicMock()
        player_spell.mastery = 50
        mock_player_spell_repository.get_player_spell = AsyncMock(return_value=player_spell)

        await spell_learning_service.increase_mastery_on_cast(player_id, "spell-1", cast_success=False)

        mock_player_spell_repository.update_mastery.assert_not_called()

    @pytest.mark.asyncio
    async def test_increase_mastery_on_cast_spell_not_known(self, spell_learning_service, mock_player_spell_repository):
        """Test mastery not increased when spell is not known."""
        player_id = uuid4()
        mock_player_spell_repository.get_player_spell = AsyncMock(return_value=None)

        await spell_learning_service.increase_mastery_on_cast(player_id, "spell-1", cast_success=True)

        mock_player_spell_repository.update_mastery.assert_not_called()

    @pytest.mark.asyncio
    async def test_increase_mastery_on_cast_at_max(
        self, spell_learning_service, mock_player_spell_repository, sample_player
    ):
        """Test mastery not increased when already at max."""
        player_id = sample_player.player_id
        player_spell = MagicMock()
        player_spell.mastery = 100
        mock_player_spell_repository.get_player_spell = AsyncMock(return_value=player_spell)

        await spell_learning_service.increase_mastery_on_cast(player_id, "spell-1", cast_success=True)

        mock_player_spell_repository.update_mastery.assert_not_called()

    @pytest.mark.asyncio
    async def test_increase_mastery_low_level(
        self, spell_learning_service, mock_player_spell_repository, sample_player
    ):
        """Test mastery increases faster at low levels."""
        player_id = sample_player.player_id
        player_spell = MagicMock()
        player_spell.mastery = 30  # Low level
        mock_player_spell_repository.get_player_spell = AsyncMock(return_value=player_spell)

        with patch("server.game.magic.spell_learning_service.logger"):
            await spell_learning_service.increase_mastery_on_cast(player_id, "spell-1", cast_success=True)

            call_args = mock_player_spell_repository.update_mastery.call_args
            new_mastery = call_args[0][2]
            assert new_mastery >= 32  # Should gain 2 points at low level

    @pytest.mark.asyncio
    async def test_increase_mastery_high_level(
        self, spell_learning_service, mock_player_spell_repository, sample_player
    ):
        """Test mastery increases slower at high levels."""
        player_id = sample_player.player_id
        player_spell = MagicMock()
        player_spell.mastery = 85  # High level
        mock_player_spell_repository.get_player_spell = AsyncMock(return_value=player_spell)

        with patch("server.game.magic.spell_learning_service.logger"):
            await spell_learning_service.increase_mastery_on_cast(player_id, "spell-1", cast_success=True)

            call_args = mock_player_spell_repository.update_mastery.call_args
            new_mastery = call_args[0][2]
            assert new_mastery <= 86  # Should gain 0-1 points at high level

    @pytest.mark.asyncio
    async def test_validate_prerequisites_player_not_found(
        self, spell_learning_service, mock_player_service, sample_spell
    ):
        """Test prerequisite validation when player is not found."""
        player_id = uuid4()
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=None)

        result = await spell_learning_service._validate_prerequisites(player_id, sample_spell)

        assert result["valid"] is False
        assert "not found" in result["error_message"]

    @pytest.mark.asyncio
    async def test_validate_prerequisites_all_met(
        self, spell_learning_service, mock_player_service, mock_player_spell_repository, sample_spell, sample_player
    ):
        """Test prerequisite validation when all prerequisites are met."""
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await spell_learning_service._validate_prerequisites(player_id, sample_spell)

        assert result["valid"] is True

    @pytest.mark.asyncio
    async def test_validate_prerequisites_required_spells_met(
        self, spell_learning_service, mock_player_service, mock_player_spell_repository, sample_player
    ):
        """Test prerequisite validation when required spells are known."""
        player_id = sample_player.player_id
        spell = Spell(
            spell_id="spell-2",
            name="Advanced Spell",
            description="Requires prerequisite",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            effect_data={"required_spells": ["spell-1"]},
        )
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        # Mock player knows the required spell
        known_spell = MagicMock()
        known_spell.spell_id = "spell-1"
        mock_player_spell_repository.get_player_spells = AsyncMock(return_value=[known_spell])

        result = await spell_learning_service._validate_prerequisites(player_id, spell)

        assert result["valid"] is True

    @pytest.mark.asyncio
    async def test_validate_prerequisites_required_spell_not_found_in_registry(
        self,
        spell_learning_service,
        mock_player_service,
        mock_player_spell_repository,
        mock_spell_registry,
        sample_player,
    ):
        """Test prerequisite validation when required spell is not found in registry."""
        player_id = sample_player.player_id
        spell = Spell(
            spell_id="spell-2",
            name="Advanced Spell",
            description="Requires prerequisite",
            school=SpellSchool.ELEMENTAL,
            mp_cost=10,
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
            effect_data={"required_spells": ["unknown-spell"]},
        )
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)
        mock_player_spell_repository.get_player_spells = AsyncMock(return_value=[])
        mock_spell_registry.get_spell.return_value = None

        result = await spell_learning_service._validate_prerequisites(player_id, spell)

        assert result["valid"] is False
        assert "unknown-spell" in result["error_message"]  # Should show spell ID when not found

    def test_service_initialization_with_repository(
        self, mock_spell_registry, mock_player_service, mock_player_spell_repository
    ):
        """Test service initialization with provided repository."""
        with patch("server.game.magic.spell_learning_service.logger"):
            service = SpellLearningService(
                spell_registry=mock_spell_registry,
                player_service=mock_player_service,
                player_spell_repository=mock_player_spell_repository,
            )
            assert service.player_spell_repository == mock_player_spell_repository

    def test_service_initialization_without_repository(self, mock_spell_registry, mock_player_service):
        """Test service initialization creates repository when not provided."""
        with patch("server.game.magic.spell_learning_service.logger"):
            with patch("server.game.magic.spell_learning_service.PlayerSpellRepository") as mock_repo_class:
                service = SpellLearningService(
                    spell_registry=mock_spell_registry,
                    player_service=mock_player_service,
                )
                assert service.player_spell_repository is not None
                mock_repo_class.assert_called_once()
