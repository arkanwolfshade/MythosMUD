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
from datetime import UTC, datetime


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
            self.timestamp = datetime.now(UTC)


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


@dataclass
class NPCAttacked(BaseEvent):
    """
    Event fired when an NPC attacks a target.

    This event is triggered when an NPC performs an attack action
    against a player or another NPC.
    """

    npc_id: str
    target_id: str
    room_id: str
    damage: int
    attack_type: str = "physical"
    combat_id: str | None = None  # Combat context
    npc_name: str | None = None  # NPC name for combat messages
    target_name: str | None = None  # Target name for combat messages

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "NPCAttacked"


@dataclass
class NPCTookDamage(BaseEvent):
    """
    Event fired when an NPC takes damage.

    This event is triggered when an NPC receives damage from
    any source (player attack, environmental, etc.).
    """

    npc_id: str
    room_id: str
    damage: int
    damage_type: str = "physical"
    source_id: str | None = None  # ID of the entity that caused the damage
    combat_id: str | None = None  # Combat context
    npc_name: str | None = None  # NPC name for combat messages
    current_hp: int | None = None  # Current HP after damage
    max_hp: int | None = None  # Maximum HP

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "NPCTookDamage"


@dataclass
class NPCDied(BaseEvent):
    """
    Event fired when an NPC dies.

    This event is triggered when an NPC's health reaches zero
    or when it is otherwise removed from the game world.
    """

    npc_id: str
    room_id: str
    cause: str = "unknown"  # How the NPC died
    killer_id: str | None = None  # ID of the entity that killed the NPC
    combat_id: str | None = None  # Combat context
    npc_name: str | None = None  # NPC name for combat messages
    xp_reward: int | None = None  # XP reward for killing the NPC

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "NPCDied"


@dataclass
class NPCSpoke(BaseEvent):
    """
    Event fired when an NPC speaks.

    This event is triggered when an NPC communicates with players
    or other NPCs through speech, emotes, or other communication methods.
    """

    npc_id: str
    room_id: str
    message: str
    channel: str = "local"  # Communication channel (local, say, whisper, etc.)
    target_id: str | None = None  # Specific target if whispering or directed speech

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "NPCSpoke"


@dataclass
class NPCListened(BaseEvent):
    """
    Event fired when an NPC receives a message.

    This event is triggered when an NPC hears or receives communication
    from players or other NPCs.
    """

    npc_id: str
    room_id: str
    message: str
    speaker_id: str
    channel: str = "local"  # Communication channel

    def __post_init__(self):
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "NPCListened"
