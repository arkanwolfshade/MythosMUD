# Any

> 17 nodes

## Key Concepts

- **MythosTickScheduler** (18 connections) — `server/time/tick_scheduler.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._truncate_to_hour()** (4 connections) — `server/time/tick_scheduler.py`
- **.start()** (3 connections) — `server/time/tick_scheduler.py`
- **._sleep_until_next_hour()** (3 connections) — `server/time/tick_scheduler.py`
- **datetime** (3 connections)
- **.stop()** (2 connections) — `server/time/tick_scheduler.py`
- **Periodic dispatcher that emits Mythos hour ticks based on the accelerated chroni** (1 connections) — `server/time/tick_scheduler.py`
- **Register the scheduler loop with the task registry.** (1 connections) — `server/time/tick_scheduler.py`
- **Cancel the scheduler loop and wait for the task to exit.** (1 connections) — `server/time/tick_scheduler.py`
- **Background coroutine that emits ticks and waits for the next hour boundary.** (1 connections) — `server/time/tick_scheduler.py`
- **Emit one or more hour tick events if we've crossed boundaries.** (1 connections) — `server/time/tick_scheduler.py`
- **Sleep until the next Mythos hour boundary, respecting compression ratio.** (1 connections) — `server/time/tick_scheduler.py`
- **Publish the hourly tick event to the EventBus.** (1 connections) — `server/time/tick_scheduler.py`
- **Return the same datetime truncated down to the closest hour.** (1 connections) — `server/time/tick_scheduler.py`

## Relationships

- [test command parser](test_command_parser.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (2 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (2 shared connections)
- [monitoring](monitoring.md) (1 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)

## Source Files

- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 51 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*