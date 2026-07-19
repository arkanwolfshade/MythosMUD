# NPC Definition Admin API

> 93 nodes · cohesion 0.05

## Key Concepts

- **get_admin_auth_service()** (38 connections) — `server/services/admin_auth_service.py`
- **validate_admin_permission()** (31 connections) — `server/api/admin/npc_router_core.py`
- **npc_definitions_api.py** (29 connections) — `server/api/admin/npc_definitions_api.py`
- **_update_npc_definition_internal()** (12 connections) — `server/api/admin/npc_definitions_api.py`
- **NPCMoveRequest** (12 connections) — `server/api/admin/npc_schemas.py`
- **NPCSpawnRequest** (12 connections) — `server/api/admin/npc_schemas.py`
- **NPCDefinitionResponse** (11 connections) — `server/api/admin/npc_schemas.py`
- **NPCDefinitionUpdate** (11 connections) — `server/api/admin/npc_schemas.py`
- **create_npc_definition()** (10 connections) — `server/api/admin/npc_definitions_api.py`
- **move_npc_instance()** (10 connections) — `server/api/admin/npc_instances_api.py`
- **spawn_npc_instance()** (10 connections) — `server/api/admin/npc_instances_api.py`
- **NPCDefinitionCreate** (10 connections) — `server/api/admin/npc_schemas.py`
- **NPCSpawnRuleResponse** (10 connections) — `server/api/admin/npc_schemas.py`
- **create_npc_spawn_rule()** (10 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_definition()** (9 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definitions()** (9 connections) — `server/api/admin/npc_definitions_api.py`
- **despawn_npc_instance()** (9 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_stats()** (9 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_population_stats()** (9 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_system_status()** (9 connections) — `server/api/admin/npc_population_api.py`
- **get_npc_zone_stats()** (9 connections) — `server/api/admin/npc_population_api.py`
- **NPCSpawnRuleCreate** (9 connections) — `server/api/admin/npc_schemas.py`
- **get_npc_spawn_rules()** (9 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Request** (9 connections) — `server/api/admin/npc_definitions_api.py`
- **User** (9 connections) — `server/api/admin/npc_definitions_api.py`
- *... and 68 more nodes in this community*

## Relationships

- [[NPC Admin API]] (42 shared connections)
- [[Container Exception Handlers]] (20 shared connections)
- [[NPC Definition Schemas]] (9 shared connections)
- [[NPC Occupant Verification]] (8 shared connections)
- [[Admin NPC Schemas]] (7 shared connections)
- [[NPC Database Sessions]] (3 shared connections)
- [[ASCII Map API]] (3 shared connections)
- [[Api Admin Npc]] (2 shared connections)
- [[Room Exploration API]] (2 shared connections)
- [[Admin Auth Service Tests]] (2 shared connections)
- [[API Test Fixtures]] (1 shared connections)
- [[Inventory Service Helpers]] (1 shared connections)

## Source Files

- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/services/admin_auth_service.py`

## Audit Trail

- EXTRACTED: 417 (82%)
- INFERRED: 90 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
