# P3 · realtime-connection + events-nats

> 13 nodes

## Key Concepts

- **ConnectionMetadata** (24 connections) — `server/realtime/connection_models.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_dataclass_fields()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_equality()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_inequality()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_init()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_with_optional_fields()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Test ConnectionMetadata equality comparison.** (2 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Metadata for tracking connection details in the WebSocket-only system. This…** (1 connections) — `server/realtime/connection_models.py`
- **Unit tests for connection models. Tests the connection_models module classes.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Test ConnectionMetadata.__init__() creates metadata with required fields.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Test ConnectionMetadata.__init__() with optional fields.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Test ConnectionMetadata has all expected dataclass fields.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`

## Relationships

- [population_control.py](population_control.py.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [test_go_command.py](test_go_command.py.md) (4 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (2 shared connections)
- [security.ts](security.ts.md) (2 shared connections)
- [test_message_handler_factory.py](test_message_handler_factory.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_models.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 31 (84%)
- INFERRED: 6 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*