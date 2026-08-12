# Zone Config Loader

> 197 nodes

## Key Concepts

- **Player** (200 connections) — `server/models/player.py`
- **player.py** (82 connections) — `server/models/player.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **_stats_int()** (17 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **int_coercion.py** (13 connections) — `server/utils/int_coercion.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **test_lucidity_adjustment_round_trip()** (7 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **test_cold_damage_resistance_reduces_damage()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **_convert_legacy_stats_string()** (3 connections) — `server/models/player.py`
- *... and 172 more nodes in this community*

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (23 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (14 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (13 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (13 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (11 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (11 shared connections)
- [Conftest Migration Plan](Conftest_Migration_Plan.md) (11 shared connections)
- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (10 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (10 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (10 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (7 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/player.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/services/test_player_death_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 730 (88%)
- INFERRED: 102 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*