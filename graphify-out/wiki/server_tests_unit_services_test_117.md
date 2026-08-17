# server tests unit services test

> 12 nodes

## Key Concepts

- **test_npc_service.py** (50 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_with_base_stats()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_spawn_rules_database_error()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_system_statistics_database_error()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_system_statistics_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_invalid_probability()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **Unit tests for NPC service. Tests the NPCService class.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_npc_definition() raises ValueError for invalid probability.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_npc_definition() handles base_stats.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_spawn_rules() handles database errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_system_statistics() successfully generates stats.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_system_statistics() handles database errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (40 shared connections)
- [server services npc service init](server_services_npc_service_init.md) (6 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (3 shared connections)
- [draft7validator](draft7validator.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 63 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*