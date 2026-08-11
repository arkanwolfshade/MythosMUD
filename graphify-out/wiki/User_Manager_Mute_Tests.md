# User Manager Mute Tests

> 560 nodes

## Key Concepts

- **ApplicationContainer** (151 connections) — `server/container/main.py`
- **GameBundle** (45 connections) — `server/container/bundles/game.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **game.py** (42 connections) — `server/container/bundles/game.py`
- **PrototypeRegistry** (37 connections) — `server/game/items/prototype_registry.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **TaskRegistry** (33 connections) — `server/app/task_registry.py`
- **main.py** (33 connections) — `server/container/main.py`
- **ItemPrototypeModel** (28 connections) — `server/game/items/models.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **time_service.py** (25 connections) — `server/time/time_service.py`
- **resolve_weapon_attack_from_equipped()** (24 connections) — `server/game/weapons.py`
- **time_event_consumer.py** (24 connections) — `server/time/time_event_consumer.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **MythosTimeEventConsumer** (23 connections) — `server/time/time_event_consumer.py`
- **CombatBundle** (21 connections) — `server/container/bundles/combat.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **EventPublisher** (20 connections) — `server/realtime/event_publisher.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **MagicBundle** (19 connections) — `server/container/bundles/magic.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **prototype_registry.py** (19 connections) — `server/game/items/prototype_registry.py`
- *... and 535 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (110 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (68 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (35 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (25 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (23 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (21 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (18 shared connections)
- [Exploration Command Factory](Exploration_Command_Factory.md) (17 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (14 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (12 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (11 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (10 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_types.py`
- `server/game/instance_manager.py`
- `server/game/items/__init__.py`
- `server/game/items/component_hooks.py`

## Audit Trail

- EXTRACTED: 2305 (91%)
- INFERRED: 221 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*