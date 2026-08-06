# world loader rationale

> 8 nodes

## Key Concepts

- **SystemAdminChannelStrategy** (9 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_system_admin_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_system_admin_channel_strategy_personal_target()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **.__init__()** (2 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Strategy for system/admin channel broadcasting.** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Initialize system/admin channel strategy.          Args:             channel_typ** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test SystemAdminChannelStrategy.broadcast() broadcasts globally.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **Personal system messages deliver to target_player_id only.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [channel realtime broadcasting](channel_realtime_broadcasting.md) (3 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (2 shared connections)
- [player room persistence](player_room_persistence.md) (1 shared connections)
- [realtime channel broadcasting](realtime_channel_broadcasting.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*