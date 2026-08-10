# E2E Playwright Conversion Plan

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

- [Magic Service Bundle](Magic_Service_Bundle.md) (9 shared connections)
- [Health Check Models](Health_Check_Models.md) (3 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (2 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_combat_mixin.py`

## Audit Trail

- EXTRACTED: 78 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*