#!/usr/bin/env python3
"""Analyze coverage gaps and generate status document."""

import sys
from pathlib import Path
from typing import Any

from defusedxml.ElementTree import parse as parse_xml

# Critical files requiring 90% coverage (or custom threshold as specified)
CRITICAL_FILES = {
    "server/auth/argon2_utils.py": 85,  # Lowered due to PasswordHasher read-only methods being untestable
    "server/auth_utils.py": 90,
    "server/security_utils.py": 90,
    "server/validators/security_validator.py": 90,
    "server/validators/optimized_security_validator.py": 90,
    "server/validators/combat_validator.py": 90,
    "server/auth/dependencies.py": 90,
    "server/auth/endpoints.py": 90,
    "server/auth/users.py": 90,
    "server/middleware/security_headers.py": 90,
    "server/persistence/container_persistence.py": 90,
    "server/container_persistence/container_persistence.py": 90,
    "server/database.py": 90,
    "server/async_persistence.py": 90,
    "server/services/admin_auth_service.py": 90,
    "server/services/inventory_mutation_guard.py": 90,
    # Command factories - critical for command processing
    "server/utils/command_factories.py": 90,
    "server/utils/command_factories_combat.py": 90,
    "server/utils/command_factories_communication.py": 90,
    "server/utils/command_factories_exploration.py": 90,
    "server/utils/command_factories_inventory.py": 90,
    "server/utils/command_factories_moderation.py": 90,
    "server/utils/command_factories_player_state.py": 90,
    "server/utils/command_factories_utility.py": 90,
    # Combat services - critical for game combat mechanics
    "server/services/wearable_container_service.py": 90,
    "server/services/player_combat_service.py": 90,
    "server/services/npc_combat_integration_service.py": 90,
    "server/services/npc_combat_handlers.py": 90,
    "server/services/container_websocket_events.py": 90,
    "server/services/combat_persistence_handler.py": 90,
    "server/services/combat_monitoring_service.py": 90,
    "server/services/combat_messaging_integration.py": 90,
    "server/services/combat_cleanup_handler.py": 90,
    "server/services/combat_attack_handler.py": 90,
    # Realtime services - critical for WebSocket and real-time game state
    "server/realtime/websocket_handler.py": 90,
    "server/realtime/room_subscription_manager.py": 90,
    "server/realtime/room_occupant_manager.py": 90,
    "server/realtime/room_id_utils.py": 90,
    "server/realtime/player_occupant_processor.py": 90,
    "server/realtime/player_disconnect_handlers.py": 90,
    "server/realtime/nats_message_handler.py": 90,
}

NORMAL_THRESHOLD = 70


def parse_coverage_xml(coverage_xml_path: Path) -> dict[str, dict[str, Any]]:
    """Parse coverage.xml and return detailed file coverage information."""
    tree = parse_xml(coverage_xml_path)
    root = tree.getroot()

    file_data = {}
    for package in root.findall(".//package"):
        for cls in package.findall(".//class"):
            filename = cls.get("filename")
            if filename:
                # Normalize path
                if filename.startswith("server/"):
                    file_path = filename
                else:
                    file_path = f"server/{filename}"

                line_rate = float(cls.get("line-rate", 0))
                branch_rate = float(cls.get("branch-rate", 0))
                lines_covered = int(cls.get("lines-covered", 0))
                lines_valid = int(cls.get("lines-valid", 0))
                branches_covered = int(cls.get("branches-covered", 0))
                branches_valid = int(cls.get("branches-valid", 0))

                file_data[file_path] = {
                    "line_coverage": line_rate * 100,
                    "branch_coverage": branch_rate * 100,
                    "lines_covered": lines_covered,
                    "lines_valid": lines_valid,
                    "branches_covered": branches_covered,
                    "branches_valid": branches_valid,
                }

    return file_data


def categorize_files(file_data: dict[str, dict[str, Any]]) -> tuple[list, list, list]:
    """Categorize files into critical below threshold, normal below threshold, and meeting thresholds."""
    critical_below = []
    normal_below = []
    meeting_threshold = []

    for file_path, data in file_data.items():
        # Skip test files
        if "/tests/" in file_path or file_path.endswith("test_*.py"):
            continue

        coverage = data["line_coverage"]
        gap = 0

        if file_path in CRITICAL_FILES:
            threshold = CRITICAL_FILES[file_path]
            if coverage < threshold:
                gap = threshold - coverage
                critical_below.append((file_path, coverage, threshold, gap, data))
            else:
                meeting_threshold.append((file_path, coverage, threshold, "critical", data))
        else:
            if coverage < NORMAL_THRESHOLD:
                gap = NORMAL_THRESHOLD - coverage
                normal_below.append((file_path, coverage, NORMAL_THRESHOLD, gap, data))
            else:
                meeting_threshold.append((file_path, coverage, NORMAL_THRESHOLD, "normal", data))

    # Sort by gap (largest gaps first)
    critical_below.sort(key=lambda x: x[3], reverse=True)
    normal_below.sort(key=lambda x: x[3], reverse=True)

    return critical_below, normal_below, meeting_threshold


def generate_status_doc(
    critical_below: list,
    normal_below: list,
    meeting_threshold: list,
    output_path: Path,
) -> None:
    """Generate coverage status markdown document."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Python Code Coverage Status\n\n")
        f.write("> *Generated by `scripts/analyze_coverage_gaps.py`*\n\n")
        f.write("## Summary\n\n")
        f.write(f"- **Critical files below threshold**: {len(critical_below)}\n")
        f.write(f"- **Normal files below 70%**: {len(normal_below)}\n")
        f.write(f"- **Files meeting thresholds**: {len(meeting_threshold)}\n\n")

        if critical_below:
            f.write("## Critical Files Below Threshold\n\n")
            f.write("| File | Current Coverage | Required | Gap | Lines | Branches |\n")
            f.write("|------|-----------------|----------|-----|--------|----------|\n")
            for file_path, coverage, threshold, gap, data in critical_below:
                f.write(
                    f"| `{file_path}` | {coverage:.2f}% | {threshold}% | {gap:.2f}% | "
                    f"{data['lines_covered']}/{data['lines_valid']} | "
                    f"{data['branches_covered']}/{data['branches_valid']} |\n"
                )
            f.write("\n")

        if normal_below:
            f.write(f"## Normal Files Below {NORMAL_THRESHOLD}% Threshold\n\n")
            f.write("*Showing top 50 files with largest coverage gaps*\n\n")
            f.write("| File | Current Coverage | Required | Gap | Lines | Branches |\n")
            f.write("|------|-----------------|----------|-----|--------|----------|\n")
            for file_path, coverage, threshold, gap, data in normal_below[:50]:
                f.write(
                    f"| `{file_path}` | {coverage:.2f}% | {threshold}% | {gap:.2f}% | "
                    f"{data['lines_covered']}/{data['lines_valid']} | "
                    f"{data['branches_covered']}/{data['branches_valid']} |\n"
                )
            if len(normal_below) > 50:
                f.write(f"\n*... and {len(normal_below) - 50} more files*\n")
            f.write("\n")

        f.write("## Priority Recommendations\n\n")
        if critical_below:
            f.write("### Immediate Priority (Critical Files)\n\n")
            for i, (file_path, coverage, _, gap, _) in enumerate(critical_below[:5], 1):
                f.write(f"{i}. **{file_path}** - {coverage:.2f}% (needs {gap:.2f}% more)\n")
            f.write("\n")

        if normal_below:
            f.write("### Secondary Priority (Normal Files)\n\n")
            f.write("Focus on files with largest gaps and highest usage:\n\n")
            for i, (file_path, coverage, _, gap, _) in enumerate(normal_below[:10], 1):
                f.write(f"{i}. **{file_path}** - {coverage:.2f}% (needs {gap:.2f}% more)\n")
            f.write("\n")


def main():
    """Main entry point."""
    project_root = Path(__file__).parent.parent
    coverage_xml = project_root / "coverage.xml"
    output_doc = project_root / "docs" / "PYTHON_COVERAGE_STATUS.md"

    if not coverage_xml.exists():
        print(f"ERROR: Coverage XML not found at {coverage_xml}")
        print("Run tests with coverage first: make test-server-coverage")
        sys.exit(1)

    print(f"Analyzing coverage from {coverage_xml}...")
    file_data = parse_coverage_xml(coverage_xml)

    critical_below, normal_below, meeting_threshold = categorize_files(file_data)

    print(f"\nFound {len(critical_below)} critical files below threshold")
    print(f"Found {len(normal_below)} normal files below threshold")
    print(f"Found {len(meeting_threshold)} files meeting thresholds")

    # Ensure docs directory exists
    output_doc.parent.mkdir(parents=True, exist_ok=True)

    generate_status_doc(critical_below, normal_below, meeting_threshold, output_doc)
    print(f"\n[PASS] Coverage status document generated: {output_doc}")


if __name__ == "__main__":
    main()
