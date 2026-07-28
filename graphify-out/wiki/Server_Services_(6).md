# Server Services (6)

> 140 nodes

## Key Concepts

- **PlayerCombatService** (76 connections) — `server/services/player_combat_service.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **player_combat_service.py** (34 connections) — `server/services/player_combat_service.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (9 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **._award_xp_via_persistence_fallback()** (6 connections) — `server/services/player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **Protocol** (6 connections)
- **player_combat_service()** (6 connections) — `server/tests/unit/services/test_player_combat_service.py`
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
- *... and 115 more nodes in this community*

## Relationships

- [Server Npc (2)](Server_Npc_%282%29.md) (17 shared connections)
- [Server Events](Server_Events.md) (16 shared connections)
- [Server Commands (29)](Server_Commands_%2829%29.md) (10 shared connections)
- [Server Commands](Server_Commands.md) (7 shared connections)
- [Server Realtime (42)](Server_Realtime_%2842%29.md) (7 shared connections)
- [Server Commands (8)](Server_Commands_%288%29.md) (6 shared connections)
- [Server Events (3)](Server_Events_%283%29.md) (5 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (4 shared connections)
- [Server Realtime (50)](Server_Realtime_%2850%29.md) (4 shared connections)
- [Server Commands (24)](Server_Commands_%2824%29.md) (3 shared connections)
- [Server Services (29)](Server_Services_%2829%29.md) (3 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (3 shared connections)

## Source Files

- `server/commands/combat_loader.py`
- `server/realtime/player_event_handlers.py`
- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 493 (92%)
- INFERRED: 41 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*