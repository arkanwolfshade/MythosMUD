# test_combat_cleanup_handler.py

> 111 nodes

## Key Concepts

- **ApplicationContainer** (152 connections) — `server/container/main.py`
- **test_application_container.py** (29 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_main.py** (18 connections) — `server/tests/unit/container/test_application_container_main.py`
- **._init_player_quest_layer()** (10 connections) — `server/container/bundles/game.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **._init_temporal_services()** (7 connections) — `server/container/bundles/time.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **.__init__()** (6 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **._create_combat_service_with_nats()** (5 connections) — `server/container/bundles/combat.py`
- **.initialize()** (5 connections) — `server/container/main.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **.initialize()** (4 connections) — `server/container/bundles/chat.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **._init_quest_service()** (4 connections) — `server/container/bundles/game.py`
- **.initialize()** (4 connections) — `server/container/bundles/time.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container_creates_new_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- *... and 86 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (45 shared connections)
- [Any](Any.md) (14 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (14 shared connections)
- [ContainerComponent](ContainerComponent.md) (12 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (10 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (8 shared connections)
- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [ChatMessage](ChatMessage.md) (5 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (4 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (3 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (3 shared connections)
- [TestHelperFunctions](TestHelperFunctions.md) (3 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/game.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 295 (93%)
- INFERRED: 23 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*