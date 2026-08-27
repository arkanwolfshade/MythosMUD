# Round-Based Combat

> 8 nodes

## Key Concepts

- **SystemAdminChannelStrategy** (9 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_system_admin_channel_strategy_broadcast()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_system_admin_channel_strategy_personal_target()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **.__init__()** (2 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Strategy for system/admin channel broadcasting.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Initialize system/admin channel strategy. Args: channel_type: Type of…** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test SystemAdminChannelStrategy.broadcast() broadcasts globally.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Personal system messages deliver to target_player_id only.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (3 shared connections)
- [required](required.md) (3 shared connections)
- [TestPostgresConnectionPool](TestPostgresConnectionPool.md) (2 shared connections)
- [_make_mock_row](_make_mock_row.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 14 (88%)
- INFERRED: 2 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*