# Test validate command basics returns

> 21 nodes

## Key Concepts

- **validate.py** (11 connections) — `scripts/hads/validate.py`
- **validate()** (10 connections) — `scripts/hads/validate.py`
- **parse_manifest()** (4 connections) — `scripts/hads/validate.py`
- **validate_manifest()** (4 connections) — `scripts/hads/validate.py`
- **load()** (3 connections) — `scripts/hads/validate.py`
- **find_h1()** (3 connections) — `scripts/hads/validate.py`
- **find_version()** (3 connections) — `scripts/hads/validate.py`
- **find_manifest()** (3 connections) — `scripts/hads/validate.py`
- **find_first_content_section()** (3 connections) — `scripts/hads/validate.py`
- **find_bug_blocks()** (3 connections) — `scripts/hads/validate.py`
- **check_loose_tags()** (3 connections) — `scripts/hads/validate.py`
- **check_bug_content()** (3 connections) — `scripts/hads/validate.py`
- **Path** (3 connections)
- **Return line index of first H1, or None.** (1 connections) — `scripts/hads/validate.py`
- **Return line index of version declaration, or None.** (1 connections) — `scripts/hads/validate.py`
- **Return line index where AI manifest starts, or None.** (1 connections) — `scripts/hads/validate.py`
- **Return line index of first H2 that is NOT the manifest.** (1 connections) — `scripts/hads/validate.py`
- **Return list of BUG blocks with their content.** (1 connections) — `scripts/hads/validate.py`
- **Find tag-like patterns that are not properly formatted.** (1 connections) — `scripts/hads/validate.py`
- **Check that a [BUG] block contains required fields.** (1 connections) — `scripts/hads/validate.py`
- **Return non-comment, non-empty paths from a HADS manifest file.** (1 connections) — `scripts/hads/validate.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/hads/validate.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*