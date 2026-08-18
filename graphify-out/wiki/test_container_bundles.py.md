# test_container_bundles.py

> 114 nodes

## Key Concepts

- **test_container_bundles.py** (65 connections) — `server/tests/unit/container/test_container_bundles.py`
- **container/main.py** (37 connections) — `server/container/main.py`
- **CombatBundle** (33 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (33 connections) — `server/container/bundles/realtime.py`
- **asyncio** (23 connections)
- **NPCBundle** (19 connections) — `server/container/bundles/npc.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **bundles/realtime.py** (15 connections) — `server/container/bundles/realtime.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **bundles/combat.py** (14 connections) — `server/container/bundles/combat.py`
- **bundles/monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- **test_realtime_bundle_nats.py** (11 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **ChatBundle** (10 connections) — `server/container/bundles/chat.py`
- **._initialize_primary_bundles()** (10 connections) — `server/container/main.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **._connect_nats()** (7 connections) — `server/container/bundles/realtime.py`
- **_flatten_bundle()** (7 connections) — `server/container/main.py`
- **_validate_magic_prerequisites()** (6 connections) — `server/container/bundles/magic.py`
- **.initialize()** (6 connections) — `server/container/bundles/npc.py`
- **._setup_nats_dependent_services()** (6 connections) — `server/container/bundles/realtime.py`
- *... and 89 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (42 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [GameBundle](GameBundle.md) (21 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (15 shared connections)
- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (3 shared connections)
- [EventPublisher](EventPublisher.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [MythosChronicle](MythosChronicle.md) (3 shared connections)

## Source Files

- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`

## Audit Trail

- EXTRACTED: 339 (84%)
- INFERRED: 64 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*