# .handle_player_death

> 20 nodes

## Key Concepts

- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **Process DP decay for a single mortally wounded player. Decreases player DP by…** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead. Args: player: Player object to…** (1 connections) — `server/services/player_death_service.py`
- **Clear player combat state when they die. BUGFIX #244: As documented in…** (1 connections) — `server/services/player_death_service.py`
- **Publish player died event if event bus is available. Args: player_id: ID of the…** (1 connections) — `server/services/player_death_service.py`
- **Handle player death when DP reaches -10 or below. Records death location and…** (1 connections) — `server/services/player_death_service.py`
- **Initialize the player death service. Args: event_bus: Optional event bus for…** (1 connections) — `server/services/player_death_service.py`
- **Get all players currently in the mortally wounded state. A player is considered…** (1 connections) — `server/services/player_death_service.py`
- **Get all players who are dead (DP <= -10). Args: session: Async database session…** (1 connections) — `server/services/player_death_service.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (10 shared connections)
- [test_command_factories_utility.py](test_command_factories_utility.py.md) (4 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)

## Source Files

- `server/services/player_death_service.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*