# Player Combat XP

> 144 nodes · cohesion 0.02

## Key Concepts

- **Protocol** (82 connections)
- **test_player_combat_service.py** (36 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **PlayerXPAwardEvent** (34 connections) — `server/services/player_combat_service.py`
- **PlayerCombatService** (29 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service.py** (22 connections) — `server/services/player_combat_service.py`
- **UUID** (19 connections) — `server/services/player_combat_service.py`
- **player_combat_service_support.py** (16 connections) — `server/services/player_combat_service_support.py`
- **PlayerCombatState** (15 connections) — `server/services/player_combat_service.py`
- **NPCCombatIntegrationReadApi** (11 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (10 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (10 connections) — `server/services/player_combat_service_support.py`
- **_EventBusPublishPort** (6 connections) — `server/realtime/event_handlers.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **NPCCombatRewardsLike** (6 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (6 connections) — `server/services/player_combat_service_support.py`
- **UUID** (5 connections) — `server/services/player_combat_service_support.py`
- **._award_xp_via_persistence_fallback()** (5 connections) — `server/services/player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (5 connections) — `server/services/player_combat_service_support.py`
- **NPCLifecycleManager** (4 connections) — `server/services/player_combat_service_support.py`
- **._award_xp_via_npc_rewards()** (4 connections) — `server/services/player_combat_service.py`
- **.calculate_xp_reward()** (4 connections) — `server/services/player_combat_service.py`
- *... and 119 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (21 shared connections)
- [[NPC Death Lifecycle]] (13 shared connections)
- [[NPC Admin API]] (10 shared connections)
- [[Player Event Handler Tests]] (9 shared connections)
- [[Realtime Event Delegation]] (7 shared connections)
- [[Spell Effect Protocols]] (6 shared connections)
- [[Combat Command Handler]] (5 shared connections)
- [[Distributed Event Bus]] (5 shared connections)
- [[Communication Command Flows]] (4 shared connections)
- [[Player Respawn Events]] (4 shared connections)
- [[Combat Flee Command]] (3 shared connections)
- [[Combat Player Broadcasts]] (3 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 534 (93%)
- INFERRED: 43 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
