# ChatLogger

> 142 nodes · cohesion 0.03

## Key Concepts

- **is_player_in_login_grace_period()** (51 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (45 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (43 connections) — `server/realtime/login_grace_period.py`
- **game_state_provider.py** (36 connections) — `server/realtime/integration/game_state_provider.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_login_grace_period.py** (25 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **get_login_grace_period_remaining()** (22 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_flow.py** (21 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **UUID** (13 connections)
- **FakeGraceManager** (13 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **handle_login_grace_period_expiration()** (10 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (10 connections)
- **_as_grace()** (9 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (9 connections)
- **_grace_period_task()** (8 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (8 connections)
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **_login_grace_period_seconds()** (7 connections) — `server/realtime/login_grace_period.py`
- **Protocol** (7 connections)
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 117 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (10 shared connections)
- [ResourceManager](ResourceManager.md) (9 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (7 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (6 shared connections)
- [Room](Room.md) (6 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (6 shared connections)
- [Communities (355 total, 223 thin omitted)](Communities_355_total,_223_thin_omitted.md) (6 shared connections)
- [security.ts](security.ts.md) (5 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (5 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (5 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (5 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 407 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*