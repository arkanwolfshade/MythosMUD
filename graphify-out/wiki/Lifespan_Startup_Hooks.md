# Lifespan Startup Hooks

> 83 nodes · cohesion 0.04

## Key Concepts

- **lifespan_startup.py** (58 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (24 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **initialize_container_and_legacy_services()** (13 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections) — `server/app/lifespan_startup.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (12 connections) — `server/app/lifespan_startup.py`
- **ApplicationContainer** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (8 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **subscribe_quest_events()** (7 connections) — `server/app/lifespan_event_subscriptions.py`
- **get_npc_startup_service()** (7 connections) — `server/services/npc_startup_service.py`
- **subscribe_room_occupants_refresh()** (6 connections) — `server/app/lifespan_event_subscriptions.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (5 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (5 connections) — `server/app/lifespan_startup.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (4 connections) — `server/app/lifespan_startup.py`
- *... and 58 more nodes in this community*

## Relationships

- [[NPC Admin API]] (13 shared connections)
- [[NPC Services Bundle]] (11 shared connections)
- [[App Lifespan Management]] (9 shared connections)
- [[Combat Service Bundle]] (8 shared connections)
- [[Database Manager Tests]] (6 shared connections)
- [[NPC Database Sessions]] (4 shared connections)
- [[NPC Death Lifecycle]] (3 shared connections)
- [[NPC Occupant Verification]] (3 shared connections)
- [[Game Tick Processing]] (3 shared connections)
- [[NPC Service Tests]] (3 shared connections)
- [[Application DI Bundles]] (2 shared connections)
- [[Chat Service Whispers]] (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 362 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
