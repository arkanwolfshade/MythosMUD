# NPCLifecycleManager

> 158 nodes

## Key Concepts

- **ApplicationContainer** (139 connections) — `server/container/main.py`
- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **npc_startup_service.py** (16 connections) — `server/services/npc_startup_service.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **FastAPI** (13 connections)
- **lifespan_event_subscriptions.py** (12 connections) — `server/app/lifespan_event_subscriptions.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **subscribe_quest_events()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **QuestCompleted** (11 connections) — `server/events/event_types.py`
- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **test_lifespan_event_subscriptions.py** (8 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (7 connections) — `server/app/lifespan_event_subscriptions.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- *... and 133 more nodes in this community*

## Relationships

- [test command parser](test_command_parser.md) (52 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (22 shared connections)
- [message handler factory](message_handler_factory.md) (18 shared connections)
- [.shutdown()](shutdown%28%29.md) (17 shared connections)
- [world](world.md) (11 shared connections)
- [. init ()](_init_%28%29.md) (11 shared connections)
- [Any](Any.md) (10 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (9 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (9 shared connections)
- [close db()](close_db%28%29.md) (6 shared connections)
- [test admin commands](test_admin_commands.md) (6 shared connections)
- [.get instance()](get_instance%28%29.md) (6 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/events/event_types.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/realtime/envelope_assertions.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/test_npc_service.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 678 (95%)
- INFERRED: 36 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*