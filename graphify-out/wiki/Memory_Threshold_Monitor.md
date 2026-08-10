# Memory Threshold Monitor

> 28 nodes

## Key Concepts

- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_get_attacker_not_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_get_attacker_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_record_attack_first_engagement()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_record_attack_subsequent_engagement()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_record_attack_overwrites_previous()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_clear_memory_exists()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_clear_memory_not_exists()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_has_memory_true()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_has_memory_false()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_has_memory_after_clear()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_multiple_npcs()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_same_player_attacks_multiple_npcs()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test suite for NPCCombatMemory class.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test NPCCombatMemory initialization.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test get_attacker returns None when no memory exists.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test get_attacker returns attacker ID when memory exists.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test record_attack returns True for first engagement.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test record_attack returns False for subsequent engagement.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test record_attack overwrites previous attacker.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test clear_memory removes memory when it exists.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test clear_memory returns False when memory doesn't exist.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test has_memory returns True when memory exists.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Test has_memory returns False when no memory exists.** (1 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- *... and 3 more nodes in this community*

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (15 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_memory.py`

## Audit Trail

- EXTRACTED: 68 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*