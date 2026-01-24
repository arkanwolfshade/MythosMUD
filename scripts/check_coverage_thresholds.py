#!/usr/bin/env python3
"""Check coverage thresholds for critical and normal files."""

import os
import sys
from pathlib import Path

from defusedxml import ElementTree as etree

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

# Normal files require 70% coverage
NORMAL_THRESHOLD = 70


def parse_coverage_xml(coverage_xml_path: Path) -> dict[str, float]:
    """Parse coverage.xml and return file coverage percentages."""
    tree = etree.parse(coverage_xml_path)
    root = tree.getroot()

    file_coverage = {}
    for package in root.findall(".//package"):
        for cls in package.findall(".//class"):
            filename = cls.get("filename")
            if filename:
                # Coverage XML uses relative paths from source root
                # Normalize to match our file paths
                if filename.startswith("server/"):
                    file_path = filename
                else:
                    file_path = f"server/{filename}"

                line_rate = float(cls.get("line-rate", 0))
                coverage_percent = line_rate * 100
                file_coverage[file_path] = coverage_percent

    return file_coverage


def check_thresholds(file_coverage: dict[str, float]) -> tuple[list[str], list[str]]:
    """Check files against their thresholds. Returns (failures, warnings)."""
    failures = []
    warnings = []

    # Check critical files
    for file_path, threshold in CRITICAL_FILES.items():
        coverage = file_coverage.get(file_path, 0)
        if coverage < threshold:
            failures.append(f"CRITICAL: {file_path} has {coverage:.2f}% coverage, requires {threshold}%")

    # Check normal files (all other server files)
    for file_path, coverage in file_coverage.items():
        # Skip if it's a critical file (already checked)
        if file_path in CRITICAL_FILES:
            continue

        # Skip test files
        if "/tests/" in file_path or file_path.endswith("test_*.py"):
            continue

        if coverage < NORMAL_THRESHOLD:
            warnings.append(f"NORMAL: {file_path} has {coverage:.2f}% coverage, requires {NORMAL_THRESHOLD}%")

    return failures, warnings


def main():
    """Main entry point."""
    project_root = Path(__file__).parent.parent
    coverage_xml = project_root / "coverage.xml"

    if not coverage_xml.exists():
        # In pre-commit context, this is okay - coverage may not have been generated yet
        # Exit with success so commits aren't blocked
        if os.getenv("PRE_COMMIT"):
            print("INFO: Coverage XML not found. Skipping threshold check.")
            print("Run 'make test-server-coverage' to generate coverage before committing.")
            sys.exit(0)
        else:
            print(f"ERROR: Coverage XML not found at {coverage_xml}")
            print("Run tests with coverage first: make test-server-coverage")
            sys.exit(1)

    print(f"Checking coverage thresholds from {coverage_xml}...")
    file_coverage = parse_coverage_xml(coverage_xml)

    failures, warnings = check_thresholds(file_coverage)

    # Print results
    if failures:
        print("\n[FAIL] CRITICAL FILES BELOW THRESHOLD:")
        for failure in failures:
            print(f"  {failure}")

    if warnings:
        print(f"\n[WARN] NORMAL FILES BELOW {NORMAL_THRESHOLD}% THRESHOLD ({len(warnings)} files):")
        # Show first 10 warnings
        for warning in warnings[:10]:
            print(f"  {warning}")
        if len(warnings) > 10:
            print(f"  ... and {len(warnings) - 10} more files")

    # Exit with error if critical files fail
    if failures:
        print(f"\n[FAIL] {len(failures)} critical file(s) below threshold")
        sys.exit(1)

    if warnings:
        print(f"\n[WARN] {len(warnings)} normal file(s) below threshold (non-blocking)")
        print("Consider improving coverage for these files in future work.")

    print("\n[PASS] All critical files meet coverage thresholds!")
    sys.exit(0)


if __name__ == "__main__":
    main()
