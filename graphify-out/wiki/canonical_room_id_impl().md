# canonical room id impl()

> 17 nodes

## Key Concepts

- **UUID** (9 connections)
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_individual_send()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_narrow_gather_delivery_dict()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_global_targets_and_stats()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Narrow asyncio.gather results when return_exceptions=True.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Read an integer delivery counter from stats dicts typed as dict[str, object].** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Compute recipient list and initial stats for broadcast_global.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Process results from batch message delivery.          Args:             delivery** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Fallback to individual message sending if batch fails.          Args:** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Merge asyncio.gather outcomes into global broadcast stats.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Send global broadcast recipients one-by-one after batch failure.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a message to all connected players.          Args:             event:** (1 connections) — `server/realtime/messaging/message_broadcaster.py`

## Relationships

- [Remove sensitive data from log](Remove_sensitive_data_from_log.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [test database](test_database.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*