# command commands talk

> 12 nodes

## Key Concepts

- **create_app()** (14 connections) — `server/app/factory.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **main()** (4 connections) — `server/main.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Create and configure the FastAPI application.      This function sets up the Fas** (1 connections) — `server/app/factory.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.** (1 connections) — `server/main.py`

## Relationships

- [app factory rationale](app_factory_rationale.md) (5 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [System Metrics](System_Metrics.md) (1 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (1 shared connections)
- [middleware security headers](middleware_security_headers.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 37 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*