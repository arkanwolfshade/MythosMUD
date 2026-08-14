# RoomSyncService

> 77 nodes

## Key Concepts

- **RoomSyncService** (19 connections) — `server/services/room_sync_service.py`
- **RoomDataValidator** (18 connections) — `server/services/room_data_validator.py`
- **test_room_data_validator.py** (16 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **.validate_room_data()** (10 connections) — `server/services/room_data_validator.py`
- **get_room_sync_service()** (8 connections) — `server/services/room_sync_service.py`
- **Any** (8 connections)
- **.validate_room_consistency()** (7 connections) — `server/services/room_data_validator.py`
- **Any** (7 connections)
- **.check_duplicate_occupants()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_field_types()** (6 connections) — `server/services/room_data_validator.py`
- **.validate_required_fields()** (6 connections) — `server/services/room_data_validator.py`
- **._handle_stale_room_data()** (6 connections) — `server/services/room_sync_service.py`
- **.__init__()** (6 connections) — `server/services/room_sync_service.py`
- **.check_empty_room_with_occupants()** (5 connections) — `server/services/room_data_validator.py`
- **.check_occupant_count_consistency()** (5 connections) — `server/services/room_data_validator.py`
- **.is_valid_room_id()** (5 connections) — `server/services/room_data_validator.py`
- **room_sync_service()** (5 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **.validate_occupant_consistency()** (4 connections) — `server/services/room_data_validator.py`
- **._fetch_fresh_room_data()** (4 connections) — `server/services/room_sync_service.py`
- **._process_room_update_with_validation()** (4 connections) — `server/services/room_sync_service.py`
- **.get_room_data_cache_stats()** (3 connections) — `server/services/room_sync_service.py`
- **._invalidate_stale_cache()** (3 connections) — `server/services/room_sync_service.py`
- **.process_event_with_ordering()** (3 connections) — `server/services/room_sync_service.py`
- **._process_room_transition()** (3 connections) — `server/services/room_sync_service.py`
- **.set_room_service()** (3 connections) — `server/services/room_sync_service.py`
- *... and 52 more nodes in this community*

## Relationships

- [test_room_sync_service.py](test_room_sync_service.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [RoomDataCache](RoomDataCache.md) (2 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (2 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/services/room_data_validator.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/services/test_room_data_validator.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 129 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*