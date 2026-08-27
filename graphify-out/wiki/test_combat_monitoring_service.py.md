# test_combat_monitoring_service.py

> 91 nodes

## Key Concepts

- **NPCBase** (77 connections) — `server/npc/npc_base.py`
- **CommunicationIntegrationProtocol** (8 connections) — `server/npc/npc_protocols.py`
- **CombatIntegrationProtocol** (6 connections) — `server/npc/npc_protocols.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **._handle_npc_death()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (5 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **.execute_behavior()** (4 connections) — `server/npc/npc_base.py`
- **.heal()** (4 connections) — `server/npc/npc_base.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **npc_protocols.py** (4 connections) — `server/npc/npc_protocols.py`
- **.add_item_to_inventory()** (3 connections) — `server/npc/npc_base.py`
- **._enrich_behavior_context()** (3 connections) — `server/npc/npc_base.py`
- **.from_dict()** (3 connections) — `server/npc/npc_base.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **.get_combat_stats()** (3 connections) — `server/npc/npc_base.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/npc_base.py`
- **.listen()** (3 connections) — `server/npc/npc_base.py`
- **._move_simple()** (3 connections) — `server/npc/npc_base.py`
- **._safe_stat_int()** (3 connections) — `server/npc/npc_base.py`
- **.schedule_idle_movement()** (3 connections) — `server/npc/npc_base.py`
- *... and 66 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (24 shared connections)
- [Invite](Invite.md) (10 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (4 shared connections)
- [useGameClientV2Container.ts](useGameClientV2Container.ts.md) (2 shared connections)
- [test_player_spell_repository.py](test_player_spell_repository.py.md) (2 shared connections)
- [handle_command](handle_command.md) (1 shared connections)
- [RoomDataCache](RoomDataCache.md) (1 shared connections)
- [useWebSocketConnection.ts](useWebSocketConnection.ts.md) (1 shared connections)
- [TestGracefulDegradation](TestGracefulDegradation.md) (1 shared connections)
- [MythosMUD Commit Messages](MythosMUD_Commit_Messages.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_protocols.py`

## Audit Trail

- EXTRACTED: 149 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*