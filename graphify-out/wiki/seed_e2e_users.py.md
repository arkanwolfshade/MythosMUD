# seed_e2e_users.py

> 12 nodes

## Key Concepts

- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **spawn_defaults.py** (9 connections) — `server/constants/spawn_defaults.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **main()** (3 connections) — `scripts/seed_e2e_users.py`
- **E2eUserSpec** (2 connections) — `scripts/seed_e2e_users.py`
- **datetime** (2 connections)
- **UUID** (2 connections)
- **Connection** (1 connections)
- **Entry point: run E2E user seed via anyio.** (1 connections) — `scripts/seed_e2e_users.py`
- **One row in users plus optional default character for login E2E.** (1 connections) — `scripts/seed_e2e_users.py`
- **Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.…** (1 connections) — `server/constants/spawn_defaults.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (1 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (1 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (1 shared connections)
- [test_npc_combat_integration_service.py](test_npc_combat_integration_service.py.md) (1 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/constants/spawn_defaults.py`

## Audit Trail

- EXTRACTED: 24 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*