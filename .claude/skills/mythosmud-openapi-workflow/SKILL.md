---
name: mythosmud-openapi-workflow
description: Regenerate MythosMUD OpenAPI spec from FastAPI app: run generate_openapi_spec.py or make openapi-spec; output docs/openapi/openapi.json. Use when API routes or schemas change, or when the user asks to update the OpenAPI spec.
---

# MythosMUD OpenAPI Workflow

## When to Regenerate

Regenerate the spec when:

- Adding, changing, or removing API routes
- Changing request/response schemas (Pydantic models used in endpoints)
- User asks to update or regenerate the OpenAPI spec

## Commands

From project root:

```powershell
make openapi-spec
```

Or:

```powershell
uv run python scripts/generate_openapi_spec.py
```

## Requirements

- **Environment:** `.env.local` must exist with minimal config (e.g. `SERVER_PORT`, `DATABASE_URL`) so the FastAPI app can load. The script does not start the server; it instantiates the app and exports the schema.

## Output

- **Path:** `docs/openapi/openapi.json`
- **Format:** OpenAPI 3.x (generated from the FastAPI application at runtime).

## Reference

- Doc: [docs/architecture/API_OPENAPI_SPECIFICATION.md](../../docs/architecture/API_OPENAPI_SPECIFICATION.md)
- Script: [scripts/generate_openapi_spec.py](../../scripts/generate_openapi_spec.py)
