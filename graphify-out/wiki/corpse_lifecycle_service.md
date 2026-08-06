# corpse lifecycle service

> 101 nodes

## Key Concepts

- **ExplorationService** (79 connections) — `server/services/exploration_service.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **.mark_room_as_explored()** (7 connections) — `server/services/exploration_service.py`
- **UUID** (7 connections)
- **._get_room_uuid_by_stable_id()** (7 connections) — `server/services/exploration_service.py`
- **.is_room_explored()** (6 connections) — `server/services/exploration_service.py`
- **AsyncSession** (5 connections)
- **._mark_explored_in_session()** (5 connections) — `server/services/exploration_service.py`
- **.get_explored_rooms()** (5 connections) — `server/services/exploration_service.py`
- **_async_session_maker_mock()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_no_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **.__init__()** (4 connections) — `server/services/exploration_service.py`
- **.mark_room_as_explored_sync()** (4 connections) — `server/services/exploration_service.py`
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
- *... and 76 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (18 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (12 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (7 shared connections)
- [panels monitoringPanelTestFixtures Monit](panels_monitoringPanelTestFixtures_Monit.md) (5 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (2 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [room game service](room_game_service.md) (1 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)

## Source Files

- `server/services/exploration_service.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 357 (95%)
- INFERRED: 19 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*