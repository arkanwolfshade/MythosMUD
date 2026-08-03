# Magic Spell Service

> 78 nodes

## Key Concepts

- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **subscribe_room_occupants_refresh()** (7 connections) — `server/app/lifespan_event_subscriptions.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (5 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **_get_item_prototype_entries()** (4 connections) — `server/app/lifespan_startup.py`
- **Any** (4 connections)
- **_validate_npc_services_prerequisites()** (4 connections) — `server/app/lifespan_startup.py`
- **_start_npc_thread_manager_and_pending()** (4 connections) — `server/app/lifespan_startup.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (4 connections) — `server/app/lifespan_startup.py`
- *... and 53 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (16 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (16 shared connections)
- [time service rationale](time_service_rationale.md) (14 shared connections)
- [NPC Combat](NPC_Combat.md) (7 shared connections)
- [item models rationale](item_models_rationale.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (3 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (3 shared connections)
- [npc service services](npc_service_services.md) (3 shared connections)
- [player respawn event](player_respawn_event.md) (3 shared connections)
- [game models player](game_models_player.md) (3 shared connections)
- [command combat models](command_combat_models.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 336 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*