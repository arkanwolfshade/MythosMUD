"""
Unit tests for NPC combat lucidity effects.

Tests the NPCCombatLucidity class for applying lucidity loss during NPC encounters.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.services.npc_combat_lucidity import NPCCombatLucidity


class _RecordingService:
    """Stands in for ActiveLucidityService; records each encounter loss's keyword arguments."""

    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    async def apply_encounter_lucidity_loss(self, **kwargs: object) -> None:
        self.calls.append(kwargs)


class TestNPCCombatLucidity:
    """Test suite for NPCCombatLucidity class."""

    def test_init(self):
        """Test NPCCombatLucidity initialization."""
        lucidity = NPCCombatLucidity(MagicMock())
        assert lucidity is not None

    def test_resolve_lucidity_category_none_npc(self):
        """Test _resolve_lucidity_category returns 'disturbing' for None NPC."""
        lucidity = NPCCombatLucidity(MagicMock())
        result = lucidity._resolve_lucidity_category(None)
        assert result == "disturbing"

    def test_resolve_lucidity_category_from_base_stats(self):
        """Test _resolve_lucidity_category gets category from base_stats."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = {"lucidity_category": "horrific"}
        result = lucidity._resolve_lucidity_category(mock_npc)
        assert result == "horrific"

    def test_resolve_lucidity_category_from_mythos_tier(self):
        """Test _resolve_lucidity_category gets category from mythos_tier."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = {"mythos_tier": "ELDRITCH"}
        result = lucidity._resolve_lucidity_category(mock_npc)
        assert result == "eldritch"

    def test_resolve_lucidity_category_from_behavior_config(self):
        """Test _resolve_lucidity_category gets category from behavior_config."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = {}
        mock_npc.get_behavior_config.return_value = {"lucidity_category": "disturbing"}
        result = lucidity._resolve_lucidity_category(mock_npc)
        assert result == "disturbing"

    def test_resolve_lucidity_category_aggressive_mob(self):
        """Test _resolve_lucidity_category returns 'horrific' for aggressive_mob."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = {}
        mock_npc.get_behavior_config.return_value = {}
        mock_npc.npc_type = "aggressive_mob"
        result = lucidity._resolve_lucidity_category(mock_npc)
        assert result == "horrific"

    def test_resolve_lucidity_category_passive_mob(self):
        """Test _resolve_lucidity_category returns 'disturbing' for passive_mob."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = {}
        mock_npc.get_behavior_config.return_value = {}
        mock_npc.npc_type = "passive_mob"
        result = lucidity._resolve_lucidity_category(mock_npc)
        assert result == "disturbing"

    def test_resolve_lucidity_category_default(self):
        """Test _resolve_lucidity_category returns 'disturbing' as default."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = {}
        mock_npc.get_behavior_config.return_value = {}
        mock_npc.npc_type = "unknown_type"
        result = lucidity._resolve_lucidity_category(mock_npc)
        assert result == "disturbing"

    def test_resolve_lucidity_category_get_base_stats_exception(self):
        """Test _resolve_lucidity_category handles get_base_stats exception."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.get_base_stats.side_effect = ValueError("Test error")
        mock_npc.get_behavior_config.return_value = {}
        result = lucidity._resolve_lucidity_category(mock_npc)
        assert result == "disturbing"

    def test_resolve_lucidity_category_get_behavior_config_exception(self):
        """Test _resolve_lucidity_category handles get_behavior_config exception."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = {}
        mock_npc.get_behavior_config.side_effect = AttributeError("Test error")
        result = lucidity._resolve_lucidity_category(mock_npc)
        assert result == "disturbing"

    def test_resolve_lucidity_category_non_dict_stats(self):
        """Test _resolve_lucidity_category handles non-dict base_stats."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = "not_a_dict"
        mock_npc.get_behavior_config.return_value = {}
        result = lucidity._resolve_lucidity_category(mock_npc)
        assert result == "disturbing"

    @pytest.mark.asyncio
    async def test_apply_encounter_lucidity_effect_without_a_player_registry_skips(self):
        """Lucidity lives in the player registry (ADR-029 step 5b-i): without one, no service is built."""
        with patch("server.services.npc_combat_lucidity.ActiveLucidityService") as mock_service_class:
            await NPCCombatLucidity().apply_encounter_lucidity_effect("player_001", "npc_001", MagicMock(), "room_001")
        mock_service_class.assert_not_called()

    @pytest.mark.asyncio
    async def test_apply_encounter_lucidity_effect_success(self):
        """Test apply_encounter_lucidity_effect successfully applies lucidity loss."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.name = "Test NPC"
        mock_npc.get_base_stats.return_value = {"lucidity_category": "disturbing"}

        mock_service = _RecordingService()

        with patch("server.services.npc_combat_lucidity.ActiveLucidityService", return_value=mock_service):
            await lucidity.apply_encounter_lucidity_effect("player_001", "npc_001", mock_npc, "room_001")

            assert len(mock_service.calls) == 1

    @pytest.mark.asyncio
    async def test_apply_encounter_lucidity_effect_with_npc_name(self):
        """Test apply_encounter_lucidity_effect uses NPC name as archetype."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.name = "Eldritch Horror"
        mock_npc.get_base_stats.return_value = {"lucidity_category": "horrific"}

        mock_service = _RecordingService()

        with patch("server.services.npc_combat_lucidity.ActiveLucidityService", return_value=mock_service):
            await lucidity.apply_encounter_lucidity_effect("player_001", "npc_001", mock_npc, "room_001")

            [call] = mock_service.calls
            assert call["entity_archetype"] == "Eldritch Horror"

    @pytest.mark.asyncio
    async def test_apply_encounter_lucidity_effect_without_npc_name(self):
        """Test apply_encounter_lucidity_effect uses NPC ID when name not available."""
        lucidity = NPCCombatLucidity(MagicMock())
        mock_npc = MagicMock()
        mock_npc.name = None
        mock_npc.get_base_stats.return_value = {"lucidity_category": "disturbing"}

        mock_service = _RecordingService()

        with patch("server.services.npc_combat_lucidity.ActiveLucidityService", return_value=mock_service):
            await lucidity.apply_encounter_lucidity_effect("player_001", "npc_001", mock_npc, "room_001")

            [call] = mock_service.calls
            assert call["entity_archetype"] == "npc_001"
