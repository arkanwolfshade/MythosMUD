# Combat Death Handling

> 59 nodes · cohesion 0.05

## Key Concepts

- **CorpseLifecycleService** (25 connections) — `server/services/corpse_lifecycle_service.py`
- **CombatInstance** (11 connections) — `server/services/combat_death_handler.py`
- **CombatParticipant** (10 connections) — `server/services/combat_death_handler.py`
- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (8 connections) — `server/services/combat_death_handler.py`
- **.cleanup_decayed_corpse()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **._create_corpse_on_death()** (7 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (7 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (7 connections) — `server/services/combat_death_handler.py`
- **UUID** (6 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (6 connections) — `server/services/combat_death_handler.py`
- **.create_corpse_on_death()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.handle_target_state_changes()** (5 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (5 connections) — `server/services/combat_death_handler.py`
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **._resolve_connection_manager_for_corpse_creation()** (4 connections) — `server/services/combat_death_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **.can_access_corpse()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- *... and 34 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (18 shared connections)
- [[Async Persistence Layer]] (6 shared connections)
- [[Combat Domain Events]] (6 shared connections)
- [[Container Component Capacity]] (6 shared connections)
- [[Combat Taunt Tests]] (5 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Player Combat XP]] (3 shared connections)
- [[Game Tick Processing]] (2 shared connections)

## Source Files

- `server/services/combat_death_handler.py`
- `server/services/combat_service.py`
- `server/services/corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 200 (87%)
- INFERRED: 31 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
