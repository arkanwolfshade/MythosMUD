# Game Mechanics Service

> 103 nodes

## Key Concepts

- **character_creation.py** (54 connections) — `server/api/character_creation.py`
- **RollStatsRequest** (22 connections) — `server/schemas/players/player_requests.py`
- **roll_character_stats()** (21 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **create_character_with_stats()** (17 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (15 connections) — `server/api/character_creation.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **Any** (10 connections)
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **RollStatsResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **ValidateStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **_raise_roll_stats_error()** (8 connections) — `server/api/character_creation.py`
- **StatSummary** (8 connections) — `server/schemas/players/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- **_validate_skills_payload()** (7 connections) — `server/api/character_creation.py`
- *... and 78 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (20 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (19 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (18 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (18 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (10 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (7 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (6 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (6 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (3 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/game/profession_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 502 (95%)
- INFERRED: 25 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*