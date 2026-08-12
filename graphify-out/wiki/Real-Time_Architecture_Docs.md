# Real-Time Architecture Docs

> 21 nodes

## Key Concepts

- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **.check_player_combat_state()** (5 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (5 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (5 connections) — `server/game/player_schema_converter.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **.__init__()** (3 connections) — `server/game/player_schema_converter.py`
- **Utility class for converting Player objects to PlayerRead schemas.** (1 connections) — `server/game/player_schema_converter.py`
- **Initialize the converter with persistence, optional combat service, and optional** (1 connections) — `server/game/player_schema_converter.py`
- **Check if player is in combat.** (1 connections) — `server/game/player_schema_converter.py`
- **Get profession information for player.** (1 connections) — `server/game/player_schema_converter.py`
- **Get stats, inventory, and status_effects from player, handling async methods.** (1 connections) — `server/game/player_schema_converter.py`
- **Compute derived stats fields (max_dp, max_magic_points, max_lucidity).** (1 connections) — `server/game/player_schema_converter.py`
- **Get PositionState from position value, with fallback to STANDING.** (1 connections) — `server/game/player_schema_converter.py`
- **Create PlayerRead schema from player object.** (1 connections) — `server/game/player_schema_converter.py`
- **Create PlayerRead schema from player dictionary.** (1 connections) — `server/game/player_schema_converter.py`
- **Convert a player object to PlayerRead schema.          Args:             player:** (1 connections) — `server/game/player_schema_converter.py`

## Relationships

- [Combat NPC Lookup](Combat_NPC_Lookup.md) (7 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (2 shared connections)
- [Test Refactoring Complete](Test_Refactoring_Complete.md) (2 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (1 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (1 shared connections)

## Source Files

- `server/game/player_schema_converter.py`

## Audit Trail

- EXTRACTED: 89 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*