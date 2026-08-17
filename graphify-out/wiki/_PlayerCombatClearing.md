# _PlayerCombatClearing

> 11 nodes

## Key Concepts

- **_PlayerCombatClearing** (5 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (5 connections) — `server/services/player_respawn_service.py`
- **.__init__()** (4 connections) — `server/services/player_respawn_service.py`
- **.clear_player_combat_state()** (3 connections) — `server/services/player_respawn_service.py`
- **.publish()** (3 connections) — `server/services/player_respawn_service.py`
- **Protocol** (3 connections)
- **Minimal surface used by this service to publish respawn-related events.** (1 connections) — `server/services/player_respawn_service.py`
- **Deliver a respawn-related domain event to the game's event bus.** (1 connections) — `server/services/player_respawn_service.py`
- **Minimal surface used to clear combat state when a player respawns.** (1 connections) — `server/services/player_respawn_service.py`
- **Drop combat involvement for this player after respawn.** (1 connections) — `server/services/player_respawn_service.py`
- **Initialize the player respawn service. Args: event_bus: Optional event bus for…** (1 connections) — `server/services/player_respawn_service.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*