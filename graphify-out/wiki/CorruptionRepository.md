# CorruptionRepository

> 119 nodes · cohesion 0.03

## Key Concepts

- **test_combat_flee_handler.py** (43 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (36 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (25 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (21 connections)
- **execute_voluntary_flee()** (19 connections) — `server/services/combat_flee_handler.py`
- **execute_flee_failed_free_hits()** (14 connections) — `server/services/combat_flee_handler.py`
- **test_lucidity_command_disruption.py** (14 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **UUID** (12 connections)
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **resolve_player_attack_damage()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **_FleeFreeHitsCombatService** (9 connections) — `server/services/combat_flee_handler.py`
- **lucidity_command_disruption.py** (9 connections) — `server/services/lucidity_command_disruption.py`
- **_make_npc_participant()** (9 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_resolve_free_hit_damage()** (8 connections) — `server/services/combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_one_opponent()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_stops_on_combat_ended()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_stops_on_target_died()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_two_opponents_turn_order()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_ordered_free_hit_attackers()** (7 connections) — `server/services/combat_flee_handler.py`
- **should_involuntary_flee()** (7 connections) — `server/services/lucidity_command_disruption.py`
- **should_misfire_command()** (7 connections) — `server/services/lucidity_command_disruption.py`
- **_alive_result()** (7 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 94 more nodes in this community*

## Relationships

- [test_player_combat_service.py](test_player_combat_service.py.md) (31 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (11 shared connections)
- [DatabaseManager](DatabaseManager.md) (10 shared connections)
- [PopulationStats](PopulationStats.md) (4 shared connections)
- [Room](Room.md) (4 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (3 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (3 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [ItemFactory](ItemFactory.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [npcs/catalog_dml.py](npcs-catalog_dml.py.md) (2 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)

## Source Files

- `server/services/combat_flee_handler.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_lucidity_command_disruption.py`

## Audit Trail

- EXTRACTED: 317 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*