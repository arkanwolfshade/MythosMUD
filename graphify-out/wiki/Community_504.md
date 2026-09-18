# Community 504

> 34 nodes

## Key Concepts

- **PlayerDeathService** (23 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (14 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **.initialize()** (7 connections) — `server/container/bundles/combat.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.process_mortally_wounded_tick()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **.set_player_combat_service()** (3 connections) — `server/realtime/connection_manager.py`
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **._get_room_name_for_death()** (3 connections) — `server/services/player_death_service.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **PlayerCombatService** (3 connections)
- **Any** (3 connections)
- **PlayerDiedEvent** (2 connections)
- **Exception** (1 connections)
- **Initialize combat services.** (1 connections) — `server/container/bundles/combat.py`
- **Set the player combat service for the connection manager.** (1 connections) — `server/realtime/connection_manager.py`
- **Delegate player died event to specialized handler.** (1 connections) — `server/realtime/event_handler.py`
- **Get all players who are dead (DP <= -10). Args: session: Async database session…** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player. Decreases player DP by…** (1 connections) — `server/services/player_death_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (6 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (4 shared connections)
- [Community 103](Community_103.md) (3 shared connections)
- [Community 125](Community_125.md) (3 shared connections)
- [Community 390](Community_390.md) (3 shared connections)
- [Community 80](Community_80.md) (2 shared connections)
- [FastAPI Dependency Providers](FastAPI_Dependency_Providers.md) (1 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (1 shared connections)
- [Catatonia Status Checks](Catatonia_Status_Checks.md) (1 shared connections)
- [Community 172](Community_172.md) (1 shared connections)
- [Community 93](Community_93.md) (1 shared connections)
- [Community 276](Community_276.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/realtime/connection_manager.py`
- `server/realtime/event_handler.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 72 (90%)
- INFERRED: 8 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*