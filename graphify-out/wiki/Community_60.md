# Community 60

> 116 nodes

## Key Concepts

- **login_grace_period.py** (45 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (43 connections) — `server/realtime/login_grace_period.py`
- **is_player_in_login_grace_period()** (39 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period.py** (25 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_login_grace_period_flow.py** (21 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **get_login_grace_period_remaining()** (18 connections) — `server/realtime/login_grace_period.py`
- **FakeGraceManager** (13 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **UUID** (13 connections)
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **asyncio** (10 connections)
- **_as_grace()** (9 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (9 connections)
- **_grace_period_task()** (8 connections) — `server/realtime/login_grace_period.py`
- **handle_login_grace_period_expiration()** (8 connections) — `server/realtime/login_grace_period.py`
- **_login_grace_period_seconds()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **Protocol** (7 connections)
- **_trigger_room_occupants_update()** (6 connections) — `server/realtime/login_grace_period.py`
- **test_grace_period_blocks_combat_initiation()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 91 more nodes in this community*

## Relationships

- [Community 326](Community_326.md) (16 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (13 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (7 shared connections)
- [Community 700](Community_700.md) (6 shared connections)
- [Community 46](Community_46.md) (4 shared connections)
- [Community 198](Community_198.md) (4 shared connections)
- [Community 61](Community_61.md) (3 shared connections)
- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (3 shared connections)
- [Community 435](Community_435.md) (3 shared connections)
- [Community 1358](Community_1358.md) (3 shared connections)
- [Community 426](Community_426.md) (2 shared connections)
- [Community 968](Community_968.md) (2 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`

## Audit Trail

- EXTRACTED: 307 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*