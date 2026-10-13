# Event Bus & Persistence Core

> 1339 nodes

## Key Concepts

- **get_logger()** (558 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (527 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Player** (275 connections) — `server/models/player.py`
- **AliasStorage** (248 connections) — `server/alias_storage.py`
- **AsyncPersistenceLayer** (192 connections) — `server/async_persistence.py`
- **Room** (132 connections) — `server/models/room.py`
- **models/player.py** (110 connections) — `server/models/player.py`
- **connection_manager.py** (110 connections) — `server/realtime/connection_manager.py`
- **time.py** (107 connections) — `server/container/bundles/time.py`
- **server/models/__init__.py** (90 connections) — `server/models/__init__.py`
- **async_persistence.py** (85 connections) — `server/async_persistence.py`
- **alias_storage.py** (80 connections) — `server/alias_storage.py`
- **test_player_respawn_service.py** (59 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **inventory_command_helpers.py** (52 connections) — `server/commands/inventory_command_helpers.py`
- **models/room.py** (51 connections) — `server/models/room.py`
- **player_service.py** (50 connections) — `server/game/player_service.py`
- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **get_config()** (46 connections) — `server/config/__init__.py`
- **player_respawn_service.py** (44 connections) — `server/services/player_respawn_service.py`
- **command_handler_unified.py** (43 connections) — `server/command_handler_unified.py`
- **spell_effects.py** (42 connections) — `server/game/magic/spell_effects.py`
- **server/models/game.py** (42 connections) — `server/models/game.py`
- **InstanceManager** (41 connections) — `server/game/instance_manager.py`
- **Base** (41 connections) — `server/models/base.py`
- *... and 1314 more nodes in this community*

## Relationships

- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (190 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (82 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (74 shared connections)
- [Community 42](Community_42.md) (66 shared connections)
- [API Response Models](API_Response_Models.md) (65 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (63 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (54 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (51 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (50 shared connections)
- [Community 141](Community_141.md) (45 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (44 shared connections)
- [Community 41](Community_41.md) (42 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `scripts/run_test_ci.py`
- `server/alias_storage.py`
- `server/api/real_time.py`
- `server/app/game_tick_corpses.py`
- `server/async_persistence.py`
- `server/async_persistence_types.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler/processing.py`
- `server/command_handler_unified.py`
- `server/commands/admin_hallucinate_command.py`
- `server/commands/admin_permission_utils.py`
- `server/commands/admin_summon_command.py`
- `server/commands/bank_commands.py`
- `server/commands/combat_handler.py`
- `server/commands/container_helpers_inventory_display.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/follow_commands.py`
- `server/commands/inventory_command_coercion.py`

## Audit Trail

- EXTRACTED: 6121 (94%)
- INFERRED: 379 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*