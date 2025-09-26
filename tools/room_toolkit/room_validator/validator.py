#!/usr/bin/env python3
"""
Room Pathing Validator CLI

Main command-line interface for validating room connectivity and structure
in the MythosMUD world. Implements the dimensional mapping techniques
described in the Pnakotic Manuscripts.
"""

import sys
from datetime import datetime

import click
from core.fixer import RoomFixer
from core.minimap_renderer import MinimapRenderer
from core.path_validator import PathValidator
from core.reporter import Reporter
from core.room_loader import RoomLoader
from core.schema_validator import SchemaValidator


@click.command()
@click.option("--zone", help="Validate specific zone only")
@click.option("--verbose", "-v", is_flag=True, help="Detailed output")
@click.option("--schema-only", is_flag=True, help="Only validate JSON schema")
@click.option("--validate-configs", is_flag=True, help="Also validate configuration files")
@click.option("--ignore", help="Comma-separated list of rule types to ignore")
@click.option("--output-format", type=click.Choice(["console", "json"]), default="console")
@click.option("--base-path", default="./data/rooms", help="Base directory for room files")
@click.option("--no-colors", is_flag=True, help="Disable colored output")
@click.option("--fix", is_flag=True, help="Automatically fix issues (use with caution)")
@click.option("--backup", is_flag=True, help="Create backup files before fixing")
@click.option("--minimap", is_flag=True, help="Generate mini-map visualization")
@click.option("--minimap-depth", default=3, help="Maximum depth for mini-map (default: 3)")
# pylint: disable=too-many-arguments
def main(
    zone: str | None,
    verbose: bool,
    schema_only: bool,
    validate_configs: bool,
    ignore: str | None,
    output_format: str,
    base_path: str,
    no_colors: bool,
    fix: bool,
    backup: bool,
    minimap: bool,
    minimap_depth: int,
):
    """
    Validate room connectivity and structure in the MythosMUD world.

    This validator checks for path consistency, validates JSON structure,
    and ensures proper connectivity between rooms organized in zones.
    """
    try:
        # Initialize components
        reporter = Reporter(use_colors=not no_colors)
        room_loader = RoomLoader(base_path)
        schema_validator = SchemaValidator("schemas/unified_room_schema.json")
        path_validator = PathValidator(schema_validator)
        fixer = RoomFixer(base_path) if fix else None

        # Print header
        reporter.print_header()
        print(f"📁 Scanning {base_path}...")

        # Loading phase
        reporter.print_progress("Processing rooms...")
        room_database = room_loader.build_room_database(show_progress=verbose)

        # Discovery phase (after loading rooms)
        zones = room_loader.get_zones()
        if zones:
            reporter.print_zone_discovery(zones)
        else:
            reporter.print_warning("No zones discovered")

        if not room_database:
            reporter.print_error("No valid rooms found")
            sys.exit(1)

        # Filter by zone if specified
        if zone:
            if zone not in zones:
                reporter.print_error(f"Zone '{zone}' not found")
                sys.exit(1)
            room_database = room_loader.get_rooms_by_zone(zone)
            print(f"🔍 Validating zone: {zone} ({len(room_database)} rooms)")

        # Validation phase
        errors = []
        warnings = []

        # Convert parsing errors to validation errors
        parsing_errors = room_loader.get_parsing_errors()
        for file_path, error_msg in parsing_errors:
            errors.append(
                {
                    "type": "parse_error",
                    "room_id": file_path,
                    "message": error_msg,
                    "suggestion": "Fix the room file format or naming convention",
                }
            )

        if not schema_only:
            # Schema validation
            reporter.print_progress("Validating JSON schema...")
            schema_errors = schema_validator.validate_room_database(room_database)

            for room_id, room_errors in schema_errors.items():
                for error_msg in room_errors:
                    errors.append(
                        {
                            "type": "schema",
                            "room_id": room_id,
                            "message": error_msg,
                            "suggestion": "Check JSON structure and required fields",
                        }
                    )

            # Path validation
            reporter.print_progress("Analyzing room connectivity...")

            # Check for unreachable rooms
            start_room_id = "earth_arkhamcity_intersection_derby_high"
            unreachable = path_validator.find_unreachable_rooms(
                start_room_id=start_room_id, room_database=room_database
            )
            for room_id in unreachable:
                errors.append(
                    {
                        "type": "unreachable",
                        "room_id": room_id,
                        "message": f"No path from starting room {start_room_id}",
                        "suggestion": f"Add connection from {start_room_id} or another reachable room",
                    }
                )

            # Check bidirectional connections
            missing_returns = path_validator.check_bidirectional_connections(room_database)
            for room_a, direction_a, room_b, direction_b, is_zone_transition in missing_returns:
                error_type = "zone_transition" if is_zone_transition else "bidirectional"
                zone_a = room_database[room_a].get("sub_zone", "unknown")
                zone_b = room_database[room_b].get("sub_zone", "unknown")
                message = (
                    (
                        f"Zone Transition: Exit '{direction_a}' → {room_b} ({zone_a} → {zone_b}), "
                        f"but {room_b} has no '{direction_b}' return"
                    )
                    if is_zone_transition
                    else (f"Exit '{direction_a}' → {room_b}, but {room_b} has no '{direction_b}' return")
                )
                errors.append(
                    {
                        "type": error_type,
                        "room_id": room_a,
                        "message": message,
                        "suggestion": f'Add "{direction_b}": "{room_a}" to {room_b} or flag as one_way',
                    }
                )

            # Check for dead ends
            dead_ends = path_validator.find_dead_ends(room_database)
            for room_id in dead_ends:
                errors.append(
                    {
                        "type": "dead_end",
                        "room_id": room_id,
                        "message": "No exits (dead end)",
                        "suggestion": "Add at least one exit to this room",
                    }
                )

            # Note: Removed potential dead end warnings as they are unnecessary
            # Rooms with only one exit are a valid design pattern

            # Check for self-references
            self_references = path_validator.find_self_references(room_database)
            for room_id, direction in self_references:
                errors.append(
                    {
                        "type": "self_reference",
                        "room_id": room_id,
                        "message": f'Room references itself in direction "{direction}"',
                        "suggestion": 'Add "self_reference" flag or fix exit target',
                    }
                )

        # Apply fixes if requested
        if fix and fixer and errors:
            reporter.print_progress("Applying automatic fixes...")

            # Fix schema issues
            if schema_errors:
                fixer.fix_schema_issues(room_database, schema_errors, backup)

            # Fix bidirectional connections
            if missing_returns:
                fixer.fix_bidirectional_connections(room_database, missing_returns, backup)

            # Fix self-references
            if self_references:
                fixer.fix_self_references(room_database, self_references, backup)

            # Get fix summary
            fix_summary = fixer.get_fix_summary()

            if fix_summary["fixes_applied"] > 0:
                reporter.print_success(f"Applied {fix_summary['fixes_applied']} fixes")
                for applied_fix in fix_summary["applied_fixes"]:
                    print(f"  ✅ {applied_fix}")

            if fix_summary["fixes_failed"] > 0:
                reporter.print_warning(f"{fix_summary['fixes_failed']} fixes failed")
                for failed_fix in fix_summary["failed_fixes"]:
                    print(f"  ⚠️  {failed_fix}")

        # Validate configuration files if requested
        if validate_configs:
            reporter.print_progress("Validating configuration files...")
            config_files = room_loader.discover_config_files(base_path)

            # Validate sub-zone configurations
            for config_path in config_files["subzone_config"]:
                config_data = room_loader.load_config_file(config_path)
                if config_data:
                    config_errors = schema_validator.validate_subzone_config(config_data, str(config_path))
                    for error_msg in config_errors:
                        errors.append(
                            {
                                "type": "config_schema",
                                "room_id": str(config_path),
                                "message": error_msg,
                                "suggestion": "Check sub-zone configuration schema",
                            }
                        )
                else:
                    errors.append(
                        {
                            "type": "config_parse",
                            "room_id": str(config_path),
                            "message": "Failed to parse sub-zone configuration",
                            "suggestion": "Check JSON syntax and structure",
                        }
                    )

            # Validate zone configurations
            for config_path in config_files["zone_config"]:
                config_data = room_loader.load_config_file(config_path)
                if config_data:
                    config_errors = schema_validator.validate_zone_config(config_data, str(config_path))
                    for error_msg in config_errors:
                        errors.append(
                            {
                                "type": "config_schema",
                                "room_id": str(config_path),
                                "message": error_msg,
                                "suggestion": "Check zone configuration schema",
                            }
                        )
                else:
                    errors.append(
                        {
                            "type": "config_parse",
                            "room_id": str(config_path),
                            "message": "Failed to parse zone configuration",
                            "suggestion": "Check JSON syntax and structure",
                        }
                    )

        # Generate mini-map if requested
        if minimap:
            reporter.print_progress("Generating mini-map visualization...")
            minimap_data = path_validator.generate_minimap_graph(room_database, minimap_depth)
            minimap_renderer = MinimapRenderer()

            print("\n" + "=" * 80)
            print("🗺️  MINI-MAP VISUALIZATION")
            print("=" * 80)

            # Render ASCII map
            ascii_map = minimap_renderer.render_ascii_map(minimap_data)
            print(ascii_map)

            # Render connectivity stats
            stats_map = minimap_renderer.render_connectivity_stats(minimap_data)
            print("\n" + stats_map)

            print("=" * 80)

        # Generate statistics
        subzones = room_loader.get_subzones()
        config_subzones = room_loader.count_config_subzones(base_path)

        stats = {
            "zones": len(zones),
            "subzones": len(subzones),
            "config_subzones": config_subzones,
            "rooms": len(room_database),
            "errors": len(errors),
            "warnings": len(warnings),
            "success": len(errors) == 0,
        }

        # Log errors to file if any exist
        if errors:
            error_log_path = "error.log"
            with open(error_log_path, "w", encoding="utf-8") as f:
                f.write(f"Room Validator Error Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 80 + "\n\n")
                for error in errors:
                    f.write(f"🏠 {error['room_id']}\n")
                    f.write(f"  ❌ {error['type'].title()}: {error['message']}\n")
                    f.write(f"     💡 Suggestion: {error['suggestion']}\n\n")
            print(f"📝 Errors logged to {error_log_path}")

        # Reporting phase
        if output_format == "json":
            json_output = reporter.generate_json_output(stats, errors, warnings)
            print(json_output)
        else:
            if errors:
                print(f"❌ {len(errors)} errors found (see error.log for details)")
            else:
                reporter.print_success("All validations passed!")
            reporter.print_validation_warnings(warnings)
            reporter.print_summary(stats)

        # Exit with appropriate code
        sys.exit(0 if len(errors) == 0 else 1)

    except Exception as e:
        if verbose:
            raise
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Click automatically handles argument parsing and calls main() with the parsed arguments
    main()  # pylint: disable=no-value-for-parameter
