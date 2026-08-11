# test_profession_meets_stat_requirements_multiple_not_met

> 19 nodes

## Key Concepts

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

- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (5 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (3 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (3 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)

## Source Files

- `server/game/player_schema_converter.py`

## Audit Trail

- EXTRACTED: 73 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*