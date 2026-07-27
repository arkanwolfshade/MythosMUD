# Config App

> 6 nodes · cohesion 0.33

## Key Concepts

- **.__init__()** (4 connections) — `server/config/models/app.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **Initialize configuration and set environment variables for legacy compatibility.** (1 connections) — `server/config/models/app.py`
- **Return first set CORS origins env var to reduce CCN in _sanitize.** (1 connections) — `server/config/models/app.py`
- **Normalize environment variables so nested configs can parse them reliably.** (1 connections) — `server/config/models/app.py`

## Relationships

- [[Application Config Settings]] (4 shared connections)

## Source Files

- `server/config/models/app.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
