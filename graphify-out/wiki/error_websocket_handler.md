# error websocket handler

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

- [services user manager](services_user_manager.md) (5 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)
- [auth invites rationale](auth_invites_rationale.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*