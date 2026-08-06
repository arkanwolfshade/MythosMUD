# commands shutdown process

> 679 nodes

## Key Concepts

- **DatabaseError** (497 connections) — `server/exceptions.py`
- **exceptions.py** (241 connections) — `server/exceptions.py`
- **log_and_raise()** (185 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (97 connections) — `server/database.py`
- **async_persistence.py** (77 connections) — `server/async_persistence.py`
- **database.py** (76 connections) — `server/database.py`
- **__init__.py** (73 connections) — `server/models/__init__.py`
- **Base** (60 connections) — `server/models/base.py`
- **error_logging.py** (60 connections) — `server/utils/error_logging.py`
- **get_async_session()** (54 connections) — `server/database.py`
- **MovementService** (43 connections) — `server/game/movement_service.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **__init__.py** (30 connections) — `server/persistence/repositories/__init__.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **test_world.py** (27 connections) — `server/tests/unit/models/test_world.py`
- **PlayerSkillRepository** (25 connections) — `server/persistence/repositories/player_skill_repository.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **PlayerSpell** (23 connections) — `server/models/player_spells.py`
- **base.py** (22 connections) — `server/models/base.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- *... and 654 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (94 shared connections)
- [add used user](add_used_user.md) (86 shared connections)
- [player room realtime](player_room_realtime.md) (61 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (53 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (53 shared connections)
- [task registry app](task_registry_app.md) (46 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (33 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (32 shared connections)
- [command combat models](command_combat_models.md) (28 shared connections)
- [player game schema](player_game_schema.md) (28 shared connections)
- [retry nats handler](retry_nats_handler.md) (26 shared connections)
- [auth users rationale](auth_users_rationale.md) (25 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/exceptions.py`
- `server/game/movement_service.py`
- `server/game/skill_service.py`
- `server/models/__init__.py`
- `server/models/base.py`
- `server/models/calendar.py`
- `server/models/dialogue.py`
- `server/models/emote.py`
- `server/models/item.py`
- `server/models/player_effect.py`
- `server/models/player_skill.py`

## Audit Trail

- EXTRACTED: 3837 (87%)
- INFERRED: 585 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*