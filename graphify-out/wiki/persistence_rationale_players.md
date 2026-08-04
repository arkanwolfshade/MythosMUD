# persistence rationale players

> 236 nodes

## Key Concepts

- **AsyncPersistenceLayer** (184 connections) — `server/async_persistence.py`
- **ScheduleService** (30 connections) — `server/services/schedule_service.py`
- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **MythosTimeEventConsumer** (24 connections) — `server/time/time_event_consumer.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Any** (19 connections)
- **MythosHourTickEvent** (16 connections) — `server/events/event_types.py`
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **test_schedule_service.py** (12 connections) — `server/tests/unit/services/test_schedule_service.py`
- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **test_time_event_consumer.py** (8 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **.__init__()** (8 connections) — `server/time/time_event_consumer.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **._handle_tick()** (6 connections) — `server/time/time_event_consumer.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- *... and 211 more nodes in this community*

## Relationships

- [schemas invite user](schemas_invite_user.md) (23 shared connections)
- [Loot Generation](Loot_Generation.md) (18 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (16 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (13 shared connections)
- [Database Config](Database_Config.md) (11 shared connections)
- [models npc rationale](models_npc_rationale.md) (11 shared connections)
- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [command parser rationale](command_parser_rationale.md) (10 shared connections)
- [holiday service services](holiday_service_services.md) (9 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (7 shared connections)
- [room game service](room_game_service.md) (6 shared connections)
- [nats services service](nats_services_service.md) (6 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/events/event_types.py`
- `server/npc/combat_integration_base.py`
- `server/npc/idle_movement.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/movement_integration.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 882 (91%)
- INFERRED: 88 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*