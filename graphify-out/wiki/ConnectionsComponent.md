# ConnectionsComponent

> 33 nodes

## Key Concepts

- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
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
- **player_death_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Initialize combat services.** (1 connections) — `server/container/bundles/combat.py`
- **Service for managing player death, mortally wounded state, and DP decay.      Th** (1 connections) — `server/services/player_death_service.py`
- **Initialize the player death service.          Args:             event_bus: Optio** (1 connections) — `server/services/player_death_service.py`
- **Get all players currently in the mortally wounded state.          A player is co** (1 connections) — `server/services/player_death_service.py`
- **Get all players who are dead (DP <= -10).          Args:             session: As** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player.          Decreases player** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead.          Args:             play** (1 connections) — `server/services/player_death_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (15 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (4 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [cfg bool()](cfg_bool%28%29.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [combat initialization](combat_initialization.md) (2 shared connections)
- [.shutdown()](shutdown%28%29.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)
- [config](config.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 127 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*