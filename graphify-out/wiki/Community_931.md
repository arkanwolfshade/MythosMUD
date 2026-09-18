# Community 931

> 16 nodes

## Key Concepts

- **._run_idle_sampler()** (8 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_path()** (7 connections) — `server/realtime/memory_monitor.py`
- **.start_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_interval_seconds()** (6 connections) — `server/realtime/memory_monitor.py`
- **_append_sample_jsonl()** (5 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_enabled()** (5 connections) — `server/realtime/memory_monitor.py`
- **test_idle_sampler_disabled_by_default()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **.is_idle_sampler_running()** (3 connections) — `server/realtime/memory_monitor.py`
- **Path** (2 connections)
- **Return True when the opt-in idle sampler env flag is set.** (1 connections) — `server/realtime/memory_monitor.py`
- **Sample interval in seconds. Defaults to 60; values below 1 are raised to 1.** (1 connections) — `server/realtime/memory_monitor.py`
- **JSONL output path for idle samples.** (1 connections) — `server/realtime/memory_monitor.py`
- **Append one JSON object. Creates parent directories as needed.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return True when the opt-in sampler task is alive.** (1 connections) — `server/realtime/memory_monitor.py`
- **Start the JSONL sampler when enabled. No-op when disabled or already running.** (1 connections) — `server/realtime/memory_monitor.py`
- **Emit one JSONL sample per interval until cancelled or stopped.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [Community 730](Community_730.md) (8 shared connections)
- [Community 42](Community_42.md) (4 shared connections)
- [Community 1306](Community_1306.md) (3 shared connections)
- [Community 1138](Community_1138.md) (1 shared connections)
- [Community 891](Community_891.md) (1 shared connections)
- [Community 57](Community_57.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 35 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*