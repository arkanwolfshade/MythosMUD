# persistence container rationale

> 74 nodes

## Key Concepts

- **log_and_raise()** (170 connections) — `server/utils/error_logging.py`
- **container_persistence_async.py** (33 connections) — `server/persistence/container_persistence_async.py`
- **skill_repository.py** (17 connections) — `server/persistence/repositories/skill_repository.py`
- **get_container_async()** (16 connections) — `server/persistence/container_persistence_async.py`
- **create_container_async()** (13 connections) — `server/persistence/container_persistence_async.py`
- **Any** (11 connections)
- **_finalize_container_creation()** (11 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (11 connections) — `server/persistence/container_persistence_async.py`
- **fetch_container_items_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **_populate_container_items_async()** (9 connections) — `server/persistence/container_persistence_async.py`
- **_row_to_player_spell()** (9 connections) — `server/persistence/repositories/player_spell_repository.py`
- **validate_lock_state()** (8 connections) — `server/persistence/container_helpers.py`
- **AsyncSession** (8 connections)
- **delete_container_async()** (8 connections) — `server/persistence/container_persistence_async.py`
- **.get_player_spells()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.get_player_spell()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.learn_spell()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.update_mastery()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.record_spell_cast()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **_call_create_container_procedure()** (7 connections) — `server/persistence/container_persistence_async.py`
- **UUID** (7 connections)
- **_row_to_skill()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_all_skills()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_id()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_key()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- *... and 49 more nodes in this community*

## Relationships

- [npc populate databases](npc_populate_databases.md) (36 shared connections)
- [persistence container extended](persistence_container_extended.md) (26 shared connections)
- [persistence container item](persistence_container_item.md) (20 shared connections)
- [Database Config](Database_Config.md) (19 shared connections)
- [command inventory factories](command_inventory_factories.md) (17 shared connections)
- [Exception Containers](Exception_Containers.md) (14 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (13 shared connections)
- [player room persistence](player_room_persistence.md) (13 shared connections)
- [world models rationale](world_models_rationale.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (8 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (8 shared connections)
- [movement service game](movement_service_game.md) (8 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence_async.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 486 (95%)
- INFERRED: 24 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*