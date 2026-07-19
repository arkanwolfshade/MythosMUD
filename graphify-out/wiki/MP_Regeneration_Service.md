# MP Regeneration Service

> 79 nodes · cohesion 0.03

## Key Concepts

- **test_mp_regeneration_service.py** (32 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **MPRegenerationService** (22 connections) — `server/game/magic/mp_regeneration_service.py`
- **mp_regeneration_service.py** (10 connections) — `server/game/magic/mp_regeneration_service.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **Any** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **UUID** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.__init__()** (3 connections) — `server/game/magic/mp_regeneration_service.py`
- **mp_regeneration_service()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_mp_regeneration_service_init()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_mp_regeneration_service_init_custom_rate()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **mock_player()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **mock_player_service()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() returns error when player not found.** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() restores MP.** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test restore_mp_from_rest() calculates max_mp from power if not present.** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test process_tick_regeneration() uses REST multiplier for sitting position.** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **sample_player_id()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_default_position()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_lying()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_sitting()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_get_regen_multiplier_standing()** (2 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- *... and 54 more nodes in this community*

## Relationships

- [[Magic Service Bundle]] (6 shared connections)
- [[Combat Command Handler]] (5 shared connections)
- [[Magic Lifespan Initialization]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Combat Player Broadcasts]] (2 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`
- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 199 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
