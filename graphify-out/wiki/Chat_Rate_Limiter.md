# Chat Rate Limiter

> 27 nodes

## Key Concepts

- **player_connection_setup.py** (24 connections) — `server/realtime/player_connection_setup.py`
- **handle_new_connection_setup()** (17 connections) — `server/realtime/player_connection_setup.py`
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **_trigger_quests_for_room_on_spawn()** (8 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_send_room_occupants_update_after_connection()** (7 connections) — `server/realtime/player_connection_setup.py`
- **_update_player_last_active()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
- **event_handler()** (6 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **_add_player_to_room_silently()** (5 connections) — `server/realtime/player_connection_setup.py`
- **test_player_connection_setup_grace_period.py** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **_stable_room_id_for_quest()** (3 connections) — `server/realtime/player_connection_setup.py`
- **test_reconnection_cancels_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_reconnection_no_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **Player** (2 connections)
- **Player connection setup functions.  This module handles the setup tasks when a p** (1 connections) — `server/realtime/player_connection_setup.py`
- **Update last_active timestamp in database when player connects.      Args:** (1 connections) — `server/realtime/player_connection_setup.py`
- **Return stable room id for quest_offers lookup; strip instance_<uuid>_ prefix if** (1 connections) — `server/realtime/player_connection_setup.py`
- **On spawn, explicitly start quests offered by this room (e.g. Leave the Tutorial)** (1 connections) — `server/realtime/player_connection_setup.py`
- **Add player to the Room object without triggering PlayerEnteredRoom.      Movemen** (1 connections) — `server/realtime/player_connection_setup.py`
- **Broadcast a structured entry event to other occupants (excluding the newcomer).** (1 connections) — `server/realtime/player_connection_setup.py`
- **Send room_occupants update so other players see the new occupant.      Args:** (1 connections) — `server/realtime/player_connection_setup.py`
- **Handle setup tasks for a new player connection.      Args:         player_id: Th** (1 connections) — `server/realtime/player_connection_setup.py`
- **Create a RealTimeEventHandler instance.** (1 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **Unit tests for player connection setup grace period integration.  Tests that rec** (1 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- *... and 2 more nodes in this community*

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (3 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)
- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (3 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)
- [3. Systematic Investigation Approach](3._Systematic_Investigation_Approach.md) (1 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Audit Trail

- EXTRACTED: 114 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*