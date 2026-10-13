# Community 176

> 79 nodes

## Key Concepts

- **CorpseLifecycleService** (71 connections) — `server/services/corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service.py** (61 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **CorpseServiceError** (16 connections) — `server/services/corpse_lifecycle_service.py`
- **asyncio** (16 connections)
- **_corpse_component()** (9 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **_dying_player()** (9 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **_stack()** (8 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_logs_but_does_not_raise_when_clearing_the_player_fails()** (8 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_nests_worn_container_contents_and_deletes_its_row()** (8 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_spills_past_the_slot_limit_onto_extra_corpses()** (8 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **CorpseNotFoundError** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_RecordingRoom** (7 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_ignores_worn_rows_for_other_items_and_non_equipment()** (7 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_keeps_an_unreadable_worn_row_instead_of_deleting_it()** (7 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_leaves_player_untouched_when_corpse_persist_fails()** (7 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_moves_carried_and_equipped_items_off_the_player()** (7 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **_created_items()** (6 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **_worn_container_row()** (6 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_delete_error()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_decay.py`
- **test_create_corpse_on_death_emit_error_does_not_fail_creation()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_empty_handed_player_still_gets_one_corpse()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_no_connection_manager_skips_emit()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_success()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_register_corpse_on_room_adds_summary()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_register_corpse_on_room_skips_objects_that_are_not_rooms()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 54 more nodes in this community*

## Relationships

- [Community 419](Community_419.md) (25 shared connections)
- [Community 292](Community_292.md) (21 shared connections)
- [Community 80](Community_80.md) (19 shared connections)
- [Community 94](Community_94.md) (11 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (5 shared connections)
- [Community 412](Community_412.md) (3 shared connections)
- [Community 490](Community_490.md) (3 shared connections)
- [Community 118](Community_118.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (1 shared connections)
- [Community 380](Community_380.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_decay.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 201 (81%)
- INFERRED: 46 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*