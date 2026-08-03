# item models rationale

> 292 nodes

## Key Concepts

- **event_types.py** (79 connections) — `server/events/event_types.py`
- **BaseEvent** (73 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (71 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (53 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **test_player_event_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **room.py** (30 connections) — `server/models/room.py`
- **event_reaction_system.py** (29 connections) — `server/npc/event_reaction_system.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **test_npc_combat_integration_class.py** (23 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **movement_integration.py** (18 connections) — `server/npc/movement_integration.py`
- **NPCSpoke** (16 connections) — `server/events/event_types.py`
- **PlayerDPDecayEvent** (16 connections) — `server/events/event_types.py`
- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **PlayerDeliriumRespawnedEvent** (15 connections) — `server/events/event_types.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- *... and 267 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (102 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (53 shared connections)
- [NATS Messaging](NATS_Messaging.md) (37 shared connections)
- [command inventory factories](command_inventory_factories.md) (30 shared connections)
- [NPC Combat](NPC_Combat.md) (20 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (18 shared connections)
- [command service commands](command_service_commands.md) (16 shared connections)
- [npc event handlers](npc_event_handlers.md) (13 shared connections)
- [Room Broadcast](Room_Broadcast.md) (13 shared connections)
- [Database Config](Database_Config.md) (12 shared connections)
- [combat attack handler](combat_attack_handler.md) (12 shared connections)
- [follow game service](follow_game_service.md) (11 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/models/room.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/population_control.py`
- `server/realtime/event_handler.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/services/player_death_service.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 1385 (89%)
- INFERRED: 172 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*