# player death service

> 197 nodes

## Key Concepts

- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_lifespan_startup.py** (39 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **PlayerDPDecayEvent** (16 connections) — `server/events/event_types.py`
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **_get_item_prototype_count()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- *... and 172 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (18 shared connections)
- [Error Conversion](Error_Conversion.md) (14 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (12 shared connections)
- [combat models rationale](combat_models_rationale.md) (10 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (9 shared connections)
- [Loot Generation](Loot_Generation.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [item models rationale](item_models_rationale.md) (6 shared connections)
- [command parser rationale](command_parser_rationale.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [command factories communication](command_factories_communication.md) (4 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (3 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/events/event_types.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 677 (96%)
- INFERRED: 25 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*