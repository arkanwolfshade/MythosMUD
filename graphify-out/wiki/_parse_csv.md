# ._parse_csv

> 24 nodes

## Key Concepts

- **._parse_csv()** (10 connections) — `server/config/models/cors.py`
- **field_validator** (6 connections)
- **._clean_list_items()** (5 connections) — `server/config/models/cors.py`
- **._parse_json_array()** (5 connections) — `server/config/models/cors.py`
- **._validate_non_empty()** (5 connections) — `server/config/models/cors.py`
- **.parse_allow_headers()** (4 connections) — `server/config/models/cors.py`
- **.parse_allow_methods()** (4 connections) — `server/config/models/cors.py`
- **.parse_allow_origins()** (4 connections) — `server/config/models/cors.py`
- **._parse_comma_separated()** (4 connections) — `server/config/models/cors.py`
- **.parse_expose_headers()** (4 connections) — `server/config/models/cors.py`
- **.parse_max_age()** (3 connections) — `server/config/models/cors.py`
- **.validate_max_age()** (3 connections) — `server/config/models/cors.py`
- **Any** (1 connections)
- **Parse comma-separated string into cleaned list.** (1 connections) — `server/config/models/cors.py`
- **Parse comma separated strings or lists into a cleaned list of strings.** (1 connections) — `server/config/models/cors.py`
- **Parse allowed origins from various input formats.** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS allowed methods. Converts all methods to uppercase.** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS allowed headers.** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS max age value. Returns default 600 if invalid.** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS exposed headers. Allows empty list.** (1 connections) — `server/config/models/cors.py`
- **Validate that max_age is non-negative.** (1 connections) — `server/config/models/cors.py`
- **Validate that cleaned list is not empty if allow_empty is False.** (1 connections) — `server/config/models/cors.py`
- **Clean and filter list items, removing empty strings.** (1 connections) — `server/config/models/cors.py`
- **Parse JSON array string if it looks like one, otherwise return None.** (1 connections) — `server/config/models/cors.py`

## Relationships

- [AppConfig](AppConfig.md) (11 shared connections)

## Source Files

- `server/config/models/cors.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*