# regeneration service magic

> 78 nodes

## Key Concepts

- **test_mp_regeneration_service.py** (33 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **MPRegenerationService** (20 connections) — `server/game/magic/mp_regeneration_service.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **UUID** (5 connections)
- **Any** (5 connections)
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **mp_regeneration_service()** (4 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **.__init__()** (3 connections) — `server/game/magic/mp_regeneration_service.py`
- **test_mp_regeneration_service_init()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_mp_regeneration_service_init_custom_rate()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **mock_player_service()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **sample_player_id()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **mock_player()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_player_not_found()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_at_max()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_restores_mp()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_calculates_max_from_power()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_fractional_accumulation()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_standing()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_sitting()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_lying()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_default_position()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- *... and 53 more nodes in this community*

## Relationships

- [coercion int inventory](coercion_int_inventory.md) (8 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)
- [realtime real time](realtime_real_time.md) (1 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`
- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 186 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*