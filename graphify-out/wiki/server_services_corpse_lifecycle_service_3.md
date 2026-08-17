# server services corpse lifecycle service

> 12 nodes

## Key Concepts

- **._require_corpse_container()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **Any** (5 connections)
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **test_get_enum_value_enum()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_string()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Safely get enum value, handling both enum instances and string values. When…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Filter out database-specific fields that are not part of the ContainerComponent…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Initialize the corpse lifecycle service. Args: persistence: Persistence layer…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Test _get_enum_value() with enum instance.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test _get_enum_value() with string.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Relationships

- [server services corpse lifecycle service](server_services_corpse_lifecycle_service.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (3 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*