# Community 491

> 36 nodes

## Key Concepts

- **game_tick_protocols.py** (31 connections) — `server/app/game_tick_protocols.py`
- **Protocol** (10 connections)
- **UUID** (10 connections)
- **_TickCombatService** (6 connections) — `server/app/game_tick_protocols.py`
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
- **AsyncSession** (5 connections)
- **_TickContainer** (4 connections) — `server/app/game_tick_protocols.py`
- **_online_player_ids()** (4 connections) — `server/app/game_tick_protocols.py`
- **_TickConnectionManager** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickCorruptionFlux** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickEventBus** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickMagicService** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickMpRegen** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickNpcLifecycle** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickRespawnService** (3 connections) — `server/app/game_tick_protocols.py`
- **_tick_online_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_combat_by_participant()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_dead_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_mortally_wounded_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.handle_player_death()** (3 connections) — `server/app/game_tick_protocols.py`
- **.process_mortally_wounded_tick()** (3 connections) — `server/app/game_tick_protocols.py`
- **.move_player_to_limbo()** (3 connections) — `server/app/game_tick_protocols.py`
- **.publish_player_dp_decay_event_to_nats()** (2 connections) — `server/app/game_tick_protocols.py`
- **.send_personal_message()** (2 connections) — `server/app/game_tick_protocols.py`
- **.process_tick_for_player()** (2 connections) — `server/app/game_tick_protocols.py`
- *... and 11 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (6 shared connections)
- [Community 893](Community_893.md) (3 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (2 shared connections)
- [Community 65](Community_65.md) (2 shared connections)
- [Community 550](Community_550.md) (2 shared connections)
- [Community 490](Community_490.md) (1 shared connections)
- [Game Event Types](Game_Event_Types.md) (1 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (1 shared connections)
- [Community 943](Community_943.md) (1 shared connections)
- [Community 412](Community_412.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*