# Error Monitor Service

> 10 nodes

## Key Concepts

- **UnknownChannelStrategy** (9 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.get_strategy()** (6 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_get_strategy_unknown()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_unknown_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **.__init__()** (2 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Strategy for unknown channel types.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Initialize unknown channel strategy.          Args:             channel_type: Un** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Get strategy for channel type.          Args:             channel_type: Type of** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test UnknownChannelStrategy.broadcast() handles unknown channel.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.get_strategy() returns UnknownChannelStr** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [Respawn Persistence Bug](Respawn_Persistence_Bug.md) (3 shared connections)
- [Channel Broadcast Strategies](Channel_Broadcast_Strategies.md) (3 shared connections)
- [Emotes JSON Schema](Emotes_JSON_Schema.md) (2 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (2 shared connections)
- [Transaction Boundaries Audit](Transaction_Boundaries_Audit.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 25 (86%)
- INFERRED: 4 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*