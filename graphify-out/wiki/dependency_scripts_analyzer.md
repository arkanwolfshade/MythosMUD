# dependency scripts analyzer

> 82 nodes

## Key Concepts

- **DependencyAnalyzer** (21 connections) — `scripts/dependency_analyzer.py`
- **ManualDependencyAnalyzer** (20 connections) — `scripts/manual_dependency_analysis.py`
- **DepInfo** (20 connections) — `scripts/utils/dependency_analysis_types.py`
- **manual_dependency_analysis.py** (16 connections) — `scripts/manual_dependency_analysis.py`
- **PriorityItem** (13 connections) — `scripts/utils/dependency_analysis_types.py`
- **.analyze_dependencies()** (11 connections) — `scripts/manual_dependency_analysis.py`
- **.analyze_all_dependencies()** (10 connections) — `scripts/dependency_analyzer.py`
- **.generate_report()** (10 connections) — `scripts/manual_dependency_analysis.py`
- **AnalysisSnapshot** (10 connections) — `scripts/utils/dependency_analysis_types.py`
- **.generate_report()** (9 connections) — `scripts/dependency_analyzer.py`
- **dependency_analysis_types.py** (9 connections) — `scripts/utils/dependency_analysis_types.py`
- **BreakingChange** (9 connections) — `scripts/utils/dependency_analysis_types.py`
- **NpmManualRow** (8 connections) — `scripts/manual_dependency_analysis.py`
- **PipManualRow** (8 connections) — `scripts/manual_dependency_analysis.py`
- **RiskAssessment** (8 connections) — `scripts/utils/dependency_analysis_types.py`
- **categorize_update()** (8 connections) — `scripts/utils/dependency_risk.py`
- **dependency_analyzer.py** (7 connections) — `scripts/dependency_analyzer.py`
- **._analyze_python_dependencies()** (7 connections) — `scripts/dependency_analyzer.py`
- **UpdateStrategy** (7 connections) — `scripts/utils/dependency_analysis_types.py`
- **_dep_info_from_npm_row()** (6 connections) — `scripts/dependency_analyzer.py`
- **._analyze_npm_dependencies()** (6 connections) — `scripts/dependency_analyzer.py`
- **main()** (6 connections) — `scripts/dependency_analyzer.py`
- **TypedDict** (6 connections)
- **dependency_risk.py** (6 connections) — `scripts/utils/dependency_risk.py`
- **_parse_npm_outdated_json()** (5 connections) — `scripts/dependency_analyzer.py`
- *... and 57 more nodes in this community*

## Relationships

- [auth dependencies rationale](auth_dependencies_rationale.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [scripts run guard](scripts_run_guard.md) (1 shared connections)

## Source Files

- `scripts/dependency_analyzer.py`
- `scripts/manual_dependency_analysis.py`
- `scripts/utils/dependency_analysis_types.py`
- `scripts/utils/dependency_risk.py`

## Audit Trail

- EXTRACTED: 315 (82%)
- INFERRED: 68 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*