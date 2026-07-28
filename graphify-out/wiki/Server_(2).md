# Server (2)

> 45 nodes

## Key Concepts

- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **sanitize_detail_value()** (19 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_string()** (5 connections) — `server/legacy_error_sanitization.py`
- **_collect_safe_context_fields()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_html_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_text_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **_truncate_detail_string()** (4 connections) — `server/legacy_error_sanitization.py`
- **.test_sanitize_context_with_safe_fields()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_context_empty()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test sanitize_detail_value with string.** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_contains_sensitive_detail_pattern()** (3 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_list()** (3 connections) — `server/legacy_error_sanitization.py`
- **.testis_safe_detail_key_safe()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.testis_safe_detail_key_unsafe()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_string()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_long_string()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_traceback()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_int()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_dict()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_detail_value_list()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_context_none()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_html_content()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_html_content_with_allowed_tags()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_text_content()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_text_content_long()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 20 more nodes in this community*

## Relationships

- [Server Error Handlers](Server_Error_Handlers.md) (34 shared connections)
- [Server Utils (3)](Server_Utils_%283%29.md) (3 shared connections)
- [Server Persistence](Server_Persistence.md) (1 shared connections)
- [Server Utils](Server_Utils.md) (1 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (1 shared connections)
- [Server Api](Server_Api.md) (1 shared connections)

## Source Files

- `server/legacy_error_sanitization.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 139 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*