# UUID

> 79 nodes

## Key Concepts

- **UserManager** (58 connections) — `server/services/user_manager.py`
- **UUID** (39 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **.is_admin()** (10 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **.get_player_mutes()** (7 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **.add_admin()** (6 connections) — `server/services/user_manager.py`
- **.remove_admin()** (6 connections) — `server/services/user_manager.py`
- **.mute_player()** (6 connections) — `server/services/user_manager.py`
- **.unmute_player()** (6 connections) — `server/services/user_manager.py`
- **.mute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_global()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **._load_player_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **._load_global_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **.mute_channel()** (5 connections) — `server/services/user_manager.py`
- **.unmute_channel()** (5 connections) — `server/services/user_manager.py`
- **.is_player_muted_async()** (5 connections) — `server/services/user_manager.py`
- **.is_channel_muted()** (5 connections) — `server/services/user_manager.py`
- *... and 54 more nodes in this community*

## Relationships

- [message filtering](message_filtering.md) (16 shared connections)
- [APIRouter](APIRouter.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [.get instance()](get_instance%28%29.md) (3 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (2 shared connections)
- [test user manager](test_user_manager.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [message formatters](message_formatters.md) (1 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 380 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*