# config models cors

> 28 nodes

## Key Concepts

- **CORSConfig** (20 connections) — `server/config/models/cors.py`
- **._parse_csv()** (10 connections) — `server/config/models/cors.py`
- **._validate_non_empty()** (5 connections) — `server/config/models/cors.py`
- **._clean_list_items()** (5 connections) — `server/config/models/cors.py`
- **._parse_json_array()** (5 connections) — `server/config/models/cors.py`
- **._parse_comma_separated()** (4 connections) — `server/config/models/cors.py`
- **.parse_allow_origins()** (3 connections) — `server/config/models/cors.py`
- **.parse_allow_methods()** (3 connections) — `server/config/models/cors.py`
- **.parse_allow_headers()** (3 connections) — `server/config/models/cors.py`
- **.parse_expose_headers()** (3 connections) — `server/config/models/cors.py`
- **._validate_and_warn_wildcards()** (2 connections) — `server/config/models/cors.py`
- **.parse_max_age()** (2 connections) — `server/config/models/cors.py`
- **.validate_max_age()** (2 connections) — `server/config/models/cors.py`
- **BaseSettings** (1 connections)
- **Any** (1 connections)
- **Cross-origin resource sharing configuration.      Configuration precedence (high** (1 connections) — `server/config/models/cors.py`
- **Validate CORS configuration and warn about wildcard origins.** (1 connections) — `server/config/models/cors.py`
- **Validate that cleaned list is not empty if allow_empty is False.** (1 connections) — `server/config/models/cors.py`
- **Clean and filter list items, removing empty strings.** (1 connections) — `server/config/models/cors.py`
- **Parse JSON array string if it looks like one, otherwise return None.** (1 connections) — `server/config/models/cors.py`
- **Parse comma-separated string into cleaned list.** (1 connections) — `server/config/models/cors.py`
- **Parse comma separated strings or lists into a cleaned list of strings.** (1 connections) — `server/config/models/cors.py`
- **Parse allowed origins from various input formats.** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS allowed methods. Converts all methods to uppercase.** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS allowed headers.** (1 connections) — `server/config/models/cors.py`
- *... and 3 more nodes in this community*

## Relationships

- [config models rationale](config_models_rationale.md) (4 shared connections)
- [app factory rationale](app_factory_rationale.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/config/models/cors.py`

## Audit Trail

- EXTRACTED: 81 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*