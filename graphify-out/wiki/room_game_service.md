# room game service

> 28 nodes

## Key Concepts

- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **list_rooms()** (12 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (6 connections) — `server/api/rooms.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **Request** (5 connections)
- **test_update_room_position_room_missing()** (5 connections) — `server/tests/unit/api/test_rooms_api.py`
- **AsyncSession** (4 connections)
- **test_get_room_not_found()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_validate_room_position_update_requires_auth()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_not_found()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_invalidate_room_cache()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_list_rooms_success()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_get_room_success()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_validate_room_position_update_delegates_to_auth_service()** (2 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_success()** (2 connections) — `server/tests/unit/api/test_rooms_api.py`
- **BaseModel** (1 connections)
- **Validate authentication and admin permissions for room position update.** (1 connections) — `server/api/rooms.py`
- **Update room position in database and verify the update succeeded.** (1 connections) — `server/api/rooms.py`
- **Invalidate room cache to force reload.** (1 connections) — `server/api/rooms.py`
- **List rooms filtered by plane, zone, and optionally sub_zone.      Returns room d** (1 connections) — `server/api/rooms.py`
- **Request model for updating room map coordinates.** (1 connections) — `server/api/rooms.py`
- *... and 3 more nodes in this community*

## Relationships

- [persistence container rationale](persistence_container_rationale.md) (13 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (10 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (10 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)
- [panels monitoringPanelTestFixtures Monit](panels_monitoringPanelTestFixtures_Monit.md) (2 shared connections)
- [postgres adapter infrastructure](postgres_adapter_infrastructure.md) (1 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (1 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/tests/unit/api/test_rooms_api.py`

## Audit Trail

- EXTRACTED: 128 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*