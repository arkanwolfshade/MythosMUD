# test_npc_combat_integration_join.py

> 272 nodes · cohesion 0.01

## Key Concepts

- **test_combat_event_publisher.py** (54 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (45 connections) — `server/services/combat_event_publisher.py`
- **CombatEventHandler** (41 connections) — `server/services/combat_event_handler.py`
- **nats_exceptions.py** (39 connections) — `server/services/nats_exceptions.py`
- **PlayerDiedEvent** (31 connections) — `server/events/event_types.py`
- **combat_event_publisher.py** (31 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (30 connections) — `server/services/combat_death_handler.py`
- **test_combat_npc_disposition.py** (30 connections) — `server/tests/unit/services/test_combat_npc_disposition.py`
- **CombatDeathHandler** (26 connections) — `server/services/combat_death_handler.py`
- **PlayerAttackedEvent** (24 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (23 connections) — `server/events/combat_events.py`
- **combat_events.py** (22 connections) — `server/events/combat_events.py`
- **combat_event_handler.py** (21 connections) — `server/services/combat_event_handler.py`
- **NPCDiedEvent** (20 connections) — `server/events/combat_events.py`
- **asyncio** (20 connections)
- **test_combat_event_handler.py** (19 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **NPCAttackedEvent** (18 connections) — `server/events/combat_events.py`
- **CombatEndedEvent** (17 connections) — `server/events/combat_events.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (15 connections) — `server/events/event_types.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatTargetSwitchEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **_participant()** (13 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- *... and 247 more nodes in this community*

## Relationships

- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (34 shared connections)
- [DatabaseManager](DatabaseManager.md) (23 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (20 shared connections)
- [look_container.py](look_container.py.md) (18 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (18 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (16 shared connections)
- [Room](Room.md) (16 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (14 shared connections)
- [get_username_from_user](get_username_from_user.md) (11 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (11 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_combat_npc_disposition.py`

## Audit Trail

- EXTRACTED: 718 (88%)
- INFERRED: 99 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*