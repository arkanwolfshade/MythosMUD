# Command Integration Summary

> 16 nodes

## Key Concepts

- **OccupantFormatter** (37 connections) — `server/realtime/occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_empty()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_add_valid_name_to_lists()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_player_name_for_update_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_npc()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_dict_players()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Formats and separates occupants by type.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Initialize occupant formatter.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Test OccupantFormatter._is_valid_name_for_occupant() returns False for empty str** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_player_name_for_update() skips UUID player name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_dict_occupant_for_update() processes NPC dict.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() separates dict players.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`

## Relationships

- [Room Occupant Formatter](Room_Occupant_Formatter.md) (15 shared connections)
- [Contexts Themecontext Hooks](Contexts_Themecontext_Hooks.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Archive Circuit Breaker](Archive_Circuit_Breaker.md) (2 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (2 shared connections)
- [test_validate_room_integrity_room_without_get_players](test_validate_room_integrity_room_without_get_players.md) (1 shared connections)
- [test_get_movement_monitor_returns_singleton](test_get_movement_monitor_returns_singleton.md) (1 shared connections)
- [test_get_alerts_slow_movement_time](test_get_alerts_slow_movement_time.md) (1 shared connections)
- [test_get_alerts_high_failure_rate](test_get_alerts_high_failure_rate.md) (1 shared connections)
- [test_get_metrics_with_data](test_get_metrics_with_data.md) (1 shared connections)
- [test_validate_room_integrity_valid](test_validate_room_integrity_valid.md) (1 shared connections)
- [test_get_metrics_integrity_rate](test_get_metrics_integrity_rate.md) (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*