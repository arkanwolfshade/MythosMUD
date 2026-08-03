# command models admin

> 22 nodes

## Key Concepts

- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (6 connections)
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_messaging_integration()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_npc_attack_on_player_started()** (3 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Protocol** (1 connections)
- **Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize them** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return combat service dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return data provider dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return messaging integration dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Start a new combat from mixin combat pipeline.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Resolve participant combat data and apply the initial attack damage through Comb** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Structured logging / observability trail when NPC-initiated combat begins.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Process combat attack, starting new combat or continuing existing one.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Start a new combat and process initial attack.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Broadcast room occupants update to killer's room after NPC death. Swallows error** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`

## Relationships

- [models npc rationale](models_npc_rationale.md) (11 shared connections)
- [movement monitor game](movement_monitor_game.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [tracked app task](tracked_app_task.md) (2 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_combat_mixin.py`

## Audit Trail

- EXTRACTED: 80 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*