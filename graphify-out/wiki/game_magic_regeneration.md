# game magic regeneration

> 16 nodes

## Key Concepts

- **decode_json_column()** (7 connections) — `server/container/utils.py`
- **_flatten_bundle()** (6 connections) — `server/container/main.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **._decode_json_column()** (4 connections) — `server/container/main.py`
- **Any** (3 connections)
- **Any** (3 connections)
- **.get_service()** (3 connections) — `server/container/main.py`
- **test_flatten_bundle_copies_existing_attrs()** (2 connections) — `server/tests/unit/container/test_application_container_main.py`
- **Wire user_manager into follow_service and nats_message_handler when present.** (1 connections) — `server/container/bundles/game.py`
- **Build a single item prototype payload from a DB row for validation.** (1 connections) — `server/container/bundles/game.py`
- **Copy bundle attributes onto container for backward compatibility.** (1 connections) — `server/container/main.py`
- **Delegate to shared util. Kept for backward compatibility.** (1 connections) — `server/container/main.py`
- **Get a service by name.** (1 connections) — `server/container/main.py`
- **Any** (1 connections)
- **Decode a JSON column value, returning the type's default on failure.      Used b** (1 connections) — `server/container/utils.py`

## Relationships

- [nats services service](nats_services_service.md) (6 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (1 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/tests/unit/container/test_application_container_main.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*