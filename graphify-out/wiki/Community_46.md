# Community 46

> 132 nodes

## Key Concepts

- **login_grace_period.py** (45 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (39 connections) — `server/realtime/login_grace_period.py`
- **is_player_in_login_grace_period()** (30 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
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
- **asyncio** (8 connections)
- **_login_grace_period_seconds()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_both_linkdead_and_warded_indicators()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- *... and 107 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (16 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (5 shared connections)
- [Player Name Extraction](Player_Name_Extraction.md) (5 shared connections)
- [Community 574](Community_574.md) (5 shared connections)
- [Community 550](Community_550.md) (4 shared connections)
- [Community 55](Community_55.md) (4 shared connections)
- [Community 263](Community_263.md) (4 shared connections)
- [Community 124](Community_124.md) (4 shared connections)
- [Community 87](Community_87.md) (3 shared connections)
- [Community 170](Community_170.md) (3 shared connections)
- [Community 1395](Community_1395.md) (3 shared connections)
- [Community 893](Community_893.md) (2 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 336 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*