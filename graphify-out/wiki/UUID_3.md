# UUID

> 39 nodes

## Key Concepts

- **UUID** (20 connections)
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **.end_combat_if_npc_died()** (5 connections) — `server/services/combat_service.py`
- **.handle_attack_events_and_xp()** (5 connections) — `server/services/combat_service.py`
- **.validate_and_get_combat_participants()** (5 connections) — `server/services/combat_service.py`
- **.award_xp_to_player()** (4 connections) — `server/services/combat_service.py`
- **.end_combat()** (4 connections) — `server/services/combat_service.py`
- **.get_combat()** (4 connections) — `server/services/combat_service.py`
- **.get_combat_by_participant()** (4 connections) — `server/services/combat_service.py`
- **._get_combat_id_for_npc()** (4 connections) — `server/services/combat_service.py`
- **.process_attack()** (4 connections) — `server/services/combat_service.py`
- **.register_combat_state()** (4 connections) — `server/services/combat_service.py`
- **.broadcast_aggro_target_switches()** (3 connections) — `server/services/combat_service.py`
- **.get_combat_id_for_npc_uuid()** (3 connections) — `server/services/combat_service.py`
- **.get_combat_id_for_participant()** (3 connections) — `server/services/combat_service.py`
- **.notify_player_combat_ended()** (3 connections) — `server/services/combat_service.py`
- **.publish_npc_damage_event()** (3 connections) — `server/services/combat_service.py`
- **.publish_npc_died_event()** (3 connections) — `server/services/combat_service.py`
- **.queue_combat_action()** (3 connections) — `server/services/combat_service.py`
- **Publish an npc_took_damage event for non-combat damage.** (1 connections) — `server/services/combat_service.py`
- **Publish an npc_died event when non-combat damage kills an NPC.** (1 connections) — `server/services/combat_service.py`
- **Return combat_id if this NPC is in combat, else None.** (1 connections) — `server/services/combat_service.py`
- **End combat if the given NPC is in combat (e.g. steal-life kill).** (1 connections) — `server/services/combat_service.py`
- **Return the active combat for combat_id, or None if not found.** (1 connections) — `server/services/combat_service.py`
- *... and 14 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (20 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [combat_service_attack.py](combat_service_attack.py.md) (3 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (2 shared connections)

## Source Files

- `server/services/combat_service.py`

## Audit Trail

- EXTRACTED: 76 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*