# Chat Archive Advanced

> 17 nodes

## Key Concepts

- **_schedule_entry_from_row()** (8 connections) — `server/services/schedule_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (3 connections) — `server/services/schedule_service.py`
- **Record** (2 connections)
- **Connection** (2 connections)
- **Normalize nullable PostgreSQL array columns to string values.** (1 connections) — `server/services/schedule_service.py`
- **Normalize nullable PostgreSQL array columns to lowercase slug strings.** (1 connections) — `server/services/schedule_service.py`
- **Return asyncpg-compatible DATABASE_URL from the environment.** (1 connections) — `server/services/schedule_service.py`
- **Build a ScheduleEntry from a calendar_npc_schedules row.** (1 connections) — `server/services/schedule_service.py`
- **Load and normalize schedule rows from PostgreSQL.** (1 connections) — `server/services/schedule_service.py`
- **Async helper to load schedules from PostgreSQL database.** (1 connections) — `server/services/schedule_service.py`
- **MonkeyPatch** (1 connections)
- **Regression: tables live in schema mythos_e2e; raw asyncpg must set search_path l** (1 connections) — `server/tests/unit/services/test_schedule_service.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (4 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (3 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (2 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (1 shared connections)

## Source Files

- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 46 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*