# room fixer services

> 154 nodes

## Key Concepts

- **RoomDataCache** (40 connections) — `server/services/room_data_cache.py`
- **TestRoomDataCache** (28 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **TestRoomDataFixer** (20 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **RoomSyncService** (19 connections) — `server/services/room_sync_service.py`
- **room_sync_service.py** (16 connections) — `server/services/room_sync_service.py`
- **RoomDataFixer** (14 connections) — `server/services/room_data_fixer.py`
- **.apply_room_data_fixes()** (13 connections) — `server/services/room_data_fixer.py`
- **room_data_fixer.py** (7 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_name()** (7 connections) — `server/services/room_data_fixer.py`
- **.fix_occupant_count_mismatch()** (7 connections) — `server/services/room_data_fixer.py`
- **Any** (7 connections)
- **Any** (6 connections)
- **.fix_missing_description()** (6 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_timestamp()** (6 connections) — `server/services/room_data_fixer.py`
- **.__init__()** (6 connections) — `server/services/room_sync_service.py`
- **._handle_stale_room_data()** (6 connections) — `server/services/room_sync_service.py`
- **Any** (5 connections)
- **.count_applied_fixes()** (5 connections) — `server/services/room_data_fixer.py`
- **.test_apply_room_data_fixes_exception_handling()** (5 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **.merge_room_data()** (4 connections) — `server/services/room_data_cache.py`
- **._is_newer_data()** (4 connections) — `server/services/room_data_cache.py`
- **._process_room_update_with_validation()** (4 connections) — `server/services/room_sync_service.py`
- **._fetch_fresh_room_data()** (4 connections) — `server/services/room_sync_service.py`
- **test_room_data_cache.py** (4 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **test_room_data_fixer.py** (4 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- *... and 129 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [room validator services](room_validator_services.md) (4 shared connections)
- [room service sync](room_service_sync.md) (4 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [item models rationale](item_models_rationale.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)

## Source Files

- `server/services/room_data_cache.py`
- `server/services/room_data_fixer.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/services/test_room_data_cache.py`
- `server/tests/unit/services/test_room_data_fixer.py`

## Audit Trail

- EXTRACTED: 467 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*