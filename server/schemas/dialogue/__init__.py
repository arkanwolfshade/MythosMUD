"""Dialogue Pydantic schemas."""

# pylint: disable=duplicate-code  # Reason: Thin package re-export; mirrors other schema package __init__ patterns

from .dialogue_tree import DialogueNode, DialogueOption, DialogueTree

__all__ = ["DialogueOption", "DialogueNode", "DialogueTree"]
