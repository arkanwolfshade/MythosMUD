# Quality Audit Report

> 12 nodes

## Key Concepts

- **PlayerChannelPreferences** (30 connections) — `server/models/player.py`
- **test_player_channel_preferences_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_with_muted_channels()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **sample_preferences()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **Player channel preferences model for Advanced Chat Channels.      Stores player** (1 connections) — `server/models/player.py`
- **Test PlayerChannelPreferences can be instantiated with required fields.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences has correct default values.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences can have muted channels.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Test PlayerChannelPreferences __repr__ method.** (1 connections) — `server/tests/unit/models/test_player_related_models.py`
- **Create sample player preferences.** (1 connections) — `server/tests/unit/services/test_player_preferences_service.py`

## Relationships

- [Client ASCII Map API](Client_ASCII_Map_API.md) (10 shared connections)
- [Dependency Upgrade Report](Dependency_Upgrade_Report.md) (6 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (2 shared connections)
- [Async Persistence Delegates](Async_Persistence_Delegates.md) (2 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/unit/models/test_player_related_models.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 30 (59%)
- INFERRED: 21 (41%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*