# NPC Combat Start Race Condition

> 8 nodes

## Key Concepts

- **UnknownChannelStrategy** (9 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.get_strategy()** (6 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_unknown_channel_strategy_broadcast()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **.__init__()** (2 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Strategy for unknown channel types.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Initialize unknown channel strategy. Args: channel_type: Unknown channel type** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Get strategy for channel type. Args: channel_type: Type of channel to get…** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test UnknownChannelStrategy.broadcast() handles unknown channel.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [required](required.md) (4 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (3 shared connections)
- [models/container.py](models-container.py.md) (2 shared connections)
- [_make_mock_row](_make_mock_row.md) (1 shared connections)
- [TestPostgresConnectionPool](TestPostgresConnectionPool.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 14 (78%)
- INFERRED: 4 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*