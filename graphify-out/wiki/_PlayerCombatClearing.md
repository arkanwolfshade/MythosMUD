# _PlayerCombatClearing

> 14 nodes

## Key Concepts

- **_PlayerCombatClearing** (5 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (5 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (5 connections) — `server/services/player_respawn_service.py`
- **.__init__()** (5 connections) — `server/services/player_respawn_service.py`
- **.publish()** (3 connections) — `server/services/player_respawn_service.py`
- **Protocol** (3 connections)
- **.choice()** (2 connections) — `server/services/player_respawn_service.py`
- **Room** (1 connections)
- **Minimal surface used by this service to publish respawn-related events.** (1 connections) — `server/services/player_respawn_service.py`
- **Deliver a respawn-related domain event to the game's event bus.** (1 connections) — `server/services/player_respawn_service.py`
- **Minimal surface used to clear combat state when a player respawns.** (1 connections) — `server/services/player_respawn_service.py`
- **Subset of random.Random / random module API used for liability picks.** (1 connections) — `server/services/player_respawn_service.py`
- **Return one element from a non-empty sequence of liability codes.** (1 connections) — `server/services/player_respawn_service.py`
- **Initialize the player respawn service. Args: event_bus: Optional event bus for…** (1 connections) — `server/services/player_respawn_service.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (2 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*