# Health Check Models

> 87 nodes

## Key Concepts

- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (23 connections) — `server/models/combat.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (14 connections) — `server/services/combat_service_events.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (10 connections) — `server/services/combat_service_attack.py`
- **_make_participant()** (10 connections) — `server/tests/unit/services/test_combat_service.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (9 connections) — `server/services/combat_service_attack.py`
- **_make_combat_instance()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **handle_combat_completion()** (8 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (8 connections) — `server/services/combat_service_attack.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **publish_npc_damage_event()** (7 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (7 connections) — `server/services/combat_service_events.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 62 more nodes in this community*

## Relationships

- [Container Exception Handlers](Container_Exception_Handlers.md) (34 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (18 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (17 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (17 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (13 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (12 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (12 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (10 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (9 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (6 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (5 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/events/combat_events.py`
- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_state.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 509 (95%)
- INFERRED: 29 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*