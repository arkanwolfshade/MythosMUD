# services admin auth

> 28 nodes

## Key Concepts

- **convert_uuids_to_strings()** (18 connections) — `server/realtime/connection_helpers.py`
- **test_connection_helpers.py** (9 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **convert_uuids_to_strings_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **._convert_uuids_to_strings()** (3 connections) — `server/realtime/connection_manager.py`
- **test_convert_uuids_to_strings_uuid()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_dict()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_list()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_nested()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_string()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_int()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **test_convert_uuids_to_strings_dict()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_convert_uuids_to_strings_list()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_convert_uuids_to_strings_uuid()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_convert_uuids_to_strings_nested()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Recursively convert UUID objects to strings for JSON serialization.      Args:** (1 connections) — `server/realtime/connection_helpers.py`
- **Recursively convert UUID objects to strings for JSON serialization.** (1 connections) — `server/realtime/connection_manager.py`
- **Recursively convert UUID objects to strings for JSON serialization.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Unit tests for connection helpers.  Tests the connection helper functions.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **Test convert_uuids_to_strings() with UUID object.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **Test convert_uuids_to_strings() with dict containing UUID.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **Test convert_uuids_to_strings() with list containing UUID.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **Test convert_uuids_to_strings() with nested structures.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **Test convert_uuids_to_strings() with string (no conversion).** (1 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **Test convert_uuids_to_strings() with int (no conversion).** (1 connections) — `server/tests/unit/realtime/test_connection_helpers.py`
- **Test convert_uuids_to_strings() converts UUIDs in dict.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 3 more nodes in this community*

## Relationships

- [realtime connection helpers](realtime_connection_helpers.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 80 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*