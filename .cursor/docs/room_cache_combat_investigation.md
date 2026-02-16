# Room cache and combat room investigation

## Summary

The combat room is **never removed** from the room cache. The cache is only ever **fully cleared** or **replaced**. A player at 0 DP can be "moved" to Arkham Square because their `current_room_id` fails validation when **the room cache does not contain that room ID**.

## How the room cache works

- **Location**: `AsyncPersistenceLayer._room_cache` (dict). Same reference is passed to `PlayerRepository` and `RoomRepository`.
- **Population**: `_load_room_cache_async()` loads all rooms from PostgreSQL (`rooms` + zones/subzones), builds room IDs via `_generate_room_id_from_zone_data()`, and does `_room_cache.clear()` then `_room_cache.update(rooms)`.
- **When it runs**: Lazy on first async use of persistence (e.g. `get_player_by_id`), or explicitly via `warmup_room_cache()` at startup (lifespan, core bundle, NPC startup).
- **Player validation**: `PlayerRepository.validate_and_fix_player_room(player)` checks `player.current_room_id not in self._room_cache`. If missing, it sets `player.current_room_id = "arkham_square"`. That runs on every `get_player_by_id()`.

## Ways the combat room can be "missing" from the cache

1. **Cache never populated (empty forever)**
   - If the first load fails (`DatabaseError`, `OSError`, `RuntimeError`), `_ensure_room_cache_loaded()` catches, clears the cache, and sets `_room_cache_loaded = True`.
   - All later calls believe the cache is "loaded" and never retry, so the cache stays **empty**.
   - Then every `get_player_by_id` sees the player's room as invalid and overwrites it to `"arkham_square"`.

2. **Room not in DB / not in query**
   - Cache is built from a single query over `rooms` and related tables.
   - If the combat room is not in that result (e.g. different schema, different source, or missing row), it will never be in the cache.

3. **Room ID format mismatch**
   - Cache keys are from `_generate_room_id_from_zone_data(zone_stable_id, subzone_stable_id, stable_id)` (e.g. `earth_arkhamcity_subzone_room_001`).
   - If `player.current_room_id` is stored in another format (e.g. from movement or another system), the key may not match and the room will appear "not in cache".

## Code paths that clear the cache

- `async_persistence.py` line 148: on exception in `_ensure_room_cache_loaded` (clear + mark loaded).
- `async_persistence.py` line 169: normal load (clear then update with new rooms).
- `async_persistence.py` line 172: load returned no rooms dict (clear only).
- `async_persistence.py` line 188: "relation does not exist" in `_load_room_cache_async` (clear only).

There is **no** code that removes a single room from the cache (no `pop`, no `del` on one key).

## Recommended fix

- **Allow retry when load failed**: In `_ensure_room_cache_loaded()`, when catching an exception and clearing the cache, **do not** set `_room_cache_loaded = True`. Leave it `False` so the next call retries loading. That way a transient DB/startup failure does not leave the cache permanently empty and avoid all room validation overwriting player rooms to Arkham Square.
