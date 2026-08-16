# get_current_tick

> 28 nodes

## Key Concepts

- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **get_current_tick()** (14 connections) — `server/app/game_tick_counter.py`
- **NPCCombatIntegrationCombatMixin** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **game_tick_counter.py** (8 connections) — `server/app/game_tick_counter.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (5 connections)
- **.get_messaging_integration()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_npc_attack_on_player_started()** (3 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Protocol** (1 connections)
- **Shared game tick counter. Kept in a leaf module so combat services can read the…** (1 connections) — `server/app/game_tick_counter.py`
- **Get the current game tick.** (1 connections) — `server/app/game_tick_counter.py`
- **Structured logging / observability trail when NPC-initiated combat begins.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Process combat attack, starting new combat or continuing existing one.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Start a new combat and process initial attack.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Broadcast room occupants update to killer's room after NPC death. Swallows…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return combat service dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return data provider dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return messaging integration dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 3 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (13 shared connections)
- [reset_current_tick](reset_current_tick.md) (4 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/services/npc_combat_integration_combat_mixin.py`

## Audit Trail

- EXTRACTED: 65 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*