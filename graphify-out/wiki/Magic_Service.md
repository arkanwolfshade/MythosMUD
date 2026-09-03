# Magic Service

> 62 nodes

## Key Concepts

- **_MagicServiceCore** (44 connections) — `server/game/magic/magic_service.py`
- **UUID** (21 connections)
- **JsonMap** (12 connections)
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (10 connections) — `server/game/magic/magic_service.py`
- **._get_spell_and_validate_target()** (9 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (9 connections) — `server/game/magic/magic_service.py`
- **._casting_roll()** (7 connections) — `server/game/magic/magic_service.py`
- **._casting_roll_or_fail_result()** (7 connections) — `server/game/magic/magic_service.py`
- **._get_player_and_normalized_stats()** (7 connections) — `server/game/magic/magic_service.py`
- **._handle_instant_cast()** (7 connections) — `server/game/magic/magic_service.py`
- **._validate_spell_casting()** (7 connections) — `server/game/magic/magic_service.py`
- **_stat_int()** (7 connections) — `server/game/magic/magic_service.py`
- **._consume_materials_if_required()** (6 connections) — `server/game/magic/magic_service.py`
- **._perform_luck_check()** (6 connections) — `server/game/magic/magic_service.py`
- **._send_spell_completion_message()** (6 connections) — `server/game/magic/magic_service.py`
- **_StatsPlayer** (5 connections) — `server/game/magic/magic_service.py`
- **._check_already_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_lucidity_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_materials_available()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_mp_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_player_knows_spell()** (5 connections) — `server/game/magic/magic_service.py`
- **.interrupt_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._player_persistence()** (5 connections) — `server/game/magic/magic_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (21 shared connections)
- [Test Magic Service](Test_Magic_Service.md) (13 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (4 shared connections)
- [Test Magic Healing Events](Test_Magic_Healing_Events.md) (1 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (1 shared connections)
- [Spell Learning Service](Spell_Learning_Service.md) (1 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (1 shared connections)
- [Spell Materials](Spell_Materials.md) (1 shared connections)
- [Connection Manager Api](Connection_Manager_Api.md) (1 shared connections)
- [Test Inventory Command Coercion](Test_Inventory_Command_Coercion.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 154 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*