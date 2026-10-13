# Community 118

> 94 nodes

## Key Concepts

- **test_combat_death_handler.py** (33 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **.get_instance()** (22 connections) — `server/container/main.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **asyncio** (12 connections)
- **.__init__()** (11 connections) — `server/services/combat_service.py`
- **patch** (10 connections)
- **CorpseConnectionManagerLike** (9 connections) — `server/services/corpse_lifecycle_service.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **test_death_location_uses_display_names_never_room_id()** (9 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **_CombatServiceDeps** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (6 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (5 connections) — `server/services/combat_death_handler.py`
- **_RoomContainers** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.handle_target_state_changes()** (5 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (5 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (5 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **Protocol** (5 connections)
- **fixture** (5 connections)
- **_NPCCombatIntegrationLike** (4 connections) — `server/services/combat_death_handler.py`
- **_SyncRoomLookup** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- *... and 69 more nodes in this community*

## Relationships

- [Combat Attack Execution](Combat_Attack_Execution.md) (11 shared connections)
- [Combat Participants](Combat_Participants.md) (11 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (10 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (6 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (5 shared connections)
- [Community 292](Community_292.md) (3 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (3 shared connections)
- [Community 176](Community_176.md) (2 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (2 shared connections)
- [Community 426](Community_426.md) (2 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (2 shared connections)
- [Community 1113](Community_1113.md) (2 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_service.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_combat_death_handler.py`

## Audit Trail

- EXTRACTED: 195 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*