# communication commands support

> 42 nodes

## Key Concepts

- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **test_npc_combat_memory.py** (4 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
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
- **.__init__()** (2 connections) — `server/services/npc_combat_memory.py`
- **.get_attacker()** (2 connections) — `server/services/npc_combat_memory.py`
- **.record_attack()** (2 connections) — `server/services/npc_combat_memory.py`
- **.clear_memory()** (2 connections) — `server/services/npc_combat_memory.py`
- **.has_memory()** (2 connections) — `server/services/npc_combat_memory.py`
- **Manages NPC combat memory - tracking attackers.** (1 connections) — `server/services/npc_combat_memory.py`
- **Initialize combat memory storage.** (1 connections) — `server/services/npc_combat_memory.py`
- **Get the last attacker for an NPC.          Args:             npc_id: ID of the N** (1 connections) — `server/services/npc_combat_memory.py`
- **Record that an NPC was attacked by a player.          Args:             npc_id:** (1 connections) — `server/services/npc_combat_memory.py`
- *... and 17 more nodes in this community*

## Relationships

- [world](world.md) (3 shared connections)
- [src/**/*.spec](src-__-_.spec.md) (2 shared connections)
- [get health service()](get_health_service%28%29.md) (1 shared connections)
- [combat](combat.md) (1 shared connections)
- [Test despawn npc handles NPC](Test_despawn_npc_handles_NPC.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_memory.py`
- `server/tests/unit/services/test_npc_combat_memory.py`

## Audit Trail

- EXTRACTED: 114 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*