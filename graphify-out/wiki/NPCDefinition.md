# NPCDefinition

> 623 nodes

## Key Concepts

- **NPCDefinition** (103 connections) — `server/models/npc.py`
- **event_types.py** (93 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (76 connections) — `server/events/event_types.py`
- **async_persistence.py** (64 connections) — `server/async_persistence.py`
- **asyncio.md** (58 connections) — `.claude/rules/asyncio.md`
- **BaseEvent** (55 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (49 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **NPCEnteredRoom** (46 connections) — `server/events/event_types.py`
- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **player_event_handlers.py** (42 connections) — `server/realtime/player_event_handlers.py`
- **test_room_sync_service.py** (41 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **event_bus.py** (39 connections) — `server/events/event_bus.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **event_handler.py** (36 connections) — `server/realtime/event_handler.py`
- **player_combat_service.py** (36 connections) — `server/services/player_combat_service.py`
- **models/room.py** (32 connections) — `server/models/room.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **event_reaction_system.py** (30 connections) — `server/npc/event_reaction_system.py`
- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- *... and 598 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (177 shared connections)
- [CombatService](CombatService.md) (63 shared connections)
- [ContainerComponent](ContainerComponent.md) (62 shared connections)
- [Invite](Invite.md) (52 shared connections)
- [InventoryCommandFactory](InventoryCommandFactory.md) (33 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (28 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (25 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (25 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (24 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (21 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (20 shared connections)
- [CommandService](CommandService.md) (20 shared connections)

## Source Files

- `.claude/rules/asyncio.md`
- `server/async_persistence.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_bus_base.py`
- `server/events/event_bus_lifecycle.py`
- `server/events/event_bus_processing.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/game/follow_service.py`
- `server/game/party_service.py`
- `server/game/quest/quest_events.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/communication_integration.py`

## Audit Trail

- EXTRACTED: 2240 (94%)
- INFERRED: 134 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*