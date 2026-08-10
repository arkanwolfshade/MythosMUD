# Who Command Tests

> 71 nodes

## Key Concepts

- **quest_events.py** (14 connections) — `server/game/quest/quest_events.py`
- **Any** (14 connections)
- **subscribe_quest_events()** (13 connections) — `server/game/quest/quest_events.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **NPCMessageQueue** (11 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (10 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (8 connections) — `server/npc/threading.py`
- **._execute_wander_movement()** (8 connections) — `server/npc/threading.py`
- **._process_wander_action()** (6 connections) — `server/npc/threading.py`
- **_make_on_player_entered()** (5 connections) — `server/game/quest/quest_events.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **Any** (4 connections)
- **_make_on_player_left()** (4 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (4 connections) — `server/game/quest/quest_events.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.get_messages()** (4 connections) — `server/npc/threading.py`
- **.clear_messages()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._parse_behavior_config()** (4 connections) — `server/npc/threading.py`
- **_parse_player_id()** (3 connections) — `server/game/quest/quest_events.py`
- **.to_json()** (3 connections) — `server/npc/threading.py`
- *... and 46 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (25 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (3 shared connections)
- [Cursor Bug Agents](Cursor_Bug_Agents.md) (3 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Chat Archive Advanced](Chat_Archive_Advanced.md) (1 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (1 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (1 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_events.py`
- `server/npc/threading.py`
- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 209 (92%)
- INFERRED: 19 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*