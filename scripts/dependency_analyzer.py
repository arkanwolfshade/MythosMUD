#!/usr/bin/env python3
"""
Dependency Analysis Tool for MythosMUD
Based on the comprehensive dependency upgrade strategy

This tool analyzes all project dependencies and provides upgrade recommendations
with risk assessment and migration guidance.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import cast

from utils.dependency_analysis_types import (
    AnalysisSnapshot,
    BreakingChange,
    DepInfo,
    PriorityItem,
    RiskAssessment,
    UpdateStrategy,
)
from utils.dependency_risk import assess_npm_risk, assess_python_risk, categorize_update
from utils.safe_subprocess import safe_run_static


def _dep_info_from_npm_row(pkg: str, info: dict[str, object]) -> DepInfo:
    """Build DepInfo from one npm outdated JSON row."""
    cur = info["current"]
    lat = info["latest"]
    cur_s = cur if isinstance(cur, str) else str(cur)
    lat_s = lat if isinstance(lat, str) else str(lat)
    wanted_o = info.get("wanted", cur_s)
    wanted_s = wanted_o if isinstance(wanted_o, str) else str(wanted_o)
    type_o = info.get("type", "dependencies")
    type_s = type_o if isinstance(type_o, str) else str(type_o)
    return {
        "current": cur_s,
        "wanted": wanted_s,
        "latest": lat_s,
        "type": type_s,
        "ecosystem": "npm",
        "update_type": categorize_update(cur_s, lat_s),
        "risk_level": assess_npm_risk(pkg, cur_s, lat_s),
    }


def _parse_npm_outdated_json(stdout: str) -> dict[str, DepInfo]:
    """Parse npm outdated --json stdout into DepInfo rows."""
    raw = cast(object, json.loads(stdout))
    if not isinstance(raw, dict):
        return {}
    npm_data = cast(dict[str, dict[str, object]], raw)
    return {pkg: _dep_info_from_npm_row(pkg, info) for pkg, info in npm_data.items()}


class DependencyAnalyzer:
    """Comprehensive dependency analysis and upgrade planning"""

    project_root: Path
    client_dir: Path
    analysis_results: AnalysisSnapshot | None

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root
        self.client_dir = project_root / "client"
        self.analysis_results = None

    def analyze_all_dependencies(self) -> AnalysisSnapshot:
        """Analyze all project dependencies"""
        print("🔍 Analyzing MythosMUD dependencies...")

        client_dependencies = self._analyze_npm_dependencies()
        server_dependencies = self._analyze_python_dependencies()
        update_strategy = self._determine_strategy(client_dependencies, server_dependencies)
        risk_assessment = self._assess_risks(client_dependencies, server_dependencies)
        priority_order = self._prioritize_updates(client_dependencies, server_dependencies)

        analysis: AnalysisSnapshot = {
            "timestamp": datetime.now().isoformat(),
            "project": "MythosMUD",
            "client_dependencies": client_dependencies,
            "server_dependencies": server_dependencies,
            "update_strategy": update_strategy,
            "risk_assessment": risk_assessment,
            "priority_order": priority_order,
        }

        self.analysis_results = analysis
        return analysis

    def _analyze_npm_dependencies(self) -> dict[str, DepInfo]:
        """Analyze NPM dependencies"""
        print("📦 Analyzing NPM dependencies...")

        try:
            # Run npm outdated using safe subprocess wrapper with static arguments
            result = safe_run_static(
                "npm",
                "outdated",
                "--json",
                cwd=self.client_dir,
                capture_output=True,
                text=True,
                check=False,
            )

            if result.returncode != 0 and result.stdout:
                return _parse_npm_outdated_json(result.stdout)
            print("✅ All NPM dependencies are up to date")
            return {}

        except Exception as e:
            print(f"❌ Error analyzing NPM dependencies: {e}")
            return {}

    def _analyze_python_dependencies(self) -> dict[str, DepInfo]:
        """Analyze Python dependencies"""
        print("🐍 Analyzing Python dependencies...")

        try:
            # Run uv pip list --outdated using safe subprocess wrapper with static arguments
            result = safe_run_static(
                "uv",
                "pip",
                "list",
                "--outdated",
                cwd=self.project_root,
                capture_output=True,
                text=True,
                check=False,
            )

            if result.returncode == 0 and result.stdout:
                # Parse the output manually since --format=json might not be available
                lines = result.stdout.strip().split("\n")
                deps: dict[str, DepInfo] = {}

                # Skip header lines
                for line in lines[2:]:  # Skip the header and separator lines
                    if line.strip():
                        parts = line.split()
                        if len(parts) >= 3:
                            pkg_name = parts[0]
                            current_version = parts[1]
                            latest_version = parts[2]

                            deps[pkg_name] = {
                                "current": current_version,
                                "latest": latest_version,
                                "ecosystem": "pip",
                                "update_type": categorize_update(current_version, latest_version),
                                "risk_level": assess_python_risk(pkg_name, current_version, latest_version),
                            }

                return deps
            print("✅ All Python dependencies are up to date")
            return {}

        except Exception as e:
            print(f"❌ Error analyzing Python dependencies: {e}")
            return {}

    def _determine_strategy(
        self,
        client_dependencies: dict[str, DepInfo],
        server_dependencies: dict[str, DepInfo],
    ) -> UpdateStrategy:
        """Determine overall upgrade strategy"""
        all_deps: dict[str, DepInfo] = {}
        all_deps.update(client_dependencies)
        all_deps.update(server_dependencies)

        # Count by update type
        update_counts = {"major": 0, "minor": 0, "patch": 0, "unknown": 0}
        risk_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}

        for dep_info in all_deps.values():
            update_counts[dep_info["update_type"]] += 1
            risk_counts[dep_info["risk_level"]] += 1

        # Determine strategy
        if update_counts["major"] > 0:
            strategy = "INCREMENTAL"
            priority = "HIGH"
        elif update_counts["minor"] > 3:
            strategy = "BATCHED"
            priority = "MEDIUM"
        else:
            strategy = "IMMEDIATE"
            priority = "LOW"

        return {
            "strategy": strategy,
            "priority": priority,
            "update_counts": update_counts,
            "risk_counts": risk_counts,
            "total_packages": len(all_deps),
        }

    def _assess_risks(
        self,
        client_dependencies: dict[str, DepInfo],
        server_dependencies: dict[str, DepInfo],
    ) -> RiskAssessment:
        """Assess overall project risks"""
        all_deps: dict[str, DepInfo] = {}
        all_deps.update(client_dependencies)
        all_deps.update(server_dependencies)

        breaking_changes: list[BreakingChange] = []
        risks: RiskAssessment = {
            "breaking_changes": breaking_changes,
            "security_vulnerabilities": [],
            "compatibility_issues": [],
            "overall_risk": "LOW",
        }

        # Check for potential breaking changes
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

        # Determine overall risk
        if len(risks["breaking_changes"]) > 2:
            risks["overall_risk"] = "HIGH"
        elif len(risks["breaking_changes"]) > 0:
            risks["overall_risk"] = "MEDIUM"

        return risks

    def _prioritize_updates(
        self,
        client_dependencies: dict[str, DepInfo],
        server_dependencies: dict[str, DepInfo],
    ) -> list[PriorityItem]:
        """Create prioritized list of updates"""
        all_deps: dict[str, DepInfo] = {}
        all_deps.update(client_dependencies)
        all_deps.update(server_dependencies)

        priority_order: list[PriorityItem] = []

        # Group by priority
        for pkg_name, dep_info in all_deps.items():
            priority_score = 0

            # Base score by update type
            if dep_info["update_type"] == "major":
                priority_score += 100
            elif dep_info["update_type"] == "minor":
                priority_score += 50
            elif dep_info["update_type"] == "patch":
                priority_score += 10

            # Adjust by risk level
            if dep_info["risk_level"] == "HIGH":
                priority_score += 20
            elif dep_info["risk_level"] == "MEDIUM":
                priority_score += 10

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

        # Sort by priority score (descending)
        priority_order.sort(key=lambda x: x["priority_score"], reverse=True)

        return priority_order

    def _report_executive_and_stats(self) -> str:
        """Build report header, executive summary, and update statistics section."""
        r = self.analysis_results
        if r is None:
            raise RuntimeError("analysis_results must be set before building report sections")
        us = r["update_strategy"]
        ra = r["risk_assessment"]
        return f"""# MythosMUD Dependency Upgrade Report

Generated: {r["timestamp"]}

## Executive Summary

**Overall Strategy**: {us["strategy"]}
**Priority Level**: {us["priority"]}
**Total Packages**: {us["total_packages"]}
**Overall Risk**: {ra["overall_risk"]}

## Update Statistics

### By Update Type

- Major Updates: {us["update_counts"]["major"]}
- Minor Updates: {us["update_counts"]["minor"]}
- Patch Updates: {us["update_counts"]["patch"]}

### By Risk Level

- High Risk: {us["risk_counts"]["HIGH"]}
- Medium Risk: {us["risk_counts"]["MEDIUM"]}
- Low Risk: {us["risk_counts"]["LOW"]}

## Priority Update List

"""

    def _report_priority_list(self, items: list[PriorityItem], top_n: int = 10) -> str:
        """Format the top N priority items as markdown."""
        risk_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}
        update_emoji = {"major": "⚡", "minor": "📈", "patch": "🔧"}
        parts: list[str] = []
        for i, item in enumerate(items[:top_n], 1):
            re_ = risk_emoji.get(item["risk_level"], "🟢")
            ue_ = update_emoji.get(item["update_type"], "🔧")
            parts.append(
                f"""### {i}. {item["package"]} {re_} {ue_}

- **Current**: {item["current"]} → **Latest**: {item["latest"]}
- **Update Type**: {item["update_type"]}
- **Risk Level**: {item["risk_level"]}
- **Ecosystem**: {item["ecosystem"]}
- **Priority Score**: {item["priority_score"]}

"""
            )
        return "".join(parts)

    def _report_breaking_changes(self, breaking_changes: list[BreakingChange]) -> str:
        """Format breaking changes section."""
        if not breaking_changes:
            return ""
        lines: list[str] = ["\n## Breaking Changes Detected\n\n"]
        for change in breaking_changes:
            lines.append(
                f"- **{change['package']}**: {change['current']} → {change['latest']} ({change['ecosystem']})\n"
            )
        return "".join(lines)

    def _report_recommendations(self, strategy: str) -> str:
        """Format recommendations section based on strategy."""
        if strategy == "INCREMENTAL":
            return """### Incremental Upgrade Strategy

1. **Phase 1**: Update patch versions (low risk)
2. **Phase 2**: Update minor versions (medium risk)
3. **Phase 3**: Plan major version updates (high risk)
4. **Testing**: Full test suite after each phase
"""
        if strategy == "BATCHED":
            return """### Batched Upgrade Strategy

1. **Batch 1**: All patch updates together
2. **Batch 2**: Minor updates in groups of 3-5
3. **Batch 3**: Major updates individually
4. **Testing**: Regression testing after each batch
"""
        return """### Immediate Upgrade Strategy

1. **All Updates**: Can be applied immediately
2. **Testing**: Standard test suite
3. **Monitoring**: Watch for any issues
"""

    def generate_report(self) -> str:
        """Generate comprehensive upgrade report."""
        if self.analysis_results is None:
            _ = self.analyze_all_dependencies()

        r = self.analysis_results
        if r is None:
            raise RuntimeError("analysis_results missing after analyze_all_dependencies")

        report = self._report_executive_and_stats()
        report += self._report_priority_list(r["priority_order"])
        report += self._report_breaking_changes(r["risk_assessment"]["breaking_changes"])
        report += "\n## Recommendations\n\n"
        report += self._report_recommendations(r["update_strategy"]["strategy"])
        return report


def main() -> int:
    """Main execution function"""
    project_root = Path(__file__).parent.parent
    analyzer = DependencyAnalyzer(project_root)

    print("🔬 MythosMUD Dependency Analysis")
    print("=" * 50)

    # Run analysis
    _ = analyzer.analyze_all_dependencies()

    # Generate report
    report = analyzer.generate_report()

    # Save report
    report_path = project_root / "dependency_upgrade_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        _ = f.write(report)

    print(f"\n📄 Report saved to: {report_path}")
    print("\n" + report)

    return 0


if __name__ == "__main__":
    sys.exit(main())
