# Community 347

> 49 nodes

## Key Concepts

- **PlayerRespawnService** (33 connections) — `server/services/player_respawn_service.py`
- **UUID** (14 connections)
- **.respawn_player()** (9 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (8 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (7 connections) — `server/services/player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **._clear_respawn_combat_state()** (6 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (6 connections) — `server/services/player_respawn_service.py`
- **.move_player_to_limbo()** (6 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (6 connections) — `server/services/player_respawn_service.py`
- **._redirect_template_respawn()** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (5 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (5 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (5 connections) — `server/services/player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **.__init__()** (5 connections) — `server/services/player_respawn_service.py`
- **._publish_delirium_respawn_event()** (5 connections) — `server/services/player_respawn_service.py`
- **.clear_player_combat_state()** (3 connections) — `server/services/player_respawn_service.py`
- **.publish()** (3 connections) — `server/services/player_respawn_service.py`
- **test_utc_now()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **Player** (3 connections)
- **Protocol** (3 connections)
- **.choice()** (2 connections) — `server/services/player_respawn_service.py`
- *... and 24 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (26 shared connections)
- [Community 138](Community_138.md) (10 shared connections)
- [Community 130](Community_130.md) (2 shared connections)
- [Community 88](Community_88.md) (2 shared connections)
- [Community 424](Community_424.md) (1 shared connections)
- [API Response Models](API_Response_Models.md) (1 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (1 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (1 shared connections)
- [Community 441](Community_441.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 113 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*