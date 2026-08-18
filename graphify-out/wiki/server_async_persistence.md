# server async persistence

> 300 nodes

## Key Concepts

- **Player** (231 connections) — `server/models/player.py`
- **models/player.py** (98 connections) — `server/models/player.py`
- **async_persistence.py** (84 connections) — `server/async_persistence.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **test_async_persistence_delegates.py** (36 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **PlayerRepositoryProtocol** (23 connections) — `server/persistence/protocols.py`
- **test_protocol_ellipsis_bodies_via_unbound_methods()** (22 connections) — `server/tests/unit/persistence/test_protocols.py`
- **asyncio** (21 connections)
- **test_health_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **player_position_service.py** (17 connections) — `server/services/player_position_service.py`
- **player_creation_service.py** (16 connections) — `server/game/player_creation_service.py`
- **player_respawn_wrapper.py** (16 connections) — `server/game/player_respawn_wrapper.py`
- **test_procedures_return_shape.py** (13 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **protocols.py** (12 connections) — `server/persistence/protocols.py`
- **RoomRepositoryProtocol** (11 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_add_player_effect_generates_id()** (9 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **asyncio** (9 connections)
- **test_health_repository_cold_resistance.py** (8 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **reset_async_persistence()** (6 connections) — `server/async_persistence.py`
- *... and 275 more nodes in this community*

## Relationships

- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (47 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (29 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (28 shared connections)
- [fixturerequest](fixturerequest.md) (20 shared connections)
- [server constants spawn defaults](server_constants_spawn_defaults.md) (18 shared connections)
- [server commands inventory command helpers](server_commands_inventory_command_helpers.md) (15 shared connections)
- [server models lucidity](server_models_lucidity.md) (15 shared connections)
- [server tests unit infrastructure test](server_tests_unit_infrastructure_test.md) (14 shared connections)
- [server models player player apply](server_models_player_player_apply.md) (14 shared connections)
- [server commands inventory get command](server_commands_inventory_get_command.md) (12 shared connections)
- [server services container service](server_services_container_service.md) (12 shared connections)
- [dropresolved](dropresolved.md) (11 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/models/player.py`
- `server/persistence/protocols.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/services/player_position_service.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 788 (85%)
- INFERRED: 143 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*