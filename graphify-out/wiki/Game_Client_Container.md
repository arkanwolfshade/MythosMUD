# Game Client Container

> 28 nodes · cohesion 0.04

## Key Concepts

- **sanitize_detail_value()** (19 connections) — `server/legacy_error_sanitization.py`
- **legacy_error_sanitization.py** (18 connections) — `server/legacy_error_sanitization.py`
- **sanitize_context()** (11 connections) — `server/legacy_error_sanitization.py`
- **is_safe_detail_key()** (10 connections) — `server/legacy_error_sanitization.py`
- **sanitize_safe_details()** (6 connections) — `server/legacy_error_sanitization.py`
- **_collect_safe_context_fields()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_context_metadata()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_string()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_html_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **sanitize_text_content()** (5 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_dict()** (4 connections) — `server/legacy_error_sanitization.py`
- **_truncate_detail_string()** (4 connections) — `server/legacy_error_sanitization.py`
- **_contains_sensitive_detail_pattern()** (3 connections) — `server/legacy_error_sanitization.py`
- **_sanitize_detail_list()** (3 connections) — `server/legacy_error_sanitization.py`
- **Return detail dict entries that use safe keys with sanitized values.** (2 connections) — `server/legacy_error_sanitization.py`
- **Sanitization helpers for legacy MythosMUD error responses.  Extracted from leg** (1 connections) — `server/legacy_error_sanitization.py`
- **Sanitize dictionary detail values, keeping only safe keys.** (1 connections) — `server/legacy_error_sanitization.py`
- **Sanitize each element in a list detail value.** (1 connections) — `server/legacy_error_sanitization.py`
- **Sanitize a detail value to prevent information exposure.      Uses bleach for** (1 connections) — `server/legacy_error_sanitization.py`
- **Collect sanitized safe fields and timestamp from error context.** (1 connections) — `server/legacy_error_sanitization.py`
- **Check if a detail key is safe to expose to users.      Args:         key: The** (1 connections) — `server/legacy_error_sanitization.py`
- **Sanitize context metadata, keeping only safe keys.** (1 connections) — `server/legacy_error_sanitization.py`
- **Sanitize error context to prevent information exposure.      Args:         co** (1 connections) — `server/legacy_error_sanitization.py`
- **Sanitize HTML content to prevent XSS attacks.      This is a general utility f** (1 connections) — `server/legacy_error_sanitization.py`
- **Sanitize plain text content to prevent information exposure.      Args:** (1 connections) — `server/legacy_error_sanitization.py`
- *... and 3 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (11 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)

## Source Files

- `server/legacy_error_sanitization.py`

## Audit Trail

- EXTRACTED: 118 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*