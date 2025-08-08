"""
Reporter for validation results.

This module handles formatting and displaying validation results,
with special consideration for dimensional anomalies and zone transitions.
"""


class Reporter:
    """
    Formats and displays validation results.
    """

    def __init__(self, use_colors: bool = True):
        """
        Initialize the reporter.

        Args:
            use_colors: Whether to use ANSI color codes
        """
        self.use_colors = use_colors

    def print_header(self):
        """Print validator header."""
        print("\n🔍 Room Validator v1.0")
        print("=" * 40)

    def print_room_header(self, room_id: str):
        """Print room header with ID."""
        print(f"\n🏠 {room_id}")

    def print_error(self, message: str):
        """Print error message."""
        print(f"❌ {message}")

    def print_warning(self, message: str):
        """Print warning message."""
        print(f"⚠️  {message}")

    def print_success(self, message: str):
        """Print success message."""
        print(f"✅ {message}")

    def print_progress(self, message: str):
        """Print progress message."""
        print(f"⏳ {message}")

    def print_suggestion(self, message: str):
        """Print suggestion."""
        print(f"   💡 Suggestion: {message}")

    def print_bidirectional_errors(
        self, missing_returns: list[tuple[str, str, str, str, bool]], room_database: dict[str, dict]
    ):
        """
        Print bidirectional connection errors with zone transition awareness.

        Args:
            missing_returns: List of (room_a, dir_a, room_b, dir_b, is_zone_transition) tuples
            room_database: Complete room database for context
        """
        current_room = None

        for room_a, dir_a, room_b, dir_b, is_zone_transition in missing_returns:
            if room_a != current_room:
                current_room = room_a
                self.print_room_header(room_a)

            # Get zone information
            zone_a = room_database[room_a].get("sub_zone", "unknown")
            zone_b = room_database[room_b].get("sub_zone", "unknown")

            if is_zone_transition:
                self.print_error(
                    f"Zone Transition: Exit '{dir_a}' → {room_b} ({zone_a} → {zone_b}), "
                    f"but {room_b} has no '{dir_b}' return"
                )
            else:
                self.print_error(f"Bidirectional: Exit '{dir_a}' → {room_b}, but {room_b} has no '{dir_b}' return")

            self.print_suggestion(f'Add "{dir_b}": "{room_a}" to {room_b} or flag as one_way')

    def print_parsing_errors(self, errors: dict[str, list[str]]):
        """Print JSON parsing errors."""
        for file_path, error_list in errors.items():
            self.print_room_header(file_path)
            for error in error_list:
                self.print_error(f"Parse Error: {error}")

    def print_zone_discovery(self, zones: list[str]):
        """Print discovered zones."""
        print(f"\n📍 Discovered {len(zones)} zones:")
        for zone in zones:
            print(f"  - {zone}")

    def print_validation_warnings(self, warnings: list[dict]):
        """Print validation warnings."""
        if warnings:
            print("\n⚠️  Warnings:")
            for warning in warnings:
                print(f"  - {warning['message']}")

    def generate_json_output(self, stats: dict, errors: list[dict], warnings: list[dict]) -> str:
        """Generate JSON output for machine consumption."""
        import json

        return json.dumps({"stats": stats, "errors": errors, "warnings": warnings}, indent=2)

    def print_summary(self, stats: dict):
        """Print validation summary with statistics."""
        print("\n=== Validation Summary ===")
        print(f"Zones: {stats['zones']}")
        print(f"Subzones: {stats['subzones']} (configured: {stats['config_subzones']})")
        print(f"Rooms: {stats['rooms']}")
        print(f"Errors: {stats['errors']}")
        print(f"Warnings: {stats['warnings']}")

        if stats["success"]:
            self.print_success("All validations passed!")
        else:
            self.print_error("Validation completed with issues.")
