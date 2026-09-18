# Community 80

> 104 nodes

## Key Concepts

- **test_container_bundles.py** (62 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (34 connections) — `server/container/bundles/game.py`
- **CombatBundle** (29 connections) — `server/container/bundles/combat.py`
- **asyncio** (25 connections)
- **NPCBundle** (16 connections) — `server/container/bundles/npc.py`
- **.initialize()** (10 connections) — `server/container/bundles/game.py`
- **._init_movement_layer()** (9 connections) — `server/container/bundles/game.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **._initialize_item_services()** (7 connections) — `server/container/bundles/game.py`
- **test_time_bundle_attrs_flatten_onto_container()** (7 connections) — `server/tests/unit/container/test_container_bundles.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._create_npc_services()** (6 connections) — `server/container/bundles/npc.py`
- **.initialize()** (6 connections) — `server/container/bundles/npc.py`
- **_patch_temporal_construction()** (6 connections) — `server/tests/unit/container/test_container_bundles.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **test_game_bundle_init_emote_service_loads_once()** (5 connections) — `server/tests/unit/container/test_container_bundles.py`
- **test_time_bundle_initialize_missing_deps()** (5 connections) — `server/tests/unit/container/test_container_bundles.py`
- **test_time_bundle_initialize_with_deps()** (5 connections) — `server/tests/unit/container/test_container_bundles.py`
- **_time_bundle_container()** (5 connections) — `server/tests/unit/container/test_container_bundles.py`
- **._create_combat_service_with_nats()** (4 connections) — `server/container/bundles/combat.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **._build_prototype_payload()** (4 connections) — `server/container/bundles/game.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- *... and 79 more nodes in this community*

## Relationships

- [Community 38](Community_38.md) (22 shared connections)
- [Community 93](Community_93.md) (21 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (14 shared connections)
- [Community 87](Community_87.md) (4 shared connections)
- [Community 1287](Community_1287.md) (3 shared connections)
- [NPC Follow System](NPC_Follow_System.md) (3 shared connections)
- [NPC Population Control](NPC_Population_Control.md) (3 shared connections)
- [Community 504](Community_504.md) (2 shared connections)
- [Community 752](Community_752.md) (2 shared connections)
- [Community 750](Community_750.md) (2 shared connections)
- [Community 260](Community_260.md) (2 shared connections)
- [Community 283](Community_283.md) (2 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/container/bundles/game.py`
- `server/container/bundles/npc.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`

## Audit Trail

- EXTRACTED: 210 (79%)
- INFERRED: 55 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*