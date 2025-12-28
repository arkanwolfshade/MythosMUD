"""
Unit tests for NPC combat memory.

Tests the NPCCombatMemory class for tracking NPC attackers.
"""

import pytest

from server.services.npc_combat_memory import NPCCombatMemory


class TestNPCCombatMemory:
    """Test suite for NPCCombatMemory class."""

    def test_init(self):
        """Test NPCCombatMemory initialization."""
        memory = NPCCombatMemory()
        assert memory._npc_combat_memory == {}

    def test_get_attacker_not_found(self):
        """Test get_attacker returns None when no memory exists."""
        memory = NPCCombatMemory()
        assert memory.get_attacker("npc_001") is None

    def test_get_attacker_found(self):
        """Test get_attacker returns attacker ID when memory exists."""
        memory = NPCCombatMemory()
        memory._npc_combat_memory["npc_001"] = "player_001"
        assert memory.get_attacker("npc_001") == "player_001"

    def test_record_attack_first_engagement(self):
        """Test record_attack returns True for first engagement."""
        memory = NPCCombatMemory()
        result = memory.record_attack("npc_001", "player_001")
        assert result is True
        assert memory.get_attacker("npc_001") == "player_001"

    def test_record_attack_subsequent_engagement(self):
        """Test record_attack returns False for subsequent engagement."""
        memory = NPCCombatMemory()
        memory.record_attack("npc_001", "player_001")
        result = memory.record_attack("npc_001", "player_002")
        assert result is False
        assert memory.get_attacker("npc_001") == "player_002"  # Updated to new attacker

    def test_record_attack_overwrites_previous(self):
        """Test record_attack overwrites previous attacker."""
        memory = NPCCombatMemory()
        memory.record_attack("npc_001", "player_001")
        memory.record_attack("npc_001", "player_002")
        assert memory.get_attacker("npc_001") == "player_002"

    def test_clear_memory_exists(self):
        """Test clear_memory removes memory when it exists."""
        memory = NPCCombatMemory()
        memory.record_attack("npc_001", "player_001")
        result = memory.clear_memory("npc_001")
        assert result is True
        assert memory.get_attacker("npc_001") is None

    def test_clear_memory_not_exists(self):
        """Test clear_memory returns False when memory doesn't exist."""
        memory = NPCCombatMemory()
        result = memory.clear_memory("npc_001")
        assert result is False

    def test_has_memory_true(self):
        """Test has_memory returns True when memory exists."""
        memory = NPCCombatMemory()
        memory.record_attack("npc_001", "player_001")
        assert memory.has_memory("npc_001") is True

    def test_has_memory_false(self):
        """Test has_memory returns False when no memory exists."""
        memory = NPCCombatMemory()
        assert memory.has_memory("npc_001") is False

    def test_has_memory_after_clear(self):
        """Test has_memory returns False after clearing."""
        memory = NPCCombatMemory()
        memory.record_attack("npc_001", "player_001")
        memory.clear_memory("npc_001")
        assert memory.has_memory("npc_001") is False

    def test_multiple_npcs(self):
        """Test memory can track multiple NPCs independently."""
        memory = NPCCombatMemory()
        memory.record_attack("npc_001", "player_001")
        memory.record_attack("npc_002", "player_002")
        assert memory.get_attacker("npc_001") == "player_001"
        assert memory.get_attacker("npc_002") == "player_002"

    def test_same_player_attacks_multiple_npcs(self):
        """Test same player can attack multiple NPCs."""
        memory = NPCCombatMemory()
        memory.record_attack("npc_001", "player_001")
        memory.record_attack("npc_002", "player_001")
        assert memory.get_attacker("npc_001") == "player_001"
        assert memory.get_attacker("npc_002") == "player_001"
