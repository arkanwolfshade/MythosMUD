"""
Validation rules for room pathing analysis.

This module contains the rule system for validating room connectivity,
structure, and consistency in the MythosMUD world.
"""

from .base_rule import ValidationRule
from .connectivity_rules import BidirectionalConnectionRule, DeadEndRule, SelfReferenceRule, UnreachableRoomRule
from .structure_rules import DuplicateIDRule, ExitReferenceRule, SchemaValidationRule

__all__ = [
    "ValidationRule",
    "SchemaValidationRule",
    "DuplicateIDRule",
    "ExitReferenceRule",
    "BidirectionalConnectionRule",
    "UnreachableRoomRule",
    "DeadEndRule",
    "SelfReferenceRule",
]
