#!/usr/bin/env python3
"""
Room Pathing Validator CLI

Main command-line interface for validating room connectivity and structure
in the MythosMUD world. Implements the dimensional mapping techniques
described in the Pnakotic Manuscripts.
"""

import sys

import click
from core.fixer import RoomFixer
from core.path_validator import PathValidator
from core.reporter import Reporter
from core.room_loader import RoomLoader
from core.schema_validator import SchemaValidator


@click.command()
@click.option("--zone", help="Validate specific zone only")
@click.option("--verbose", "-v", is_flag=True, help="Detailed output")
@click.option("--schema-only", is_flag=True, help="Only validate JSON schema")
@click.option("--ignore", help="Comma-separated list of rule types to ignore")
@click.option("--output-format", type=click.Choice(["console", "json"]), default="console")
@click.option("--base-path", default="./data/rooms", help="Base directory for room files")
@click.option("--no-colors", is_flag=True, help="Disable colored output")
@click.option("--fix", is_flag=True, help="Automatically fix issues (use with caution)")
@click.option("--backup", is_flag=True, help="Create backup files before fixing")
# pylint: disable=too-many-arguments
def main(
    zone: str | None,
    verbose: bool,
    schema_only: bool,
    ignore: str | None,
    output_format: str,
    base_path: str,
    no_colors: bool,
    fix: bool,
    backup: bool,
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
        schema_validator = SchemaValidator()
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

        # Print parsing errors if any
        parsing_errors = room_loader.get_parsing_errors()
        if parsing_errors:
            reporter.print_parsing_errors(parsing_errors)

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
            unreachable = path_validator.find_unreachable_rooms(room_database=room_database)
            for room_id in unreachable:
                errors.append(
                    {
                        "type": "unreachable",
                        "room_id": room_id,
                        "message": "No path from starting room arkham_001",
                        "suggestion": "Add connection from arkham_001 or another reachable room",
                    }
                )

            # Check bidirectional connections
            missing_returns = path_validator.check_bidirectional_connections(room_database)
            for room_a, direction_a, room_b, direction_b in missing_returns:
                errors.append(
                    {
                        "type": "bidirectional",
                        "room_id": room_a,
                        "message": f"Exit '{direction_a}' → {room_b}, but {room_b} has no '{direction_b}' return",
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

        # Generate statistics
        stats = {
            "zones": len(zones),
            "rooms": len(room_database),
            "errors": len(errors),
            "warnings": len(warnings),
            "success": len(errors) == 0,
        }

        # Reporting phase
        if output_format == "json":
            json_output = reporter.generate_json_output(stats, errors, warnings)
            print(json_output)
        else:
            reporter.print_validation_errors(errors)
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
