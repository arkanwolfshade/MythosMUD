# Client ASCII Map API

> 45 nodes

## Key Concepts

- **PlayerChannelPreferences** (30 connections) — `server/models/player.py`
- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **UUID** (10 connections)
- **player_preferences_service.py** (9 connections) — `server/services/player_preferences_service.py`
- **AsyncSession** (8 connections)
- **Any** (8 connections)
- **.update_default_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.mute_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.unmute_channel()** (8 connections) — `server/services/player_preferences_service.py`
- **.is_channel_muted()** (8 connections) — `server/services/player_preferences_service.py`
- **.create_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.get_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.get_muted_channels()** (7 connections) — `server/services/player_preferences_service.py`
- **.delete_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **._is_valid_channel()** (6 connections) — `server/services/player_preferences_service.py`
- **test_player_channel_preferences_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_with_muted_channels()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **preferences_service()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **sample_preferences()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **.__init__()** (2 connections) — `server/services/player_preferences_service.py`
- **._is_valid_json_array()** (2 connections) — `server/services/player_preferences_service.py`
- **Player channel preferences model for Advanced Chat Channels.      Stores player** (1 connections) — `server/models/player.py`
- *... and 20 more nodes in this community*

## Relationships

- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (11 shared connections)
- [Dependency Upgrade Report](Dependency_Upgrade_Report.md) (5 shared connections)
- [Async Persistence Delegates](Async_Persistence_Delegates.md) (5 shared connections)
- [Plan Modernization Archive](Plan_Modernization_Archive.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/services/player_preferences_service.py`
- `server/tests/unit/models/test_player_related_models.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 174 (85%)
- INFERRED: 30 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*