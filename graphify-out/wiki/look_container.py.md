# look_container.py

> 293 nodes · cohesion 0.01

## Key Concepts

- **MessageCategory** (135 connections) — `server/constants/message_category.py`
- **test_message_category_invariants.py** (107 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **NpcDisposition** (95 connections) — `server/constants/npc_disposition.py`
- **message_category.py** (56 connections) — `server/constants/message_category.py`
- **npc_disposition.py** (46 connections) — `server/constants/npc_disposition.py`
- **NPCEventHandler** (41 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (38 connections) — `server/realtime/message_builders.py`
- **websocket_handler_commands.py** (36 connections) — `server/realtime/websocket_handler_commands.py`
- **player_event_handlers_respawn.py** (34 connections) — `server/realtime/player_event_handlers_respawn.py`
- **event_handlers.py** (32 connections) — `server/realtime/event_handlers.py`
- **npc_name_segment()** (31 connections) — `server/constants/message_segments.py`
- **message_segments.py** (30 connections) — `server/constants/message_segments.py`
- **npc_event_handlers.py** (27 connections) — `server/realtime/npc_event_handlers.py`
- **format_message_content()** (24 connections) — `server/realtime/message_formatters.py`
- **message_with_segments()** (22 connections) — `server/constants/message_segments.py`
- **message_formatters.py** (22 connections) — `server/realtime/message_formatters.py`
- **hallucinations.py** (21 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **message_builders.py** (20 connections) — `server/realtime/message_builders.py`
- **combat_broadcasts.py** (20 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **MessageSegment** (19 connections) — `server/constants/message_segments.py`
- **PlayerDeliriumRespawnedEvent** (18 connections) — `server/events/event_types.py`
- **test_npc_event_handlers_segments.py** (18 connections) — `server/tests/unit/realtime/test_npc_event_handlers_segments.py`
- **format_message_segments()** (16 connections) — `server/realtime/message_formatters.py`
- **join_parts()** (15 connections) — `server/constants/message_segments.py`
- **.call()** (15 connections) — `server/realtime/circuit_breaker.py`
- *... and 268 more nodes in this community*

## Relationships

- [Room](Room.md) (44 shared connections)
- [.publish_with_pool](publish_with_pool.md) (26 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (25 shared connections)
- [security.ts](security.ts.md) (23 shared connections)
- [test_room_subscription_manager_drops.py](test_room_subscription_manager_drops.py.md) (22 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (21 shared connections)
- [BaseCommand](BaseCommand.md) (20 shared connections)
- [PerformanceTester](PerformanceTester.md) (20 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (19 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (18 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (17 shared connections)
- [deque](deque.md) (17 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/constants/message_category.py`
- `server/constants/message_segments.py`
- `server/constants/npc_disposition.py`
- `server/events/event_types.py`
- `server/realtime/__init__.py`
- `server/realtime/circuit_breaker.py`
- `server/realtime/event_handler.py`
- `server/realtime/event_handlers.py`
- `server/realtime/message_builders.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/websocket_handler_commands.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/passive_lucidity_flux/hallucinations.py`

## Audit Trail

- EXTRACTED: 1050 (85%)
- INFERRED: 181 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*