# player persistence repository

> 15 nodes

## Key Concepts

- **_process_mortally_wounded_player()** (10 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (6 connections)
- **_process_passive_lucidity_flux()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_dead_players()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_players()** (5 connections) — `server/app/game_tick_processing.py`
- **test_process_mortally_wounded_skips_active_combat()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_mortally_wounded_death_threshold()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dead_players_moves_to_limbo()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_passive_lucidity_flux()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Process a single mortally wounded player's DP decay and death check.      CRITIC** (1 connections) — `server/app/game_tick_processing.py`
- **Process all mortally wounded players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process passive lucidity flux service if available.** (1 connections) — `server/app/game_tick_processing.py`
- **Process dead players and move them to limbo if needed.** (1 connections) — `server/app/game_tick_processing.py`
- **Process DP decay and death for a single database session.** (1 connections) — `server/app/game_tick_processing.py`

## Relationships

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (14 shared connections)
- [realtime message nats](realtime_message_nats.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [models player rationale](models_player_rationale.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*