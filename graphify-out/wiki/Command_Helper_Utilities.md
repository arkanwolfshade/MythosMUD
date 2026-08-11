# Command Helper Utilities

> 57 nodes

## Key Concepts

- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (9 connections) — `server/services/combat_death_handler.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **._log_room_subscribers_before_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (8 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **.handle_attack_events_and_xp()** (8 connections) — `server/services/combat_event_handler.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **.award_xp_to_player()** (5 connections) — `server/services/combat_event_handler.py`
- **.publish_combat_ended_event()** (5 connections) — `server/services/combat_event_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **._resolve_participant_display_name()** (4 connections) — `server/services/combat_event_handler.py`
- **UUID** (4 connections)
- **._calculate_xp_reward()** (4 connections) — `server/services/combat_event_handler.py`
- **Protocol** (3 connections)
- **.canonical_room_id()** (3 connections) — `server/services/combat_death_handler.py`
- **UUID** (3 connections)
- *... and 32 more nodes in this community*

## Relationships

- [Inventory Command Models](Inventory_Command_Models.md) (13 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (11 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (10 shared connections)
- [Health Check Models](Health_Check_Models.md) (9 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (8 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (5 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (5 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (5 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (3 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (2 shared connections)

## Source Files

- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_service.py`

## Audit Trail

- EXTRACTED: 189 (83%)
- INFERRED: 39 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*