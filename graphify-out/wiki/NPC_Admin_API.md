# NPC Admin API

> 800 nodes · cohesion 0.01

## Key Concepts

- **get_logger()** (506 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (368 connections) — `server/structured_logging/enhanced_logging_config.py`
- **DatabaseError** (247 connections) — `server/exceptions.py`
- **exceptions.py** (194 connections) — `server/exceptions.py`
- **ValidationError** (189 connections) — `server/exceptions.py`
- **log_and_raise()** (164 connections) — `server/utils/error_logging.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **dependencies.py** (104 connections) — `server/dependencies.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **database.py** (74 connections) — `server/database.py`
- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **get_async_session()** (53 connections) — `server/database.py`
- **users.py** (46 connections) — `server/auth/users.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **error_logging.py** (41 connections) — `server/utils/error_logging.py`
- **user.py** (38 connections) — `server/models/user.py`
- **nats_message_handler.py** (38 connections) — `server/realtime/nats_message_handler.py`
- **player_respawn_service.py** (37 connections) — `server/services/player_respawn_service.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **enhanced_error_logging.py** (36 connections) — `server/utils/enhanced_error_logging.py`
- **Enum** (35 connections)
- **rooms.py** (34 connections) — `server/api/rooms.py`
- **player_service.py** (32 connections) — `server/game/player_service.py`
- **PlayerRepository** (32 connections) — `server/persistence/repositories/player_repository.py`
- *... and 775 more nodes in this community*

## Relationships

- [[Standardized Error Responses]] (116 shared connections)
- [[Alias Expansion Logic]] (105 shared connections)
- [[Game Service Bundle]] (57 shared connections)
- [[Distributed Event Bus]] (51 shared connections)
- [[Room Occupant Events]] (50 shared connections)
- [[NPC Database Sessions]] (44 shared connections)
- [[NPC Definition Admin API]] (42 shared connections)
- [[Inventory Service Helpers]] (33 shared connections)
- [[Container Exception Handlers]] (32 shared connections)
- [[SQLAlchemy Model Base]] (32 shared connections)
- [[Argon2 Password Hashing]] (31 shared connections)
- [[NPC Combat Lifecycle]] (31 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/api/__init__.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/api/base.py`
- `server/api/containers.py`
- `server/api/game.py`
- `server/api/player_helpers.py`
- `server/api/player_respawn.py`
- `server/api/professions.py`
- `server/api/rooms.py`
- `server/api/skills.py`
- `server/app/lifespan_event_subscriptions.py`

## Audit Trail

- EXTRACTED: 5724 (95%)
- INFERRED: 304 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
