# Communication Command Flows

> 92 nodes

## Key Concepts

- **NPCBase** (82 connections) — `server/npc/npc_base.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **CommunicationIntegrationProtocol** (10 connections) — `server/npc/npc_protocols.py`
- **CombatIntegrationProtocol** (7 connections) — `server/npc/npc_protocols.py`
- **._handle_npc_death()** (6 connections) — `server/npc/npc_base.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **.heal()** (4 connections) — `server/npc/npc_base.py`
- **.speak()** (4 connections) — `server/npc/npc_base.py`
- **.listen()** (4 connections) — `server/npc/npc_base.py`
- **.execute_behavior()** (4 connections) — `server/npc/npc_base.py`
- **npc_protocols.py** (4 connections) — `server/npc/npc_protocols.py`
- **._setup_base_behavior_rules()** (3 connections) — `server/npc/npc_base.py`
- **.get_stats()** (3 connections) — `server/npc/npc_base.py`
- **._safe_stat_int()** (3 connections) — `server/npc/npc_base.py`
- **.get_combat_stats()** (3 connections) — `server/npc/npc_base.py`
- **._update_determination_points()** (3 connections) — `server/npc/npc_base.py`
- **._sync_dp_stats()** (3 connections) — `server/npc/npc_base.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/npc_base.py`
- **._move_simple()** (3 connections) — `server/npc/npc_base.py`
- *... and 67 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (27 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (13 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (4 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (3 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (3 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (3 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (3 shared connections)
- [Player Position Service](Player_Position_Service.md) (2 shared connections)
- [Container Data Models](Container_Data_Models.md) (2 shared connections)
- [Chat Archive Advanced](Chat_Archive_Advanced.md) (1 shared connections)
- [Test Refactoring Complete](Test_Refactoring_Complete.md) (1 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_protocols.py`
- `server/npc/spawning_service.py`

## Audit Trail

- EXTRACTED: 258 (91%)
- INFERRED: 25 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*