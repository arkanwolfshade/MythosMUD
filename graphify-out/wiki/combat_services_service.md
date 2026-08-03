# combat services service

> 15 nodes

## Key Concepts

- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (7 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (6 connections)
- **_process_mp_regeneration()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_players()** (5 connections) — `server/app/game_tick_processing.py`
- **_process_passive_lucidity_flux()** (4 connections) — `server/app/game_tick_processing.py`
- **_process_dead_players()** (4 connections) — `server/app/game_tick_processing.py`
- **_validate_mp_regeneration_services()** (3 connections) — `server/app/game_tick_processing.py`
- **Process a single mortally wounded player's DP decay and death check.      CRITIC** (1 connections) — `server/app/game_tick_processing.py`
- **Process all mortally wounded players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process passive lucidity flux service if available.** (1 connections) — `server/app/game_tick_processing.py`
- **Validate that required services exist for MP regeneration.      Args:         co** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process dead players and move them to limbo if needed.** (1 connections) — `server/app/game_tick_processing.py`
- **Process DP decay and death for a single database session.** (1 connections) — `server/app/game_tick_processing.py`

## Relationships

- [auth endpoints rationale](auth_endpoints_rationale.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [models player rationale](models_player_rationale.md) (1 shared connections)
- [invite models rationale](invite_models_rationale.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*