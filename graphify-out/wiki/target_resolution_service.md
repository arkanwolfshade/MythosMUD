# target resolution service

> 290 nodes

## Key Concepts

- **TargetMatch** (122 connections) — `server/schemas/shared/target_resolution.py`
- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **SpellTargetingService** (31 connections) — `server/game/magic/spell_targeting.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **handle_follow_command()** (18 connections) — `server/commands/follow_commands.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **follow_commands.py** (15 connections) — `server/commands/follow_commands.py`
- **TargetMetadata** (12 connections) — `server/schemas/shared/target_metadata.py`
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **handle_unfollow_command()** (10 connections) — `server/commands/follow_commands.py`
- **handle_following_command()** (10 connections) — `server/commands/follow_commands.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- *... and 265 more nodes in this community*

## Relationships

- [game models player](game_models_player.md) (58 shared connections)
- [NPC Combat](NPC_Combat.md) (39 shared connections)
- [spell game magic](spell_game_magic.md) (21 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (16 shared connections)
- [command factories exploration](command_factories_exploration.md) (15 shared connections)
- [commands admin mute](commands_admin_mute.md) (13 shared connections)
- [Item Instances](Item_Instances.md) (11 shared connections)
- [command inventory factories](command_inventory_factories.md) (10 shared connections)
- [Error Conversion](Error_Conversion.md) (7 shared connections)
- [models player related](models_player_related.md) (6 shared connections)
- [combat flee commands](combat_flee_commands.md) (5 shared connections)
- [command factories create](command_factories_create.md) (4 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/follow_commands.py`
- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_follow_commands.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_damage_grace_period.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 1171 (94%)
- INFERRED: 77 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*