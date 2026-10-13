# Game Event Types

> 241 nodes

## Key Concepts

- **event_types.py** (101 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (54 connections) — `server/events/event_types.py`
- **event_handler.py** (42 connections) — `server/realtime/event_handler.py`
- **player_event_handlers.py** (41 connections) — `server/realtime/player_event_handlers.py`
- **test_room_sync_service.py** (40 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **PlayerLeftRoom** (32 connections) — `server/events/event_types.py`
- **NPCEventReaction** (23 connections) — `server/npc/event_reaction_system.py`
- **RoomSyncService** (22 connections) — `server/services/room_sync_service.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **register_default_reactions_for_npc()** (18 connections) — `server/npc/npc_default_reactions.py`
- **room_sync_service.py** (17 connections) — `server/services/room_sync_service.py`
- **test_reaction_revival_integration.py** (17 connections) — `server/tests/unit/npc/test_reaction_revival_integration.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_player_event_handlers_room_left.py** (15 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **NPCEventReactionTemplates** (14 connections) — `server/npc/event_reaction_system.py`
- **asyncio** (14 connections)
- **corruption_reactions.py** (13 connections) — `server/npc/corruption_reactions.py`
- **message_builders.py** (13 connections) — `server/realtime/message_builders.py`
- **PlayerDiedEvent** (11 connections) — `server/events/event_types.py`
- **PlayerDPUpdated** (11 connections) — `server/events/event_types.py`
- **test_npc_default_reactions.py** (11 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **asyncio** (11 connections)
- **NPCListened** (10 connections) — `server/events/event_types.py`
- **schedule_npc_room_speech()** (10 connections) — `server/game/chat_npc_system.py`
- **build_corruption_aware_greeting()** (10 connections) — `server/npc/corruption_reactions.py`
- *... and 216 more nodes in this community*

## Relationships

- [NPC Behavior Engine](NPC_Behavior_Engine.md) (56 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (30 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (26 shared connections)
- [Community 75](Community_75.md) (16 shared connections)
- [Community 244](Community_244.md) (14 shared connections)
- [Community 318](Community_318.md) (12 shared connections)
- [Community 337](Community_337.md) (11 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (10 shared connections)
- [Community 209](Community_209.md) (9 shared connections)
- [Community 65](Community_65.md) (8 shared connections)
- [Community 212](Community_212.md) (8 shared connections)
- [Community 53](Community_53.md) (6 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/chat_npc_system.py`
- `server/npc/corruption_reactions.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/player_event_handlers.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/npc/test_corruption_reactions.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`
- `server/tests/unit/npc/test_reaction_revival_integration.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 665 (95%)
- INFERRED: 36 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*