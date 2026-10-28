# Test Suite Refactoring Plan

> 47 nodes · cohesion 0.12

## Key Concepts

- **quality_fragmentation_lizard.py** (25 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **quality_fragmentation_guard.py** (24 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **quality_fragmentation_core.py** (18 connections) — `scripts/ci/quality_fragmentation_core.py`
- **ChangedFile** (11 connections) — `scripts/ci/quality_fragmentation_core.py`
- **check_ai_guardrails()** (9 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **git_show_file()** (9 connections) — `scripts/ci/quality_fragmentation_core.py`
- **GuardContext** (9 connections) — `scripts/ci/quality_fragmentation_core.py`
- **run_cmd()** (9 connections) — `scripts/ci/quality_fragmentation_core.py`
- **check_fragmentation_trends()** (9 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **quality_fragmentation_trends.py** (9 connections) — `scripts/ci/quality_fragmentation_trends.py`
- **main()** (8 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **_check_head_rows()** (8 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **LizardFunctionRow** (8 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_process_head_lizard()** (8 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **build_context()** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **is_safe_git_ref()** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **check_lizard_limits()** (7 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_has_override_in_file()** (7 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **parse_lizard_output()** (7 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **run_lizard_on_content()** (7 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_process_base_lizard()** (6 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **is_code_file()** (5 connections) — `scripts/ci/quality_fragmentation_core.py`
- **parse_args()** (5 connections) — `scripts/ci/quality_fragmentation_core.py`
- **file_nloc_failures()** (5 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_map_function_node_to_row()** (5 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- *... and 22 more nodes in this community*

## Relationships

- [test_aggressive_mob_npc.py](test_aggressive_mob_npc.py.md) (14 shared connections)
- [EventPublisher](EventPublisher.md) (11 shared connections)
- [format_occupant_display_name](format_occupant_display_name.md) (4 shared connections)
- [CorruptionTierCache](CorruptionTierCache.md) (1 shared connections)

## Source Files

- `scripts/ci/quality_fragmentation_ai_guardrails.py`
- `scripts/ci/quality_fragmentation_core.py`
- `scripts/ci/quality_fragmentation_guard.py`
- `scripts/ci/quality_fragmentation_lizard.py`
- `scripts/ci/quality_fragmentation_trends.py`

## Audit Trail

- EXTRACTED: 141 (87%)
- INFERRED: 21 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*