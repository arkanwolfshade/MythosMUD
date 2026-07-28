# Playwright Remediation Plan

> 20 nodes · cohesion 0.13

## Key Concepts

- **MessageFilteringHelper** (23 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (7 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- **.preload_receiver_mute_data()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **message_filtering_helper()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **.collect_room_targets()** (2 connections) — `server/realtime/message_filtering.py`
- **Determine if mute check should be applied for a channel.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Compare two room IDs using canonical room ID resolution.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Get player's current room ID from online players cache.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Get player's current room ID from async persistence layer.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Helper class for message filtering operations.** (1 connections) — `server/realtime/message_filtering.py`
- **Check if a player is currently in the specified room.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Collect all players subscribed to a room (canonical and original IDs).** (1 connections) — `server/realtime/message_filtering.py`
- **Filter target players based on room location and mute status.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Pre-load mute data for all potential receivers.          Args:             user_** (1 connections) — `server/realtime/message_filtering.py`
- **Create a MessageFilteringHelper instance.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`

## Relationships

- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (6 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (2 shared connections)
- [Mythos Calendar Time Service](Mythos_Calendar_Time_Service.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering.py`

## Audit Trail

- EXTRACTED: 63 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*