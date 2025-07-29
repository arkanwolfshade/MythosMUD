"""
Reporter for formatted validation output.

This module handles formatting and displaying validation results with
colors and structured output for both console and JSON formats.
"""

import json
from typing import Any

from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init()


class Reporter:
    """
    Formats and displays validation results with colors and structure.

    Provides both console output with colors and structured JSON output
    for programmatic consumption of validation results.
    """

    def __init__(self, use_colors: bool = True):
        """
        Initialize the reporter.

        Args:
            use_colors: Whether to use colored output
        """
        self.use_colors = use_colors

    def format_error(self, error_type: str, room_id: str, message: str, suggestion: str = "") -> str:
        """
        Format a single error message.

        Args:
            error_type: Type of error (e.g., 'bidirectional', 'unreachable')
            room_id: Room ID where error occurred
            message: Error message
            suggestion: Optional suggestion for fixing the error

        Returns:
            Formatted error string
        """
        if self.use_colors:
            room_part = f"{Fore.RED}🏠 {room_id}{Style.RESET_ALL}"
            error_part = f"{Fore.RED}❌ {error_type.title()}:{Style.RESET_ALL} {message}"

            if suggestion:
                suggestion_part = f"{Fore.YELLOW}💡 Suggestion: {suggestion}{Style.RESET_ALL}"
                return f"{room_part}\n  {error_part}\n     {suggestion_part}"
            else:
                return f"{room_part}\n  {error_part}"
        else:
            room_part = f"🏠 {room_id}"
            error_part = f"❌ {error_type.title()}: {message}"

            if suggestion:
                suggestion_part = f"💡 Suggestion: {suggestion}"
                return f"{room_part}\n  {error_part}\n     {suggestion_part}"
            else:
                return f"{room_part}\n  {error_part}"

    def format_warning(self, warning_type: str, room_id: str, message: str) -> str:
        """
        Format a single warning message.

        Args:
            warning_type: Type of warning
            room_id: Room ID where warning occurred
            message: Warning message

        Returns:
            Formatted warning string
        """
        if self.use_colors:
            room_part = f"{Fore.YELLOW}🏠 {room_id}{Style.RESET_ALL}"
            warning_part = f"{Fore.YELLOW}⚠️  {warning_type.title()}:{Style.RESET_ALL} {message}"
            return f"{room_part}\n  {warning_part}"
        else:
            room_part = f"🏠 {room_id}"
            warning_part = f"⚠️  {warning_type.title()}: {message}"
            return f"{room_part}\n  {warning_part}"

    def print_summary(self, stats: dict[str, Any]) -> None:
        """
        Print validation summary statistics.

        Args:
            stats: Dictionary containing validation statistics
        """
        zones = stats.get("zones", 0)
        rooms = stats.get("rooms", 0)
        errors = stats.get("errors", 0)
        warnings = stats.get("warnings", 0)
        success = stats.get("success", True)

        print("\n📊 SUMMARY:")
        print(f"  Zones: {zones}")
        print(f"  Rooms: {rooms} total")
        print(f"  Errors: {errors} 🔴")
        print(f"  Warnings: {warnings} 🟡")

        if self.use_colors:
            if success:
                print(f"\n{Fore.GREEN}✅ Validation passed{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}❌ Validation failed - please fix errors above{Style.RESET_ALL}")
        else:
            if success:
                print("\n✅ Validation passed")
            else:
                print("\n❌ Validation failed - please fix errors above")

    def print_zone_discovery(self, zones: list[str]) -> None:
        """
        Print discovered zones information.

        Args:
            zones: List of discovered zone names
        """
        print("📁 Scanning zones...")

        for zone in zones:
            if self.use_colors:
                print(f"✅ {Fore.GREEN}{zone}{Style.RESET_ALL} zone discovered")
            else:
                print(f"✅ {zone} zone discovered")

    def print_parsing_errors(self, parsing_errors: list[tuple]) -> None:
        """
        Print parsing errors encountered during file loading.

        Args:
            parsing_errors: List of (file_path, error_message) tuples
        """
        if not parsing_errors:
            return

        print("\n❌ PARSING ERRORS:")

        for file_path, error_msg in parsing_errors:
            if self.use_colors:
                print(f"  {Fore.RED}{file_path}: {error_msg}{Style.RESET_ALL}")
            else:
                print(f"  {file_path}: {error_msg}")

    def print_validation_errors(self, errors: list[dict]) -> None:
        """
        Print validation errors.

        Args:
            errors: List of error dictionaries
        """
        if not errors:
            return

        print("\n❌ ERRORS FOUND:")

        for error in errors:
            formatted = self.format_error(
                error.get("type", "unknown"),
                error.get("room_id", "unknown"),
                error.get("message", ""),
                error.get("suggestion", ""),
            )
            print(f"\n{formatted}")

    def print_validation_warnings(self, warnings: list[dict]) -> None:
        """
        Print validation warnings.

        Args:
            warnings: List of warning dictionaries
        """
        if not warnings:
            return

        print("\n⚠️  WARNINGS:")

        for warning in warnings:
            formatted = self.format_warning(
                warning.get("type", "unknown"), warning.get("room_id", "unknown"), warning.get("message", "")
            )
            print(f"\n{formatted}")

    def generate_json_output(self, stats: dict[str, Any], errors: list[dict], warnings: list[dict]) -> str:
        """
        Generate JSON output for programmatic consumption.

        Args:
            stats: Validation statistics
            errors: List of error dictionaries
            warnings: List of warning dictionaries

        Returns:
            JSON string representation of validation results
        """
        output = {"summary": stats, "errors": errors, "warnings": warnings}

        return json.dumps(output, indent=2)

    def colorize_output(self, text: str, color: str) -> str:
        """
        Apply color to text output.

        Args:
            text: Text to colorize
            color: Color name ('red', 'green', 'yellow', 'blue')

        Returns:
            Colorized text string
        """
        if not self.use_colors:
            return text

        color_map = {"red": Fore.RED, "green": Fore.GREEN, "yellow": Fore.YELLOW, "blue": Fore.BLUE}

        color_code = color_map.get(color.lower(), "")
        return f"{color_code}{text}{Style.RESET_ALL}"

    def print_header(self, title: str = "Room Validator v1.0") -> None:
        """
        Print validator header.

        Args:
            title: Title to display
        """
        if self.use_colors:
            print(f"{Fore.CYAN}🔍 {title}{Style.RESET_ALL}")
        else:
            print(f"🔍 {title}")

    def print_progress(self, message: str) -> None:
        """
        Print progress message.

        Args:
            message: Progress message to display
        """
        if self.use_colors:
            print(f"{Fore.BLUE}🔄 {message}{Style.RESET_ALL}")
        else:
            print(f"🔄 {message}")

    def print_success(self, message: str) -> None:
        """
        Print success message.

        Args:
            message: Success message to display
        """
        if self.use_colors:
            print(f"{Fore.GREEN}✅ {message}{Style.RESET_ALL}")
        else:
            print(f"✅ {message}")

    def print_error(self, message: str) -> None:
        """
        Print error message.

        Args:
            message: Error message to display
        """
        if self.use_colors:
            print(f"{Fore.RED}❌ {message}{Style.RESET_ALL}")
        else:
            print(f"❌ {message}")

    def print_warning(self, message: str) -> None:
        """
        Print warning message.

        Args:
            message: Warning message to display
        """
        if self.use_colors:
            print(f"{Fore.YELLOW}⚠️  {message}{Style.RESET_ALL}")
        else:
            print(f"⚠️  {message}")
