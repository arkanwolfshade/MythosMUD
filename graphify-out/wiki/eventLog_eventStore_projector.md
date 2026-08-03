# eventLog eventStore projector

> 27 nodes

## Key Concepts

- **test_chat_moderation.py** (30 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_normalize_player_id_accepts_uuid()** (2 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **player_service()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **user_manager()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_mute_channel_delegates_to_user_manager()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_mute_player_returns_false_when_target_missing()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_is_channel_muted()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_add_admin_returns_true()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_can_send_message()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_format_mute_duration_permanent()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_format_mute_duration_remaining_minutes()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_format_mute_duration_expired()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_get_mute_status_player_not_found()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_get_mute_status_invalid_player_id()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_unmute_channel()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_mute_player_success()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_unmute_player_success()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_mute_global_success()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_unmute_global_success()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_is_player_muted_and_global()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_remove_admin()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_get_player_mutes_and_stats()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_format_mute_entry_and_section()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_get_mute_status_with_personal_mutes()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **test_get_mute_status_includes_player_name()** (1 connections) — `server/tests/unit/game/test_chat_moderation.py`
- *... and 2 more nodes in this community*

## Relationships

- [chat moderation game](chat_moderation_game.md) (2 shared connections)
- [dialogue schemas tree](dialogue_schemas_tree.md) (2 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_chat_moderation.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*