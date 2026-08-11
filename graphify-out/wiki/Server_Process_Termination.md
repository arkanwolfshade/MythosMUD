# Server Process Termination

> 20 nodes

## Key Concepts

- **MPRegenerationService** (20 connections) — `server/game/magic/mp_regeneration_service.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **UUID** (5 connections)
- **Any** (5 connections)
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.__init__()** (3 connections) — `server/game/magic/mp_regeneration_service.py`
- **MP regeneration service for passive and active magic point recovery.  This modul** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Service for managing MP regeneration.      Handles passive regeneration over tim** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Initialize the MP regeneration service.          Args:             player_servic** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Process MP regeneration for a player on a game tick.          Args:** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Get MP regeneration multiplier based on player state.          Args:** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from resting (accelerated regeneration).          Args:             p** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from meditation (highly accelerated regeneration).          Args:** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from consuming an item.          Args:             player_id: Player** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **# NOTE: Server tick rate is 0.1 seconds, so 0.01 MP per tick = 0.1 MP per second** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **# TODO: Check status effects for meditation when status effect system supports i** (1 connections) — `server/game/magic/mp_regeneration_service.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Cursor Agents Quick](Cursor_Agents_Quick.md) (4 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (2 shared connections)
- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (1 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 75 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*