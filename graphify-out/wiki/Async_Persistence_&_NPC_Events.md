# Async Persistence & NPC Events

> 273 nodes

## Key Concepts

- **event_types.py** (97 connections) — `server/events/event_types.py`
- **async_persistence.py** (78 connections) — `server/async_persistence.py`
- **NPCEnteredRoom** (49 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (49 connections) — `server/events/event_types.py`
- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
- **event_bus.py** (40 connections) — `server/events/event_bus.py`
- **lifecycle_manager.py** (37 connections) — `server/npc/lifecycle_manager.py`
- **models/room.py** (36 connections) — `server/models/room.py`
- **event_reaction_system.py** (30 connections) — `server/npc/event_reaction_system.py`
- **NPCDied** (29 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (28 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **server/events/__init__.py** (26 connections) — `server/events/__init__.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **player_event_handlers_respawn.py** (24 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_event_reaction_speech.py** (22 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **NPCEventReaction** (21 connections) — `server/npc/event_reaction_system.py`
- **NPCEventReactionSystem** (20 connections) — `server/npc/event_reaction_system.py`
- **despawn_npc_impl()** (20 connections) — `server/npc/lifecycle_despawn.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_make_manager()** (18 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **register_default_reactions_for_npc()** (17 connections) — `server/npc/npc_default_reactions.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **combat_hp_sync.py** (15 connections) — `server/services/combat_hp_sync.py`
- *... and 248 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (63 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (50 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (34 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (23 shared connections)
- [Test Event Handler](Test_Event_Handler.md) (22 shared connections)
- [Async Persistence](Async_Persistence.md) (18 shared connections)
- [Npc Base](Npc_Base.md) (18 shared connections)
- [Test Npc Utils](Test_Npc_Utils.md) (14 shared connections)
- [Test Quest Events](Test_Quest_Events.md) (13 shared connections)
- [Test Npc Event Handlers](Test_Npc_Event_Handlers.md) (13 shared connections)
- [Test Chat Npc System](Test_Chat_Npc_System.md) (11 shared connections)
- [Event Types](Event_Types.md) (9 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_types.py`
- `server/events/__init__.py`
- `server/events/event_bus.py`
- `server/events/event_bus_base.py`
- `server/events/event_bus_processing.py`
- `server/events/event_types.py`
- `server/models/room.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/shopkeeper_npc.py`

## Audit Trail

- EXTRACTED: 1002 (93%)
- INFERRED: 71 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*