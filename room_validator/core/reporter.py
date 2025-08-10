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

    def print_header(self, title: str = "Room Validator v1.0"):
        """Print validator header."""
        print(f"\n🔍 {title}")
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
        print(f"🔄 {message}")

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

    def print_parsing_errors(self, errors: list[tuple[str, str]]):
        """Print JSON parsing errors."""
        for file_path, error in errors:
            self.print_room_header(file_path)
            self.print_error(f"Parse Error: {error}")

    def print_zone_discovery(self, zones: list[str]):
        """Print discovered zones."""
        print(f"\n📍 Discovered {len(zones)} zones:")
        for zone in zones:
            print(f"  - {zone}")

    def print_validation_warnings(self, warnings: list[dict]):
        """Print validation warnings."""
        if warnings:
            print("\n⚠️  WARNINGS:")
            for warning in warnings:
                self.print_warning(warning.get("message", "Unknown warning"))

    def format_error(self, error_type: str, room_id: str, message: str, suggestion: str = None) -> str:
        """Format an error message."""
        formatted = f"{error_type.upper()}: {room_id} - {message}"
        if suggestion:
            formatted += f" (Suggestion: {suggestion})"
        return formatted

    def format_warning(self, warning_type: str, room_id: str, message: str) -> str:
        """Format a warning message."""
        return f"{warning_type.upper()}: {room_id} - {message}"

    def colorize_output(self, text: str, color: str) -> str:
        """Colorize output text."""
        if not self.use_colors:
            return text

        colors = {"red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m", "blue": "\033[94m", "reset": "\033[0m"}

        return f"{colors.get(color, '')}{text}{colors['reset']}"

    def print_validation_errors(self, errors: list[dict]):
        """Print validation errors."""
        if errors:
            print("\n❌ Errors:")
            for error in errors:
                error_msg = self.format_error(
                    error.get("type", "ERROR"),
                    error.get("room_id", "UNKNOWN"),
                    error.get("message", "Unknown error"),
                    error.get("suggestion"),
                )
                self.print_error(error_msg)

    def generate_json_output(self, stats: dict, errors: list[dict], warnings: list[dict]) -> str:
        """Generate JSON output for machine consumption."""
        import json

        return json.dumps({"stats": stats, "errors": errors, "warnings": warnings}, indent=2)

    def print_summary(self, stats: dict):
        """Print validation summary with statistics."""
        print("\n=== Validation Summary ===")
        print(f"Zones: {stats.get('zones', 0)}")
        print(f"Subzones: {stats.get('subzones', 0)} (configured: {stats.get('config_subzones', 0)})")
        print(f"Rooms: {stats.get('rooms', 0)}")
        print(f"Errors: {stats.get('errors', 0)}")
        print(f"Warnings: {stats.get('warnings', 0)}")

        if stats.get("success", False):
            self.print_success("All validations passed!")
        else:
            self.print_error("Validation completed with issues.")
