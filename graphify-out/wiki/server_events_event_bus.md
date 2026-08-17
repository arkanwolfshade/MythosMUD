# server events event bus

> 132 nodes

## Key Concepts

- **event_types.py** (87 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
- **event_bus.py** (32 connections) — `server/events/event_bus.py`
- **event_reaction_system.py** (30 connections) — `server/npc/event_reaction_system.py`
- **NPCDied** (29 connections) — `server/events/event_types.py`
- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **test_lifecycle_manager.py** (27 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **server/events/__init__.py** (25 connections) — `server/events/__init__.py`
- **NPCLifecycleState** (24 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **despawn_npc_impl()** (20 connections) — `server/npc/lifecycle_despawn.py`
- **aggressive_mob_npc.py** (19 connections) — `server/npc/aggressive_mob_npc.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_make_manager()** (18 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **NPCSpoke** (14 connections) — `server/events/event_types.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **communication_integration.py** (13 connections) — `server/npc/communication_integration.py`
- **shopkeeper_npc.py** (13 connections) — `server/npc/shopkeeper_npc.py`
- *... and 107 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (69 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (36 shared connections)
- [moduletype](moduletype.md) (26 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (26 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (19 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (15 shared connections)
- [server events event types playerleftroom](server_events_event_types_playerleftroom.md) (13 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (12 shared connections)
- [server models npc npcdefinition is](server_models_npc_npcdefinition_is.md) (11 shared connections)
- [server config npc config](server_config_npc_config.md) (11 shared connections)
- [server game chat npc system](server_game_chat_npc_system.md) (10 shared connections)
- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (9 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/models/room.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/combat_integration.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/shopkeeper_npc.py`
- `server/realtime/event_handler.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 593 (91%)
- INFERRED: 61 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*