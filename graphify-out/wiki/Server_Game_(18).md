# Server Game (18)

> 54 nodes

## Key Concepts

- **_MagicServiceCore** (42 connections) — `server/game/magic/magic_service.py`
- **UUID** (20 connections)
- **Any** (18 connections)
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (8 connections) — `server/game/magic/magic_service.py`
- **._get_spell_and_validate_target()** (7 connections) — `server/game/magic/magic_service.py`
- **._validate_spell_casting()** (6 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (6 connections) — `server/game/magic/magic_service.py`
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

- [Server Game (4)](Server_Game_%284%29.md) (8 shared connections)
- [Server Models (13)](Server_Models_%2813%29.md) (7 shared connections)
- [Server Game (14)](Server_Game_%2814%29.md) (3 shared connections)
- [Server Realtime (48)](Server_Realtime_%2848%29.md) (2 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (2 shared connections)
- [Server Game (2)](Server_Game_%282%29.md) (1 shared connections)
- [Server Game (34)](Server_Game_%2834%29.md) (1 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 228 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*