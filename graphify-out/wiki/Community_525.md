# Community 525

> 33 nodes

## Key Concepts

- **_NPCCombatIntegrationDeps** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCCombatIntegrationCombatMixin** (11 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.join_existing_combat_for_mixin()** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.join_player_to_combat()** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (9 connections)
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_messaging_integration()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.join_existing_combat_for_mixin()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.join_player_to_combat()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_npc_attack_on_player_started()** (3 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **CombatMessagingIntegration** (1 connections)
- **Protocol** (1 connections)
- **Structured logging / observability trail when NPC-initiated combat begins.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Process combat attack, starting new combat or continuing existing one.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Join the combat the target NPC is already in (#833); the first attack is queued…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Add a player to a fight already under way and tell the room (#833, #991).…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Start a new combat and process initial attack.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Broadcast room occupants update to killer's room after NPC death. Swallows…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 8 more nodes in this community*

## Relationships

- [Combat Attack Execution](Combat_Attack_Execution.md) (9 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (4 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (2 shared connections)
- [Community 369](Community_369.md) (2 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (1 shared connections)
- [Community 170](Community_170.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_combat_mixin.py`

## Audit Trail

- EXTRACTED: 75 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*