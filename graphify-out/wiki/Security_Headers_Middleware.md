# Security Headers Middleware

> 44 nodes

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
- **._get_player_and_normalized_stats()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_mp_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_lucidity_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_player_knows_spell()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_materials_available()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_already_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._handle_instant_cast()** (5 connections) — `server/game/magic/magic_service.py`
- **._consume_materials_if_required()** (5 connections) — `server/game/magic/magic_service.py`
- **._casting_roll()** (5 connections) — `server/game/magic/magic_service.py`
- **._get_spell_from_registry()** (4 connections) — `server/game/magic/magic_service.py`
- **._calculate_initiative_tick()** (4 connections) — `server/game/magic/magic_service.py`
- **.restore_mp()** (4 connections) — `server/game/magic/magic_service.py`
- **._resolve_heal_spell_id()** (3 connections) — `server/game/magic/magic_service.py`
- **Core magic service for spellcasting operations.      Handles MP management, sp** (1 connections) — `server/game/magic/magic_service.py`
- **Load player and return normalized stats (MP/max_MP). Returns (player, stats) or** (1 connections) — `server/game/magic/magic_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (20 shared connections)
- [Services Exploration Service](Services_Exploration_Service.md) (6 shared connections)
- [Config Cors](Config_Cors.md) (5 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (2 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (1 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (1 shared connections)
- [Archive Room Hierarchy](Archive_Room_Hierarchy.md) (1 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 202 (94%)
- INFERRED: 14 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*