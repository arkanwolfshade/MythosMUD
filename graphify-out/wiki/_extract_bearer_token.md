# _extract_bearer_token

> 8 nodes

## Key Concepts

- **_extract_bearer_token()** (6 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (5 connections) — `server/api/real_time.py`
- **test_extract_bearer_token_empty()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_extract_bearer_token_last_part()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_extract_bearer_token_with_marker()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_subprotocol_token()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Parse token from WebSocket subprotocol header. Example formats: "bearer,…** (1 connections) — `server/api/real_time.py`
- **Extract bearer token from parsed subprotocol parts. If 'bearer' marker is…** (1 connections) — `server/api/real_time.py`

## Relationships

- [test_real_time_helpers.py](test_real_time_helpers.py.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [_resolve_player_id](_resolve_player_id.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*