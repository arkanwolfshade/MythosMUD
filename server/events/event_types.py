"""
Event types for MythosMUD.

This module defines the event classes used by the event system to track
room state changes, player movements, and other game events. Each event
type contains the relevant data for that specific event.

As documented in the Cultes des Goules, proper categorization of
dimensional events is essential for maintaining the integrity of our
eldritch architecture.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseEvent:
    """
    Base class for all events in the MythosMUD system.

    All events inherit from this class and provide a consistent
    interface for event handling and logging.
    """

    timestamp: datetime
    event_type: str

    def __post_init__(self):
        """Set timestamp if not provided."""
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


@dataclass
class PlayerEnteredRoom(BaseEvent):
    """
    Event fired when a player enters a room.

    This event is triggered when a player successfully moves into
    a new room and is added to that room's occupant list.
    """

    player_id: str
    room_id: str
    from_room_id: str | None = None

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "PlayerEnteredRoom"


@dataclass
class PlayerLeftRoom(BaseEvent):
    """
    Event fired when a player leaves a room.

    This event is triggered when a player successfully moves out of
    a room and is removed from that room's occupant list.
    """

    player_id: str
    room_id: str
    to_room_id: str | None = None

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "PlayerLeftRoom"


@dataclass
class ObjectAddedToRoom(BaseEvent):
    """
    Event fired when an object is added to a room.

    This event is triggered when an object is placed or dropped
    in a room and is added to that room's object list.
    """

    object_id: str
    room_id: str
    player_id: str | None = None  # Player who added the object

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "ObjectAddedToRoom"


@dataclass
class ObjectRemovedFromRoom(BaseEvent):
    """
    Event fired when an object is removed from a room.

    This event is triggered when an object is picked up or
    otherwise removed from a room and is removed from that
    room's object list.
    """

    object_id: str
    room_id: str
    player_id: str | None = None  # Player who removed the object

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "ObjectRemovedFromRoom"


@dataclass
class NPCEnteredRoom(BaseEvent):
    """
    Event fired when an NPC enters a room.

    This event is triggered when an NPC successfully moves into
    a room and is added to that room's NPC list.
    """

    npc_id: str
    room_id: str
    from_room_id: str | None = None

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "NPCEnteredRoom"


@dataclass
class NPCLeftRoom(BaseEvent):
    """
    Event fired when an NPC leaves a room.

    This event is triggered when an NPC successfully moves out of
    a room and is removed from that room's NPC list.
    """

    npc_id: str
    room_id: str
    to_room_id: str | None = None

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "NPCLeftRoom"
