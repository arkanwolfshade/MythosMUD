# test_logging_file_categories.py

> 22 nodes

## Key Concepts

- **test_logging_file_categories.py** (14 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **_reset_logger()** (5 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_combat_loggers_still_get_debug_level_in_e2e_test()** (4 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_npc_loggers_keep_debug_level_in_local_environment()** (4 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_npc_loggers_suppressed_to_info_in_e2e_test_regardless_of_debug_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_inventory_category_also_catches_equip_unequip_command_logs()** (3 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_inventory_category_covers_every_container_and_inventory_service_module()** (3 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_realtime_module_loggers_match_communications_category()** (3 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_infrastructure_category_removed()** (2 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_no_category_still_references_infrastructure_module()** (2 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_persistence_category_does_not_reference_deleted_persistence_layer_class()** (2 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **Unit tests for DEFAULT_LOG_CATEGORIES. Regression coverage for #687: the…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **Undo add_handler_to_loggers' effects on both loggers it touches for a given…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **#297/#610: NPC behavior-engine/threading debug lines fire continuously enough…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **The e2e-only suppression must not leak into local development, where full NPC…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **Regression guard: the new npc-specific e2e branch must not shadow the existing…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **No "infrastructure" category: server/infrastructure/ (its only logger source)…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **No surviving category's logger-name list should point at the deleted…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **#60 audit: the sync `PersistenceLayer` class was deleted 2025-12-08…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **#297: get_logger(__name__) in server/realtime/*.py produces…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **#688: DEFAULT_LOG_CATEGORIES["inventory"] must list every server/services/…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **#688: server/commands/inventory_equip_command.py and…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`

## Relationships

- [logging_file_setup.py](logging_file_setup.py.md) (9 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_logging_file_categories.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*