# NPC Combat

> 410 nodes

## Key Concepts

- **NPCCombatIntegrationService** (90 connections) — `server/services/npc_combat_integration_service.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **test_npc_combat_integration_service.py** (46 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **UUID** (15 connections)
- **combat.py** (14 connections) — `server/container/bundles/combat.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **EventBusPublish** (9 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- *... and 385 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (32 shared connections)
- [target resolution service](target_resolution_service.md) (24 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (17 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (15 shared connections)
- [Loot Generation](Loot_Generation.md) (14 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (14 shared connections)
- [spell game magic](spell_game_magic.md) (12 shared connections)
- [item models rationale](item_models_rationale.md) (12 shared connections)
- [command parser rationale](command_parser_rationale.md) (11 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (10 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (10 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (9 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/container/bundles/combat.py`
- `server/game/magic/spell_targeting.py`
- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_player_combat_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 1397 (90%)
- INFERRED: 152 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*