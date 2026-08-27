# test_metrics.py

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

- [eventHandlers/types.ts](eventHandlers-types.ts.md) (16 shared connections)
- [Any](Any.md) (11 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (5 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (4 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)
- [migrate_rooms.py](migrate_rooms.py.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [debugLogger](debugLogger.md) (1 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)
- [PlayerStatsConfig](PlayerStatsConfig.md) (1 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 154 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*