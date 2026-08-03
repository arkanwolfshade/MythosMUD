# npc behavior engine

> 12 nodes

## Key Concepts

- **ChannelBroadcastingStrategyFactory** (11 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_get_strategy_unknown()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **.register_strategy()** (3 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_init()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_register_strategy()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_global_channel_strategy_factory_instance()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Factory for creating channel broadcasting strategies.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Register a new strategy for a channel type.          Args:             channel_t** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.__init__() initializes with default stra** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.get_strategy() returns UnknownChannelStr** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.register_strategy() registers new strate** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test global channel_strategy_factory instance exists.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [channel realtime broadcasting](channel_realtime_broadcasting.md) (5 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (4 shared connections)
- [message handler factory](message_handler_factory.md) (1 shared connections)
- [channel broadcasting realtime](channel_broadcasting_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 30 (91%)
- INFERRED: 3 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*