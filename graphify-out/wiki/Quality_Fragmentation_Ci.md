# Quality Fragmentation Ci

> 24 nodes · cohesion 0.19

## Key Concepts

- **quality_fragmentation_lizard.py** (23 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **LizardFunctionRow** (10 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **git_show_file()** (9 connections) — `scripts/ci/quality_fragmentation_core.py`
- **_check_head_rows()** (7 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **check_lizard_limits()** (7 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **parse_lizard_output()** (7 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_process_head_lizard()** (7 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **run_lizard_on_content()** (7 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_has_override_in_file()** (6 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **ChangedFile** (6 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_map_function_node_to_row()** (5 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_process_base_lizard()** (5 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **test_git_show_file_decodes_subprocess_output_as_utf8()** (4 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_run_cmd_decodes_subprocess_output_as_utf8()** (4 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **has_lizard_override()** (3 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_iter_lizard_function_maps()** (3 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_row_exceeds()** (3 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_row_reason()** (3 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_lizard_entries()** (2 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_to_int()** (2 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_to_str()** (2 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **MonkeyPatch** (2 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **Windows defaults text=True to cp1252; lizard/git can emit UTF-8 bytes (e.g. 0x8f** (1 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **git show of UTF-8 sources must not use the Windows cp1252 locale codec.** (1 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`

## Relationships

- [[AI Quality Guardrails]] (20 shared connections)
- [[Quality Fragmentation Guard]] (3 shared connections)
- [[CI Quality Scripts]] (1 shared connections)
- [[Dependency Risk Analyzer]] (1 shared connections)

## Source Files

- `scripts/ci/quality_fragmentation_core.py`
- `scripts/ci/quality_fragmentation_lizard.py`
- `server/tests/unit/test_quality_fragmentation_guard.py`

## Audit Trail

- EXTRACTED: 121 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
