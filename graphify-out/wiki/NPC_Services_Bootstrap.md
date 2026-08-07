# NPC Services Bootstrap

> 234 nodes

## Key Concepts

- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (42 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (40 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **TargetType** (39 connections) — `server/schemas/shared/target_resolution.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **TargetMetadata** (16 connections) — `server/schemas/shared/target_metadata.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **combat_validator.py** (7 connections) — `server/validators/combat_validator.py`
- *... and 209 more nodes in this community*

## Relationships

- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (42 shared connections)
- [player respawn event](player_respawn_event.md) (25 shared connections)
- [shutdown commands admin](shutdown_commands_admin.md) (11 shared connections)
- [mythosApp appLazyScreens mythosAppViewMo](mythosApp_appLazyScreens_mythosAppViewMo.md) (10 shared connections)
- [commands position system](commands_position_system.md) (9 shared connections)
- [commands npc admin](commands_npc_admin.md) (9 shared connections)
- [Database Config](Database_Config.md) (9 shared connections)
- [Player Stats](Player_Stats.md) (8 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (8 shared connections)
- [Error Conversion](Error_Conversion.md) (7 shared connections)
- [container helpers loot](container_helpers_loot.md) (7 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 860 (89%)
- INFERRED: 106 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*