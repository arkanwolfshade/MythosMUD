# MP Regeneration Service

> 64 nodes

## Key Concepts

- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (5 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (4 connections) — `server/app/lifespan_startup.py`
- **Any** (4 connections)
- **_validate_npc_services_prerequisites()** (4 connections) — `server/app/lifespan_startup.py`
- **_start_npc_thread_manager_and_pending()** (4 connections) — `server/app/lifespan_startup.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (4 connections) — `server/app/lifespan_startup.py`
- **test_initialize_container_and_legacy_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_no_item_factory()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_async_registry()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_npc_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 39 more nodes in this community*

## Relationships

- [Test Optimization Insights](Test_Optimization_Insights.md) (12 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (11 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (9 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (6 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (5 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (3 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (3 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (3 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (3 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 283 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*