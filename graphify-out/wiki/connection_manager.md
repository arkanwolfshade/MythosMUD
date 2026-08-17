# .connection_manager

> 39 nodes

## Key Concepts

- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **_CombatServiceDeps** (6 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (6 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (6 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (5 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (5 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (4 connections) — `server/services/combat_death_handler.py`
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **Protocol** (3 connections)
- **.get_npc_combat_integration_service()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **.canonical_room_id()** (2 connections) — `server/services/combat_death_handler.py`
- **UUID** (2 connections)
- **setter** (1 connections)
- **Check connection state before publishing combat ended event.** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Create corpse container when player dies.** (1 connections) — `server/services/combat_death_handler.py`
- **Best-effort connection diagnostics before publishing NPC death event.** (1 connections) — `server/services/combat_death_handler.py`
- **Resolve UUID participant id to canonical NPC string id when mapping exists.** (1 connections) — `server/services/combat_death_handler.py`
- **Connection manager surface used for room subscriber diagnostics.** (1 connections) — `server/services/combat_death_handler.py`
- *... and 14 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (16 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [NPCStartupService](NPCStartupService.md) (3 shared connections)
- [CombatMessagingService](CombatMessagingService.md) (3 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (1 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (1 shared connections)
- [._handle_npc_death_on_combat_end](_handle_npc_death_on_combat_end.md) (1 shared connections)
- [combat_service_attack.py](combat_service_attack.py.md) (1 shared connections)
- [NPCCombatRewards](NPCCombatRewards.md) (1 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`

## Audit Trail

- EXTRACTED: 66 (84%)
- INFERRED: 13 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*