# Community 640

> 26 nodes

## Key Concepts

- **create_app()** (14 connections) — `server/app/factory.py`
- **generate_openapi_spec.py** (7 connections) — `scripts/generate_openapi_spec.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **main()** (5 connections) — `scripts/generate_openapi_spec.py`
- **_render_tag_table()** (5 connections) — `scripts/generate_openapi_spec.py`
- **_update_tag_table_doc()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_openapi_spec()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_route_declared_tags()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_route_declared_tags()** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **_tag_descriptions()** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **test_openapi_tags_matches_route_declared_tags()** (2 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **test_create_app_auth_rate_limit_paths_match()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **Rewrite the generated tag table between its markers in the spec doc.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Tags actually declared by routes, in first-seen order. This is the authority.** (1 connections) — `scripts/generate_openapi_spec.py`
- **name -> description, from the spec's top-level tags block (OPENAPI_TAGS).** (1 connections) — `scripts/generate_openapi_spec.py`
- **Build the markdown table, failing loudly if a route tag has no description.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Mount all versioned API routers under /v1.** (1 connections) — `server/app/factory.py`
- **Create and configure the FastAPI application. This function sets up the FastAPI…** (1 connections) — `server/app/factory.py`
- **Unit tests guarding OPENAPI_TAGS against drift from route-declared tags. route-…** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **FastAPI's .openapi() is typed dict[str, Any]; erase that at the boundary.** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`
- *... and 1 more nodes in this community*

## Relationships

- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (8 shared connections)
- [Community 377](Community_377.md) (2 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/tests/unit/app/test_openapi_tags.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*