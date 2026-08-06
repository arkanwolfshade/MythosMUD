# add used user

> 154 nodes

## Key Concepts

- **log_and_raise()** (186 connections) — `server/utils/error_logging.py`
- **error_logging.py** (61 connections) — `server/utils/error_logging.py`
- **movement_service.py** (28 connections) — `server/game/movement_service.py`
- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **container_service_session.py** (28 connections) — `server/services/container_service_session.py`
- **GameMechanicsService** (27 connections) — `server/game/mechanics.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **ContainerAccessMixin** (19 connections) — `server/services/container_service_access.py`
- **experience_repository.py** (16 connections) — `server/persistence/repositories/experience_repository.py`
- **SpellRepository** (16 connections) — `server/persistence/repositories/spell_repository.py`
- **test_mechanics.py** (16 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **skill_use_log_repository.py** (14 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **spell_repository.py** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **ContainerLockMixin** (14 connections) — `server/services/container_service_lock.py`
- **test_spell_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **mechanics.py** (13 connections) — `server/game/mechanics.py`
- **._require_container_for_lock_ops()** (10 connections) — `server/services/container_service_lock.py`
- **fetch_user_by_username_case_insensitive()** (9 connections) — `server/async_persistence_direct_queries.py`
- **fetch_professions()** (9 connections) — `server/async_persistence_direct_queries.py`
- **._validate_container_access()** (8 connections) — `server/services/container_service_access.py`
- **._require_player_for_lock_ops()** (8 connections) — `server/services/container_service_lock.py`
- **._raise_if_cannot_lock()** (8 connections) — `server/services/container_service_lock.py`
- **._persist_lock_state()** (8 connections) — `server/services/container_service_lock.py`
- *... and 129 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (42 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (34 shared connections)
- [commands party examples](commands_party_examples.md) (29 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (24 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (20 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (18 shared connections)
- [command inventory models](command_inventory_models.md) (17 shared connections)
- [player event handlers](player_event_handlers.md) (17 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (16 shared connections)
- [level curve game](level_curve_game.md) (14 shared connections)
- [command combat models](command_combat_models.md) (12 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (11 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/npc/combat_integration_base.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/services/container_service_access.py`
- `server/services/container_service_lock.py`
- `server/services/container_service_session.py`
- `server/tests/unit/game/test_mechanics.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 893 (94%)
- INFERRED: 57 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*