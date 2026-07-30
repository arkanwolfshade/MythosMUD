# UUID

> 61 nodes

## Key Concepts

- **UserManager** (59 connections) — `server/services/user_manager.py`
- **UUID** (39 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
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
- **.is_globally_muted()** (5 connections) — `server/services/user_manager.py`
- **._convert_mute_info_timestamps()** (5 connections) — `server/services/user_manager.py`
- **._convert_mute_info_uuids()** (5 connections) — `server/services/user_manager.py`
- **._load_channel_mutes_from_data()** (5 connections) — `server/services/user_manager.py`
- *... and 36 more nodes in this community*

## Relationships

- [message filtering](message_filtering.md) (16 shared connections)
- [Tests for get stats generator](Tests_for_get_stats_generator.md) (16 shared connections)
- [circuit breaker](circuit_breaker.md) (4 shared connections)
- [MythosValidationError](MythosValidationError.md) (4 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (3 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [test user manager](test_user_manager.md) (2 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (2 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (2 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`
- `server/tests/unit/services/test_user_manager.py`

## Audit Trail

- EXTRACTED: 306 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*