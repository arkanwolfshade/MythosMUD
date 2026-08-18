# server realtime memory monitor append

> 13 nodes

## Key Concepts

- **._run_idle_sampler()** (8 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_path()** (7 connections) — `server/realtime/memory_monitor.py`
- **.start_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_interval_seconds()** (6 connections) — `server/realtime/memory_monitor.py`
- **_append_sample_jsonl()** (5 connections) — `server/realtime/memory_monitor.py`
- **.is_idle_sampler_running()** (3 connections) — `server/realtime/memory_monitor.py`
- **Path** (2 connections)
- **Sample interval in seconds. Defaults to 60; values below 1 are raised to 1.** (1 connections) — `server/realtime/memory_monitor.py`
- **JSONL output path for idle samples.** (1 connections) — `server/realtime/memory_monitor.py`
- **Append one JSON object. Creates parent directories as needed.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return True when the opt-in sampler task is alive.** (1 connections) — `server/realtime/memory_monitor.py`
- **Start the JSONL sampler when enabled. No-op when disabled or already running.** (1 connections) — `server/realtime/memory_monitor.py`
- **Emit one JSONL sample per interval until cancelled or stopped.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [server realtime memory monitor memorymonitor](server_realtime_memory_monitor_memorymonitor.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server realtime memory monitor idle](server_realtime_memory_monitor_idle.md) (3 shared connections)
- [server realtime memory monitor collect](server_realtime_memory_monitor_collect.md) (2 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 28 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*