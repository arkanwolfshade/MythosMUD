# User Manager Mute Tests

> 105 nodes

## Key Concepts

- **ApplicationContainer** (151 connections) — `server/container/main.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **reset_container()** (8 connections) — `server/container/main.py`
- **__init__.py** (7 connections) — `server/container/__init__.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **.reset_instance()** (6 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **._connect_nats()** (5 connections) — `server/container/bundles/realtime.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
- **.initialize()** (5 connections) — `server/container/main.py`
- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._require_core_services()** (4 connections) — `server/container/bundles/realtime.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **._get_project_root()** (4 connections) — `server/container/main.py`
- **._decode_json_column()** (4 connections) — `server/container/main.py`
- **._normalize_path_from_url_or_path()** (4 connections) — `server/container/main.py`
- **test_reset_container()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container_creates_new_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- *... and 80 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (43 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (14 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (11 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (10 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (6 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (6 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (5 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (5 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (5 shared connections)
- [Message Broker Errors](Message_Broker_Errors.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 426 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*