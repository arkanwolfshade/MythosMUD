# Test Timing Analysis

> 20 nodes · cohesion 0.10

## Key Concepts

- **test_npc_startup_service.py** (39 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_npc_startup_service_init()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_no_prior_spawns_returns_empty()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_optional_npcs()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_probability_attribute()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_spawn_room()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_with_probability()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_success()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_arena_room_ids()** (2 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Unit tests for NPC startup service.  Tests the NPCStartupService class.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_required_npcs() successfully spawns required NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() spawns based on probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test get_npc_startup_service() returns service instance.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles missing spawn room.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test ARENA_ROOM_IDS defines 121 arena rooms (11x11) and includes center.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() spawns optional NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test NPCStartupService initialization.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Arena pass is skipped when required/optional passes spawned nothing.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [E2E Playwright Conversion Plan](E2E_Playwright_Conversion_Plan.md) (16 shared connections)
- [Multiplayer Browser Helpers](Multiplayer_Browser_Helpers.md) (10 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Community 1599](Community_1599.md) (1 shared connections)
- [Community 1598](Community_1598.md) (1 shared connections)
- [Community 1597](Community_1597.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 75 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*