# Realtime Payload Optimizer

> 13 nodes · cohesion 0.22

## Key Concepts

- **PayloadOptimizer** (8 connections) — `server/realtime/payload_optimizer.py`
- **.optimize_payload()** (5 connections) — `server/realtime/payload_optimizer.py`
- **.compress_payload()** (4 connections) — `server/realtime/payload_optimizer.py`
- **.get_payload_size()** (4 connections) — `server/realtime/payload_optimizer.py`
- **Any** (4 connections) — `server/realtime/payload_optimizer.py`
- **.create_incremental_update()** (3 connections) — `server/realtime/payload_optimizer.py`
- **.__init__()** (2 connections) — `server/realtime/payload_optimizer.py`
- **Create an incremental update payload containing only changed fields.          Ar** (1 connections) — `server/realtime/payload_optimizer.py`
- **Optimizes payloads for WebSocket transmission.      Features:     - Size limit e** (1 connections) — `server/realtime/payload_optimizer.py`
- **Initialize the payload optimizer.          Args:             max_payload_size: M** (1 connections) — `server/realtime/payload_optimizer.py`
- **Calculate the size of a payload in bytes.          Args:             payload: Th** (1 connections) — `server/realtime/payload_optimizer.py`
- **Compress a large payload using gzip compression.          Args:             payl** (1 connections) — `server/realtime/payload_optimizer.py`
- **Optimize a payload by applying size limits and compression if needed.          A** (1 connections) — `server/realtime/payload_optimizer.py`

## Relationships

- [[NPC Admin API]] (2 shared connections)

## Source Files

- `server/realtime/payload_optimizer.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
