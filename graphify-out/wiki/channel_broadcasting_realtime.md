# channel broadcasting realtime

> 10 nodes

## Key Concepts

- **RoomBasedChannelStrategy** (10 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_get_strategy_known()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_room_based_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_room_based_channel_strategy_broadcast_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **.__init__()** (2 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Strategy for room-based channels (say, local, emote, pose).** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Initialize room-based channel strategy.          Args:             channel_type:** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test RoomBasedChannelStrategy.broadcast() broadcasts to room.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test RoomBasedChannelStrategy.broadcast() handles missing room_id.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [channel realtime broadcasting](channel_realtime_broadcasting.md) (4 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (2 shared connections)
- [world loader room](world_loader_room.md) (1 shared connections)
- [realtime channel broadcasting](realtime_channel_broadcasting.md) (1 shared connections)
- [channel broadcasting realtime](channel_broadcasting_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 25 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*