# lucidity event services

> 194 nodes

## Key Concepts

- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (67 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_request_execution.py** (20 connections) — `server/npc/spawning_request_execution.py`
- **SimpleNPCDefinition** (17 connections) — `server/npc/spawning_models.py`
- **NPCSpawnRequest** (17 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (17 connections) — `server/npc/spawning_request_execution.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (16 connections) — `server/npc/spawning_models.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **CommunicationIntegrationProtocol** (10 connections) — `server/npc/npc_protocols.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (9 connections) — `server/npc/spawning_instance_factory.py`
- **CombatIntegrationProtocol** (7 connections) — `server/npc/npc_protocols.py`
- **_spawn_success()** (7 connections) — `server/npc/spawning_request_execution.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **._handle_npc_death()** (6 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- *... and 169 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (110 shared connections)
- [room look commands](room_look_commands.md) (12 shared connections)
- [container events rationale](container_events_rationale.md) (10 shared connections)
- [player event realtime](player_event_realtime.md) (7 shared connections)
- [services nats service](services_nats_service.md) (6 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (4 shared connections)
- [player event handlers](player_event_handlers.md) (4 shared connections)
- [party service game](party_service_game.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [error logging rationale](error_logging_rationale.md) (2 shared connections)
- [room occupant manager](room_occupant_manager.md) (2 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (2 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`
- `server/npc/npc_protocols.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/realtime/connection_manager.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 718 (90%)
- INFERRED: 83 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*