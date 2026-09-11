# room_update_event_builder.py

> 47 nodes

## Key Concepts

- **room_update_event_builder.py** (23 connections) — `server/realtime/room_update_event_builder.py`
- **build_room_update_event()** (21 connections) — `server/realtime/room_update_event_builder.py`
- **get_hallucinated_exits()** (16 connections) — `server/services/exit_hallucination.py`
- **test_exit_hallucination.py** (12 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **exit_hallucination.py** (10 connections) — `server/services/exit_hallucination.py`
- **test_websocket_room_updates_build_event.py** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **seed_from()** (7 connections) — `server/services/exit_hallucination.py`
- **mulberry32()** (5 connections) — `server/services/exit_hallucination.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_build_room_update_event_hallucinates_exits_for_deranged_viewer()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_build_room_update_event_no_viewer_id_leaves_exits_untouched()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **_hash_string()** (3 connections) — `server/services/exit_hallucination.py`
- **_shuffle()** (3 connections) — `server/services/exit_hallucination.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_get_hallucinated_exits_differs_by_player()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_get_hallucinated_exits_is_stable_for_same_room_and_player()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_get_hallucinated_exits_matches_js_reference()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_get_hallucinated_exits_only_uses_the_real_direction_pool()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_mulberry32_yields_floats_in_unit_interval()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_seed_from_matches_js_reference()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **test_seed_from_order_matters()** (3 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **asyncio** (3 connections)
- **mock_room()** (2 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **fixture** (2 connections)
- **ConnectionManager** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [build_event](build_event.md) (17 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (5 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [LucidityTierCache](LucidityTierCache.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/realtime/room_update_event_builder.py`
- `server/services/exit_hallucination.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/services/test_exit_hallucination.py`

## Audit Trail

- EXTRACTED: 104 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*