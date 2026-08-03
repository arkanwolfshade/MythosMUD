# project paths rationale

> 38 nodes

## Key Concepts

- **HolidayService** (41 connections) — `server/services/holiday_service.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **datetime** (7 connections)
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **test_holiday_service.py** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_ensure_utc()** (4 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- **.get_active_holiday_names()** (3 connections) — `server/services/holiday_service.py`
- **.get_upcoming_summary()** (3 connections) — `server/services/holiday_service.py`
- **._day_ordinal()** (3 connections) — `server/services/holiday_service.py`
- **.last_refresh()** (3 connections) — `server/services/holiday_service.py`
- **.validate_tradition()** (2 connections) — `server/schemas/calendar/calendar.py`
- **.validate_season()** (2 connections) — `server/schemas/calendar/calendar.py`
- **.validate_bonus_tags()** (2 connections) — `server/schemas/calendar/calendar.py`
- **Path** (2 connections)
- **Single holiday definition loaded from data/<env>/calendar/holidays.json.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate tradition value.          Args:             value: The tradition string** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate season value.          Args:             value: The season string to va** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate bonus tags format.** (1 connections) — `server/schemas/calendar/calendar.py`
- *... and 13 more nodes in this community*

## Relationships

- [holiday service services](holiday_service_services.md) (24 shared connections)
- [NATS Messaging](NATS_Messaging.md) (10 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (8 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [time service rationale](time_service_rationale.md) (4 shared connections)
- [commands party examples](commands_party_examples.md) (3 shared connections)
- [game rationale schemas](game_rationale_schemas.md) (3 shared connections)
- [holiday services service](holiday_services_service.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 163 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*