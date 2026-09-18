# Community 884

> 17 nodes

## Key Concepts

- **UUID** (10 connections)
- **_TickCombatService** (6 connections) — `server/app/game_tick_protocols.py`
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
- **AsyncSession** (5 connections)
- **.get_combat_by_participant()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_dead_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_mortally_wounded_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.handle_player_death()** (3 connections) — `server/app/game_tick_protocols.py`
- **.process_mortally_wounded_tick()** (3 connections) — `server/app/game_tick_protocols.py`
- **.move_player_to_limbo()** (3 connections) — `server/app/game_tick_protocols.py`
- **.publish_player_dp_decay_event_to_nats()** (2 connections) — `server/app/game_tick_protocols.py`
- **.send_personal_message()** (2 connections) — `server/app/game_tick_protocols.py`
- **.process_tick_for_player()** (2 connections) — `server/app/game_tick_protocols.py`
- **.process_tick_regeneration()** (2 connections) — `server/app/game_tick_protocols.py`
- **.cleanup_stale_combats()** (1 connections) — `server/app/game_tick_protocols.py`
- **.process_game_tick()** (1 connections) — `server/app/game_tick_protocols.py`
- **PlayerDPDecayEvent** (1 connections)

## Relationships

- [Community 370](Community_370.md) (9 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (2 shared connections)
- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (1 shared connections)
- [Community 831](Community_831.md) (1 shared connections)
- [Community 542](Community_542.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*