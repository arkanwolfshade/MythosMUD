# test_combat_service_modules.py

> 80 nodes · cohesion 0.04

## Key Concepts

- **test_rescue_service.py** (32 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service.py** (19 connections) — `server/services/rescue_service.py`
- **asyncio** (17 connections)
- **RescueService** (12 connections) — `server/services/rescue_service.py`
- **fixture** (10 connections)
- **.rescue()** (8 connections) — `server/services/rescue_service.py`
- **Any** (7 connections)
- **.__init__()** (7 connections) — `server/services/rescue_service.py`
- **_load_rescue_participants()** (6 connections) — `server/services/rescue_service.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **._apply_rescue_adjustment()** (5 connections) — `server/services/rescue_service.py`
- **_dispatch_rescue_events()** (4 connections) — `server/services/rescue_service.py`
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **async_session_factory()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **lucidity_service_factory()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_lucidity_record()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_no_persistence()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **UUID** (3 connections)
- **_rescue_success_payload()** (3 connections) — `server/services/rescue_service.py`
- **mock_event_dispatcher()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_lucidity_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_rescuer()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- *... and 55 more nodes in this community*

## Relationships

- [PopulationStats](PopulationStats.md) (9 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (3 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_command_registry_consistency.py](test_command_registry_consistency.py.md) (2 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (2 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)
- [endpoints.py](endpoints.py.md) (1 shared connections)

## Source Files

- `server/services/rescue_service.py`
- `server/tests/unit/services/test_rescue_service.py`

## Audit Trail

- EXTRACTED: 136 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*