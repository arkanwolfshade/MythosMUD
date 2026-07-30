# Any

> 13 nodes

## Key Concepts

- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._truncate_to_hour()** (4 connections) — `server/time/tick_scheduler.py`
- **.start()** (3 connections) — `server/time/tick_scheduler.py`
- **._sleep_until_next_hour()** (3 connections) — `server/time/tick_scheduler.py`
- **datetime** (3 connections)
- **Register the scheduler loop with the task registry.** (1 connections) — `server/time/tick_scheduler.py`
- **Background coroutine that emits ticks and waits for the next hour boundary.** (1 connections) — `server/time/tick_scheduler.py`
- **Emit one or more hour tick events if we've crossed boundaries.** (1 connections) — `server/time/tick_scheduler.py`
- **Sleep until the next Mythos hour boundary, respecting compression ratio.** (1 connections) — `server/time/tick_scheduler.py`
- **Publish the hourly tick event to the EventBus.** (1 connections) — `server/time/tick_scheduler.py`
- **Return the same datetime truncated down to the closest hour.** (1 connections) — `server/time/tick_scheduler.py`

## Relationships

- [emit close container event()](emit_close_container_event%28%29.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)

## Source Files

- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*