# Health Check Models

> 42 nodes

## Key Concepts

- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (23 connections) — `server/models/combat.py`
- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (10 connections) — `server/services/combat_service_attack.py`
- **_make_participant()** (10 connections) — `server/tests/unit/services/test_combat_service.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (9 connections) — `server/services/combat_service_attack.py`
- **_make_combat_instance()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **apply_damage_and_check_involuntary_flee()** (8 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (6 connections) — `server/services/combat_service_attack.py`
- **UUID** (6 connections)
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **_effective_room_for_melee()** (5 connections) — `server/services/combat_service_attack.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **_melee_location_fail_reason()** (4 connections) — `server/services/combat_service_attack.py`
- **Result of a combat action.** (1 connections) — `server/models/combat.py`
- **Apply attack damage and check for involuntary flee.** (1 connections) — `server/services/combat_service.py`
- *... and 17 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (15 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (13 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (11 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (10 shared connections)
- [E2E Playwright Conversion Plan](E2E_Playwright_Conversion_Plan.md) (3 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (3 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (3 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 221 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*