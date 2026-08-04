# player preferences service

> 101 nodes

## Key Concepts

- **test_player_preferences_service.py** (59 connections) — `server/tests/unit/services/test_player_preferences_service.py`
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
- *... and 76 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (26 shared connections)
- [npc population stats](npc_population_stats.md) (7 shared connections)
- [combat models rationale](combat_models_rationale.md) (4 shared connections)
- [player room realtime](player_room_realtime.md) (3 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (1 shared connections)
- [effect player repository](effect_player_repository.md) (1 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/services/player_preferences_service.py`
- `server/tests/unit/models/test_player_related_models.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 315 (91%)
- INFERRED: 30 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*