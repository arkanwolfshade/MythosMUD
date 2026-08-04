# map layout useMapLayout

> 18 nodes

## Key Concepts

- **NPCStartupService** (44 connections) — `server/services/npc_startup_service.py`
- **test_npc_startup_service_init()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_spawn_failure()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_case_insensitive()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_optional_npcs()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_no_prior_spawns_returns_empty()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_skips_unknown_definition_id()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.__init__()** (2 connections) — `server/services/npc_startup_service.py`
- **Service for automatic NPC spawning during server startup.      This service coor** (1 connections) — `server/services/npc_startup_service.py`
- **Initialize the NPC startup service.** (1 connections) — `server/services/npc_startup_service.py`
- **Test NPCStartupService initialization.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_required_npcs() handles spawn failures.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns correct room for known sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() is case insensitive.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() spawns optional NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Arena pass is skipped when required/optional passes spawned nothing.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Stale definition_id in spawned_npcs that is not in definitions list is ignored.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [realtime player connection](realtime_player_connection.md) (16 shared connections)
- [services npc startup](services_npc_startup.md) (9 shared connections)
- [panels monitoringPanelTestFixtures Monit](panels_monitoringPanelTestFixtures_Monit.md) (6 shared connections)
- [quests players rationale](quests_players_rationale.md) (5 shared connections)
- [player death service](player_death_service.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [test_spawn_arena_npcs_spawns_each_spawned_definition](test_spawn_arena_npcs_spawns_each_spawned_definition.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 74 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*