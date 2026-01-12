#!/usr/bin/env python3
"""
Manual Dependency Analysis for MythosMUD
Based on the data we collected from npm outdated and uv pip list --outdated
"""

from datetime import datetime
from pathlib import Path
from typing import Any

from packaging import version


class ManualDependencyAnalyzer:
    """Manual dependency analysis based on collected data"""

    def __init__(self):
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
            "requests": {"current": "2.32.4", "latest": "2.32.5"},
            "rich": {"current": "13.5.3", "latest": "14.1.0"},
            "ruff": {"current": "0.12.5", "latest": "0.12.12"},
            "tomli": {"current": "2.0.2", "latest": "2.2.1"},
            "wcmatch": {"current": "8.5.2", "latest": "10.1"},
        }

    def categorize_update(self, current_ver: str, latest_ver: str) -> str:
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

    def assess_npm_risk(self, package_name: str, current: str, latest: str) -> str:
        """Assess risk level for NPM package updates"""
        update_type = self.categorize_update(current, latest)

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

    def assess_python_risk(self, package_name: str, current: str, latest: str) -> str:
        """Assess risk level for Python package updates"""
        update_type = self.categorize_update(current, latest)

        # High-risk packages that require careful handling
        high_risk_packages = ["fastapi", "pydantic", "sqlalchemy", "uvicorn", "pytest", "pytest-asyncio", "structlog"]

        # Medium-risk packages
        medium_risk_packages = ["requests", "httpx", "python-jose", "argon2-cffi", "fastapi-users", "click", "nats-py"]

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

    def _process_npm_dependencies(self) -> dict[str, Any]:
        """Process NPM dependencies."""
        npm_deps = {}
        for pkg, info in self.npm_outdated_data.items():
            npm_deps[pkg] = {
                "current": info["current"],
                "wanted": info["wanted"],
                "latest": info["latest"],
                "ecosystem": "npm",
                "update_type": self.categorize_update(info["current"], info["latest"]),
                "risk_level": self.assess_npm_risk(pkg, info["current"], info["latest"]),
            }
        return npm_deps

    def _process_python_dependencies(self) -> dict[str, Any]:
        """Process Python dependencies."""
        python_deps = {}
        for pkg, info in self.python_outdated_data.items():
            python_deps[pkg] = {
                "current": info["current"],
                "latest": info["latest"],
                "ecosystem": "pip",
                "update_type": self.categorize_update(info["current"], info["latest"]),
                "risk_level": self.assess_python_risk(pkg, info["current"], info["latest"]),
            }
        return python_deps

    def _count_updates_and_risks(self, all_deps: dict[str, Any]) -> tuple[dict[str, int], dict[str, int]]:
        """Count dependencies by update type and risk level."""
        update_counts = {"major": 0, "minor": 0, "patch": 0, "unknown": 0}
        risk_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}

        for dep_info in all_deps.values():
            update_counts[dep_info["update_type"]] += 1
            risk_counts[dep_info["risk_level"]] += 1

        return update_counts, risk_counts

    def _determine_update_strategy(self, update_counts: dict[str, int]) -> tuple[str, str]:
        """Determine update strategy and priority."""
        if update_counts["major"] > 0:
            return "INCREMENTAL", "HIGH"
        elif update_counts["minor"] > 3:
            return "BATCHED", "MEDIUM"
        else:
            return "IMMEDIATE", "LOW"

    def _calculate_priority_score(self, dep_info: dict[str, Any]) -> int:
        """Calculate priority score for a dependency."""
        priority_score = 0

        if dep_info["update_type"] == "major":
            priority_score += 100
        elif dep_info["update_type"] == "minor":
            priority_score += 50
        elif dep_info["update_type"] == "patch":
            priority_score += 10

        if dep_info["risk_level"] == "HIGH":
            priority_score += 20
        elif dep_info["risk_level"] == "MEDIUM":
            priority_score += 10

        return priority_score

    def _create_priority_order(self, all_deps: dict[str, Any]) -> list[dict[str, Any]]:
        """Create priority order for dependencies."""
        priority_order = []
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

    def _identify_breaking_changes(self, all_deps: dict[str, Any]) -> list[dict[str, Any]]:
        """Identify breaking changes (major version updates)."""
        breaking_changes = []
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

    def _determine_overall_risk(self, breaking_changes: list[dict[str, Any]]) -> str:
        """Determine overall risk level."""
        if len(breaking_changes) > 2:
            return "HIGH"
        elif len(breaking_changes) > 0:
            return "MEDIUM"
        else:
            return "LOW"

    def _build_analysis_dict(
        self,
        npm_deps: dict[str, Any],
        python_deps: dict[str, Any],
        all_deps: dict[str, Any],
        update_counts: dict[str, int],
        risk_counts: dict[str, int],
        strategy: str,
        priority: str,
        breaking_changes: list[dict[str, Any]],
        overall_risk: str,
        priority_order: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Build the final analysis dictionary."""
        return {
            "timestamp": datetime.now().isoformat(),
            "project": "MythosMUD",
            "client_dependencies": npm_deps,
            "server_dependencies": python_deps,
            "update_strategy": {
                "strategy": strategy,
                "priority": priority,
                "update_counts": update_counts,
                "risk_counts": risk_counts,
                "total_packages": len(all_deps),
            },
            "risk_assessment": {"breaking_changes": breaking_changes, "overall_risk": overall_risk},
            "priority_order": priority_order,
        }

    def analyze_dependencies(self) -> dict[str, Any]:
        """Analyze all dependencies"""
        print("🔍 Analyzing MythosMUD dependencies...")

        npm_deps = self._process_npm_dependencies()
        python_deps = self._process_python_dependencies()
        all_deps = {**npm_deps, **python_deps}

        update_counts, risk_counts = self._count_updates_and_risks(all_deps)
        strategy, priority = self._determine_update_strategy(update_counts)
        priority_order = self._create_priority_order(all_deps)
        breaking_changes = self._identify_breaking_changes(all_deps)
        overall_risk = self._determine_overall_risk(breaking_changes)

        return self._build_analysis_dict(
            npm_deps, python_deps, all_deps, update_counts, risk_counts, strategy, priority, breaking_changes, overall_risk, priority_order
        )

    def generate_report(self, analysis: dict[str, Any]) -> str:
        """Generate comprehensive upgrade report"""
        report = f"""
# MythosMUD Dependency Upgrade Report
Generated: {analysis["timestamp"]}

## Executive Summary

**Overall Strategy**: {analysis["update_strategy"]["strategy"]}
**Priority Level**: {analysis["update_strategy"]["priority"]}
**Total Packages**: {analysis["update_strategy"]["total_packages"]}
**Overall Risk**: {analysis["risk_assessment"]["overall_risk"]}

## Update Statistics

### By Update Type
- Major Updates: {analysis["update_strategy"]["update_counts"]["major"]}
- Minor Updates: {analysis["update_strategy"]["update_counts"]["minor"]}
- Patch Updates: {analysis["update_strategy"]["update_counts"]["patch"]}

### By Risk Level
- High Risk: {analysis["update_strategy"]["risk_counts"]["HIGH"]}
- Medium Risk: {analysis["update_strategy"]["risk_counts"]["MEDIUM"]}
- Low Risk: {analysis["update_strategy"]["risk_counts"]["LOW"]}

## Priority Update List

"""

        for i, item in enumerate(analysis["priority_order"][:15], 1):
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
        if analysis["risk_assessment"]["breaking_changes"]:
            report += "\n## ⚠️ Breaking Changes Detected\n\n"
            for change in analysis["risk_assessment"]["breaking_changes"]:
                report += (
                    f"- **{change['package']}**: {change['current']} → {change['latest']} ({change['ecosystem']})\n"
                )

        # Detailed recommendations
        report += "\n## 📋 Detailed Recommendations\n\n"

        strategy = analysis["update_strategy"]["strategy"]
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

        # Specific upgrade commands
        report += "\n## 🚀 Upgrade Commands\n\n"

        # NPM upgrades
        npm_packages = [pkg for pkg in analysis["priority_order"] if pkg["ecosystem"] == "npm"]
        if npm_packages:
            report += "### NPM Package Updates\n\n"
            report += "```bash\n"
            report += "cd client\n"
            for pkg in npm_packages[:5]:  # Top 5 NPM packages
                report += f"npm install {pkg['package']}@{pkg['latest']}\n"
            report += "```\n\n"

        # Python upgrades
        python_packages = [pkg for pkg in analysis["priority_order"] if pkg["ecosystem"] == "pip"]
        if python_packages:
            report += "### Python Package Updates\n\n"
            report += "```bash\n"
            for pkg in python_packages[:5]:  # Top 5 Python packages
                report += f"uv pip install {pkg['package']}=={pkg['latest']}\n"
            report += "```\n\n"

        # Testing strategy
        report += "\n## 🧪 Testing Strategy\n\n"
        report += """
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

        return report


def main():
    """Main execution function"""
    analyzer = ManualDependencyAnalyzer()

    print("🔬 MythosMUD Manual Dependency Analysis")
    print("=" * 50)

    # Run analysis
    analysis = analyzer.analyze_dependencies()

    # Generate report
    report = analyzer.generate_report(analysis)

    # Save report
    report_path = Path("dependency_upgrade_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\n📄 Report saved to: {report_path}")
    print("\n" + report)

    return 0


if __name__ == "__main__":
    main()
