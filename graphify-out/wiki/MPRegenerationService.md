# MPRegenerationService

> 20 nodes

## Key Concepts

- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.__init__()** (3 connections) — `server/game/magic/mp_regeneration_service.py`
- **test_mp_regeneration_service_init()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **test_mp_regeneration_service_init_custom_rate()** (3 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Get MP regeneration multiplier based on player state. Args: stats: Player stats…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from resting (accelerated regeneration). Args: player_id: Player ID…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from meditation (highly accelerated regeneration). Args: player_id:…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from consuming an item. Args: player_id: Player ID amount: Amount of…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Service for managing MP regeneration. Handles passive regeneration over time…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Initialize the MP regeneration service. Args: player_service: Player service…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Process MP regeneration for a player on a game tick. Args: player_id: Player ID…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Test MPRegenerationService initialization.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test MPRegenerationService initialization with custom regen_rate.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [SpellEffects](SpellEffects.md) (3 shared connections)
- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [mp_regeneration_service](mp_regeneration_service.md) (1 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`
- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 39 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*