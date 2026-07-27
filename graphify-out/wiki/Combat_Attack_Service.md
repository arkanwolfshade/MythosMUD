# Combat Attack Service

> 54 nodes · cohesion 0.07

## Key Concepts

- **combat_service_attack.py** (21 connections) — `server/services/combat_service_attack.py`
- **get_current_tick()** (14 connections) — `server/app/game_tick_processing.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **CombatResult** (12 connections) — `server/models/combat.py`
- **finalize_attack_result()** (12 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (11 connections) — `server/services/combat_service_attack.py`
- **CombatService** (9 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **CombatParticipant** (8 connections) — `server/services/combat_service_attack.py`
- **UUID** (8 connections) — `server/services/combat_service_attack.py`
- **UUID** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **CombatInstance** (7 connections) — `server/services/combat_service_attack.py`
- **handle_combat_completion()** (7 connections) — `server/services/combat_service_attack.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **CombatResult** (6 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (6 connections) — `server/services/combat_service_attack.py`
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **CombatResult** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_effective_room_for_melee()** (5 connections) — `server/services/combat_service_attack.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 29 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (20 shared connections)
- [[NPC Combat Lifecycle]] (15 shared connections)
- [[Combat Taunt Tests]] (9 shared connections)
- [[Combat Domain Events]] (6 shared connections)
- [[App Game Tick]] (3 shared connections)
- [[Magic Service Bundle]] (2 shared connections)
- [[Look Command Helpers]] (2 shared connections)
- [[Combat Aggro Threat]] (2 shared connections)
- [[Players API Endpoints]] (1 shared connections)
- [[Game Tick Processing]] (1 shared connections)
- [[App Lifespan Management]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/models/combat.py`
- `server/services/combat_service_attack.py`
- `server/services/npc_combat_integration_combat_mixin.py`

## Audit Trail

- EXTRACTED: 239 (90%)
- INFERRED: 27 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
