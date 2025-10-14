#!/usr/bin/env python3
"""
Batch migration script for test suite refactoring.

This script automates the migration of test files from the flat structure
to the new hierarchical organization.

Usage:
    python migrate_batch.py --phase <phase_number>
    python migrate_batch.py --domain <domain_name>
    python migrate_batch.py --dry-run  # Show what would be migrated without moving files
"""

import argparse
import shutil
import sys
from pathlib import Path

# Project root
SCRIPT_DIR = Path(__file__).parent
BASE = SCRIPT_DIR.parent

# Migration mappings by phase/domain
MIGRATION_MAP = {
    # Phase 3: Feature Domains - Player
    "player": [
        ("test_player_service.py", "unit/player/test_player_service.py"),
        ("test_player_service_layer.py", "unit/player/test_player_service_layer_legacy.py"),  # To merge
        ("test_player_stats.py", "unit/player/test_player_stats.py"),
        ("test_player_channel_preferences.py", "unit/player/test_player_preferences.py"),
        ("test_player_guid_formatter.py", "unit/player/test_player_guid_formatter.py"),
        ("test_character_creation_service_layer.py", "unit/player/test_character_creation.py"),
        ("test_character_recovery_flow.py", "unit/player/test_character_recovery.py"),
        ("test_stats_generator.py", "unit/player/test_stats_generator.py"),
        ("test_stats_random_generation.py", "unit/player/test_stats_random_generation_legacy.py"),  # To merge
        ("test_user_manager.py", "unit/player/test_user_manager.py"),
    ],
    # Phase 3: Feature Domains - Authentication
    "auth": [
        ("test_auth.py", "unit/auth/test_auth.py"),
        ("test_auth_utils.py", "unit/auth/test_auth_utils.py"),
        ("test_jwt_authentication_flow.py", "unit/auth/test_jwt_authentication.py"),
        ("test_argon2_utils.py", "unit/auth/test_argon2_utils.py"),
        ("test_email_utils.py", "unit/auth/test_email_utils.py"),
    ],
    # Phase 3: Feature Domains - NPC
    "npc": [
        ("test_npc_models.py", "unit/npc/test_npc_models.py"),
        ("test_npc_behaviors.py", "unit/npc/test_npc_behaviors.py"),
        ("test_npc_spawning_service.py", "unit/npc/test_npc_spawning_service.py"),
        ("test_npc_lifecycle_manager.py", "unit/npc/test_npc_lifecycle_manager.py"),
        ("test_npc_population_control.py", "unit/npc/test_npc_population_control.py"),
        ("test_npc_population_management.py", "unit/npc/test_npc_population_management_legacy.py"),  # To merge
        ("test_npc_startup_service.py", "unit/npc/test_npc_startup_service.py"),
        ("test_npc_name_formatting.py", "unit/npc/test_npc_name_formatting.py"),
        ("test_npc_threading.py", "unit/npc/test_npc_threading.py"),
        ("test_npc_admin_api_simple.py", "unit/npc/test_npc_admin_api.py"),
        ("test_npc_admin_api.py", "unit/npc/test_npc_admin_api_full_legacy.py"),  # To merge
    ],
    # Phase 3: Feature Domains - World/Rooms
    "world": [
        ("test_room_service.py", "unit/world/test_room_service.py"),
        ("test_room_service_layer.py", "unit/world/test_room_service_layer_legacy.py"),  # To merge
        ("test_room_utils.py", "unit/world/test_room_utils.py"),
        ("test_world_loader.py", "unit/world/test_world_loader.py"),
        ("test_world_loader_hierarchy.py", "unit/world/test_world_hierarchy.py"),
        ("test_movement_service.py", "unit/world/test_movement_service.py"),
        ("test_movement_comprehensive.py", "unit/world/test_movement_comprehensive_legacy.py"),  # To merge
        ("test_movement_persistence.py", "unit/world/test_movement_persistence.py"),
        ("test_room_based_mute_filtering.py", "unit/world/test_room_mute_filtering.py"),
    ],
    # Phase 3: Feature Domains - Chat/Communication
    "chat": [
        ("test_chat_service.py", "unit/chat/test_chat_service.py"),
        ("test_emote_service.py", "unit/chat/test_emote_service.py"),
        ("test_emote_mute_filtering.py", "unit/chat/test_emote_filtering.py"),
        ("test_emote_types_mute_filtering.py", "unit/chat/test_emote_types_filtering_legacy.py"),  # To merge
        ("test_whisper_channel.py", "unit/chat/test_whisper_channel.py"),
        ("test_local_channel.py", "unit/chat/test_local_channel.py"),
        ("test_local_channel_commands.py", "unit/chat/test_local_channel_commands_legacy.py"),  # To merge
        ("test_global_channel_commands.py", "unit/chat/test_global_channel.py"),
        ("test_system_channel.py", "unit/chat/test_system_channel.py"),
        ("test_channel_broadcasting_strategies.py", "unit/chat/test_broadcasting_strategies.py"),
        ("test_channel_broadcasting_strategies_implementation.py", "unit/chat/test_broadcasting_strategies_impl_legacy.py"),  # To merge
    ],
    # Phase 3: Feature Domains - API
    "api": [
        ("test_api_base.py", "unit/api/test_base.py"),
        ("test_api_players.py", "unit/api/test_players.py"),
        ("test_api_professions.py", "unit/api/test_professions.py"),
        ("test_api_real_time.py", "unit/api/test_real_time.py"),
        ("test_health_endpoint.py", "unit/api/test_health_endpoints.py"),
        ("test_monitoring_api_endpoints.py", "unit/api/test_monitoring_endpoints.py"),
        ("test_monitoring_api.py", "unit/api/test_monitoring_api_legacy.py"),  # To merge
        ("test_api_endpoints_dual_connection.py", "unit/api/test_dual_connection_endpoints.py"),
    ],
    # Phase 3: Feature Domains - Commands
    "commands": [
        ("test_command_handler.py", "unit/commands/test_command_handler.py"),
        ("test_command_handler_v2.py", "unit/commands/test_command_handler_v2_legacy.py"),  # To merge
        ("test_command_handler_unified.py", "unit/commands/test_command_handler_unified_legacy.py"),  # To merge
        ("test_unified_command_handler.py", "unit/commands/test_unified_command_handler_legacy.py"),  # To merge
        ("test_command_validation.py", "unit/commands/test_command_validation.py"),
        ("test_command_rate_limiter.py", "unit/commands/test_command_rate_limiter.py"),
        ("test_admin_teleport_commands.py", "unit/commands/test_admin_commands.py"),
        ("test_utility_commands.py", "unit/commands/test_utility_commands.py"),
    ],
    # Phase 3: Feature Domains - Events
    "events": [
        ("test_event_bus.py", "unit/events/test_event_bus.py"),
        ("test_event_publisher.py", "unit/events/test_event_publisher.py"),
        ("test_event_handler_timestamps.py", "unit/events/test_event_handler.py"),
        ("test_event_handler_broadcasting.py", "unit/events/test_event_handler_broadcasting_legacy.py"),  # To merge
        ("test_message_handler_factory.py", "unit/events/test_message_handler_factory.py"),
        ("test_working_event_system.py", "unit/events/test_event_system.py"),
    ],
    # Phase 3: Feature Domains - Real-time
    "realtime": [
        ("test_websocket_handler.py", "unit/realtime/test_websocket_handler.py"),
        ("test_websocket_message_handler.py", "unit/realtime/test_websocket_message_handler.py"),
        ("test_websocket_connection_stability.py", "unit/realtime/test_websocket_connection.py"),
        ("test_sse_handler.py", "unit/realtime/test_sse_handler.py"),
        ("test_sse_auth.py", "unit/realtime/test_sse_auth.py"),
        ("test_nats_service.py", "unit/realtime/test_nats_service.py"),
        ("test_nats_message_handler.py", "unit/realtime/test_nats_message_handler.py"),
        ("test_nats_message_handler_subzone.py", "unit/realtime/test_nats_message_handler_subzone_legacy.py"),  # To merge
        ("test_nats_retry_handler.py", "unit/realtime/test_nats_retry_handler.py"),
        ("test_dead_letter_queue.py", "unit/realtime/test_dead_letter_queue.py"),
        ("test_real_time.py", "unit/realtime/test_real_time.py"),
    ],
    # Phase 3: Feature Domains - Middleware
    "middleware": [
        ("test_error_handling_middleware.py", "unit/middleware/test_error_handling_middleware.py"),
        ("test_comprehensive_logging_middleware.py", "unit/middleware/test_logging_middleware.py"),
        ("test_security_middleware.py", "unit/middleware/test_security_middleware.py"),
        ("test_cors_configuration_verification.py", "unit/middleware/test_cors_configuration.py"),
    ],
    # Phase 3: Feature Domains - Logging
    "logging": [
        ("test_audit_logger.py", "unit/logging/test_audit_logger.py"),
        ("test_chat_logger.py", "unit/logging/test_chat_logger.py"),
        ("test_admin_actions_logger.py", "unit/logging/test_admin_actions_logger.py"),
        ("test_log_analysis_tools.py", "unit/logging/test_log_analysis_tools.py"),
        ("test_local_channel_logging.py", "unit/logging/test_local_channel_logging.py"),
        ("test_global_channel_logging.py", "unit/logging/test_global_channel_logging.py"),
    ],
    # Phase 3: Feature Domains - Utilities
    "utilities": [
        ("test_security_utils.py", "unit/utilities/test_security_utils.py"),
        ("test_security_validator.py", "unit/utilities/test_security_validator.py"),
        ("test_rate_limiter.py", "unit/utilities/test_rate_limiter.py"),
        ("test_utils_rate_limiter.py", "unit/utilities/test_utils_rate_limiter_legacy.py"),  # To merge
        ("test_circuit_breaker.py", "unit/utilities/test_circuit_breaker.py"),
        ("test_alias_graph.py", "unit/utilities/test_alias_graph.py"),
        ("test_alias_storage.py", "unit/utilities/test_alias_storage.py"),
        ("test_centralized_validation_functions.py", "unit/utilities/test_validation_functions.py"),
        ("test_error_handlers.py", "unit/utilities/test_error_handlers.py"),
        ("test_legacy_error_handlers.py", "unit/utilities/test_legacy_error_handlers_legacy.py"),  # To merge
        ("test_standardized_error_handling.py", "unit/utilities/test_standardized_error_handling_legacy.py"),  # To merge
        ("test_standardized_responses.py", "unit/utilities/test_standardized_responses.py"),
        ("test_pydantic_error_handler.py", "unit/utilities/test_pydantic_error_handler.py"),
    ],
}


def migrate_files(domain: str, dry_run: bool = False) -> tuple[int, int]:
    """
    Migrate files for a specific domain.

    Args:
        domain: Domain name (e.g., 'player', 'npc', 'chat')
        dry_run: If True, show what would be migrated without actually moving files

    Returns:
        Tuple of (migrated_count, error_count)
    """
    if domain not in MIGRATION_MAP:
        print(f"Error: Unknown domain '{domain}'")
        print(f"Available domains: {', '.join(MIGRATION_MAP.keys())}")
        return 0, 0

    migrations = MIGRATION_MAP[domain]
    migrated = 0
    errors = 0

    print(f"{'DRY RUN: ' if dry_run else ''}Migrating {domain} tests...")
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

    return migrated, errors


def list_domains() -> None:
    """List available domains for migration."""
    print("Available domains for migration:")
    print("=" * 70)
    for domain, files in MIGRATION_MAP.items():
        print(f"{domain}: {len(files)} files")
    print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Batch migrate test files to new structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--domain", help="Domain to migrate (player, npc, chat, etc.)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be migrated without moving files")
    parser.add_argument("--list", action="store_true", help="List available domains")

    args = parser.parse_args()

    if args.list:
        list_domains()
        return 0

    if not args.domain:
        print("Error: --domain is required (or use --list to see available domains)")
        list_domains()
        return 1

    migrated, errors = migrate_files(args.domain, dry_run=args.dry_run)

    if errors > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
