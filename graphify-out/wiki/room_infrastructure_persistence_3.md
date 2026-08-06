# room infrastructure persistence

> 2 nodes

## Key Concepts

- **.test_should_trigger_sanitarium_failover_within_debounce_window()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **should_trigger_sanitarium_failover returns False within debounce window.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`

## Relationships

- [catatonia registry services](catatonia_registry_services.md) (1 shared connections)
- [commands time handle](commands_time_handle.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*