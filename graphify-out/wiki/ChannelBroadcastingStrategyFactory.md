# ChannelBroadcastingStrategyFactory

> 12 nodes

## Key Concepts

- **ChannelBroadcastingStrategyFactory** (10 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.register_strategy()** (3 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_get_strategy_known()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_get_strategy_unknown()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_init()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_register_strategy()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Factory for creating channel broadcasting strategies.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Register a new strategy for a channel type. Args: channel_type: Channel type to…** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.__init__() initializes with default…** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.get_strategy() returns…** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.register_strategy() registers new…** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [test_channel_broadcasting_strategies.py](test_channel_broadcasting_strategies.py.md) (5 shared connections)
- [channel_broadcasting_strategies.py](channel_broadcasting_strategies.py.md) (3 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*