# Skill Service Tests

> 46 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_enum()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_expired()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_invalid_grace_period()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_not_decayed()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_no_name()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_custom_grace_period()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_timezone_aware()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_timezone_naive_vs_aware()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_success()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpses_in_room()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_all_decayed_corpses()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_all_decayed_corpses()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_decayed_corpses_in_room_validation_error()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_decayed_corpses_in_room_non_corpse()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpses_in_room_handles_errors()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_all_decayed_corpses_empty()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_all_decayed_corpses_uses_real_time_not_mythos_time()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_all_decayed_corpses_validation_error()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_all_decayed_corpses_non_corpse()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_all_decayed_corpses_handles_errors()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_all_decayed_corpses_timezone_aware_utc()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Unit tests for corpse lifecycle service.  Tests the CorpseLifecycleService class** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test _get_enum_value() with enum instance.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 21 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (11 shared connections)
- [Archive Npc Population](Archive_Npc_Population.md) (9 shared connections)
- [Player State Factories](Player_State_Factories.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [corpse_service](corpse_service.md) (1 shared connections)
- [mock_persistence](mock_persistence.md) (1 shared connections)
- [test_can_access_corpse_admin](test_can_access_corpse_admin.md) (1 shared connections)
- [test_can_access_corpse_grace_period_active](test_can_access_corpse_grace_period_active.md) (1 shared connections)
- [test_can_access_corpse_grace_period_type_error](test_can_access_corpse_grace_period_type_error.md) (1 shared connections)
- [test_can_access_corpse_no_grace_period_start](test_can_access_corpse_no_grace_period_start.md) (1 shared connections)
- [test_can_access_corpse_no_owner](test_can_access_corpse_no_owner.md) (1 shared connections)
- [test_can_access_corpse_owner](test_can_access_corpse_owner.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 128 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*