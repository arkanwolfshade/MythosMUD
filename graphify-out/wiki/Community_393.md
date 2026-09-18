# Community 393

> 45 nodes

## Key Concepts

- **RoomSyncService** (21 connections) — `server/services/room_sync_service.py`
- **RoomDataValidator** (16 connections) — `server/services/room_data_validator.py`
- **Any** (8 connections)
- **.validate_room_data()** (7 connections) — `server/services/room_data_validator.py`
- **Any** (7 connections)
- **.validate_room_consistency()** (6 connections) — `server/services/room_data_validator.py`
- **._handle_stale_room_data()** (6 connections) — `server/services/room_sync_service.py`
- **.__init__()** (6 connections) — `server/services/room_sync_service.py`
- **.check_duplicate_occupants()** (4 connections) — `server/services/room_data_validator.py`
- **.check_empty_room_with_occupants()** (4 connections) — `server/services/room_data_validator.py`
- **.check_occupant_count_consistency()** (4 connections) — `server/services/room_data_validator.py`
- **.is_valid_room_id()** (4 connections) — `server/services/room_data_validator.py`
- **.validate_field_types()** (4 connections) — `server/services/room_data_validator.py`
- **.validate_occupant_consistency()** (4 connections) — `server/services/room_data_validator.py`
- **.validate_required_fields()** (4 connections) — `server/services/room_data_validator.py`
- **._fetch_fresh_room_data()** (4 connections) — `server/services/room_sync_service.py`
- **._process_room_update_with_validation()** (4 connections) — `server/services/room_sync_service.py`
- **.get_room_data_cache_stats()** (3 connections) — `server/services/room_sync_service.py`
- **._invalidate_stale_cache()** (3 connections) — `server/services/room_sync_service.py`
- **.process_event_with_ordering()** (3 connections) — `server/services/room_sync_service.py`
- **._process_room_transition()** (3 connections) — `server/services/room_sync_service.py`
- **.set_room_service()** (3 connections) — `server/services/room_sync_service.py`
- **.clear_cache()** (2 connections) — `server/services/room_sync_service.py`
- **T** (1 connections)
- **Validate occupant count consistency. Args: room_data: Room data to validate…** (1 connections) — `server/services/room_data_validator.py`
- *... and 20 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (5 shared connections)
- [Community 192](Community_192.md) (4 shared connections)
- [Community 1085](Community_1085.md) (2 shared connections)
- [Community 318](Community_318.md) (2 shared connections)
- [NPC Event Types](NPC_Event_Types.md) (1 shared connections)
- [Community 567](Community_567.md) (1 shared connections)
- [Community 568](Community_568.md) (1 shared connections)

## Source Files

- `server/services/room_data_validator.py`
- `server/services/room_sync_service.py`

## Audit Trail

- EXTRACTED: 78 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*