# Dependency Risk Analyzer

> 82 nodes · cohesion 0.07

## Key Concepts

- **TypedDict** (42 connections)
- **DependencyAnalyzer** (21 connections) — `scripts/dependency_analyzer.py`
- **ManualDependencyAnalyzer** (20 connections) — `scripts/manual_dependency_analysis.py`
- **DepInfo** (19 connections) — `scripts/utils/dependency_analysis_types.py`
- **AnalysisSnapshot** (18 connections) — `scripts/utils/dependency_analysis_types.py`
- **BreakingChange** (18 connections) — `scripts/utils/dependency_analysis_types.py`
- **PriorityItem** (18 connections) — `scripts/utils/dependency_analysis_types.py`
- **RiskAssessment** (18 connections) — `scripts/utils/dependency_analysis_types.py`
- **UpdateStrategy** (18 connections) — `scripts/utils/dependency_analysis_types.py`
- **DepInfo** (13 connections) — `scripts/dependency_analyzer.py`
- **DepInfo** (12 connections) — `scripts/manual_dependency_analysis.py`
- **.analyze_dependencies()** (11 connections) — `scripts/manual_dependency_analysis.py`
- **PriorityItem** (11 connections) — `scripts/manual_dependency_analysis.py`
- **.analyze_all_dependencies()** (10 connections) — `scripts/dependency_analyzer.py`
- **.generate_report()** (9 connections) — `scripts/dependency_analyzer.py`
- **AnalysisSnapshot** (9 connections) — `scripts/manual_dependency_analysis.py`
- **dependency_analysis_types.py** (9 connections) — `scripts/utils/dependency_analysis_types.py`
- **Path** (8 connections) — `scripts/dependency_analyzer.py`
- **PriorityItem** (8 connections) — `scripts/dependency_analyzer.py`
- **NpmManualRow** (8 connections) — `scripts/manual_dependency_analysis.py`
- **PipManualRow** (8 connections) — `scripts/manual_dependency_analysis.py`
- **BreakingChange** (8 connections) — `scripts/manual_dependency_analysis.py`
- **categorize_update()** (8 connections) — `scripts/utils/dependency_risk.py`
- **dependency_analyzer.py** (7 connections) — `scripts/dependency_analyzer.py`
- **._analyze_python_dependencies()** (7 connections) — `scripts/dependency_analyzer.py`
- *... and 57 more nodes in this community*

## Relationships

- [[Manual Dependency Analysis]] (15 shared connections)
- [[Pydantic Error Handlers]] (7 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Zone Config Loader]] (4 shared connections)
- [[CI Quality Scripts]] (3 shared connections)
- [[Emote Schema Validator]] (3 shared connections)
- [[Database Manager Tests]] (2 shared connections)
- [[Player Respawn Events]] (2 shared connections)
- [[Inventory Service Helpers]] (2 shared connections)
- [[Quality Fragmentation Ci]] (1 shared connections)
- [[FastAPI App Factory]] (1 shared connections)
- [[Flee Command Tests]] (1 shared connections)

## Source Files

- `scripts/dependency_analyzer.py`
- `scripts/manual_dependency_analysis.py`
- `scripts/utils/dependency_analysis_types.py`
- `scripts/utils/dependency_risk.py`
- `server/error_types.py`
- `server/realtime/monitoring/performance_tracker.py`

## Audit Trail

- EXTRACTED: 316 (62%)
- INFERRED: 194 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
