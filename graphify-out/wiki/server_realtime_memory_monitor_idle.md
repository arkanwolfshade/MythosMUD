# server realtime memory monitor idle

> 9 nodes

## Key Concepts

- **idle_sampler_enabled()** (5 connections) — `server/realtime/memory_monitor.py`
- **test_idle_sampler_interval_and_path()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_writes_jsonl_and_stops()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_disabled_by_default()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_stays_stopped_when_disabled()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **MonkeyPatch** (4 connections)
- **asyncio** (3 connections)
- **Path** (2 connections)
- **Return True when the opt-in idle sampler env flag is set.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [server realtime memory monitor memorymonitor](server_realtime_memory_monitor_memorymonitor.md) (9 shared connections)
- [server realtime memory monitor append](server_realtime_memory_monitor_append.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 21 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*