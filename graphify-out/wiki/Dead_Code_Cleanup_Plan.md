# Dead Code Cleanup Plan

> 191 nodes

## Key Concepts

- **__init__.py** (70 connections) — `server/schemas/__init__.py`
- **players.py** (69 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **FastAPIRequest** (17 connections)
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **UUID** (15 connections)
- **npc_admin.py** (15 connections) — `server/schemas/admin/npc_admin.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **AdminSession** (14 connections) — `server/schemas/admin/admin_data.py`
- **AuditLogEntry** (14 connections) — `server/schemas/admin/admin_data.py`
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (13 connections) — `server/api/players.py`
- **__init__.py** (13 connections) — `server/schemas/admin/__init__.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **select_character()** (12 connections) — `server/api/players.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- *... and 166 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (114 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (37 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (16 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (15 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (14 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (9 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (7 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (7 shared connections)
- [Quest Service Core](Quest_Service_Core.md) (5 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (5 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (5 shared connections)

## Source Files

- `server/api/players.py`
- `server/game/player_service.py`
- `server/schemas/__init__.py`
- `server/schemas/admin/__init__.py`
- `server/schemas/admin/admin_data.py`
- `server/schemas/admin/npc_admin.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 982 (92%)
- INFERRED: 84 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*