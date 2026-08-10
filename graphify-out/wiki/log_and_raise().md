# log_and_raise()

> God node · 174 connections · `server/utils/error_logging.py`

**Community:** [Optimization Archive Modernization](Optimization_Archive_Modernization.md)

## Connections by Relation

### calls
- log_and_raise_enhanced() `EXTRACTED`
- create_access_token() `EXTRACTED`
- hash_password() `EXTRACTED`
- update_container() `EXTRACTED`
- create_container() `EXTRACTED`
- ._initialize_database() `EXTRACTED`
- create_container() `EXTRACTED`
- get_container() `EXTRACTED`
- hash_password() `EXTRACTED`
- .transfer_from_container() `EXTRACTED`
- update_container() `EXTRACTED`
- get_container() `EXTRACTED`
- .open_container() `EXTRACTED`
- get_containers_by_entity_id() `EXTRACTED`
- delete_container() `EXTRACTED`
- get_containers_by_room_id() `EXTRACTED`
- create_container_async() `EXTRACTED`
- get_decayed_containers() `EXTRACTED`
- .transfer_to_container() `EXTRACTED`
- get_container_async() `EXTRACTED`

### contains
- error_logging.py `EXTRACTED`

### imports
- database.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- container_service.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- container_persistence_async.py `EXTRACTED`
- player_repository.py `EXTRACTED`
- npc_database.py `EXTRACTED`
- container_helpers.py `EXTRACTED`
- database_config_helpers.py `EXTRACTED`
- container_query_helpers_async.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- container_query_helpers.py `EXTRACTED`
- player_effect_repository.py `EXTRACTED`
- item_instance_persistence.py `EXTRACTED`
- player_spell_repository.py `EXTRACTED`
- wearable_container_service.py `EXTRACTED`
- argon2_utils.py `EXTRACTED`
- emote_service.py `EXTRACTED`
- quest_instance_repository.py `EXTRACTED`
- corpse_lifecycle_service.py `EXTRACTED`

### rationale_for
- Log and raise; uses legacy behavior (no skip_log for ValidationError). Delegates `EXTRACTED`

### references
- MythosMUDError `EXTRACTED`
- Any `EXTRACTED`
- NoReturn `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*