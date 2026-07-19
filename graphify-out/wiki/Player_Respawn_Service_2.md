# Player Respawn Service

> 52 nodes · cohesion 0.07

## Key Concepts

- **PlayerRespawnService** (51 connections) — `server/services/player_respawn_service.py`
- **UUID** (17 connections) — `server/services/player_respawn_service.py`
- **._prepare_sanitarium_respawn()** (11 connections) — `server/services/player_respawn_service.py`
- **Player** (9 connections) — `server/services/player_respawn_service.py`
- **.respawn_player()** (9 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (8 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (8 connections) — `server/services/player_respawn_service.py`
- **._clear_respawn_combat_state()** (7 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (7 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (6 connections) — `server/services/player_respawn_service.py`
- **._publish_delirium_respawn_event()** (6 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (6 connections) — `server/services/player_respawn_service.py`
- **._apply_standard_respawn_state()** (5 connections) — `server/services/player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_delirium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_sanitarium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_standard_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **.move_player_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **.publish()** (5 connections) — `server/services/player_respawn_service.py`
- **.clear_player_combat_state()** (4 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_player_state()** (4 connections) — `server/services/player_respawn_service.py`
- **.__init__()** (4 connections) — `server/services/player_respawn_service.py`
- *... and 27 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (20 shared connections)
- [[NPC Admin API]] (8 shared connections)
- [[Lucidity State Models]] (7 shared connections)
- [[Player Respawn Service]] (5 shared connections)
- [[Services Player Respawn]] (4 shared connections)
- [[Player Combat XP]] (2 shared connections)
- [[Lifespan Startup Hooks]] (2 shared connections)
- [[Integer Coercion Utils]] (2 shared connections)
- [[Player Respawn Events]] (2 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[Player Service Tests]] (1 shared connections)
- [[Services Hallucination Frequency]] (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 224 (90%)
- INFERRED: 24 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
