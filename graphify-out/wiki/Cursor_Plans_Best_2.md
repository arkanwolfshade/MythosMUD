# Cursor Plans Best

> 7 nodes · cohesion 0.29

## Key Concepts

- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **_get_proper_data_dir()** (4 connections) — `server/services/user_manager.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **Path** (3 connections)
- **Get the mute data file path for a specific player.** (1 connections) — `server/services/user_manager.py`
- **Get the proper environment-aware data directory for user management.      Uses** (1 connections) — `server/services/user_manager.py`
- **Initialize the user manager.          Args:             data_dir: Directory f** (1 connections) — `server/services/user_manager.py`

## Relationships

- [Player Mute Persistence](Player_Mute_Persistence.md) (4 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [SSE Authentication Docs](SSE_Authentication_Docs.md) (1 shared connections)
- [E2E Suite Overview](E2E_Suite_Overview.md) (1 shared connections)
- [Services Npc Startup](Services_Npc_Startup.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*