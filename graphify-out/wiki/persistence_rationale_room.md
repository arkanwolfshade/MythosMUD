# persistence rationale room

> 16 nodes

## Key Concepts

- **ConnectionMetadata** (21 connections) — `server/realtime/connection_models.py`
- **connection_models.py** (9 connections) — `server/realtime/connection_models.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_init()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_with_optional_fields()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_dataclass_fields()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_equality()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_inequality()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Data models for connection management.  This module defines data structures used** (1 connections) — `server/realtime/connection_models.py`
- **Metadata for tracking connection details in the WebSocket-only system.      This** (1 connections) — `server/realtime/connection_models.py`
- **Unit tests for connection models.  Tests the connection_models module classes.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Test ConnectionMetadata.__init__() creates metadata with required fields.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Test ConnectionMetadata.__init__() with optional fields.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Test ConnectionMetadata has all expected dataclass fields.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Test ConnectionMetadata equality comparison.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **Test ConnectionMetadata inequality comparison.** (1 connections) — `server/tests/unit/realtime/test_connection_models.py`

## Relationships

- [connection realtime delegates](connection_realtime_delegates.md) (6 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (5 shared connections)
- [connection establishment realtime](connection_establishment_realtime.md) (3 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (2 shared connections)
- [services chat logger](services_chat_logger.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/connection_models.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 56 (90%)
- INFERRED: 6 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*