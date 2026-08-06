# schemas player respawn

> 8 nodes

## Key Concepts

- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **._get_project_root()** (4 connections) — `server/container/main.py`
- **._normalize_path_from_url_or_path()** (4 connections) — `server/container/main.py`
- **Path** (2 connections)
- **Return and cache the repository root directory.** (1 connections) — `server/container/main.py`
- **Delegate to shared util. Kept for backward compatibility.** (1 connections) — `server/container/main.py`
- **Path** (1 connections)
- **Normalize an item database override into a filesystem path.      DEPRECATED: Ite** (1 connections) — `server/container/utils.py`

## Relationships

- [nats services service](nats_services_service.md) (3 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/container/utils.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*