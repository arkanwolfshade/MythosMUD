# Server Services (99)

> 12 nodes

## Key Concepts

- **RoomDataCache** (40 connections) — `server/services/room_data_cache.py`
- **.test_clear_cache_nonexistent_room()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_merge_room_data_new_field()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_newer_data_new_has_timestamp_old_doesnt()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.__init__()** (2 connections) — `server/services/room_data_cache.py`
- **.clear_cache()** (2 connections) — `server/services/room_data_cache.py`
- **Manages room data caching and freshness validation.** (1 connections) — `server/services/room_data_cache.py`
- **Initialize the room data cache.          Args:             freshness_threshold_s** (1 connections) — `server/services/room_data_cache.py`
- **Clear room data cache.          Args:             room_id: Specific room ID to c** (1 connections) — `server/services/room_data_cache.py`
- **Test clear_cache handles nonexistent room gracefully.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test merge_room_data adds new fields from new data.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test _is_newer_data when new has timestamp but old doesn't.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`

## Relationships

- [Server Services (91)](Server_Services_%2891%29.md) (11 shared connections)
- [Server Services (96)](Server_Services_%2896%29.md) (6 shared connections)
- [Server Services (20)](Server_Services_%2820%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)
- [Server Events](Server_Events.md) (1 shared connections)
- [Server Services (278)](Server_Services_%28278%29.md) (1 shared connections)
- [Server Services (293)](Server_Services_%28293%29.md) (1 shared connections)
- [Server Services (291)](Server_Services_%28291%29.md) (1 shared connections)
- [Server Services (279)](Server_Services_%28279%29.md) (1 shared connections)
- [Server Services (283)](Server_Services_%28283%29.md) (1 shared connections)
- [Server Services (284)](Server_Services_%28284%29.md) (1 shared connections)
- [Server Services (288)](Server_Services_%28288%29.md) (1 shared connections)

## Source Files

- `server/services/room_data_cache.py`
- `server/tests/unit/services/test_room_data_cache.py`

## Audit Trail

- EXTRACTED: 57 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*