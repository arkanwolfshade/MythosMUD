# Npc Config Parsing

> 6 nodes · cohesion 0.20

## Key Concepts

- **UnknownChannelStrategy** (9 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.get_strategy()** (6 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_channel_broadcasting_strategy_factory_get_strategy_unknown()** (4 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **test_unknown_channel_strategy_broadcast()** (3 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`
- **.__init__()** (2 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Personal system messages deliver to target_player_id only.** (1 connections) — `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Relationships

- [Phase Three Complete Summary](Phase_Three_Complete_Summary.md) (3 shared connections)
- [Realtime Statistics Aggregator](Realtime_Statistics_Aggregator.md) (3 shared connections)
- [Validation Rule Base](Validation_Rule_Base.md) (3 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (2 shared connections)
- [Channel Broadcast Strategies](Channel_Broadcast_Strategies.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/realtime/test_channel_broadcasting_strategies.py`

## Audit Trail

- EXTRACTED: 21 (84%)
- INFERRED: 4 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*