# Dual Connection API Reference

> 20 nodes

## Key Concepts

- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **.get_mortally_wounded_players()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **Initialize the player death service.          Args:             event_bus: Optio** (1 connections) — `server/services/player_death_service.py`
- **Get all players currently in the mortally wounded state.          A player is co** (1 connections) — `server/services/player_death_service.py`
- **Get all players who are dead (DP <= -10).          Args:             session: As** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player.          Decreases player** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead.          Args:             play** (1 connections) — `server/services/player_death_service.py`
- **Clear player combat state when they die.          BUGFIX #244: As documented in** (1 connections) — `server/services/player_death_service.py`
- **Publish player died event if event bus is available.          Args:** (1 connections) — `server/services/player_death_service.py`
- **Handle player death when DP reaches -10 or below.          Records death locatio** (1 connections) — `server/services/player_death_service.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (4 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (4 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (2 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)

## Source Files

- `server/services/player_death_service.py`

## Audit Trail

- EXTRACTED: 68 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*