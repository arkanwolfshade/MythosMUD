# Magic Command Handlers

> 126 nodes

## Key Concepts

- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container.py** (26 connections) — `server/models/container.py`
- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **container_models.py** (12 connections) — `server/api/container_models.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **TestEmitTransferEventDirections** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **UUID** (6 connections)
- **UUID** (5 connections)
- **Any** (5 connections)
- **Any** (4 connections)
- **.test_emit_transfer_event_success()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_connection_manager()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_container_in_result()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_room_id()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 101 more nodes in this community*

## Relationships

- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (47 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (43 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (17 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (3 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (3 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (3 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (1 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 484 (94%)
- INFERRED: 33 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*