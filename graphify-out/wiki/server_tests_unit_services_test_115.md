# server tests unit services test

> 14 nodes

## Key Concepts

- **asyncio** (35 connections)
- **test_get_npc_definitions_by_type()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_npc_definition_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_database_error()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_empty()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_invalid_max_population()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_invalid_type()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_error()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_npc_definition() raises ValueError for invalid type.** (2 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions() returns empty list when no definitions.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions() handles database errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition() handles errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test delete_npc_definition() returns False when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions_by_type() filters by type.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (38 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (1 shared connections)
- [server services npc service init](server_services_npc_service_init.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 53 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*