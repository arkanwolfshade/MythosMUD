#!/usr/bin/env python3
"""
MythosMUD Room Toolkit CLI

Unified command-line interface for room management, validation, mapping, and analysis.
Consolidates functionality from the original validator and mapbuilder tools.
"""

import sys

import click

from .core.analyzer import RoomAnalyzer
from .core.fixer import RoomFixer
from .core.loader import RoomLoader
from .core.mapper import RoomMapper
from .core.reporter import Reporter
from .core.validator import RoomValidator


@click.group()
@click.option("--base-path", default="./data/rooms", help="Base directory for room files")
@click.option("--verbose", "-v", is_flag=True, help="Detailed output")
@click.option("--no-colors", is_flag=True, help="Disable colored output")
@click.pass_context
def main(ctx, base_path: str, verbose: bool, no_colors: bool):
    """
    MythosMUD Room Toolkit - Unified room management tool

    This toolkit consolidates room validation, mapping, analysis, and fixing
    capabilities into a single, powerful command-line interface.
    """
    ctx.ensure_object(dict)
    ctx.obj["base_path"] = base_path
    ctx.obj["verbose"] = verbose
    ctx.obj["no_colors"] = no_colors


@main.command()
@click.option("--zone", help="Validate specific zone only")
@click.option("--schema-only", is_flag=True, help="Only validate JSON schema")
@click.option("--validate-configs", is_flag=True, help="Also validate configuration files")
@click.option("--fix", is_flag=True, help="Automatically fix issues (use with caution)")
@click.option("--backup", is_flag=True, help="Create backup files before fixing")
@click.option("--output-format", type=click.Choice(["console", "json"]), default="console")
@click.option("--ignore", help="Comma-separated list of rule types to ignore")
@click.pass_context
def validate(
    ctx,
    zone: str | None,
    schema_only: bool,
    validate_configs: bool,
    fix: bool,
    backup: bool,
    output_format: str,
    ignore: str | None,
):
    """
    Validate room connectivity and structure in the MythosMUD world.

    This command checks for path consistency, validates JSON structure,
    and ensures proper connectivity between rooms organized in zones.
    """
    base_path = ctx.obj["base_path"]
    verbose = ctx.obj["verbose"]
    no_colors = ctx.obj["no_colors"]

    try:
        # Initialize components
        reporter = Reporter(use_colors=not no_colors)
        loader = RoomLoader(base_path)
        validator = RoomValidator()
        fixer = RoomFixer(base_path) if fix else None

        # Print header
        reporter.print_header()
        print(f"📁 Scanning {base_path}...")

        # Loading phase
        if verbose:
            reporter.print_progress("Processing rooms...")

        room_database = loader.build_room_database(show_progress=verbose)

        if not room_database:
            reporter.print_error("No valid rooms found")
            sys.exit(1)

        # Filter by zone if specified
        if zone:
            zones = loader.get_zones()
            if zone not in zones:
                reporter.print_error(f"Zone '{zone}' not found")
                sys.exit(1)
            room_database = loader.get_rooms_by_zone(zone)
            print(f"🔍 Validating zone: {zone} ({len(room_database)} rooms)")

        # Validation phase
        errors = []
        warnings = []

        # Convert parsing errors to validation errors
        parsing_errors = loader.get_parsing_errors()
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
            if verbose:
                reporter.print_progress("Validating JSON schema...")
            schema_errors = validator.validate_schema(room_database)

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

            # Connectivity validation
            if verbose:
                reporter.print_progress("Analyzing room connectivity...")

            connectivity_errors = validator.validate_connectivity(room_database)
            errors.extend(connectivity_errors)

        # Apply fixes if requested
        if fix and fixer and errors:
            if verbose:
                reporter.print_progress("Applying automatic fixes...")

            fix_summary = fixer.apply_fixes(room_database, errors, backup)

            if fix_summary["fixes_applied"] > 0:
                reporter.print_success(f"Applied {fix_summary['fixes_applied']} fixes")
                for applied_fix in fix_summary["applied_fixes"]:
                    print(f"  ✅ {applied_fix}")

            if fix_summary["fixes_failed"] > 0:
                reporter.print_warning(f"{fix_summary['fixes_failed']} fixes failed")
                for failed_fix in fix_summary["failed_fixes"]:
                    print(f"  ⚠️  {failed_fix}")

        # Generate statistics
        zones = loader.get_zones()
        subzones = loader.get_subzones()

        stats = {
            "zones": len(zones),
            "subzones": len(subzones),
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
            if errors:
                print(f"❌ {len(errors)} errors found")
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


@main.command()
@click.option("--start-room", required=True, help="Room ID to use as starting point")
@click.option("--render", type=click.Choice(["tcod", "text", "none"]), default="tcod", help="Rendering backend")
@click.option("--output", help="Output file for map data")
@click.option("--title", default="MythosMUD Map", help="Map title")
@click.option("--validate", is_flag=True, help="Validate rooms before mapping")
@click.pass_context
def map(
    ctx,
    start_room: str,
    render: str,
    output: str | None,
    title: str,
    validate: bool,
):
    """
    Build and render room maps from the MythosMUD world.

    This command loads room data, infers coordinates, and renders
    interactive or static maps using various backends.
    """
    base_path = ctx.obj["base_path"]
    verbose = ctx.obj["verbose"]

    try:
        # Initialize components
        loader = RoomLoader(base_path)
        mapper = RoomMapper()

        if verbose:
            print(f"📁 Loading rooms from {base_path}...")

        # Load rooms
        room_database = loader.build_room_database(show_progress=verbose)

        if not room_database:
            print("❌ No valid rooms found")
            sys.exit(1)

        # Validate if requested
        if validate:
            if verbose:
                print("🔍 Validating rooms before mapping...")
            validator = RoomValidator()
            errors = validator.validate_connectivity(room_database)
            if errors:
                print(f"⚠️  Found {len(errors)} validation errors:")
                for error in errors[:5]:  # Show first 5 errors
                    print(f"  - {error['message']}")
                if len(errors) > 5:
                    print(f"  ... and {len(errors) - 5} more errors")

        # Build map
        if verbose:
            print(f"🗺️  Building map from start room: {start_room}")

        grid, rid_to_coord, messages = mapper.build_map(room_database, start_room)

        if messages:
            print("Info/Warnings from layout:")
            for m in messages:
                print(" - ", m)

        # Output map data if requested
        if output:
            mapper.export_map(grid, "ascii", output)
            print(f"📄 Wrote map to {output}")

        # Render map
        if render == "tcod":
            print("🎮 Launching tcod renderer. Close window or press q/ESC to exit.")
            mapper.render_map(grid, "tcod", title=title)
        elif render == "text":
            mapper.render_map(grid, "text")
        else:
            print("✅ Map built in memory (no rendering requested)")

    except Exception as e:
        if verbose:
            raise
        print(f"❌ Error: {e}")
        sys.exit(1)


@main.command()
@click.option("--connectivity", is_flag=True, help="Analyze room connectivity patterns")
@click.option("--environment", is_flag=True, help="Analyze environment type distribution")
@click.option("--zones", is_flag=True, help="Analyze zone and subzone structure")
@click.option("--format", type=click.Choice(["console", "json", "html"]), default="console")
@click.option("--output", help="Output file for analysis report")
@click.pass_context
def analyze(
    ctx,
    connectivity: bool,
    environment: bool,
    zones: bool,
    format: str,
    output: str | None,
):
    """
    Analyze room data and generate comprehensive reports.

    This command provides detailed analysis of room connectivity,
    environment distribution, and structural patterns.
    """
    base_path = ctx.obj["base_path"]
    verbose = ctx.obj["verbose"]

    try:
        # Initialize components
        loader = RoomLoader(base_path)
        analyzer = RoomAnalyzer()

        if verbose:
            print(f"📁 Loading rooms from {base_path}...")

        # Load rooms
        room_database = loader.build_room_database(show_progress=verbose)

        if not room_database:
            print("❌ No valid rooms found")
            sys.exit(1)

        # Perform analysis
        analysis_results = {}

        if connectivity:
            if verbose:
                print("🔗 Analyzing connectivity patterns...")
            analysis_results["connectivity"] = analyzer.analyze_connectivity(room_database)

        if environment:
            if verbose:
                print("🌍 Analyzing environment distribution...")
            analysis_results["environment"] = analyzer.analyze_environment_distribution(room_database)

        if zones:
            if verbose:
                print("🗺️  Analyzing zone structure...")
            analysis_results["zones"] = analyzer.analyze_zone_structure(room_database)

        # Generate report
        if format == "json":
            report = analyzer.generate_json_report(analysis_results)
        elif format == "html":
            report = analyzer.generate_html_report(analysis_results)
        else:
            report = analyzer.generate_console_report(analysis_results)

        # Output report
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"📄 Analysis report written to {output}")
        else:
            print(report)

    except Exception as e:
        if verbose:
            raise
        print(f"❌ Error: {e}")
        sys.exit(1)


@main.command()
@click.option("--id-mismatches", is_flag=True, help="Fix room ID mismatches")
@click.option("--environment-types", is_flag=True, help="Fix environment type categorization")
@click.option("--intersection-ids", is_flag=True, help="Fix intersection room IDs")
@click.option("--backup", is_flag=True, help="Create backup files before fixing")
@click.option("--dry-run", is_flag=True, help="Show what would be fixed without making changes")
@click.pass_context
def fix(
    ctx,
    id_mismatches: bool,
    environment_types: bool,
    intersection_ids: bool,
    backup: bool,
    dry_run: bool,
):
    """
    Automatically fix common room issues.

    This command can fix various types of room data issues
    including ID mismatches, environment type problems, and more.
    """
    base_path = ctx.obj["base_path"]
    verbose = ctx.obj["verbose"]

    try:
        # Initialize components
        loader = RoomLoader(base_path)
        fixer = RoomFixer(base_path)

        if verbose:
            print(f"📁 Loading rooms from {base_path}...")

        # Load rooms
        room_database = loader.build_room_database(show_progress=verbose)

        if not room_database:
            print("❌ No valid rooms found")
            sys.exit(1)

        # Apply fixes
        fix_results = {}

        if id_mismatches:
            if verbose:
                print("🔧 Fixing room ID mismatches...")
            fix_results["id_mismatches"] = fixer.fix_id_mismatches(room_database, backup=backup, dry_run=dry_run)

        if environment_types:
            if verbose:
                print("🌍 Fixing environment type categorization...")
            fix_results["environment_types"] = fixer.fix_environment_types(
                room_database, backup=backup, dry_run=dry_run
            )

        if intersection_ids:
            if verbose:
                print("🚦 Fixing intersection room IDs...")
            fix_results["intersection_ids"] = fixer.fix_intersection_ids(room_database, backup=backup, dry_run=dry_run)

        # Report results
        total_fixes = sum(result.get("fixes_applied", 0) for result in fix_results.values())
        total_failed = sum(result.get("fixes_failed", 0) for result in fix_results.values())

        if dry_run:
            print(f"🔍 Dry run complete: {total_fixes} fixes would be applied")
        else:
            print(f"✅ Applied {total_fixes} fixes")
            if total_failed > 0:
                print(f"⚠️  {total_failed} fixes failed")

        # Show detailed results
        for fix_type, result in fix_results.items():
            if result.get("fixes_applied", 0) > 0:
                print(f"  {fix_type}: {result['fixes_applied']} fixes applied")
                for fix in result.get("applied_fixes", [])[:3]:  # Show first 3
                    print(f"    ✅ {fix}")
                if len(result.get("applied_fixes", [])) > 3:
                    print(f"    ... and {len(result['applied_fixes']) - 3} more")

    except Exception as e:
        if verbose:
            raise
        print(f"❌ Error: {e}")
        sys.exit(1)


@main.command()
@click.option("--zone", help="Generate report for specific zone")
@click.option("--format", type=click.Choice(["console", "json", "html"]), default="console")
@click.option("--output", help="Output file for report")
@click.option("--include-maps", is_flag=True, help="Include map visualizations in report")
@click.pass_context
def report(
    ctx,
    zone: str | None,
    format: str,
    output: str | None,
    include_maps: bool,
):
    """
    Generate comprehensive room reports.

    This command creates detailed reports including validation results,
    analysis data, and optional map visualizations.
    """
    base_path = ctx.obj["base_path"]
    verbose = ctx.obj["verbose"]

    try:
        # Initialize components
        loader = RoomLoader(base_path)
        validator = RoomValidator()
        analyzer = RoomAnalyzer()
        reporter = Reporter(use_colors=not ctx.obj["no_colors"])

        if verbose:
            print(f"📁 Loading rooms from {base_path}...")

        # Load rooms
        room_database = loader.build_room_database(show_progress=verbose)

        if not room_database:
            print("❌ No valid rooms found")
            sys.exit(1)

        # Filter by zone if specified
        if zone:
            zones = loader.get_zones()
            if zone not in zones:
                print(f"❌ Zone '{zone}' not found")
                sys.exit(1)
            room_database = loader.get_rooms_by_zone(zone)
            print(f"🔍 Generating report for zone: {zone} ({len(room_database)} rooms)")

        # Perform validation
        if verbose:
            print("🔍 Validating rooms...")
        errors = validator.validate_connectivity(room_database)

        # Perform analysis
        if verbose:
            print("📊 Analyzing room data...")
        analysis = {
            "connectivity": analyzer.analyze_connectivity(room_database),
            "environment": analyzer.analyze_environment_distribution(room_database),
            "zones": analyzer.analyze_zone_structure(room_database),
        }

        # Generate report
        if format == "json":
            report_content = reporter.generate_json_report(room_database, errors, analysis)
        elif format == "html":
            report_content = reporter.generate_html_report(room_database, errors, analysis, include_maps=include_maps)
        else:
            report_content = reporter.generate_console_report(room_database, errors, analysis)

        # Output report
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(report_content)
            print(f"📄 Report written to {output}")
        else:
            print(report_content)

    except Exception as e:
        if verbose:
            raise
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
