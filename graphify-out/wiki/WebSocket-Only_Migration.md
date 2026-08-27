# WebSocket-Only Migration

> 8 nodes

## Key Concepts

- **RoomBasedChannelStrategy** (10 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_room_based_channel_strategy_broadcast()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_room_based_channel_strategy_broadcast_no_room_id()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **.__init__()** (2 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Strategy for room-based channels (say, local, emote, pose).** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Initialize room-based channel strategy. Args: channel_type: Type of room-based…** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test RoomBasedChannelStrategy.broadcast() broadcasts to room.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test RoomBasedChannelStrategy.broadcast() handles missing room_id.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [required](required.md) (4 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (3 shared connections)
- [TestPostgresConnectionPool](TestPostgresConnectionPool.md) (2 shared connections)
- [_make_mock_row](_make_mock_row.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 14 (82%)
- INFERRED: 3 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*