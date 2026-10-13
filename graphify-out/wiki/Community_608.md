# Community 608

> 28 nodes

## Key Concepts

- **create_app()** (16 connections) — `server/app/factory.py`
- **generate_openapi_spec.py** (7 connections) — `scripts/generate_openapi_spec.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **main()** (5 connections) — `scripts/generate_openapi_spec.py`
- **_render_tag_table()** (5 connections) — `scripts/generate_openapi_spec.py`
- **_update_tag_table_doc()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
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
- **Create and configure the FastAPI application. This function sets up the FastAPI…** (1 connections) — `server/app/factory.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.…** (1 connections) — `server/main.py`
- *... and 3 more nodes in this community*

## Relationships

- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (7 shared connections)
- [Community 496](Community_496.md) (2 shared connections)
- [Community 351](Community_351.md) (2 shared connections)
- [Community 445](Community_445.md) (1 shared connections)
- [Community 317](Community_317.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`
- `server/tests/unit/app/test_openapi_tags.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 49 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*