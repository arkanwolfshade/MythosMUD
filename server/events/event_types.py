"""
Event types for MythosMUD.

This module defines the event classes used by the event system to track
room state changes, player movements, and other game events. Each event
type contains the relevant data for that specific event.

As documented in the Cultes des Goules, proper categorization of
dimensional events is essential for maintaining the integrity of our
eldritch architecture.
"""

# pylint: disable=too-many-instance-attributes  # Reason: Event dataclasses require many fields to capture complete event state

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID


def _default_timestamp() -> datetime:
    """Factory function for default timestamp."""
    return datetime.now(UTC)


@dataclass
class BaseEvent:
    """
    Base class for all events in the MythosMUD system.

    All events inherit from this class and provide a consistent
    interface for event handling and logging.
    """

    timestamp: datetime = field(default_factory=_default_timestamp, init=False)
    event_type: str = field(default="", init=False)
    sequence_number: int = field(default=0, init=False)

    def __post_init__(self) -> None:
        """Initialize the event timestamp if not already set."""
        # Timestamp is already set by default_factory
        # event_type is set by child classes


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

    def __post_init__(self) -> None:
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

    def __post_init__(self) -> None:
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

    def __post_init__(self) -> None:
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

    def __post_init__(self) -> None:
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

    def __post_init__(self) -> None:
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

    def __post_init__(self) -> None:
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

    def __post_init__(self) -> None:
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
    current_dp: int | None = None  # Current DP after damage
    max_dp: int | None = None  # Maximum DP

    def __post_init__(self) -> None:
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "NPCTookDamage"


@dataclass
class NPCDied(BaseEvent):
    """
    Event fired when an NPC dies.

    This event is triggered when an NPC's determination points reaches zero
    or when it is otherwise removed from the game world.
    """

    npc_id: str
    room_id: str
    cause: str = "unknown"  # How the NPC died
    killer_id: str | None = None  # ID of the entity that killed the NPC
    combat_id: str | None = None  # Combat context
    npc_name: str | None = None  # NPC name for combat messages
    xp_reward: int | None = None  # XP reward for killing the NPC

    def __post_init__(self) -> None:
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

    def __post_init__(self) -> None:
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

    def __post_init__(self) -> None:
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "NPCListened"


@dataclass
class PlayerDPUpdated(BaseEvent):
    """
    Event fired when a player's DP changes.

    This event is triggered when a player takes damage, heals,
    or otherwise has their DP modified.
    """

    player_id: UUID
    old_dp: int
    new_dp: int
    max_dp: int
    damage_taken: int = 0  # Amount of damage taken (negative for healing)
    source_id: str | None = None  # ID of the entity that caused the change
    combat_id: str | None = None  # Combat context if applicable
    room_id: str | None = None  # Room where the change occurred

    def __post_init__(self) -> None:
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "PlayerDPUpdated"


@dataclass
class PlayerMortallyWoundedEvent(BaseEvent):
    """
    Event fired when a player enters mortally wounded state (DP = 0).

    This event is triggered when a player's DP reaches 0 but before they die.
    The player enters a mortally wounded state where they lose 1 DP per tick
    until reaching -10 DP (death).
    """

    player_id: str
    player_name: str
    room_id: str
    attacker_id: str | None = None  # ID of the entity that caused mortally wounded state
    attacker_name: str | None = None  # Name of the attacker
    combat_id: str | None = None  # Combat context if applicable

    def __post_init__(self) -> None:
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "PlayerMortallyWoundedEvent"


@dataclass
class PlayerDPDecayEvent(BaseEvent):
    """
    Event fired when a mortally wounded player loses DP due to decay.

    This event is triggered once per game tick for players in mortally wounded
    state, decreasing their DP by 1 until they reach -10 DP (death).
    """

    player_id: UUID
    old_dp: int
    new_dp: int
    decay_amount: int = 1  # Amount of DP lost due to decay
    room_id: str | None = None  # Room where the decay occurred

    def __post_init__(self) -> None:
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "PlayerDPDecayEvent"


@dataclass
class PlayerDiedEvent(BaseEvent):
    """
    Event fired when a player dies (DP <= -10).

    This event is triggered when a player's DP reaches -10 or below,
    signaling the transition to the death/respawn sequence.
    """

    player_id: UUID
    player_name: str
    room_id: str
    killer_id: str | None = None  # ID of the entity that killed the player
    killer_name: str | None = None  # Name of the killer
    combat_id: str | None = None  # Combat context if applicable
    death_location: str | None = None  # Detailed death location information

    def __post_init__(self) -> None:
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "PlayerDiedEvent"


@dataclass
class PlayerRespawnedEvent(BaseEvent):
    """
    Event fired when a player respawns after death.

    This event is triggered when a player completes the death/respawn sequence
    and returns to the game world at their respawn location.
    """

    player_id: UUID
    player_name: str
    respawn_room_id: str
    old_dp: int
    new_dp: int
    death_room_id: str | None = None  # Where the player died

    def __post_init__(self) -> None:
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "PlayerRespawnedEvent"


@dataclass
class PlayerDeliriumRespawnedEvent(BaseEvent):
    """
    Event fired when a player respawns after delirium.

    This event is triggered when a player completes the delirium/respawn sequence
    and returns to the game world at the Sanitarium with restored lucidity.
    """

    player_id: UUID
    player_name: str
    respawn_room_id: str
    old_lucidity: int
    new_lucidity: int
    delirium_location: str | None = None  # Where the player entered delirium

    def __post_init__(self) -> None:
        """Initialize the event with proper type."""
        super().__post_init__()
        self.event_type = "PlayerDeliriumRespawnedEvent"


@dataclass
class MythosHourTickEvent(BaseEvent):
    """Event fired when the accelerated Mythos clock rolls over to a new hour."""

    mythos_datetime: datetime
    month_name: str
    day_of_month: int
    week_of_month: int
    day_of_week: int
    day_name: str
    season: str
    is_daytime: bool
    is_witching_hour: bool
    daypart: str
    active_holidays: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        super().__post_init__()
        self.event_type = "MythosHourTickEvent"
