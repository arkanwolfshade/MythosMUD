# log_and_raise()

> God node · 189 connections · `server/utils/error_logging.py`

**Community:** [DatabaseError](DatabaseError.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- create_access_token() `EXTRACTED`
- hash_password() `EXTRACTED`
- update_container() `EXTRACTED`
- create_container() `EXTRACTED`
- get_container() `EXTRACTED`
- hash_password() `EXTRACTED`
- ._initialize_database() `EXTRACTED`
- create_container_async() `EXTRACTED`
- get_container_async() `EXTRACTED`
- get_decayed_containers_async() `EXTRACTED`
- delete_container() `EXTRACTED`
- get_containers_by_entity_id_async() `EXTRACTED`
- get_decayed_containers() `EXTRACTED`
- create_item_instance_async() `EXTRACTED`
- get_containers_by_room_id_async() `EXTRACTED`
- get_containers_by_entity_id() `EXTRACTED`
- get_containers_by_room_id() `EXTRACTED`
- create_item_instance() `EXTRACTED`
- init_npc_db() `EXTRACTED`

### contains
- error_logging.py `EXTRACTED`

### imports
- database.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- container_persistence_async.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- container_service_transfer_to.py `EXTRACTED`
- [npc_database.py](npc_database.py.md) `EXTRACTED`
- player_repository.py `EXTRACTED`
- container_service_session.py `EXTRACTED`
- container_service_lock.py `EXTRACTED`
- container_service_transfer_from.py `EXTRACTED`
- [container_query_helpers_async.py](container_query_helpers_async.py.md) `EXTRACTED`
- test_error_logging.py `EXTRACTED`
- database_config_helpers.py `EXTRACTED`
- [persistence/container_helpers.py](persistence-container_helpers.py.md) `EXTRACTED`
- [player_effect_repository.py](player_effect_repository.py.md) `EXTRACTED`
- player_spell_repository.py `EXTRACTED`
- container_query_helpers.py `EXTRACTED`
- [item_instance_persistence.py](item_instance_persistence.py.md) `EXTRACTED`
- dialogue_definition_repository.py `EXTRACTED`
- [item_instance_persistence_async.py](item_instance_persistence_async.py.md) `EXTRACTED`

### rationale_for
- Log and raise; uses legacy behavior (no skip_log for ValidationError).… `EXTRACTED`

### references
- [MythosMUDError](MythosMUDError.md) `EXTRACTED`
- [Any](Any.md) `EXTRACTED`
- NoReturn `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*