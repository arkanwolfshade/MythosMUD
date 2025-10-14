#!/usr/bin/env python3
"""
Migrate integration, e2e, security, performance, coverage, regression,
monitoring, and verification tests to new structure.

Usage:
    python migrate_specialized.py --all
    python migrate_specialized.py --category <category>
    python migrate_specialized.py --dry-run
"""

import argparse
import shutil
import sys
from pathlib import Path

# Base path
SCRIPT_DIR = Path(__file__).parent
BASE = SCRIPT_DIR.parent

# Migration mappings for specialized test categories
MIGRATION_MAP = {
    "integration": [
        ("test_api_players_integration.py", "integration/api/test_api_players_integration.py"),
        ("test_dual_connection_integration.py", "integration/api/test_dual_connection_integration.py"),
        ("test_monitoring_dual_connections.py", "integration/api/test_monitoring_integration.py"),
        ("test_game_api_broadcast.py", "integration/api/test_game_api_broadcast.py"),
        ("test_admin_teleport_integration.py", "integration/commands/test_admin_teleport_integration.py"),
        ("test_whisper_command_integration.py", "integration/chat/test_whisper_integration.py"),
        ("test_player_channel_preferences_integration.py", "integration/chat/test_player_preferences_integration.py"),
        ("test_mute_unmute_workflow_integration.py", "integration/chat/test_mute_workflow_integration.py"),
        ("test_system_channel_integration.py", "integration/chat/test_system_channel_integration.py"),
        ("test_event_broadcasting_bugs.py", "integration/events/test_event_broadcasting.py"),
        ("test_complete_event_flow_integration.py", "integration/events/test_event_flow_integration.py"),
        ("test_real_event_flow.py", "integration/events/test_real_event_flow_legacy.py"),  # To merge
        ("test_realtime_event_handler_integration.py", "integration/events/test_realtime_event_handler_integration.py"),
        ("test_websocket_connection_events.py", "integration/events/test_websocket_connection_events.py"),
        ("test_connection_manager_occupant_events.py", "integration/events/test_connection_manager_events.py"),
        ("test_simple_connection_events.py", "integration/events/test_simple_connection_events_legacy.py"),  # To merge
        ("test_npc_integration.py", "integration/npc/test_npc_integration.py"),
        ("test_npc_room_integration.py", "integration/npc/test_npc_room_integration.py"),
        ("test_npc_admin_commands.py", "integration/npc/test_npc_admin_commands_integration.py"),
        ("test_npc_admin_commands_fixed.py", "integration/npc/test_npc_admin_commands_fixed_legacy.py"),  # To merge
        ("test_movement_integration.py", "integration/movement/test_movement_integration.py"),
        ("test_room_synchronization.py", "integration/movement/test_room_synchronization.py"),
        ("test_nats_integration_e2e.py", "integration/nats/test_nats_integration_e2e.py"),
        ("test_connection_manager_nats_integration.py", "integration/nats/test_connection_manager_nats.py"),
        ("test_local_channel_nats_integration.py", "integration/nats/test_local_channel_nats.py"),
        ("test_comprehensive_integration.py", "integration/comprehensive/test_comprehensive_integration.py"),
        ("test_simple_integration.py", "integration/comprehensive/test_simple_integration.py"),
        ("test_integration_bug_prevention.py", "integration/comprehensive/test_bug_prevention.py"),
        ("test_alias_integration.py", "integration/comprehensive/test_alias_integration.py"),
        ("test_logging_integration.py", "integration/comprehensive/test_logging_integration.py"),
    ],
    "e2e": [
        ("test_multiplayer_integration.py", "e2e/test_multiplayer_integration.py"),
        ("test_e2e_multiplayer_connection_messaging.py", "e2e/test_multiplayer_connection_messaging.py"),
        ("test_logout_integration.py", "e2e/test_logout_integration.py"),
        ("test_dual_connection_testing_strategy.py", "e2e/test_dual_connection_testing_strategy.py"),
        ("test_game_mechanics.py", "e2e/test_game_mechanics.py"),
    ],
    "security": [
        ("test_admin_teleport_security.py", "security/test_admin_teleport_security.py"),
        ("test_security_penetration.py", "security/test_security_penetration.py"),
        ("test_security_headers_verification.py", "security/test_security_headers_verification.py"),
        ("test_centralized_security_validation.py", "security/test_centralized_security_validation.py"),
        ("test_global_channel_access_control.py", "security/test_global_channel_access_control.py"),
        ("test_file_containment.py", "security/test_file_containment.py"),
    ],
    "performance": [
        ("test_dual_connection_performance.py", "performance/test_dual_connection_performance.py"),
        ("test_error_logging_performance.py", "performance/test_error_logging_performance.py"),
        ("test_mute_filtering_performance.py", "performance/test_mute_filtering_performance.py"),
        ("test_model_performance_benchmarks.py", "performance/test_model_performance_benchmarks.py"),
    ],
    "coverage": [
        ("test_command_handler_coverage.py", "coverage/test_command_handler_coverage.py"),
        ("test_command_handler_unified_coverage.py", "coverage/test_command_handler_unified_coverage_legacy.py"),  # To merge
        ("test_command_rate_limiter_coverage.py", "coverage/test_command_rate_limiter_coverage.py"),
        ("test_comprehensive_logging_coverage.py", "coverage/test_comprehensive_logging_coverage.py"),
        ("test_system_commands_coverage.py", "coverage/test_system_commands_coverage.py"),
        ("test_help_content_coverage.py", "coverage/test_help_content_coverage.py"),
        ("test_simple_coverage_gaps.py", "coverage/test_simple_coverage_gaps.py"),
        ("test_comprehensive_error_logging.py", "coverage/test_error_logging_coverage.py"),
        ("test_error_logging_integration.py", "coverage/test_error_logging_integration_legacy.py"),  # To merge
    ],
    "regression": [
        ("test_unknown_room_fix.py", "regression/test_unknown_room_fix.py"),
        ("test_movement_fix.py", "regression/test_movement_fix.py"),
        ("test_self_message_bug.py", "regression/test_self_message_bug.py"),
        ("test_self_message_exclusion.py", "regression/test_self_message_exclusion_legacy.py"),  # To merge
        ("test_npc_spawn_fix.py", "regression/test_npc_spawn_fix.py"),
        ("test_unresolved_bugs.py", "regression/test_unresolved_bugs.py"),
        ("test_debug_infinite_loop.py", "regression/test_infinite_loop_debug.py"),
    ],
    "monitoring": [
        ("test_mute_filtering_monitoring.py", "monitoring/test_mute_filtering_monitoring.py"),
        ("test_movement_monitor.py", "monitoring/test_movement_monitor.py"),
        ("test_occupant_count_integration.py", "monitoring/test_occupant_count_integration.py"),
        ("test_occupant_count_simple_integration.py", "monitoring/test_occupant_count_simple_legacy.py"),  # To merge
        ("test_multiple_players_muting.py", "monitoring/test_multiple_players_muting.py"),
        ("test_temporary_permanent_mutes.py", "monitoring/test_temporary_permanent_mutes.py"),
    ],
    "verification": [
        ("test_async_operations_verification.py", "verification/test_async_operations_verification.py"),
        ("test_async_pattern_standardization.py", "verification/test_async_pattern_standardization.py"),
        ("test_async_route_handlers.py", "verification/test_async_route_handlers.py"),
        ("test_base_testing_async.py", "verification/test_base_testing_async.py"),
        ("test_pure_async_eventbus_verification.py", "verification/test_pure_async_eventbus_verification.py"),
        ("test_event_bus_pure_asyncio_verification.py", "verification/test_event_bus_pure_asyncio_verification_legacy.py"),  # To merge
        ("test_running_event_loop.py", "verification/test_running_event_loop.py"),
        ("test_help_topic_validation.py", "verification/test_help_topic_validation.py"),
        ("test_validation_error_imports.py", "verification/test_validation_error_imports.py"),
        ("test_mute_data_consistency.py", "verification/test_mute_data_consistency.py"),
        ("test_event_verification_demo.py", "verification/test_event_verification_demo.py"),
    ],
}


def migrate_category(category: str, dry_run: bool = False) -> tuple[int, int]:
    """
    Migrate files for a specific category.

    Args:
        category: Category name (integration, e2e, security, etc.)
        dry_run: If True, show what would be migrated without moving files

    Returns:
        Tuple of (migrated_count, error_count)
    """
    if category not in MIGRATION_MAP:
        print(f"Error: Unknown category '{category}'")
        print(f"Available categories: {', '.join(MIGRATION_MAP.keys())}")
        return 0, 0

    migrations = MIGRATION_MAP[category]
    migrated = 0
    errors = 0

    print(f"{'DRY RUN: ' if dry_run else ''}Migrating {category} tests...")
    print("=" * 70)

    for old_path, new_path in migrations:
        old_file = BASE / old_path
        new_file = BASE / new_path

        if not old_file.exists():
            print(f"  [SKIP] {old_path} (not found)")
            continue

        if dry_run:
            print(f"  [WOULD MOVE] {old_path}")
            print(f"            -> {new_path}")
            migrated += 1
        else:
            try:
                # Ensure destination directory exists
                new_file.parent.mkdir(parents=True, exist_ok=True)

                # Move file
                shutil.move(str(old_file), str(new_file))
                print(f"  [MOVED] {old_path}")
                print(f"       -> {new_path}")
                migrated += 1
            except Exception as e:
                print(f"  [ERROR] {old_path}: {e}")
                errors += 1

    print()
    print(f"{'Would migrate' if dry_run else 'Migrated'}: {migrated} files")
    if errors > 0:
        print(f"Errors: {errors} files")
    print()

    return migrated, errors


def migrate_all(dry_run: bool = False) -> None:
    """Migrate all specialized test categories."""
    total_migrated = 0
    total_errors = 0

    for category in MIGRATION_MAP.keys():
        migrated, errors = migrate_category(category, dry_run=dry_run)
        total_migrated += migrated
        total_errors += errors

    print("=" * 70)
    print(f"TOTAL: {'Would migrate' if dry_run else 'Migrated'} {total_migrated} files")
    if total_errors > 0:
        print(f"TOTAL ERRORS: {total_errors} files")
    print("=" * 70)


def list_categories() -> None:
    """List available categories for migration."""
    print("Available categories for migration:")
    print("=" * 70)
    for category, files in MIGRATION_MAP.items():
        print(f"{category}: {len(files)} files")
    print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Batch migrate specialized test files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--category", help="Category to migrate (integration, e2e, security, etc.)")
    parser.add_argument("--all", action="store_true", help="Migrate all categories")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be migrated without moving files")
    parser.add_argument("--list", action="store_true", help="List available categories")

    args = parser.parse_args()

    if args.list:
        list_categories()
        return 0

    if args.all:
        migrate_all(dry_run=args.dry_run)
        return 0

    if not args.category:
        print("Error: --category or --all is required (or use --list to see available categories)")
        list_categories()
        return 1

    migrated, errors = migrate_category(args.category, dry_run=args.dry_run)

    if errors > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
