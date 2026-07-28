# Server Services (62)

> 26 nodes

## Key Concepts

- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **.initialize()** (8 connections) — `server/container/bundles/combat.py`
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **.get_mortally_wounded_players()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **._get_room_name_for_death()** (4 connections) — `server/services/player_death_service.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **Initialize combat services.** (1 connections) — `server/container/bundles/combat.py`
- **Service for managing player death, mortally wounded state, and DP decay.      Th** (1 connections) — `server/services/player_death_service.py`
- **Initialize the player death service.          Args:             event_bus: Optio** (1 connections) — `server/services/player_death_service.py`
- **Get all players currently in the mortally wounded state.          A player is co** (1 connections) — `server/services/player_death_service.py`
- **Get all players who are dead (DP <= -10).          Args:             session: As** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player.          Decreases player** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead.          Args:             play** (1 connections) — `server/services/player_death_service.py`
- **Clear player combat state when they die.          BUGFIX #244: As documented in** (1 connections) — `server/services/player_death_service.py`
- **Get room name for death location display.          Args:             death_locat** (1 connections) — `server/services/player_death_service.py`
- **Publish player died event if event bus is available.          Args:** (1 connections) — `server/services/player_death_service.py`
- *... and 1 more nodes in this community*

## Relationships

- [Server Services](Server_Services.md) (9 shared connections)
- [Server App](Server_App.md) (4 shared connections)
- [Server Events](Server_Events.md) (4 shared connections)
- [Server Structured Logging (9)](Server_Structured_Logging_%289%29.md) (4 shared connections)
- [Server App (2)](Server_App_%282%29.md) (3 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (2 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (2 shared connections)
- [Server Services (30)](Server_Services_%2830%29.md) (1 shared connections)
- [Server Services (41)](Server_Services_%2841%29.md) (1 shared connections)
- [Server Services (6)](Server_Services_%286%29.md) (1 shared connections)
- [Server Services (29)](Server_Services_%2829%29.md) (1 shared connections)
- [Server Services (103)](Server_Services_%28103%29.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/player_death_service.py`

## Audit Trail

- EXTRACTED: 103 (90%)
- INFERRED: 12 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*