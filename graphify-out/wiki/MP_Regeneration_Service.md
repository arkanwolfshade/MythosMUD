# MP Regeneration Service

> 82 nodes · cohesion 0.03

## Key Concepts

- **test_mp_regeneration_service.py** (33 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **MPRegenerationService** (20 connections) — `server/game/magic/mp_regeneration_service.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **mp_regeneration_service()** (4 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **.__init__()** (3 connections) — `server/game/magic/mp_regeneration_service.py`
- **test_mp_regeneration_service_init()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_mp_regeneration_service_init_custom_rate()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **mock_player()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **mock_player_service()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **sample_player_id()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_default_position()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_lying()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_sitting()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_standing()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_at_max()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_calculates_max_from_power()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_fractional_accumulation()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_process_tick_regeneration_lying_position()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- *... and 57 more nodes in this community*

## Relationships

- [Players API Endpoints](Players_API_Endpoints.md) (4 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (3 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (3 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (3 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Lucidity Recovery Commands](Lucidity_Recovery_Commands.md) (1 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`
- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 202 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*