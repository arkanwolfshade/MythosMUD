# container inventory display

> 22 nodes

## Key Concepts

- **test_container_helpers_inventory_display.py** (18 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **get_container_data_for_inventory()** (10 connections) — `server/commands/container_helpers_inventory_display.py`
- **match_container_to_slot()** (9 connections) — `server/commands/container_helpers_inventory_display.py`
- **update_equipped_with_container_info()** (7 connections) — `server/commands/container_helpers_inventory_display.py`
- **_equipped_matches_container_metadata()** (6 connections) — `server/commands/container_helpers_inventory_display.py`
- **_lock_state_as_str()** (5 connections) — `server/commands/container_helpers_inventory_display.py`
- **test_equipped_matches_by_name()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_equipped_matches_by_id()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_equipped_no_match()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_match_container_to_slot_found()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_match_container_to_slot_not_found()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_lock_state_as_str_with_value_attr()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_lock_state_as_str_fallback()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_get_container_data_for_inventory_success()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_get_container_data_for_inventory_handles_error()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_update_equipped_with_container_info()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **test_update_equipped_skips_missing_slot()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`
- **Player** (1 connections)
- **Match a container component to an equipped slot. Returns slot name or None.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Get container contents, capacities, and lock states for equipped containers.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Update equipped items' metadata to include container information.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Unit tests for container_helpers_inventory_display.** (1 connections) — `server/tests/unit/commands/test_container_helpers_inventory_display.py`

## Relationships

- [task registry app](task_registry_app.md) (10 shared connections)
- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (3 shared connections)
- [realtime real time](realtime_real_time.md) (2 shared connections)
- [player cache rationale](player_cache_rationale.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_display.py`
- `server/tests/unit/commands/test_container_helpers_inventory_display.py`

## Audit Trail

- EXTRACTED: 80 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*