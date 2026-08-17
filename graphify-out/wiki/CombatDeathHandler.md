# CombatDeathHandler

> 37 nodes

## Key Concepts

- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **_CombatServiceDeps** (6 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (6 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (6 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (6 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (5 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (5 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (4 connections) — `server/services/combat_death_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **Protocol** (3 connections)
- **.get_npc_combat_integration_service()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **.canonical_room_id()** (2 connections) — `server/services/combat_death_handler.py`
- **UUID** (2 connections)
- **Create corpse container when player dies.** (1 connections) — `server/services/combat_death_handler.py`
- **Best-effort connection diagnostics before publishing NPC death event.** (1 connections) — `server/services/combat_death_handler.py`
- **Resolve UUID participant id to canonical NPC string id when mapping exists.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish NPC death event to NATS when combat publisher is available.** (1 connections) — `server/services/combat_death_handler.py`
- **Connection manager surface used for room subscriber diagnostics.** (1 connections) — `server/services/combat_death_handler.py`
- **Handle NPC death event publishing and ID resolution.** (1 connections) — `server/services/combat_death_handler.py`
- *... and 12 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (11 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [CombatParticipant](CombatParticipant.md) (6 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (2 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (2 shared connections)
- [NPCStartupService](NPCStartupService.md) (2 shared connections)
- [.connection_manager](connection_manager.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [get_connection_manager](get_connection_manager.md) (1 shared connections)

## Source Files

- `server/services/combat_death_handler.py`

## Audit Trail

- EXTRACTED: 68 (87%)
- INFERRED: 10 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*