# Player State Factories

> 27 nodes

## Key Concepts

- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (17 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (11 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **Check if player is resting or in login grace period, interrupt rest if needed. P** (1 connections) — `server/commands/combat_handler.py`
- **Check if player is resting or in login grace period, interrupt rest if needed.** (1 connections) — `server/commands/combat_handler.py`
- **Rest command handler for clean disconnection.  This module handles the /rest com** (1 connections) — `server/commands/rest_command.py`
- **Check if a player is currently in combat.      Args:         player_id: The play** (1 connections) — `server/commands/rest_command.py`
- **Check if the current room is a rest location (inn/hotel/motel).      Args:** (1 connections) — `server/commands/rest_command.py`
- **Disconnect a player intentionally (via /rest command).      This marks the disco** (1 connections) — `server/commands/rest_command.py`
- **Start the 10-second rest countdown.      Args:         player_id: The player's I** (1 connections) — `server/commands/rest_command.py`
- **Cancel the rest countdown for a player.      Called from combat, movement, and s** (1 connections) — `server/commands/rest_command.py`
- **Check if a player is currently resting (in /rest countdown).      Args:** (1 connections) — `server/commands/rest_command.py`
- **Get persistence and connection_manager services from app state.      Args:** (1 connections) — `server/commands/rest_command.py`
- **Load app, services, and player for /rest.      Returns:         Error response d** (1 connections) — `server/commands/rest_command.py`
- *... and 2 more nodes in this community*

## Relationships

- [Party Service Management](Party_Service_Management.md) (26 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (5 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (5 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (5 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (4 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (2 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (1 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (1 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`

## Audit Trail

- EXTRACTED: 165 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*