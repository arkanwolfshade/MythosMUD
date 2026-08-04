# countdown rest task

> 15 nodes

## Key Concepts

- **get_npc_population_stats()** (13 connections) — `server/api/admin/npc_population_api.py`
- **test_npc_population_api.py** (13 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **get_npc_zone_stats()** (11 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_system_status()** (11 connections) — `server/api/admin/npc_population_api.py`
- **Request** (3 connections)
- **test_get_npc_population_stats_generic_error()** (3 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **test_get_npc_population_stats_success()** (2 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **test_get_npc_population_stats_http_exception_reraises()** (2 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **test_get_npc_zone_stats_success()** (2 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **test_get_npc_system_status_success()** (2 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **Get NPC population statistics.** (1 connections) — `server/api/admin/npc_population_api.py`
- **Get NPC zone statistics.** (1 connections) — `server/api/admin/npc_population_api.py`
- **Get NPC system status.** (1 connections) — `server/api/admin/npc_population_api.py`
- **admin_user()** (1 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`
- **Unit tests for admin NPC population API endpoints.** (1 connections) — `server/tests/unit/api/admin/test_npc_population_api.py`

## Relationships

- [player preferences services](player_preferences_services.md) (10 shared connections)
- [logging setup structured](logging_setup_structured.md) (6 shared connections)
- [Exception Containers](Exception_Containers.md) (5 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_population_api.py`
- `server/tests/unit/api/admin/test_npc_population_api.py`

## Audit Trail

- EXTRACTED: 66 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*