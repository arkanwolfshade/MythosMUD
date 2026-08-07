# services rescue service

> 7 nodes

## Key Concepts

- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **_get_proper_data_dir()** (4 connections) — `server/services/user_manager.py`
- **Path** (3 connections)
- **Initialize the user manager.          Args:             data_dir: Directory f** (1 connections) — `server/services/user_manager.py`
- **Get the mute data file path for a specific player.** (1 connections) — `server/services/user_manager.py`
- **Get the proper environment-aware data directory for user management.      Uses** (1 connections) — `server/services/user_manager.py`

## Relationships

- [services user manager](services_user_manager.md) (4 shared connections)
- [chat services logger](chat_services_logger.md) (1 shared connections)
- [room persistence loader](room_persistence_loader.md) (1 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (1 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*