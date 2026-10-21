# websocket_integration.py

> 53 nodes · cohesion 0.05

## Key Concepts

- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **.get_instance()** (22 connections) — `server/container/main.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container_creates_new_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_dict()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_empty_string()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_invalid()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_list()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_none()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_project_root()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_service()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_service_invalid()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_service_not_initialized_service()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_is_initialized()** (3 connections) — `server/tests/unit/test_application_container.py`
- *... and 28 more nodes in this community*

## Relationships

- [test_message_handlers.py](test_message_handlers.py.md) (31 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (3 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (1 shared connections)
- [dependencies](dependencies.md) (1 shared connections)
- [RoomLoader](RoomLoader.md) (1 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/npc/npc_base.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 130 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*