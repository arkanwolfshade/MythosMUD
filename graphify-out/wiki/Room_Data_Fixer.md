# Room Data Fixer

> 46 nodes · cohesion 0.06

## Key Concepts

- **RoomSyncService** (19 connections) — `server/services/room_sync_service.py`
- **RoomDataFixer** (15 connections) — `server/services/room_data_fixer.py`
- **Any** (10 connections) — `server/services/room_sync_service.py`
- **.apply_room_data_fixes()** (8 connections) — `server/services/room_data_fixer.py`
- **._handle_stale_room_data()** (6 connections) — `server/services/room_sync_service.py`
- **.__init__()** (6 connections) — `server/services/room_sync_service.py`
- **Any** (5 connections) — `server/services/room_data_fixer.py`
- **T** (4 connections) — `server/services/room_sync_service.py`
- **.fix_missing_description()** (4 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_name()** (4 connections) — `server/services/room_data_fixer.py`
- **.fix_missing_timestamp()** (4 connections) — `server/services/room_data_fixer.py`
- **.fix_occupant_count_mismatch()** (4 connections) — `server/services/room_data_fixer.py`
- **._fetch_fresh_room_data()** (4 connections) — `server/services/room_sync_service.py`
- **._process_room_update_with_validation()** (4 connections) — `server/services/room_sync_service.py`
- **room_service()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **.count_applied_fixes()** (3 connections) — `server/services/room_data_fixer.py`
- **.get_room_data_cache_stats()** (3 connections) — `server/services/room_sync_service.py`
- **._invalidate_stale_cache()** (3 connections) — `server/services/room_sync_service.py`
- **.process_event_with_ordering()** (3 connections) — `server/services/room_sync_service.py`
- **._process_room_transition()** (3 connections) — `server/services/room_sync_service.py`
- **.set_room_service()** (3 connections) — `server/services/room_sync_service.py`
- **test_room_data_fixer.py** (3 connections) — `server/tests/unit/services/test_room_data_fixer.py`
- **room_sync_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **room_sync_service_with_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **Create a RoomService instance.** (2 connections) — `server/tests/unit/game/test_room_service.py`
- *... and 21 more nodes in this community*

## Relationships

- [[Room Data Cache]] (4 shared connections)
- [[NPC Combat Lifecycle]] (4 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Room Sync Service]] (3 shared connections)
- [[Room Data Fixer Tests]] (2 shared connections)
- [[Maps API Endpoints]] (1 shared connections)
- [[Room Service Tests]] (1 shared connections)
- [[Player Respawn Events]] (1 shared connections)

## Source Files

- `server/services/room_data_fixer.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/services/test_room_data_fixer.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 138 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
