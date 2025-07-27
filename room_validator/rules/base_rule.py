"""
Base validation rule class.

This module defines the abstract base class for all validation rules
in the room pathing validator system.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class ValidationError:
    """
    Represents a validation error with metadata.

    As documented in the restricted archives, proper error categorization
    is essential for maintaining dimensional mapping integrity.
    """

    def __init__(self, rule_name: str, room_id: str, message: str,
                 suggestion: str = "", error_type: str = "error"):
        """
        Initialize a validation error.

        Args:
            rule_name: Name of the rule that generated this error
            room_id: Room ID where the error occurred
            message: Error message
            suggestion: Optional suggestion for fixing the error
            error_type: Type of error ('error' or 'warning')
        """
        self.rule_name = rule_name
        self.room_id = room_id
        self.message = message
        self.suggestion = suggestion
        self.error_type = error_type

    def to_dict(self) -> Dict:
        """Convert error to dictionary format."""
        return {
            'type': self.rule_name,
            'room_id': self.room_id,
            'message': self.message,
            'suggestion': self.suggestion,
            'error_type': self.error_type
        }

    def __str__(self) -> str:
        """String representation of the error."""
        return f"{self.rule_name}: {self.room_id} - {self.message}"


class ValidationRule(ABC):
    """
    Abstract base class for all validation rules.

    Each rule implements specific validation logic for room connectivity,
    structure, or consistency checks as outlined in the Pnakotic Manuscripts.
    """

    def __init__(self, name: str, description: str):
        """
        Initialize the validation rule.

        Args:
            name: Name of the rule
            description: Description of what the rule validates
        """
        self.name = name
        self.description = description

    @abstractmethod
    def validate(self, room_database: Dict[str, Dict],
                zone_filter: Optional[str] = None) -> List[ValidationError]:
        """
        Validate rooms according to this rule.

        Args:
            room_database: Dictionary mapping room IDs to room data
            zone_filter: Optional zone to filter validation to

        Returns:
            List of ValidationError objects
        """
        pass

    def _filter_rooms_by_zone(self, room_database: Dict[str, Dict],
                             zone_filter: Optional[str]) -> Dict[str, Dict]:
        """
        Filter rooms by zone if specified.

        Args:
            room_database: Dictionary mapping room IDs to room data
            zone_filter: Zone to filter by

        Returns:
            Filtered room database
        """
        if zone_filter is None:
            return room_database

        filtered = {}
        for room_id, room_data in room_database.items():
            if room_data.get('zone') == zone_filter:
                filtered[room_id] = room_data

        return filtered

    def create_error(self, room_id: str, message: str,
                    suggestion: str = "") -> ValidationError:
        """
        Create a validation error for this rule.

        Args:
            room_id: Room ID where error occurred
            message: Error message
            suggestion: Optional suggestion for fixing the error

        Returns:
            ValidationError object
        """
        return ValidationError(self.name, room_id, message, suggestion, "error")

    def create_warning(self, room_id: str, message: str) -> ValidationError:
        """
        Create a validation warning for this rule.

        Args:
            room_id: Room ID where warning occurred
            message: Warning message

        Returns:
            ValidationError object with warning type
        """
        return ValidationError(self.name, room_id, message, "", "warning")

    def get_rule_info(self) -> Dict:
        """
        Get information about this rule.

        Returns:
            Dictionary with rule information
        """
        return {
            'name': self.name,
            'description': self.description
        }
