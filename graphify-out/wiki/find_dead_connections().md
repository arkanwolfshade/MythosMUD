# find dead connections()

> 5 nodes

## Key Concepts

- **datetime** (6 connections)
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **.get_decayed_containers()** (4 connections) — `server/async_persistence.py`
- **Update the last_active timestamp for a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get decayed containers.** (1 connections) — `server/async_persistence.py`

## Relationships

- [chat nats publisher](chat_nats_publisher.md) (2 shared connections)
- [init](init.md) (1 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (1 shared connections)
- [time commands](time_commands.md) (1 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [PlayerChannelPreferences](PlayerChannelPreferences.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 13 (81%)
- INFERRED: 3 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*