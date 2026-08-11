# NATS Docs Review

> 18 nodes

## Key Concepts

- **test_npc_combat_integration_service_npc_aggro.py** (19 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **mock_async_persistence()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_grace_period_blocked()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_npc_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_npc_dead()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_existing_combat_with_same_npc()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_existing_combat_with_other_npc()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_skips_already_dead_target()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_setup_combat_uuids_npc_attacker_value_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Create mock async persistence layer.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **Unit tests for NPC combat integration service - NPC-initiated aggro combat paths** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player blocks attack when player is in login grace per** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when NPC instance cannot be found** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when NPC is dead.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns True when combat already exists with sa** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when player is in combat with dif** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **ValueError from combat path when player is dead must not log as error.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test _setup_combat_uuids_npc_attacker falls back to random UUIDs on ValueError.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (4 shared connections)
- [Combat Disconnect Bug](Combat_Disconnect_Bug.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [test_ensure_room_cache_loaded_concurrent_load](test_ensure_room_cache_loaded_concurrent_load.md) (1 shared connections)
- [test_ensure_room_cache_loaded_database_error](test_ensure_room_cache_loaded_database_error.md) (1 shared connections)
- [test_process_room_rows_zone_without_slash](test_process_room_rows_zone_without_slash.md) (1 shared connections)
- [test_ensure_room_cache_loaded_os_error](test_ensure_room_cache_loaded_os_error.md) (1 shared connections)
- [test_ensure_room_cache_loaded_runtime_error](test_ensure_room_cache_loaded_runtime_error.md) (1 shared connections)
- [test_process_room_rows_with_none_attributes](test_process_room_rows_with_none_attributes.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*