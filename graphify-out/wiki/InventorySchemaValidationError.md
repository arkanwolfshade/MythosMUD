# InventorySchemaValidationError

> 270 nodes · cohesion 0.01

## Key Concepts

- **models/combat.py** (83 connections) — `server/models/combat.py`
- **CombatParticipantType** (82 connections) — `server/models/combat.py`
- **TargetType** (54 connections) — `server/schemas/shared/target_resolution.py`
- **CombatAction** (45 connections) — `server/models/combat.py`
- **test_utility_threat.py** (44 connections) — `server/tests/unit/services/test_utility_threat.py`
- **combat_attack.py** (40 connections) — `server/commands/combat_attack.py`
- **CombatResult** (32 connections) — `server/models/combat.py`
- **combat_service_attack.py** (32 connections) — `server/services/combat_service_attack.py`
- **combat_taunt.py** (29 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (28 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (27 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **combat_turn_processor.py** (26 connections) — `server/services/combat_turn_processor.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **test_combat_attack.py** (23 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **combat_attack_handler.py** (22 connections) — `server/services/combat_attack_handler.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **_combat()** (18 connections) — `server/tests/unit/services/test_utility_threat.py`
- **_p()** (18 connections) — `server/tests/unit/services/test_utility_threat.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_counter.py`
- **_execute_combat_action()** (15 connections) — `server/commands/combat_attack.py`
- **spell_effects_threat.py** (15 connections) — `server/game/magic/spell_effects_threat.py`
- **add_utility_threat_for_spell()** (15 connections) — `server/game/magic/spell_effects_threat.py`
- **CombatStatus** (15 connections) — `server/models/combat.py`
- **_hate()** (15 connections) — `server/tests/unit/services/test_utility_threat.py`
- *... and 245 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (95 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (77 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (57 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (36 shared connections)
- [RoomService](RoomService.md) (30 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (30 shared connections)
- [Room](Room.md) (17 shared connections)
- [look_container.py](look_container.py.md) (16 shared connections)
- [ValidationError](ValidationError.md) (16 shared connections)
- [Reporter](Reporter.md) (16 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (14 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (12 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/commands/combat_attack.py`
- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effects_threat.py`
- `server/game/magic/spell_targeting.py`
- `server/models/combat.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/tests/unit/commands/test_combat_attack.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`
- `server/tests/unit/services/test_damage_grace_period.py`
- `server/tests/unit/services/test_utility_threat.py`

## Audit Trail

- EXTRACTED: 1039 (96%)
- INFERRED: 47 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*