# Test Container Bundles

> 136 nodes

## Key Concepts

- **test_container_bundles.py** (72 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (52 connections) — `server/container/bundles/game.py`
- **CombatBundle** (33 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (33 connections) — `server/container/bundles/realtime.py`
- **asyncio** (25 connections)
- **NPCBundle** (20 connections) — `server/container/bundles/npc.py`
- **MagicBundle** (13 connections) — `server/container/bundles/magic.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
- **test_realtime_bundle_nats.py** (11 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **._connect_nats()** (7 connections) — `server/container/bundles/realtime.py`
- **._setup_nats_dependent_services()** (7 connections) — `server/container/bundles/realtime.py`
- **test_time_bundle_attrs_flatten_onto_container()** (7 connections) — `server/tests/unit/container/test_container_bundles.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **.initialize()** (6 connections) — `server/container/bundles/magic.py`
- **_validate_magic_prerequisites()** (6 connections) — `server/container/bundles/magic.py`
- **.initialize()** (6 connections) — `server/container/bundles/npc.py`
- **test_time_bundle_initialize_missing_deps()** (6 connections) — `server/tests/unit/container/test_container_bundles.py`
- **._init_emote_service()** (5 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **._handle_nats_connect_error()** (5 connections) — `server/container/bundles/realtime.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/realtime.py`
- **_patch_temporal_construction()** (5 connections) — `server/tests/unit/container/test_container_bundles.py`
- **test_time_bundle_initialize_with_deps()** (5 connections) — `server/tests/unit/container/test_container_bundles.py`
- *... and 111 more nodes in this community*

## Relationships

- [Application Container Bundles](Application_Container_Bundles.md) (73 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (10 shared connections)
- [Player Skill Repository](Player_Skill_Repository.md) (5 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (5 shared connections)
- [Cache Service](Cache_Service.md) (4 shared connections)
- [Emote Service](Emote_Service.md) (4 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (3 shared connections)
- [Lucidity Helpers & Catatonia](Lucidity_Helpers_&_Catatonia.md) (3 shared connections)
- [Test Catatonia Registry](Test_Catatonia_Registry.md) (2 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (2 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (2 shared connections)
- [NATS Service Client](NATS_Service_Client.md) (2 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/container/bundles/game.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 303 (80%)
- INFERRED: 77 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*