# ChannelBroadcastingStrategyFactory

> 10 nodes · cohesion 0.20

## Key Concepts

- **ChannelBroadcastingStrategyFactory** (11 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.register_strategy()** (3 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_init()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_register_strategy()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_global_channel_strategy_factory_instance()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Factory for creating channel broadcasting strategies.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Register a new strategy for a channel type.          Args:             channel_t** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.__init__() initializes with default stra** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.register_strategy() registers new strate** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test global channel_strategy_factory instance exists.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [test_channel_broadcasting_strategies.py](test_channel_broadcasting_strategies.py.md) (4 shared connections)
- [channel_broadcasting_strategies.py](channel_broadcasting_strategies.py.md) (3 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (2 shared connections)
- [RoomBasedChannelStrategy](RoomBasedChannelStrategy.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 26 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*