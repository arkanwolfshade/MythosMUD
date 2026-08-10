# Security Headers Middleware

> 54 nodes

## Key Concepts

- **_MagicServiceCore** (43 connections) — `server/game/magic/magic_service.py`
- **UUID** (20 connections)
- **Any** (18 connections)
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (8 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (7 connections) — `server/game/magic/magic_service.py`
- **._get_spell_and_validate_target()** (7 connections) — `server/game/magic/magic_service.py`
- **._validate_spell_casting()** (6 connections) — `server/game/magic/magic_service.py`
- **._casting_roll_or_fail_result()** (6 connections) — `server/game/magic/magic_service.py`
- **._send_spell_completion_message()** (6 connections) — `server/game/magic/magic_service.py`
- **._get_player_and_normalized_stats()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_mp_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_lucidity_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_player_knows_spell()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_materials_available()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_already_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._handle_instant_cast()** (5 connections) — `server/game/magic/magic_service.py`
- **._consume_materials_if_required()** (5 connections) — `server/game/magic/magic_service.py`
- **._casting_roll()** (5 connections) — `server/game/magic/magic_service.py`
- **.send_spell_execution_notifications()** (5 connections) — `server/game/magic/magic_service.py`
- **.interrupt_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._get_spell_from_registry()** (4 connections) — `server/game/magic/magic_service.py`
- **._calculate_initiative_tick()** (4 connections) — `server/game/magic/magic_service.py`
- **.restore_mp()** (4 connections) — `server/game/magic/magic_service.py`
- *... and 29 more nodes in this community*

## Relationships

- [NPC Service Tests](NPC_Service_Tests.md) (20 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (1 shared connections)
- [Async Persistence Migration](Async_Persistence_Migration.md) (1 shared connections)
- [Quality Audit Report](Quality_Audit_Report.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (1 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 229 (94%)
- INFERRED: 14 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*