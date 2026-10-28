# asyncio

> 115 nodes · cohesion 0.03

## Key Concepts

- **look_helpers.py** (30 connections) — `server/commands/look_helpers.py`
- **test_look_helpers.py** (30 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_look_helpers_functions.py** (29 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **_get_health_label()** (17 connections) — `server/commands/look_helpers.py`
- **_get_lucidity_label()** (17 connections) — `server/commands/look_helpers.py`
- **_get_visible_equipment()** (11 connections) — `server/commands/look_helpers.py`
- **_get_wearable_container_service()** (11 connections) — `server/commands/look_helpers.py`
- **_is_direction()** (11 connections) — `server/commands/look_helpers.py`
- **_parse_instance_number()** (11 connections) — `server/commands/look_helpers.py`
- **_get_corruption_label()** (9 connections) — `server/commands/look_helpers.py`
- **_get_corruption_prose()** (9 connections) — `server/commands/look_helpers.py`
- **Protocol** (5 connections)
- **_stat_number()** (5 connections) — `server/commands/look_helpers.py`
- **_EquippedPlayer** (4 connections) — `server/commands/look_helpers.py`
- **test_get_corruption_label_all_tiers()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_corruption_label_defaults_to_untainted_when_missing()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_corruption_prose_none_below_marked()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_health_label_critical()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_health_label_healthy()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_health_label_mortally_wounded()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_health_label_wounded()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_lucidity_label_disturbed_medium()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_lucidity_label_lucid()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_lucidity_label_mad()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **test_get_lucidity_label_mad_negative()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- *... and 90 more nodes in this community*

## Relationships

- [FeatureFlagService](FeatureFlagService.md) (12 shared connections)
- [_RecordingRoom](_RecordingRoom.md) (6 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (5 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (3 shared connections)
- [look_helpers.py](look_helpers.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_helpers.py`
- `server/tests/unit/commands/test_look_helpers_functions.py`

## Audit Trail

- EXTRACTED: 210 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*