# scripts dependency analyzer

> 82 nodes

## Key Concepts

- **manual_dependency_analysis.py** (25 connections) — `scripts/manual_dependency_analysis.py`
- **DependencyAnalyzer** (21 connections) — `scripts/dependency_analyzer.py`
- **ManualDependencyAnalyzer** (20 connections) — `scripts/manual_dependency_analysis.py`
- **DepInfo** (20 connections) — `scripts/utils/dependency_analysis_types.py`
- **dependency_analyzer.py** (17 connections) — `scripts/dependency_analyzer.py`
- **PriorityItem** (13 connections) — `scripts/utils/dependency_analysis_types.py`
- **AnalysisSnapshot** (10 connections) — `scripts/utils/dependency_analysis_types.py`
- **.analyze_dependencies()** (10 connections) — `scripts/manual_dependency_analysis.py`
- **categorize_update()** (10 connections) — `scripts/utils/dependency_risk.py`
- **BreakingChange** (9 connections) — `scripts/utils/dependency_analysis_types.py`
- **.analyze_all_dependencies()** (9 connections) — `scripts/dependency_analyzer.py`
- **.generate_report()** (9 connections) — `scripts/manual_dependency_analysis.py`
- **dependency_analysis_types.py** (9 connections) — `scripts/utils/dependency_analysis_types.py`
- **RiskAssessment** (8 connections) — `scripts/utils/dependency_analysis_types.py`
- **UpdateStrategy** (7 connections) — `scripts/utils/dependency_analysis_types.py`
- **._analyze_python_dependencies()** (7 connections) — `scripts/dependency_analyzer.py`
- **.generate_report()** (7 connections) — `scripts/dependency_analyzer.py`
- **assess_npm_risk()** (7 connections) — `scripts/utils/dependency_risk.py`
- **assess_python_risk()** (7 connections) — `scripts/utils/dependency_risk.py`
- **_dep_info_from_npm_row()** (6 connections) — `scripts/dependency_analyzer.py`
- **._analyze_npm_dependencies()** (6 connections) — `scripts/dependency_analyzer.py`
- **TypedDict** (6 connections)
- **dependency_risk.py** (6 connections) — `scripts/utils/dependency_risk.py`
- **._assess_risks()** (5 connections) — `scripts/dependency_analyzer.py`
- **._determine_strategy()** (5 connections) — `scripts/dependency_analyzer.py`
- *... and 57 more nodes in this community*

## Relationships

- [scripts bandit](scripts_bandit.md) (4 shared connections)

## Source Files

- `scripts/dependency_analyzer.py`
- `scripts/manual_dependency_analysis.py`
- `scripts/utils/dependency_analysis_types.py`
- `scripts/utils/dependency_risk.py`

## Audit Trail

- EXTRACTED: 175 (90%)
- INFERRED: 20 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*