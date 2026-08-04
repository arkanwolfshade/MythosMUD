# Async Query Helpers

> 72 nodes

## Key Concepts

- **player_respawn_service.py** (44 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnService** (39 connections) — `server/services/player_respawn_service.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_liability_update()** (12 connections) — `server/services/player_respawn_service.py`
- **.respawn_player()** (11 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (10 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (10 connections) — `server/services/player_respawn_service.py`
- **Player** (8 connections)
- **._clear_respawn_combat_state()** (8 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (8 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (8 connections) — `server/services/player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **.move_player_to_limbo()** (7 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (7 connections) — `server/services/player_respawn_service.py`
- **DecodeLiabilitiesFn** (7 connections) — `server/utils/liability_types.py`
- **EncodeLiabilitiesFn** (7 connections) — `server/utils/liability_types.py`
- **_RespawnEventPublisher** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (6 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (6 connections) — `server/services/player_respawn_service.py`
- **._publish_delirium_respawn_event()** (6 connections) — `server/services/player_respawn_service.py`
- **.publish()** (5 connections) — `server/services/player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **._apply_standard_respawn_state()** (5 connections) — `server/services/player_respawn_service.py`
- *... and 47 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (16 shared connections)
- [Loot Generation](Loot_Generation.md) (10 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [combat models rationale](combat_models_rationale.md) (7 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (6 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (4 shared connections)
- [models player rationale](models_player_rationale.md) (4 shared connections)
- [aggro threat services](aggro_threat_services.md) (4 shared connections)
- [player death service](player_death_service.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 322 (91%)
- INFERRED: 31 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*