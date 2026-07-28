# Nats Anti Patterns

> 11 nodes · cohesion 0.20

## Key Concepts

- **wrap_third_party_exception()** (6 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception()** (5 connections) — `server/utils/error_logging.py`
- **log_error_with_context()** (5 connections) — `server/utils/error_logging.py`
- **Any** (5 connections)
- **log_and_raise_http()** (4 connections) — `server/utils/error_logging.py`
- **Exception** (2 connections)
- **HTTPException** (1 connections)
- **Log an error with structured context. Delegates to log_structured_error.** (1 connections) — `server/utils/error_logging.py`
- **Create an HTTPException with proper logging and return it. Delegates to enhanced** (1 connections) — `server/utils/error_logging.py`
- **Log HTTP error and raise HTTPException. Delegates to enhanced.** (1 connections) — `server/utils/error_logging.py`
- **Wrap a third-party exception in a MythosMUD error. Delegates to enhanced.** (1 connections) — `server/utils/error_logging.py`

## Relationships

- [Realtime Connection Impl](Realtime_Connection_Impl.md) (5 shared connections)
- [Api Player](Api_Player.md) (4 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)

## Source Files

- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*