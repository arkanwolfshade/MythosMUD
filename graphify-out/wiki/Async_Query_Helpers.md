# Async Query Helpers

> 75 nodes

## Key Concepts

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
- **._log_standard_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- *... and 50 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (16 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (15 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [combat models rationale](combat_models_rationale.md) (5 shared connections)
- [command base models](command_base_models.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [item models rationale](item_models_rationale.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [models player rationale](models_player_rationale.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)
- [alias command models](alias_command_models.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 288 (90%)
- INFERRED: 31 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*