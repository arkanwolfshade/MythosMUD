# Archive Fixture Optimization

> 11 nodes

## Key Concepts

- **_RespawnEventPublisher** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (6 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (6 connections) — `server/services/player_respawn_service.py`
- **.__init__()** (4 connections) — `server/services/player_respawn_service.py`
- **Protocol** (3 connections)
- **.choice()** (3 connections) — `server/services/player_respawn_service.py`
- **Minimal surface used by this service to publish respawn-related events.** (1 connections) — `server/services/player_respawn_service.py`
- **Minimal surface used to clear combat state when a player respawns.** (1 connections) — `server/services/player_respawn_service.py`
- **Subset of random.Random / random module API used for liability picks.** (1 connections) — `server/services/player_respawn_service.py`
- **Return one element from a non-empty sequence of liability codes.** (1 connections) — `server/services/player_respawn_service.py`
- **Initialize the player respawn service.          Args:             event_bus: Opt** (1 connections) — `server/services/player_respawn_service.py`

## Relationships

- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (5 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)

## Source Files

- `server/services/player_respawn_service.py`

## Audit Trail

- EXTRACTED: 30 (91%)
- INFERRED: 3 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*