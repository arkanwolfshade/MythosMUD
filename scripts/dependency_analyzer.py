#!/usr/bin/env python3
"""
Dependency Analysis Tool for MythosMUD
Based on the comprehensive dependency upgrade strategy

This tool analyzes all project dependencies and provides upgrade recommendations
with risk assessment and migration guidance.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from packaging import version


class DependencyAnalyzer:
    """Comprehensive dependency analysis and upgrade planning"""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.client_dir = project_root / "client"
        self.analysis_results = {}

    def analyze_all_dependencies(self) -> dict[str, Any]:
        """Analyze all project dependencies"""
        print("🔍 Analyzing MythosMUD dependencies...")

        analysis = {
            "timestamp": datetime.now().isoformat(),
            "project": "MythosMUD",
            "client_dependencies": self._analyze_npm_dependencies(),
            "server_dependencies": self._analyze_python_dependencies(),
            "update_strategy": self._determine_strategy(),
            "risk_assessment": self._assess_risks(),
            "priority_order": self._prioritize_updates(),
        }

        self.analysis_results = analysis
        return analysis

    def _analyze_npm_dependencies(self) -> dict[str, Any]:
        """Analyze NPM dependencies"""
        print("📦 Analyzing NPM dependencies...")

        try:
            # Run npm outdated
            result = subprocess.run(
                ["npm", "outdated", "--json"],
                cwd=self.client_dir,
                capture_output=True,
                text=True,
                shell=False,  # Use shell=True for Windows compatibility
            )

            if result.returncode != 0 and result.stdout:
                npm_data = json.loads(result.stdout)
                deps = {}

                for pkg, info in npm_data.items():
                    deps[pkg] = {
                        "current": info["current"],
                        "wanted": info["wanted"],
                        "latest": info["latest"],
                        "type": info.get("type", "dependencies"),
                        "ecosystem": "npm",
                        "update_type": self._categorize_update(info["current"], info["latest"]),
                        "risk_level": self._assess_npm_risk(pkg, info["current"], info["latest"]),
                    }

                return deps
            else:
                print("✅ All NPM dependencies are up to date")
                return {}

        except Exception as e:
            print(f"❌ Error analyzing NPM dependencies: {e}")
            return {}

    def _analyze_python_dependencies(self) -> dict[str, Any]:
        """Analyze Python dependencies"""
        print("🐍 Analyzing Python dependencies...")

        try:
            # Run uv pip list --outdated
            result = subprocess.run(
                ["uv", "pip", "list", "--outdated"],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                shell=False,  # Use shell=True for Windows compatibility
            )

            if result.returncode == 0 and result.stdout:
                # Parse the output manually since --format=json might not be available
                lines = result.stdout.strip().split("\n")
                deps = {}

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
                                "update_type": self._categorize_update(current_version, latest_version),
                                "risk_level": self._assess_python_risk(pkg_name, current_version, latest_version),
                            }

                return deps
            else:
                print("✅ All Python dependencies are up to date")
                return {}

        except Exception as e:
            print(f"❌ Error analyzing Python dependencies: {e}")
            return {}

    def _categorize_update(self, current_ver: str, latest_ver: str) -> str:
        """Categorize update by semver"""
        try:
            current = version.parse(current_ver)
            latest = version.parse(latest_ver)

            if latest.major > current.major:
                return "major"
            elif latest.minor > current.minor:
                return "minor"
            elif latest.micro > current.micro:
                return "patch"
            else:
                return "none"
        except Exception:
            return "unknown"

    def _assess_npm_risk(self, package_name: str, current: str, latest: str) -> str:
        """Assess risk level for NPM package updates"""
        update_type = self._categorize_update(current, latest)

        # High-risk packages that require careful handling
        high_risk_packages = [
            "react",
            "react-dom",
            "typescript",
            "vite",
            "eslint",
            "@types/react",
            "@types/react-dom",
            "tailwindcss",
        ]

        # Medium-risk packages
        medium_risk_packages = [
            "@playwright/test",
            "@testing-library/react",
            "prettier",
            "typescript-eslint",
            "@vitejs/plugin-react",
        ]

        if update_type == "major":
            return "HIGH"
        elif update_type == "minor" and package_name in high_risk_packages:
            return "MEDIUM"
        elif update_type == "minor" and package_name in medium_risk_packages:
            return "LOW"
        elif update_type == "patch":
            return "LOW"
        else:
            return "LOW"

    def _assess_python_risk(self, package_name: str, current: str, latest: str) -> str:
        """Assess risk level for Python package updates"""
        update_type = self._categorize_update(current, latest)

        # High-risk packages that require careful handling
        high_risk_packages = ["fastapi", "pydantic", "sqlalchemy", "uvicorn", "pytest", "pytest-asyncio", "structlog"]

        # Medium-risk packages
        medium_risk_packages = ["httpx", "python-jose", "argon2-cffi", "fastapi-users", "click", "nats-py"]

        if update_type == "major":
            return "HIGH"
        elif update_type == "minor" and package_name in high_risk_packages:
            return "MEDIUM"
        elif update_type == "minor" and package_name in medium_risk_packages:
            return "LOW"
        elif update_type == "patch":
            return "LOW"
        else:
            return "LOW"

    def _determine_strategy(self) -> dict[str, Any]:
        """Determine overall upgrade strategy"""
        all_deps = {}
        all_deps.update(self.analysis_results.get("client_dependencies", {}))
        all_deps.update(self.analysis_results.get("server_dependencies", {}))

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

    def _assess_risks(self) -> dict[str, Any]:
        """Assess overall project risks"""
        all_deps = {}
        all_deps.update(self.analysis_results.get("client_dependencies", {}))
        all_deps.update(self.analysis_results.get("server_dependencies", {}))

        risks = {
            "breaking_changes": [],
            "security_vulnerabilities": [],
            "compatibility_issues": [],
            "overall_risk": "LOW",
        }

        # Check for potential breaking changes
        for pkg_name, dep_info in all_deps.items():
            if dep_info["update_type"] == "major":
                risks["breaking_changes"].append(
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

    def _prioritize_updates(self) -> list[dict[str, Any]]:
        """Create prioritized list of updates"""
        all_deps = {}
        all_deps.update(self.analysis_results.get("client_dependencies", {}))
        all_deps.update(self.analysis_results.get("server_dependencies", {}))

        # Sort by priority
        priority_order = []

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

    def generate_report(self) -> str:
        """Generate comprehensive upgrade report"""
        if not self.analysis_results:
            self.analyze_all_dependencies()

        report = f"""
# MythosMUD Dependency Upgrade Report
Generated: {self.analysis_results["timestamp"]}

## Executive Summary

**Overall Strategy**: {self.analysis_results["update_strategy"]["strategy"]}
**Priority Level**: {self.analysis_results["update_strategy"]["priority"]}
**Total Packages**: {self.analysis_results["update_strategy"]["total_packages"]}
**Overall Risk**: {self.analysis_results["risk_assessment"]["overall_risk"]}

## Update Statistics

### By Update Type
- Major Updates: {self.analysis_results["update_strategy"]["update_counts"]["major"]}
- Minor Updates: {self.analysis_results["update_strategy"]["update_counts"]["minor"]}
- Patch Updates: {self.analysis_results["update_strategy"]["update_counts"]["patch"]}

### By Risk Level
- High Risk: {self.analysis_results["update_strategy"]["risk_counts"]["HIGH"]}
- Medium Risk: {self.analysis_results["update_strategy"]["risk_counts"]["MEDIUM"]}
- Low Risk: {self.analysis_results["update_strategy"]["risk_counts"]["LOW"]}

## Priority Update List

"""

        for i, item in enumerate(self.analysis_results["priority_order"][:10], 1):
            risk_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}[item["risk_level"]]
            update_emoji = {"major": "⚡", "minor": "📈", "patch": "🔧"}[item["update_type"]]

            report += f"""
### {i}. {item["package"]} {risk_emoji} {update_emoji}
- **Current**: {item["current"]} → **Latest**: {item["latest"]}
- **Update Type**: {item["update_type"]}
- **Risk Level**: {item["risk_level"]}
- **Ecosystem**: {item["ecosystem"]}
- **Priority Score**: {item["priority_score"]}
"""

        # Breaking changes section
        if self.analysis_results["risk_assessment"]["breaking_changes"]:
            report += "\n## ⚠️ Breaking Changes Detected\n\n"
            for change in self.analysis_results["risk_assessment"]["breaking_changes"]:
                report += (
                    f"- **{change['package']}**: {change['current']} → {change['latest']} ({change['ecosystem']})\n"
                )

        # Recommendations
        report += "\n## 📋 Recommendations\n\n"

        strategy = self.analysis_results["update_strategy"]["strategy"]
        if strategy == "INCREMENTAL":
            report += """
### Incremental Upgrade Strategy
1. **Phase 1**: Update patch versions (low risk)
2. **Phase 2**: Update minor versions (medium risk)
3. **Phase 3**: Plan major version updates (high risk)
4. **Testing**: Full test suite after each phase
"""
        elif strategy == "BATCHED":
            report += """
### Batched Upgrade Strategy
1. **Batch 1**: All patch updates together
2. **Batch 2**: Minor updates in groups of 3-5
3. **Batch 3**: Major updates individually
4. **Testing**: Regression testing after each batch
"""
        else:
            report += """
### Immediate Upgrade Strategy
1. **All Updates**: Can be applied immediately
2. **Testing**: Standard test suite
3. **Monitoring**: Watch for any issues
"""

        return report


def main():
    """Main execution function"""
    project_root = Path(__file__).parent.parent
    analyzer = DependencyAnalyzer(project_root)

    print("🔬 MythosMUD Dependency Analysis")
    print("=" * 50)

    # Run analysis
    analyzer.analyze_all_dependencies()

    # Generate report
    report = analyzer.generate_report()

    # Save report
    report_path = project_root / "dependency_upgrade_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\n📄 Report saved to: {report_path}")
    print("\n" + report)

    return 0


if __name__ == "__main__":
    sys.exit(main())
