# Spell Effects Tests

> 38 nodes

## Key Concepts

- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **test_warded_indicator_removed_after_expiration()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_both_linkdead_and_warded_indicators()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **test_warded_indicator_in_player_occupant_processor()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **test_warded_indicator_in_look_room()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_look_player()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_websocket_room_updates()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_not_shown_for_reconnections()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Any** (3 connections)
- **test_player_occupant_processor_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Player occupant processing utilities.  This module handles querying and processi** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Processes player occupants for rooms.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Initialize player occupant processor.          Args:             connection_mana** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Ensure a player is included in the player ID strings list if specified.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Convert player ID strings to UUIDs for batch loading.          Args:** (1 connections) — `server/realtime/player_occupant_processor.py`
- *... and 13 more nodes in this community*

## Relationships

- [Player Respawn Events](Player_Respawn_Events.md) (15 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (8 shared connections)
- [Look Player Command](Look_Player_Command.md) (7 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (5 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [API Type Guards](API_Type_Guards.md) (3 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (2 shared connections)
- [NATS Retry Handler](NATS_Retry_Handler.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)

## Source Files

- `server/realtime/player_occupant_processor.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 156 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*