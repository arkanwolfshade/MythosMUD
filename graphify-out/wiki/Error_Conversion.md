# Error Conversion

> 277 nodes

## Key Concepts

- **EventBus** (159 connections) — `server/events/event_bus.py`
- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (67 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **event_bus.py** (31 connections) — `server/events/event_bus.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_request_execution.py** (20 connections) — `server/npc/spawning_request_execution.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **SimpleNPCDefinition** (17 connections) — `server/npc/spawning_models.py`
- **NPCSpawnRequest** (17 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (17 connections) — `server/npc/spawning_request_execution.py`
- **party_service.py** (16 connections) — `server/game/party_service.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (16 connections) — `server/npc/spawning_models.py`
- **NPCSpawnStatistics** (16 connections) — `server/npc/spawning_service.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **test_follow_flow.py** (13 connections) — `server/tests/integration/test_follow_flow.py`
- **PartyUpdated** (12 connections) — `server/events/event_types.py`
- **Party** (12 connections) — `server/game/party_service.py`
- **shopkeeper_npc.py** (12 connections) — `server/npc/shopkeeper_npc.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **test_party_flow.py** (12 connections) — `server/tests/integration/test_party_flow.py`
- **Any** (10 connections)
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- *... and 252 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (104 shared connections)
- [NPC Combat](NPC_Combat.md) (35 shared connections)
- [container events rationale](container_events_rationale.md) (24 shared connections)
- [item models rationale](item_models_rationale.md) (16 shared connections)
- [services nats service](services_nats_service.md) (15 shared connections)
- [party game service](party_game_service.md) (14 shared connections)
- [models npc rationale](models_npc_rationale.md) (13 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (9 shared connections)
- [Room Broadcast](Room_Broadcast.md) (8 shared connections)
- [command input commands](command_input_commands.md) (8 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (8 shared connections)
- [party service game](party_service_game.md) (7 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/npc/behaviors.py`
- `server/npc/npc_base.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/realtime/connection_manager.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/npc/test_spawning_modules.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 1202 (91%)
- INFERRED: 116 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*