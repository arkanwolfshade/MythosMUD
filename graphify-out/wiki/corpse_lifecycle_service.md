# corpse lifecycle service

> 89 nodes

## Key Concepts

- **ExplorationService** (75 connections) — `server/services/exploration_service.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_filter_explored_rooms_calls_room_service()** (5 connections) — `server/tests/unit/api/test_maps.py`
- **_async_session_maker_mock()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_no_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_scalar_one()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_fetchall()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_no_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_with_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_not_found()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_string_uuid()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_like_uuid_object()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_new_record()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_existing_record()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_empty()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_true()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_false()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- *... and 64 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (24 shared connections)
- [room game service](room_game_service.md) (15 shared connections)
- [Database Config](Database_Config.md) (8 shared connections)
- [combat services service](combat_services_service.md) (7 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (2 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)

## Source Files

- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 318 (92%)
- INFERRED: 26 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*