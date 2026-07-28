# Planning Contingency Plans

> 9 nodes · cohesion 0.20

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

## Relationships

- [Validation Rule Base](Validation_Rule_Base.md) (4 shared connections)
- [Phase Three Complete Summary](Phase_Three_Complete_Summary.md) (3 shared connections)
- [Channel Broadcast Strategies](Channel_Broadcast_Strategies.md) (1 shared connections)
- [Realtime Statistics Aggregator](Realtime_Statistics_Aggregator.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 24 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*