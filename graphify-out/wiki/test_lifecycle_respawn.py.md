# test_lifecycle_respawn.py

> 31 nodes · cohesion 0.11

## Key Concepts

- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (11 connections) — `server/services/player_death_service.py`
- **.initialize()** (9 connections) — `server/container/bundles/combat.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **._get_room_name_for_death()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **._persist_death_location_stats()** (4 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **Player** (4 connections)
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Initialize combat services.** (1 connections) — `server/container/bundles/combat.py`
- **Get all players who are dead (DP <= -10). Args: session: Async database session…** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player. Decreases player DP by…** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead. Args: player: Player object to…** (1 connections) — `server/services/player_death_service.py`
- **Clear player combat state when they die. BUGFIX #244: As documented in…** (1 connections) — `server/services/player_death_service.py`
- **Get room name for death location display. Args: death_location: Room ID where…** (1 connections) — `server/services/player_death_service.py`
- **Store death room id/name on player stats so login can show the place of death.** (1 connections) — `server/services/player_death_service.py`
- **Publish player died event if event bus is available. Args: player_id: ID of the…** (1 connections) — `server/services/player_death_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [Room](Room.md) (5 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (4 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (2 shared connections)
- [Quick Start: Running E2E Tests](Quick_Start-_Running_E2E_Tests.md) (2 shared connections)
- [test_check_codacy_yaml.py](test_check_codacy_yaml.py.md) (2 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (2 shared connections)
- [validate_secure_path](validate_secure_path.md) (1 shared connections)
- [FollowService](FollowService.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 77 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*