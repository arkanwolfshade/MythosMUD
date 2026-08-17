# HolidayService

> 189 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **get_mythos_chronicle()** (27 connections) — `server/time/time_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **holiday_service.py** (25 connections) — `server/services/holiday_service.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **test_time_bundle.py** (21 connections) — `server/tests/unit/container/test_time_bundle.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **test_holiday_service.py** (10 connections) — `server/tests/unit/services/test_holiday_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- *... and 164 more nodes in this community*

## Relationships

- [HolidayCollection](HolidayCollection.md) (33 shared connections)
- [get_logger](get_logger.md) (29 shared connections)
- [bundles/game.py](bundles-game.py.md) (13 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (6 shared connections)
- [.__post_init__](__post_init__.md) (6 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [._build_broadcast_payload](_build_broadcast_payload.md) (5 shared connections)
- [ExplorationService](ExplorationService.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (4 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/container/bundles/time.py`
- `server/services/holiday_service.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 440 (94%)
- INFERRED: 27 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*