# Community 1085

> 12 nodes

## Key Concepts

- **RoomDataCache** (40 connections) — `server/services/room_data_cache.py`
- **test_room_data_cache.py** (4 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_newer_data_old_newer_than_new()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_custom_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.clear_cache()** (2 connections) — `server/services/room_data_cache.py`
- **.__init__()** (2 connections) — `server/services/room_data_cache.py`
- **Manages room data caching and freshness validation.** (1 connections) — `server/services/room_data_cache.py`
- **Initialize the room data cache. Args: freshness_threshold_seconds: Threshold in…** (1 connections) — `server/services/room_data_cache.py`
- **Clear room data cache. Args: room_id: Specific room ID to clear, or None to…** (1 connections) — `server/services/room_data_cache.py`
- **Unit tests for room data cache. Tests the RoomDataCache class for caching and…** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test _is_newer_data when old is newer than new.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test is_room_data_fresh with custom threshold parameter.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`

## Relationships

- [Community 936](Community_936.md) (11 shared connections)
- [Community 1047](Community_1047.md) (6 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (3 shared connections)
- [Community 393](Community_393.md) (2 shared connections)
- [Community 1986](Community_1986.md) (1 shared connections)
- [Community 2001](Community_2001.md) (1 shared connections)
- [Community 1999](Community_1999.md) (1 shared connections)
- [Community 1987](Community_1987.md) (1 shared connections)
- [Community 1994](Community_1994.md) (1 shared connections)
- [Community 1990](Community_1990.md) (1 shared connections)
- [Community 1993](Community_1993.md) (1 shared connections)
- [Community 1992](Community_1992.md) (1 shared connections)

## Source Files

- `server/services/room_data_cache.py`
- `server/tests/unit/services/test_room_data_cache.py`

## Audit Trail

- EXTRACTED: 47 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*