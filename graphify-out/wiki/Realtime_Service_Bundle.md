# Realtime Service Bundle

> 215 nodes

## Key Concepts

- **time.py** (89 connections) — `server/container/bundles/time.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **npc_base.py** (41 connections) — `server/npc/npc_base.py`
- **PassiveMobNPC** (29 connections) — `server/npc/passive_mob_npc.py`
- **event_reaction_system.py** (27 connections) — `server/npc/event_reaction_system.py`
- **NPCDied** (25 connections) — `server/events/event_types.py`
- **combat_integration.py** (25 connections) — `server/npc/combat_integration.py`
- **NPCThreadManager** (25 connections) — `server/npc/threading.py`
- **lifecycle_death.py** (23 connections) — `server/npc/lifecycle_death.py`
- **__init__.py** (22 connections) — `server/npc/__init__.py`
- **NPCEventReactionSystem** (21 connections) — `server/npc/event_reaction_system.py`
- **aggressive_mob_npc.py** (18 connections) — `server/npc/aggressive_mob_npc.py`
- **movement_integration.py** (18 connections) — `server/npc/movement_integration.py`
- **passive_mob_npc.py** (18 connections) — `server/npc/passive_mob_npc.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **_SpawnTrackedNPC** (17 connections) — `server/npc/lifecycle_manager.py`
- **NPCLifecycleRecord** (17 connections) — `server/npc/lifecycle_types.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- **_SpawningServiceProtocol** (16 connections) — `server/npc/lifecycle_manager.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **Any** (14 connections)
- *... and 190 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (52 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (46 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (43 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (41 shared connections)
- [NPC Movement Integration](NPC_Movement_Integration.md) (12 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (12 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (9 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (8 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (8 shared connections)
- [Player Position Service](Player_Position_Service.md) (8 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (8 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (7 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/container/bundles/time.py`
- `server/events/event_types.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behavior_engine.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 1110 (92%)
- INFERRED: 102 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*