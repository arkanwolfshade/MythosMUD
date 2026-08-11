# NPC Services Bundle

> 113 nodes

## Key Concepts

- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **._award_xp_via_persistence_fallback()** (6 connections) — `server/services/player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **player_combat_service()** (6 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_end()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_npc_death()** (4 connections) — `server/services/player_combat_service.py`
- **._award_xp_via_npc_rewards()** (4 connections) — `server/services/player_combat_service.py`
- **.calculate_xp_reward()** (4 connections) — `server/services/player_combat_service.py`
- **test_is_player_in_combat_sync_true()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_cleanup_stale_combat_states()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.set_player_combat_service()** (3 connections) — `server/services/combat_service.py`
- **.is_player_in_combat_sync()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.get_players_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.cleanup_stale_combat_states()** (3 connections) — `server/services/player_combat_service.py`
- *... and 88 more nodes in this community*

## Relationships

- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (10 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (7 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (3 shared connections)
- [Redis to NATS Migration](Redis_to_NATS_Migration.md) (3 shared connections)
- [Mythos Calendar Time Service](Mythos_Calendar_Time_Service.md) (2 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [Container Open Events](Container_Open_Events.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/models/npc.py`
- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 357 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*