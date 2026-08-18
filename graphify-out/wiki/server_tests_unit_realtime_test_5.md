# server tests unit realtime test

> 9 nodes

## Key Concepts

- **npc_event_handler()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **fixture** (4 connections)
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **mock_message_builder()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **mock_send_occupants_update()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Create a mock message builder.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Create a mock send_occupants_update function.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Create an NPCEventHandler instance.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (4 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 12 (92%)
- INFERRED: 1 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*