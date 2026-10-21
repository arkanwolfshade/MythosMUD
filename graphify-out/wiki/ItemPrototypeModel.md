# ItemPrototypeModel

> 24 nodes · cohesion 0.09

## Key Concepts

- **_FakeMuteRepository** (21 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_channel_success()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_global_success()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_player_admin_immune()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_player_database_failure_leaves_memory_untouched()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_player_success()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_unmute_channel_success()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_unmute_global_success()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_unmute_player_not_muted()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_unmute_player_success()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **user_manager()** (6 connections) — `server/tests/unit/services/test_user_manager.py`
- **mute_repo()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **fixture** (2 connections)
- **Test mute_player() persists, then indexes the mute.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **A failed write must not leave a mute that would silently vanish on restart.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test mute_player() fails when trying to mute admin.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test unmute_player() successfully unmutes a player.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test unmute_player() when player is not muted.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test mute_channel() successfully mutes a channel.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test unmute_channel() successfully unmutes a channel.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test mute_global() successfully globally mutes a player.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **In-memory stand-in for the player_mutes procedures.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test unmute_global() successfully unmutes a player.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Create a UserManager instance backed by the fake repository.** (1 connections) — `server/tests/unit/services/test_user_manager.py`

## Relationships

- [asyncio](asyncio.md) (24 shared connections)
- [Stats](Stats.md) (19 shared connections)
- [test_aggression.py](test_aggression.py.md) (5 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_user_manager.py`

## Audit Trail

- EXTRACTED: 61 (84%)
- INFERRED: 12 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*