# Dependency Risk Analyzer

> 63 nodes · cohesion 0.06

## Key Concepts

- **DependencyAnalyzer** (21 connections) — `scripts/dependency_analyzer.py`
- **ManualDependencyAnalyzer** (20 connections) — `scripts/manual_dependency_analysis.py`
- **manual_dependency_analysis.py** (16 connections) — `scripts/manual_dependency_analysis.py`
- **.analyze_dependencies()** (11 connections) — `scripts/manual_dependency_analysis.py`
- **.analyze_all_dependencies()** (10 connections) — `scripts/dependency_analyzer.py`
- **.generate_report()** (10 connections) — `scripts/manual_dependency_analysis.py`
- **.generate_report()** (9 connections) — `scripts/dependency_analyzer.py`
- **Path** (8 connections) — `scripts/dependency_analyzer.py`
- **NpmManualRow** (8 connections) — `scripts/manual_dependency_analysis.py`
- **PipManualRow** (8 connections) — `scripts/manual_dependency_analysis.py`
- **dependency_analyzer.py** (7 connections) — `scripts/dependency_analyzer.py`
- **._analyze_python_dependencies()** (7 connections) — `scripts/dependency_analyzer.py`
- **_dep_info_from_npm_row()** (6 connections) — `scripts/dependency_analyzer.py`
- **._analyze_npm_dependencies()** (6 connections) — `scripts/dependency_analyzer.py`
- **main()** (6 connections) — `scripts/dependency_analyzer.py`
- **._assess_risks()** (5 connections) — `scripts/dependency_analyzer.py`
- **._determine_strategy()** (5 connections) — `scripts/dependency_analyzer.py`
- **._prioritize_updates()** (5 connections) — `scripts/dependency_analyzer.py`
- **_parse_npm_outdated_json()** (5 connections) — `scripts/dependency_analyzer.py`
- **main()** (5 connections) — `scripts/manual_dependency_analysis.py`
- **._create_priority_order()** (5 connections) — `scripts/manual_dependency_analysis.py`
- **._process_npm_dependencies()** (5 connections) — `scripts/manual_dependency_analysis.py`
- **._process_python_dependencies()** (5 connections) — `scripts/manual_dependency_analysis.py`
- **_report_priority_block()** (5 connections) — `scripts/manual_dependency_analysis.py`
- **_report_upgrade_commands()** (5 connections) — `scripts/manual_dependency_analysis.py`
- *... and 38 more nodes in this community*

## Relationships

- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)

## Source Files

- `scripts/dependency_analyzer.py`
- `scripts/manual_dependency_analysis.py`

## Audit Trail

- EXTRACTED: 243 (88%)
- INFERRED: 32 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*