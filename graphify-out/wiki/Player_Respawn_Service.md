# Player Respawn Service

> 46 nodes

## Key Concepts

- **sanitize_detail_value()** (19 connections) — `server/legacy_error_sanitization.py`
- **legacy_error_sanitization.py** (18 connections) — `server/legacy_error_sanitization.py`
- **is_safe_detail_key()** (10 connections) — `server/legacy_error_sanitization.py`
- **sanitize_safe_details()** (6 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_string()** (5 connections) — `server/legacy_error_sanitization.py`
- **_collect_safe_context_fields()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_context_metadata()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_html_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_text_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **_truncate_detail_string()** (4 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_dict()** (4 connections) — `server/legacy_error_sanitization.py`
- **_contains_sensitive_detail_pattern()** (3 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_list()** (3 connections) — `server/legacy_error_sanitization.py`
- **.test_sanitize_detail_value_string()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_long_string()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_traceback()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_int()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_dict()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_list()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_html_content()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_html_content_with_allowed_tags()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_text_content()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_text_content_long()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Return detail dict entries that use safe keys with sanitized values.** (2 connections) — `server/legacy_error_sanitization.py`
- **Sanitization helpers for legacy MythosMUD error responses.  Extracted from leg** (1 connections) — `server/legacy_error_sanitization.py`
- *... and 21 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (27 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (2 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (1 shared connections)

## Source Files

- `server/legacy_error_sanitization.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 146 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*