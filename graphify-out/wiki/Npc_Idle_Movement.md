# Npc Idle Movement

> 9 nodes · cohesion 0.07

## Key Concepts

- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (2 connections) — `server/app/factory.py`
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Any** (1 connections) — `server/app/factory.py`
- **ASGIApp** (1 connections) — `server/middleware/comprehensive_logging.py`
- **ASGIApp** (1 connections) — `server/middleware/security_headers.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/middleware/comprehensive_logging.py`
- `server/middleware/security_headers.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*