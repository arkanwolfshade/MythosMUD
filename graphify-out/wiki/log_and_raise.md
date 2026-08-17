# log_and_raise()

> God node · 196 connections · `server/utils/error_logging.py`

**Community:** [claude rules asyncio](claude_rules_asyncio.md)

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
- update_container() `EXTRACTED`
- get_container() `EXTRACTED`
- ._initialize_database() `EXTRACTED`
- create_container_async() `EXTRACTED`
- get_container_async() `EXTRACTED`
- get_decayed_containers_async() `EXTRACTED`
- get_containers_by_entity_id() `EXTRACTED`
- delete_container() `EXTRACTED`
- get_containers_by_entity_id_async() `EXTRACTED`
- get_decayed_containers() `EXTRACTED`
- create_item_instance_async() `EXTRACTED`
- get_containers_by_room_id() `EXTRACTED`

### contains
- error_logging.py `EXTRACTED`

### imports
- database.py `EXTRACTED`
- persistence/container_persistence.py `EXTRACTED`
- container_persistence/container_persistence.py `EXTRACTED`
- container_persistence_async.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- container_service_transfer_to.py `EXTRACTED`
- npc_database.py `EXTRACTED`
- player_repository.py `EXTRACTED`
- container_service_session.py `EXTRACTED`
- persistence/container_helpers.py `EXTRACTED`
- container_service_lock.py `EXTRACTED`
- container_service_transfer_from.py `EXTRACTED`
- container_persistence/container_helpers.py `EXTRACTED`
- database_config_helpers.py `EXTRACTED`
- container_query_helpers_async.py `EXTRACTED`
- test_error_logging.py `EXTRACTED`
- player_effect_repository.py `EXTRACTED`
- player_spell_repository.py `EXTRACTED`
- emote_service.py `EXTRACTED`
- container_query_helpers.py `EXTRACTED`

### rationale_for
- Log and raise; uses legacy behavior (no skip_log for ValidationError).… `EXTRACTED`

### references
- MythosMUDError `EXTRACTED`
- Any `EXTRACTED`
- NoReturn `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*