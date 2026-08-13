# log_and_raise()

> God node · 174 connections · `server/utils/error_logging.py`

**Community:** [log_and_raise](log_and_raise.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- create_access_token() `EXTRACTED`
- hash_password() `EXTRACTED`
- update_container() `EXTRACTED`
- create_container() `EXTRACTED`
- create_container() `EXTRACTED`
- get_container() `EXTRACTED`
- hash_password() `EXTRACTED`
- .transfer_from_container() `EXTRACTED`
- get_container() `EXTRACTED`
- update_container() `EXTRACTED`
- ._initialize_database() `EXTRACTED`
- get_containers_by_entity_id() `EXTRACTED`
- delete_container() `EXTRACTED`
- get_containers_by_room_id() `EXTRACTED`
- create_container_async() `EXTRACTED`
- get_decayed_containers() `EXTRACTED`
- get_container_async() `EXTRACTED`
- get_containers_by_entity_id() `EXTRACTED`
- get_containers_by_room_id() `EXTRACTED`

### contains
- error_logging.py `EXTRACTED`

### imports
- database.py `EXTRACTED`
- [persistence/container_persistence.py](persistence-container_persistence.py.md) `EXTRACTED`
- container_service.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- [container_persistence_async.py](container_persistence_async.py.md) `EXTRACTED`
- player_repository.py `EXTRACTED`
- [npc_database.py](npc_database.py.md) `EXTRACTED`
- [persistence/container_helpers.py](persistence-container_helpers.py.md) `EXTRACTED`
- database_config_helpers.py `EXTRACTED`
- container_query_helpers_async.py `EXTRACTED`
- container_persistence/container_persistence.py `EXTRACTED`
- container_query_helpers.py `EXTRACTED`
- [player_effect_repository.py](player_effect_repository.py.md) `EXTRACTED`
- item_instance_persistence.py `EXTRACTED`
- player_spell_repository.py `EXTRACTED`
- wearable_container_service.py `EXTRACTED`
- argon2_utils.py `EXTRACTED`
- emote_service.py `EXTRACTED`
- quest_instance_repository.py `EXTRACTED`
- corpse_lifecycle_service.py `EXTRACTED`

### rationale_for
- Log and raise; uses legacy behavior (no skip_log for ValidationError).… `EXTRACTED`

### references
- [MythosMUDError](MythosMUDError.md) `EXTRACTED`
- [Any](Any.md) `EXTRACTED`
- NoReturn `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*