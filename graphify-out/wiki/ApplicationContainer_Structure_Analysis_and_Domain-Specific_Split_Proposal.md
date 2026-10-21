# ApplicationContainer Structure Analysis and Domain-Specific Split Proposal

> 22 nodes · cohesion 0.10

## Key Concepts

- **asyncio** (38 connections)
- **test_get_adjacent_rooms_null_exit()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_local_chat_scope()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_cache_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_exits_success()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_info_success()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_cache_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_with_cache_dict()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_with_plane_zone()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_with_sub_zone()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_lookup_explored_stable_ids_calls_procedure_and_binds_uuid_list()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_room_service_init_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_adjacent_rooms() skips null exits.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_local_chat_scope() returns current room and adjacent rooms.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() handles room dict.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() returns empty list when room not found.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_exits() returns exits dictionary.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test list_rooms() filters by plane and zone.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_info() returns comprehensive room information.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test _lookup_explored_stable_ids() calls get_room_stable_ids_by_uuids with the…** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test RoomService initialization with cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room() returns None when room not in cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`

## Relationships

- [test_request_schema_security.py](test_request_schema_security.py.md) (11 shared connections)
- [🚀 DEPLOYMENT STRATEGY](🚀_DEPLOYMENT_STRATEGY.md) (2 shared connections)
- [remove_dir](remove_dir.md) (1 shared connections)
- [check_postgresql.sh](check_postgresql.sh.md) (1 shared connections)
- [apply_account_sanctions_migration.py](apply_account_sanctions_migration.py.md) (1 shared connections)
- [e2e_place_player.py](e2e_place_player.py.md) (1 shared connections)
- [e2e_player_state.py](e2e_player_state.py.md) (1 shared connections)
- [@testing-library/react](@testing-library-react.md) (1 shared connections)
- [@testing-library/jest-dom](@testing-library-jest-dom.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [patch-package](patch-package.md) (1 shared connections)
- [@stoplight/spectral-cli](@stoplight-spectral-cli.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*