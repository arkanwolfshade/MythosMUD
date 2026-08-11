# Security Headers Middleware

> 38 nodes

## Key Concepts

- **_MagicServiceCore** (43 connections) — `server/game/magic/magic_service.py`
- **UUID** (20 connections)
- **Any** (18 connections)
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (8 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (7 connections) — `server/game/magic/magic_service.py`
- **._get_spell_and_validate_target()** (7 connections) — `server/game/magic/magic_service.py`
- **._validate_spell_casting()** (6 connections) — `server/game/magic/magic_service.py`
- **._casting_roll_or_fail_result()** (6 connections) — `server/game/magic/magic_service.py`
- **._send_spell_completion_message()** (6 connections) — `server/game/magic/magic_service.py`
- **._get_player_and_normalized_stats()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_already_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._handle_instant_cast()** (5 connections) — `server/game/magic/magic_service.py`
- **._consume_materials_if_required()** (5 connections) — `server/game/magic/magic_service.py`
- **._casting_roll()** (5 connections) — `server/game/magic/magic_service.py`
- **.send_spell_execution_notifications()** (5 connections) — `server/game/magic/magic_service.py`
- **._get_spell_from_registry()** (4 connections) — `server/game/magic/magic_service.py`
- **._calculate_initiative_tick()** (4 connections) — `server/game/magic/magic_service.py`
- **.restore_mp()** (4 connections) — `server/game/magic/magic_service.py`
- **._resolve_heal_spell_id()** (3 connections) — `server/game/magic/magic_service.py`
- **Core magic service for spellcasting operations.      Handles MP management, sp** (1 connections) — `server/game/magic/magic_service.py`
- **Load player and return normalized stats (MP/max_MP). Returns (player, stats) or** (1 connections) — `server/game/magic/magic_service.py`
- **Check if player is already casting a spell.** (1 connections) — `server/game/magic/magic_service.py`
- **Get spell from registry by ID or name.** (1 connections) — `server/game/magic/magic_service.py`
- **Validate spell can be cast and resolve target.** (1 connections) — `server/game/magic/magic_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (25 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Archive Database Migration](Archive_Database_Migration.md) (5 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (1 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 180 (93%)
- INFERRED: 14 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*