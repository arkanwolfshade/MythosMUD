# Command Parser

> 87 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **CORSConfig** (19 connections) — `server/config/models/cors.py`
- **GameConfig** (15 connections) — `server/config/models/game.py`
- **__init__.py** (11 connections) — `server/config/__init__.py`
- **._parse_csv()** (10 connections) — `server/config/models/cors.py`
- **PlayerStatsConfig** (9 connections) — `server/config/models/player_stats.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **Any** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **._validate_non_empty()** (5 connections) — `server/config/models/cors.py`
- **._clean_list_items()** (5 connections) — `server/config/models/cors.py`
- **._parse_json_array()** (5 connections) — `server/config/models/cors.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **._parse_comma_separated()** (4 connections) — `server/config/models/cors.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **.parse_allow_origins()** (3 connections) — `server/config/models/cors.py`
- **.parse_allow_methods()** (3 connections) — `server/config/models/cors.py`
- **.parse_allow_headers()** (3 connections) — `server/config/models/cors.py`
- *... and 62 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (18 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (6 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (3 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (2 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (2 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (1 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/config/models/cors.py`
- `server/config/models/game.py`
- `server/config/models/player_stats.py`

## Audit Trail

- EXTRACTED: 249 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*