# Community 490

> 36 nodes

## Key Concepts

- **game_tick_death.py** (38 connections) — `server/app/game_tick_death.py`
- **_process_mortally_wounded_player()** (15 connections) — `server/app/game_tick_death.py`
- **_TickContainer** (11 connections)
- **_process_session_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **process_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **_process_mortally_wounded_players()** (9 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (9 connections) — `server/app/game_tick_death.py`
- **_process_passive_corruption_flux()** (9 connections) — `server/app/game_tick_death.py`
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (8 connections)
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_death.py`
- **_create_bleed_out_corpse()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **_dp_decay_due()** (3 connections) — `server/app/game_tick_death.py`
- **Player** (3 connections)
- **FastAPI** (2 connections)
- **UUID** (2 connections)
- **_TickMpRegen** (1 connections)
- **DP decay, death, and MP regeneration for the game tick loop.** (1 connections) — `server/app/game_tick_death.py`
- **Process a single mortally wounded player's DP decay and death check. CRITICAL:…** (1 connections) — `server/app/game_tick_death.py`
- **True once per second of game time: DP decay is 1 DP/second regardless of tick…** (1 connections) — `server/app/game_tick_death.py`
- **Process all mortally wounded players.** (1 connections) — `server/app/game_tick_death.py`
- *... and 11 more nodes in this community*

## Relationships

- [Community 412](Community_412.md) (15 shared connections)
- [Community 550](Community_550.md) (9 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Community 441](Community_441.md) (4 shared connections)
- [Community 380](Community_380.md) (4 shared connections)
- [Community 176](Community_176.md) (3 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (2 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (2 shared connections)
- [Community 893](Community_893.md) (1 shared connections)
- [Community 118](Community_118.md) (1 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)
- [Game Event Types](Game_Event_Types.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`

## Audit Trail

- EXTRACTED: 117 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*