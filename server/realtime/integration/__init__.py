"""
Integration components for connection management.

This package provides integration with game systems including room events
and initial game state generation.
"""

from .game_state_provider import GameStateProvider
from .room_event_handler import RoomEventHandler

__all__ = ["GameStateProvider", "RoomEventHandler"]
