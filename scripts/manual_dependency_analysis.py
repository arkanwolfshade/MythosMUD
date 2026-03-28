#!/usr/bin/env python3
"""
Manual Dependency Analysis for MythosMUD
Based on the data we collected from npm outdated and uv pip list --outdated
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import TypedDict

from utils.dependency_analysis_types import (
    AnalysisSnapshot,
    BreakingChange,
    DepInfo,
    PriorityItem,
    RiskAssessment,
    UpdateStrategy,
)
from utils.dependency_risk import assess_npm_risk, assess_python_risk, categorize_update


class NpmManualRow(TypedDict):
    current: str
    wanted: str
    latest: str


class PipManualRow(TypedDict):
    current: str
    latest: str


def _report_executive_and_stats(analysis: AnalysisSnapshot) -> str:
    us = analysis["update_strategy"]
    ra = analysis["risk_assessment"]
    uc = us["update_counts"]
    rc = us["risk_counts"]
    return f"""
# MythosMUD Dependency Upgrade Report
Generated: {analysis["timestamp"]}

## Executive Summary

**Overall Strategy**: {us["strategy"]}
**Priority Level**: {us["priority"]}
**Total Packages**: {us["total_packages"]}
**Overall Risk**: {ra["overall_risk"]}

## Update Statistics

### By Update Type
- Major Updates: {uc["major"]}
- Minor Updates: {uc["minor"]}
- Patch Updates: {uc["patch"]}

### By Risk Level
- High Risk: {rc["HIGH"]}
- Medium Risk: {rc["MEDIUM"]}
- Low Risk: {rc["LOW"]}

## Priority Update List

"""


def _risk_label(level: str) -> str:
    return {"HIGH": "[HIGH]", "MEDIUM": "[MED]", "LOW": "[LOW]"}.get(level, level)


def _update_label(u: str) -> str:
    return {"major": "(major)", "minor": "(minor)", "patch": "(patch)"}.get(u, u)


def _report_priority_block(order: list[PriorityItem]) -> str:
    lines: list[str] = []
    for i, item in enumerate(order[:15], 1):
        risk = _risk_label(item["risk_level"])
        ut = _update_label(item["update_type"])
        lines.append(
            f"""
### {i}. {item["package"]} {risk} {ut}
- **Current**: {item["current"]} -> **Latest**: {item["latest"]}
- **Update Type**: {item["update_type"]}
- **Risk Level**: {item["risk_level"]}
- **Ecosystem**: {item["ecosystem"]}
- **Priority Score**: {item["priority_score"]}
"""
        )
    return "".join(lines)


def _report_breaking_section(ra: RiskAssessment) -> str:
    if not ra["breaking_changes"]:
        return ""
    lines = ["\n## Breaking Changes Detected\n\n"]
    for change in ra["breaking_changes"]:
        lines.append(f"- **{change['package']}**: {change['current']} -> {change['latest']} ({change['ecosystem']})\n")
    return "".join(lines)


def _report_strategy_block(strategy: str) -> str:
    header = "\n## Detailed Recommendations\n\n"
    if strategy == "INCREMENTAL":
        return (
            header
            + """
### Incremental Upgrade Strategy
1. **Phase 1**: Update patch versions (low risk)
2. **Phase 2**: Update minor versions (medium risk)
3. **Phase 3**: Plan major version updates (high risk)
4. **Testing**: Full test suite after each phase
"""
        )
    if strategy == "BATCHED":
        return (
            header
            + """
### Batched Upgrade Strategy
1. **Batch 1**: All patch updates together
2. **Batch 2**: Minor updates in groups of 3-5
3. **Batch 3**: Major updates individually
4. **Testing**: Regression testing after each batch
"""
        )
    return (
        header
        + """
### Immediate Upgrade Strategy
1. **All Updates**: Can be applied immediately
2. **Testing**: Standard test suite
3. **Monitoring**: Watch for any issues
"""
    )


def _npm_upgrade_block(npm_packages: list[PriorityItem]) -> str:
    if not npm_packages:
        return ""
    lines = ["### NPM Package Updates\n\n", "```bash\n", "cd client\n"]
    for pkg in npm_packages[:5]:
        lines.append(f"npm install {pkg['package']}@{pkg['latest']}\n")
    lines.extend(["```\n\n"])
    return "".join(lines)


def _pip_upgrade_block(python_packages: list[PriorityItem]) -> str:
    if not python_packages:
        return ""
    lines = ["### Python Package Updates\n\n", "```bash\n"]
    for pkg in python_packages[:5]:
        lines.append(f"uv pip install {pkg['package']}=={pkg['latest']}\n")
    lines.extend(["```\n\n"])
    return "".join(lines)


def _report_upgrade_commands(priority_order: list[PriorityItem]) -> str:
    npm_packages = [p for p in priority_order if p["ecosystem"] == "npm"]
    python_packages = [p for p in priority_order if p["ecosystem"] == "pip"]
    return "\n## Upgrade Commands\n\n" + _npm_upgrade_block(npm_packages) + _pip_upgrade_block(python_packages)


def _report_testing_section() -> str:
    return """
## Testing Strategy

### Pre-Upgrade Testing
1. **Current State**: Run full test suite to establish baseline
2. **Backup**: Create git commit point before upgrades
3. **Documentation**: Note current working state

### Post-Upgrade Testing
1. **Unit Tests**: `make test` (from project root)
2. **Integration Tests**: `make test`
3. **Client Tests**: `cd client && npm test`
4. **Linting**: `make lint`
5. **Manual Testing**: Key user flows

### Rollback Plan
```bash
# If issues arise, rollback to previous state
git checkout HEAD~1
cd client && npm install
uv pip install -r requirements.txt  # or equivalent
```
"""


class ManualDependencyAnalyzer:
    """Manual dependency analysis based on collected data"""

    npm_outdated_data: dict[str, NpmManualRow]
    python_outdated_data: dict[str, PipManualRow]

    def __init__(self) -> None:
        self.npm_outdated_data = {
            "@eslint/js": {"current": "9.33.0", "wanted": "9.35.0", "latest": "9.35.0"},
            "@playwright/test": {"current": "1.54.2", "wanted": "1.55.0", "latest": "1.55.0"},
            "@tailwindcss/postcss": {"current": "4.1.12", "wanted": "4.1.13", "latest": "4.1.13"},
            "@testing-library/jest-dom": {"current": "6.7.0", "wanted": "6.8.0", "latest": "6.8.0"},
            "@types/node": {"current": "24.3.0", "wanted": "24.3.1", "latest": "24.3.1"},
            "@types/react": {"current": "19.1.10", "wanted": "19.1.12", "latest": "19.1.12"},
            "@types/react-dom": {"current": "19.1.7", "wanted": "19.1.9", "latest": "19.1.9"},
            "@vitejs/plugin-react": {"current": "5.0.0", "wanted": "5.0.2", "latest": "5.0.2"},
            "eslint": {"current": "9.33.0", "wanted": "9.35.0", "latest": "9.35.0"},
            "lucide-react": {"current": "0.540.0", "wanted": "0.540.0", "latest": "0.542.0"},
            "tailwindcss": {"current": "4.1.12", "wanted": "4.1.13", "latest": "4.1.13"},
            "typescript-eslint": {"current": "8.40.0", "wanted": "8.42.0", "latest": "8.42.0"},
            "vite": {"current": "7.1.3", "wanted": "7.1.4", "latest": "7.1.4"},
        }

        self.python_outdated_data = {
            "argon2-cffi": {"current": "23.1.0", "latest": "25.1.0"},
            "argon2-cffi-bindings": {"current": "21.2.0", "latest": "25.1.0"},
            "boltons": {"current": "21.0.0", "latest": "25.0.0"},
            "click": {"current": "8.1.8", "latest": "8.2.1"},
            "email-validator": {"current": "2.2.0", "latest": "2.3.0"},
            "exceptiongroup": {"current": "1.2.2", "latest": "1.3.0"},
            "glom": {"current": "22.1.0", "latest": "24.11.0"},
            "importlib-metadata": {"current": "7.1.0", "latest": "8.7.0"},
            "opentelemetry-api": {"current": "1.25.0", "latest": "1.36.0"},
            "opentelemetry-exporter-otlp-proto-common": {"current": "1.25.0", "latest": "1.36.0"},
            "opentelemetry-exporter-otlp-proto-http": {"current": "1.25.0", "latest": "1.36.0"},
            "opentelemetry-proto": {"current": "1.25.0", "latest": "1.36.0"},
            "opentelemetry-sdk": {"current": "1.25.0", "latest": "1.36.0"},
            "protobuf": {"current": "4.25.8", "latest": "6.32.0"},
            "pydantic-core": {"current": "2.33.2", "latest": "2.39.0"},
            "pytest": {"current": "8.4.1", "latest": "8.4.2"},
            "pytest-asyncio": {"current": "0.24.0", "latest": "1.1.0"},
            "pytest-cov": {"current": "6.2.1", "latest": "6.3.0"},
            "python-dotenv": {"current": "1.0.0", "latest": "1.1.1"},
            "rich": {"current": "13.5.3", "latest": "14.1.0"},
            "ruff": {"current": "0.12.5", "latest": "0.12.12"},
            "tomli": {"current": "2.0.2", "latest": "2.2.1"},
            "wcmatch": {"current": "8.5.2", "latest": "10.1"},
        }

    def _process_npm_dependencies(self) -> dict[str, DepInfo]:
        npm_deps: dict[str, DepInfo] = {}
        for pkg, info in self.npm_outdated_data.items():
            cur, lat = info["current"], info["latest"]
            npm_deps[pkg] = {
                "current": cur,
                "wanted": info["wanted"],
                "latest": lat,
                "ecosystem": "npm",
                "update_type": categorize_update(cur, lat),
                "risk_level": assess_npm_risk(pkg, cur, lat),
            }
        return npm_deps

    def _process_python_dependencies(self) -> dict[str, DepInfo]:
        python_deps: dict[str, DepInfo] = {}
        for pkg, info in self.python_outdated_data.items():
            cur, lat = info["current"], info["latest"]
            python_deps[pkg] = {
                "current": cur,
                "latest": lat,
                "ecosystem": "pip",
                "update_type": categorize_update(cur, lat),
                "risk_level": assess_python_risk(pkg, cur, lat),
            }
        return python_deps

    def _count_updates_and_risks(self, all_deps: dict[str, DepInfo]) -> tuple[dict[str, int], dict[str, int]]:
        update_counts = {"major": 0, "minor": 0, "patch": 0, "unknown": 0}
        risk_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}

        for dep_info in all_deps.values():
            update_counts[dep_info["update_type"]] += 1
            risk_counts[dep_info["risk_level"]] += 1

        return update_counts, risk_counts

    def _determine_update_strategy(self, update_counts: dict[str, int]) -> tuple[str, str]:
        if update_counts["major"] > 0:
            return "INCREMENTAL", "HIGH"
        if update_counts["minor"] > 3:
            return "BATCHED", "MEDIUM"
        return "IMMEDIATE", "LOW"

    def _calculate_priority_score(self, dep_info: DepInfo) -> int:
        priority_score = 0
        ut = dep_info["update_type"]
        if ut == "major":
            priority_score += 100
        elif ut == "minor":
            priority_score += 50
        elif ut == "patch":
            priority_score += 10

        rl = dep_info["risk_level"]
        if rl == "HIGH":
            priority_score += 20
        elif rl == "MEDIUM":
            priority_score += 10

        return priority_score

    def _create_priority_order(self, all_deps: dict[str, DepInfo]) -> list[PriorityItem]:
        priority_order: list[PriorityItem] = []
        for pkg_name, dep_info in all_deps.items():
            priority_score = self._calculate_priority_score(dep_info)
            priority_order.append(
                {
                    "package": pkg_name,
                    "priority_score": priority_score,
                    "update_type": dep_info["update_type"],
                    "risk_level": dep_info["risk_level"],
                    "current": dep_info["current"],
                    "latest": dep_info["latest"],
                    "ecosystem": dep_info["ecosystem"],
                }
            )

        priority_order.sort(key=lambda x: x["priority_score"], reverse=True)
        return priority_order

    def _identify_breaking_changes(self, all_deps: dict[str, DepInfo]) -> list[BreakingChange]:
        breaking_changes: list[BreakingChange] = []
        for pkg_name, dep_info in all_deps.items():
            if dep_info["update_type"] == "major":
                breaking_changes.append(
                    {
                        "package": pkg_name,
                        "current": dep_info["current"],
                        "latest": dep_info["latest"],
                        "ecosystem": dep_info["ecosystem"],
                    }
                )
        return breaking_changes

    def _determine_overall_risk(self, breaking_changes: list[BreakingChange]) -> str:
        if len(breaking_changes) > 2:
            return "HIGH"
        if len(breaking_changes) > 0:
            return "MEDIUM"
        return "LOW"

    def analyze_dependencies(self) -> AnalysisSnapshot:
        """Analyze all dependencies"""
        print("Analyzing MythosMUD dependencies...")

        npm_deps = self._process_npm_dependencies()
        python_deps = self._process_python_dependencies()
        all_deps: dict[str, DepInfo] = {**npm_deps, **python_deps}

        update_counts, risk_counts = self._count_updates_and_risks(all_deps)
        strategy, priority = self._determine_update_strategy(update_counts)
        priority_order = self._create_priority_order(all_deps)
        breaking_changes = self._identify_breaking_changes(all_deps)
        overall_risk = self._determine_overall_risk(breaking_changes)

        update_strategy: UpdateStrategy = {
            "strategy": strategy,
            "priority": priority,
            "update_counts": update_counts,
            "risk_counts": risk_counts,
            "total_packages": len(all_deps),
        }
        risk_assessment: RiskAssessment = {
            "breaking_changes": breaking_changes,
            "security_vulnerabilities": [],
            "compatibility_issues": [],
            "overall_risk": overall_risk,
        }

        return {
            "timestamp": datetime.now().isoformat(),
            "project": "MythosMUD",
            "client_dependencies": npm_deps,
            "server_dependencies": python_deps,
            "update_strategy": update_strategy,
            "risk_assessment": risk_assessment,
            "priority_order": priority_order,
        }

    def generate_report(self, analysis: AnalysisSnapshot) -> str:
        """Generate comprehensive upgrade report"""
        us = analysis["update_strategy"]
        parts = [
            _report_executive_and_stats(analysis),
            _report_priority_block(analysis["priority_order"]),
            _report_breaking_section(analysis["risk_assessment"]),
            _report_strategy_block(us["strategy"]),
            _report_upgrade_commands(analysis["priority_order"]),
            _report_testing_section(),
        ]
        return "".join(parts)


def main() -> int:
    """Main execution function"""
    analyzer = ManualDependencyAnalyzer()

    print("MythosMUD Manual Dependency Analysis")
    print("=" * 50)

    analysis = analyzer.analyze_dependencies()
    report = analyzer.generate_report(analysis)

    report_path = Path("dependency_upgrade_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        _ = f.write(report)

    print(f"\nReport saved to: {report_path}")
    print("\n" + report)

    return 0


if __name__ == "__main__":
    _ = main()
