# Services Lucidity Repository

> 8 nodes

## Key Concepts

- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_create_player_preferences_already_exists()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_false()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **Test get_shutdown_blocking_message() returns default message for unknown context** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test creating player preferences when they already exist.** (1 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **Test checking if channel is muted (returns False).** (1 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **Test checking if channel is muted when preferences not found.** (1 connections) — `server/tests/unit/services/test_player_preferences_service.py`

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (4 shared connections)
- [Async Persistence Delegates](Async_Persistence_Delegates.md) (3 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_admin_shutdown_command.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 13 (81%)
- INFERRED: 3 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*