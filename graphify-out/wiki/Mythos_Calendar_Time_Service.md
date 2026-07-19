# Mythos Calendar Time Service

> 29 nodes · cohesion 0.12

## Key Concepts

- **datetime** (15 connections) — `server/time/time_service.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **MythosCalendarComponents** (4 connections) — `server/time/time_service.py`
- **.format_clock()** (4 connections) — `server/time/time_service.py`
- **.format_clock()** (3 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (3 connections) — `server/time/time_service.py`
- **_season_for_month()** (3 connections) — `server/time/time_service.py`
- **Get the current Mythos datetime.          Returns:             datetime: The cur** (1 connections) — `server/time/time_service.py`
- **Format the clock display string.          Args:             mythos_dt: Optional** (1 connections) — `server/time/time_service.py`
- **Convert a real-world timestamp into Mythos time.** (1 connections) — `server/time/time_service.py`
- **Convert a Mythos timestamp back into real-world time.** (1 connections) — `server/time/time_service.py`
- **Return the Mythos timestamp corresponding to now.** (1 connections) — `server/time/time_service.py`
- **Provide a simple HH:MM clock string for UI surfaces.** (1 connections) — `server/time/time_service.py`
- **Return normalized calendar metadata for the supplied Mythos timestamp.** (1 connections) — `server/time/time_service.py`
- **Return True when the timestamp falls within the 23:00–01:00 witching window.** (1 connections) — `server/time/time_service.py`
- **Return True when the timestamp is between dawn (06:00) and dusk (18:00).** (1 connections) — `server/time/time_service.py`
- **Return a coarse textual descriptor for the given timestamp.** (1 connections) — `server/time/time_service.py`
- *... and 4 more nodes in this community*

## Relationships

- [[Async Task Registry]] (10 shared connections)
- [[Time Service]] (5 shared connections)
- [[NPC Admin API]] (4 shared connections)
- [[Time Event Consumer]] (2 shared connections)

## Source Files

- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 115 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
