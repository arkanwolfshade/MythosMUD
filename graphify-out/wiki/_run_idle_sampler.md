# ._run_idle_sampler

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

- [MemoryMonitor](MemoryMonitor.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [idle_sampler_enabled](idle_sampler_enabled.md) (3 shared connections)
- [IdleMemorySample](IdleMemorySample.md) (1 shared connections)
- [collect_idle_memory_sample](collect_idle_memory_sample.md) (1 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 28 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*