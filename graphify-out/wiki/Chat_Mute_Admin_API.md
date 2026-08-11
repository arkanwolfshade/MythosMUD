# Chat Mute Admin API

> 160 nodes

## Key Concepts

- **ChatService** (83 connections) — `server/game/chat_service.py`
- **test_chat_service.py** (39 connections) — `server/tests/unit/game/test_chat_service.py`
- **UUID** (26 connections)
- **Any** (14 connections)
- **ChatPoseManager** (11 connections) — `server/game/chat_pose_manager.py`
- **ChatWhisperTracker** (10 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (7 connections) — `server/game/chat_service.py`
- **chat_pose_manager.py** (5 connections) — `server/game/chat_pose_manager.py`
- **.normalize_player_id()** (5 connections) — `server/game/chat_pose_manager.py`
- **chat_whisper_tracker.py** (5 connections) — `server/game/chat_whisper_tracker.py`
- **.send_say_message()** (4 connections) — `server/game/chat_service.py`
- **.send_local_message()** (4 connections) — `server/game/chat_service.py`
- **.send_global_message()** (4 connections) — `server/game/chat_service.py`
- **.send_party_message()** (4 connections) — `server/game/chat_service.py`
- **.send_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_whisper_message()** (4 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (4 connections) — `server/game/chat_service.py`
- **.set_player_pose()** (4 connections) — `server/game/chat_service.py`
- **.send_predefined_emote()** (4 connections) — `server/game/chat_service.py`
- **.get_player_mutes()** (4 connections) — `server/game/chat_service.py`
- **test_get_room_messages()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **.set_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.get_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.clear_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **._normalize_player_id()** (3 connections) — `server/game/chat_service.py`
- *... and 135 more nodes in this community*

## Relationships

- [Who Command Tests](Who_Command_Tests.md) (17 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Container Open Events](Container_Open_Events.md) (3 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Chat Moderation Service](Chat_Moderation_Service.md) (2 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (1 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (1 shared connections)
- [Feature Implementation Phases](Feature_Implementation_Phases.md) (1 shared connections)
- [Commands Time](Commands_Time.md) (1 shared connections)

## Source Files

- `server/game/chat_pose_manager.py`
- `server/game/chat_service.py`
- `server/game/chat_whisper_tracker.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 484 (98%)
- INFERRED: 12 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*