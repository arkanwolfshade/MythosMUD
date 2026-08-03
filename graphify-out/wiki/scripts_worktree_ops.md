# scripts worktree ops

> 31 nodes

## Key Concepts

- **UUID** (20 connections)
- **.end_combat_if_npc_died()** (5 connections) — `server/services/combat_service.py`
- **._get_combat_id_for_npc()** (4 connections) — `server/services/combat_service.py`
- **.get_combat()** (4 connections) — `server/services/combat_service.py`
- **.get_combat_by_participant()** (4 connections) — `server/services/combat_service.py`
- **.award_xp_to_player()** (4 connections) — `server/services/combat_service.py`
- **.process_attack()** (4 connections) — `server/services/combat_service.py`
- **.register_combat_state()** (4 connections) — `server/services/combat_service.py`
- **.end_combat()** (4 connections) — `server/services/combat_service.py`
- **.publish_npc_damage_event()** (3 connections) — `server/services/combat_service.py`
- **.publish_npc_died_event()** (3 connections) — `server/services/combat_service.py`
- **.get_combat_id_for_participant()** (3 connections) — `server/services/combat_service.py`
- **.get_combat_id_for_npc_uuid()** (3 connections) — `server/services/combat_service.py`
- **.broadcast_aggro_target_switches()** (3 connections) — `server/services/combat_service.py`
- **.queue_combat_action()** (3 connections) — `server/services/combat_service.py`
- **.notify_player_combat_ended()** (3 connections) — `server/services/combat_service.py`
- **Publish an npc_took_damage event for non-combat damage.** (1 connections) — `server/services/combat_service.py`
- **Publish an npc_died event when non-combat damage kills an NPC.** (1 connections) — `server/services/combat_service.py`
- **Return combat_id if this NPC is in combat, else None.** (1 connections) — `server/services/combat_service.py`
- **End combat if the given NPC is in combat (e.g. steal-life kill).** (1 connections) — `server/services/combat_service.py`
- **Return the active combat for combat_id, or None if not found.** (1 connections) — `server/services/combat_service.py`
- **Return combat_id if a participant is in combat, else None.** (1 connections) — `server/services/combat_service.py`
- **Return combat_id if an NPC UUID is in combat, else None.** (1 connections) — `server/services/combat_service.py`
- **Return the combat instance for a specific participant, if any.** (1 connections) — `server/services/combat_service.py`
- **Broadcast one room message per aggro target switch (ADR-016).         switches:** (1 connections) — `server/services/combat_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (15 shared connections)
- [command factories exploration](command_factories_exploration.md) (5 shared connections)
- [movement monitor game](movement_monitor_game.md) (3 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)

## Source Files

- `server/services/combat_service.py`

## Audit Trail

- EXTRACTED: 89 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*