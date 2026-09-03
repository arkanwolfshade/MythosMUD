# Check Coverage Thresholds

> 11 nodes

## Key Concepts

- **main()** (6 connections) — `scripts/check_coverage_thresholds.py`
- **check_coverage_thresholds.py** (5 connections) — `scripts/check_coverage_thresholds.py`
- **_ensure_coverage_xml_or_exit()** (4 connections) — `scripts/check_coverage_thresholds.py`
- **parse_coverage_xml()** (4 connections) — `scripts/check_coverage_thresholds.py`
- **check_thresholds()** (3 connections) — `scripts/check_coverage_thresholds.py`
- **_print_results_and_exit()** (3 connections) — `scripts/check_coverage_thresholds.py`
- **Path** (3 connections)
- **Check files against their thresholds. Returns hard-fail messages.** (1 connections) — `scripts/check_coverage_thresholds.py`
- **Exit if coverage.xml not found. In pre-commit context, exit 0 so commits aren't…** (1 connections) — `scripts/check_coverage_thresholds.py`
- **Print coverage results and exit with appropriate code.** (1 connections) — `scripts/check_coverage_thresholds.py`
- **Parse coverage.xml and return file coverage percentages.** (1 connections) — `scripts/check_coverage_thresholds.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/check_coverage_thresholds.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*