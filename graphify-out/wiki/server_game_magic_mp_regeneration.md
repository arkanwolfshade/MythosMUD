# server game magic mp regeneration

> 80 nodes

## Key Concepts

- **test_mp_regeneration_service.py** (34 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **asyncio** (20 connections)
- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **mp_regeneration_service()** (5 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **fixture** (4 connections)
- **.__init__()** (3 connections) — `server/game/magic/mp_regeneration_service.py`
- **mock_player()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **mock_player_service()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **sample_player_id()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_mp_regeneration_service_init()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_mp_regeneration_service_init_custom_rate()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_at_max()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_calculates_max_from_power()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_fractional_accumulation()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_lying_position()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_player_not_found()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_restores_mp()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_sitting_position()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- *... and 55 more nodes in this community*

## Relationships

- [server app lifespan magic](server_app_lifespan_magic.md) (4 shared connections)
- [followtargetvalue](followtargetvalue.md) (4 shared connections)
- [server api players](server_api_players.md) (2 shared connections)
- [server dependencies](server_dependencies.md) (1 shared connections)
- [server commands lucidity recovery commands](server_commands_lucidity_recovery_commands.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`
- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 122 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*