# Database Config

> 797 nodes

## Key Concepts

- **DatabaseError** (440 connections) — `server/exceptions.py`
- **exceptions.py** (199 connections) — `server/exceptions.py`
- **log_and_raise()** (170 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (97 connections) — `server/database.py`
- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **test_container_persistence.py** (61 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **error_logging.py** (56 connections) — `server/utils/error_logging.py`
- **MovementService** (43 connections) — `server/game/movement_service.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_player_repository.py** (40 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **container_persistence_async.py** (33 connections) — `server/persistence/container_persistence_async.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **__init__.py** (30 connections) — `server/persistence/repositories/__init__.py`
- **_parse_jsonb_column()** (28 connections) — `server/container_persistence/container_persistence.py`
- **movement_service.py** (28 connections) — `server/game/movement_service.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **container_helpers.py** (26 connections) — `server/persistence/container_helpers.py`
- **_fetch_container_items()** (25 connections) — `server/container_persistence/container_persistence.py`
- **ContainerData** (23 connections) — `server/container_persistence/container_persistence.py`
- **create_container()** (23 connections) — `server/container_persistence/container_persistence.py`
- **container_query_helpers_async.py** (23 connections) — `server/persistence/container_query_helpers_async.py`
- **container_repository.py** (23 connections) — `server/persistence/repositories/container_repository.py`
- **DialogueDefinitionRepository** (22 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- *... and 772 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (143 shared connections)
- [command inventory models](command_inventory_models.md) (67 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (66 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (60 shared connections)
- [world models rationale](world_models_rationale.md) (60 shared connections)
- [commands admin mute](commands_admin_mute.md) (34 shared connections)
- [persistence container item](persistence_container_item.md) (33 shared connections)
- [Room Broadcast](Room_Broadcast.md) (33 shared connections)
- [follow service game](follow_service_game.md) (32 shared connections)
- [NPC Combat](NPC_Combat.md) (24 shared connections)
- [game models player](game_models_player.md) (23 shared connections)
- [combat models rationale](combat_models_rationale.md) (21 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/container_persistence/__init__.py`
- `server/container_persistence/container_persistence.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/character_creation_service.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/models/dialogue.py`
- `server/models/profession.py`
- `server/models/quest.py`
- `server/models/skill.py`
- `server/npc/combat_integration_base.py`
- `server/persistence/container_create_params.py`

## Audit Trail

- EXTRACTED: 3985 (88%)
- INFERRED: 557 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*