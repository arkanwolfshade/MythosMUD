# Async Query Helpers

> 92 nodes

## Key Concepts

- **player_respawn_service.py** (44 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnService** (39 connections) — `server/services/player_respawn_service.py`
- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **int_coercion.py** (13 connections) — `server/utils/int_coercion.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **._apply_sanitarium_liability_update()** (12 connections) — `server/services/player_respawn_service.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
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
- **inventory_command_coercion.py** (6 connections) — `server/commands/inventory_command_coercion.py`
- **_RespawnEventPublisher** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (6 connections) — `server/services/player_respawn_service.py`
- *... and 67 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (34 shared connections)
- [combat models rationale](combat_models_rationale.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (6 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (5 shared connections)
- [nats services service](nats_services_service.md) (5 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/services/lucidity_helpers.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 419 (91%)
- INFERRED: 39 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*