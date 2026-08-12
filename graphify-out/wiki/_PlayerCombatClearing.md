# _PlayerCombatClearing

> 15 nodes

## Key Concepts

- **_PlayerCombatClearing** (6 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (6 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (6 connections) — `server/services/player_respawn_service.py`
- **.__init__()** (4 connections) — `server/services/player_respawn_service.py`
- **.clear_player_combat_state()** (3 connections) — `server/services/player_respawn_service.py`
- **.publish()** (3 connections) — `server/services/player_respawn_service.py`
- **Protocol** (3 connections)
- **.choice()** (2 connections) — `server/services/player_respawn_service.py`
- **Minimal surface used by this service to publish respawn-related events.** (1 connections) — `server/services/player_respawn_service.py`
- **Deliver a respawn-related domain event to the game's event bus.** (1 connections) — `server/services/player_respawn_service.py`
- **Minimal surface used to clear combat state when a player respawns.** (1 connections) — `server/services/player_respawn_service.py`
- **Drop combat involvement for this player after respawn.** (1 connections) — `server/services/player_respawn_service.py`
- **Subset of random.Random / random module API used for liability picks.** (1 connections) — `server/services/player_respawn_service.py`
- **Return one element from a non-empty sequence of liability codes.** (1 connections) — `server/services/player_respawn_service.py`
- **Initialize the player respawn service. Args: event_bus: Optional event bus for…** (1 connections) — `server/services/player_respawn_service.py`

## Relationships

- [Player](Player.md) (3 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (3 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`

## Audit Trail

- EXTRACTED: 22 (88%)
- INFERRED: 3 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*