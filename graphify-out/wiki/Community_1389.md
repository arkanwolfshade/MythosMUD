# Community 1389

> 7 nodes

## Key Concepts

- **_extract_bearer_token()** (5 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (5 connections) — `server/api/real_time.py`
- **test_extract_bearer_token_empty()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_extract_bearer_token_last_part()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_subprotocol_token()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Extract bearer token from parsed subprotocol parts. If 'bearer' marker is…** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol header. Example formats: "bearer,…** (1 connections) — `server/api/real_time.py`

## Relationships

- [Community 586](Community_586.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 643](Community_643.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*