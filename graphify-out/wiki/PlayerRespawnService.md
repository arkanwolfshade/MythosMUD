# PlayerRespawnService

> 41 nodes

## Key Concepts

- **PlayerRespawnService** (37 connections) — `server/services/player_respawn_service.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (13 connections) — `server/services/player_respawn_service.py`
- **.respawn_player()** (9 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (8 connections) — `server/services/player_respawn_service.py`
- **Player** (8 connections)
- **._prepare_delirium_respawn()** (7 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **._clear_respawn_combat_state()** (6 connections) — `server/services/player_respawn_service.py`
- **._apply_standard_respawn_state()** (5 connections) — `server/services/player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_delirium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_sanitarium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_standard_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **.move_player_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **._publish_delirium_respawn_event()** (5 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_player_state()** (4 connections) — `server/services/player_respawn_service.py`
- **.clear_player_combat_state()** (3 connections) — `server/services/player_respawn_service.py`
- **._normalize_current_dp()** (3 connections) — `server/services/player_respawn_service.py`
- **Return current_dp as an int, defaulting to 0 for non-numeric values.** (1 connections) — `server/services/player_respawn_service.py`
- **Return (allowed, current_dp_int) for limbo movement gate checks.** (1 connections) — `server/services/player_respawn_service.py`
- **Publish delirium respawn event when event bus is available.** (1 connections) — `server/services/player_respawn_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [Player](Player.md) (19 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [Stats](Stats.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`

## Audit Trail

- EXTRACTED: 107 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*