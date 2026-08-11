# Game State Provider

> 43 nodes

## Key Concepts

- **.state()** (36 connections) — `server/realtime/connection_state_machine.py`
- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (15 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (8 connections) — `server/realtime/nats_message_handler.py`
- **._convert_player_uuids_to_names()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **.get_room_occupants()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **Current FSM state as a single State.          Narrows base class type (Any | Mut** (1 connections) — `server/realtime/connection_state_machine.py`
- **Provides initial game state for newly connected players.      This class provide** (1 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 18 more nodes in this community*

## Relationships

- [Player Respawn Events](Player_Respawn_Events.md) (8 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (3 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (2 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (2 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (2 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (2 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (2 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (2 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (2 shared connections)
- [WebSocket Helper Utilities](WebSocket_Helper_Utilities.md) (2 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 187 (80%)
- INFERRED: 47 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*