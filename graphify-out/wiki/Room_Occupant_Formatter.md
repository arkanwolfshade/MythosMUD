# Room Occupant Formatter

> 18 nodes

## Key Concepts

- **test_occupant_formatter.py** (29 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_valid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_valid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_player()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_string_occupant_for_update_valid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_dict_npcs()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_strings()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_mixed()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_empty()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Unit tests for occupant formatter.  Tests the occupant_formatter module classes** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._is_valid_name_for_occupant() returns True for valid name** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_npc_name_for_update() adds valid NPC name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_dict_occupant_for_update() processes player dict** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_string_occupant_for_update() adds valid string.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() separates dict NPCs.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() processes string occupants.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() handles mixed types.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() handles empty list.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`

## Relationships

- [Command Integration Summary](Command_Integration_Summary.md) (15 shared connections)
- [Archive Circuit Breaker](Archive_Circuit_Breaker.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [test_validate_room_integrity_room_without_get_players](test_validate_room_integrity_room_without_get_players.md) (1 shared connections)
- [test_get_movement_monitor_returns_singleton](test_get_movement_monitor_returns_singleton.md) (1 shared connections)
- [test_get_alerts_slow_movement_time](test_get_alerts_slow_movement_time.md) (1 shared connections)
- [test_get_alerts_high_failure_rate](test_get_alerts_high_failure_rate.md) (1 shared connections)
- [test_get_metrics_with_data](test_get_metrics_with_data.md) (1 shared connections)
- [test_validate_room_integrity_valid](test_validate_room_integrity_valid.md) (1 shared connections)
- [test_get_metrics_integrity_rate](test_get_metrics_integrity_rate.md) (1 shared connections)
- [test_get_alerts_no_alerts](test_get_alerts_no_alerts.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*