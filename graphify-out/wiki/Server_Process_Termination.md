# Server Process Termination

> 22 nodes

## Key Concepts

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
- **Service for managing MP regeneration.      Handles passive regeneration over tim** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Initialize the MP regeneration service.          Args:             player_servic** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Process MP regeneration for a player on a game tick.          Args:** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Get MP regeneration multiplier based on player state.          Args:** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from resting (accelerated regeneration).          Args:             p** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from meditation (highly accelerated regeneration).          Args:** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from consuming an item.          Args:             player_id: Player** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Create an MPRegenerationService instance.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test MPRegenerationService initialization.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`
- **Test MPRegenerationService initialization with custom regen_rate.** (1 connections) — `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Relationships

- [NPC Service Tests](NPC_Service_Tests.md) (5 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (4 shared connections)
- [Cursor Agents Quick](Cursor_Agents_Quick.md) (4 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`
- `server/tests/unit/game/magic/test_mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 71 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*