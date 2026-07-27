# Player Related Models

> 65 nodes · cohesion 0.05

## Key Concepts

- **PlayerChannelPreferences** (25 connections) — `server/models/player.py`
- **PlayerPreferencesService** (19 connections) — `server/services/player_preferences_service.py`
- **test_player_related_models.py** (18 connections) — `server/tests/unit/models/test_player_related_models.py`
- **UUID** (11 connections) — `server/services/player_preferences_service.py`
- **._is_valid_player_id()** (11 connections) — `server/services/player_preferences_service.py`
- **Any** (9 connections) — `server/services/player_preferences_service.py`
- **AsyncSession** (9 connections) — `server/services/player_preferences_service.py`
- **.create_player_preferences()** (7 connections) — `server/services/player_preferences_service.py`
- **.is_channel_muted()** (7 connections) — `server/services/player_preferences_service.py`
- **.mute_channel()** (7 connections) — `server/services/player_preferences_service.py`
- **.unmute_channel()** (7 connections) — `server/services/player_preferences_service.py`
- **.update_default_channel()** (7 connections) — `server/services/player_preferences_service.py`
- **player_preferences_service.py** (6 connections) — `server/services/player_preferences_service.py`
- **.delete_player_preferences()** (6 connections) — `server/services/player_preferences_service.py`
- **.get_muted_channels()** (6 connections) — `server/services/player_preferences_service.py`
- **.get_player_preferences()** (6 connections) — `server/services/player_preferences_service.py`
- **._is_valid_channel()** (6 connections) — `server/services/player_preferences_service.py`
- **test_player_channel_preferences_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_with_muted_channels()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_multiple_rooms()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- *... and 40 more nodes in this community*

## Relationships

- [[SQLAlchemy Model Base]] (10 shared connections)
- [[Player Domain Model]] (6 shared connections)
- [[Lucidity Database Models]] (4 shared connections)
- [[Player Preferences Service]] (3 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[API Test Fixtures]] (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/services/player_preferences_service.py`
- `server/tests/unit/models/test_player_related_models.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 226 (93%)
- INFERRED: 18 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
