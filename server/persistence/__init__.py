"""
Persistence package for MythosMUD.

This package contains persistence utilities for various game systems.
"""

# Import container persistence functions
from .container_persistence import (
    ContainerData,
    create_container,
    delete_container,
    get_container,
    get_containers_by_entity_id,
    get_containers_by_room_id,
    get_decayed_containers,
    update_container,
)

# Import item instance persistence functions
from .item_instance_persistence import (
    create_item_instance,
    ensure_item_instance,
    get_item_instance,
    item_instance_exists,
)

# Import new async repositories (available for gradual migration)
from .repositories import (
    ContainerRepository,
    ExperienceRepository,
    HealthRepository,
    ItemRepository,
    PlayerRepository,
    ProfessionRepository,
    RoomRepository,
)

# NOTE: PersistenceLayer and get_persistence removed - all code now uses AsyncPersistenceLayer
# from server.async_persistence import AsyncPersistenceLayer

__all__ = [
    # Container persistence (legacy functions)
    "ContainerData",
    "create_container",
    "get_container",
    "get_containers_by_room_id",
    "get_containers_by_entity_id",
    "get_decayed_containers",
    "update_container",
    "delete_container",
    # Item persistence (legacy functions)
    "create_item_instance",
    "ensure_item_instance",
    "get_item_instance",
    "item_instance_exists",
    # New async repositories (gradual migration)
    "PlayerRepository",
    "RoomRepository",
    "HealthRepository",
    "ExperienceRepository",
    "ProfessionRepository",
    "ContainerRepository",
    "ItemRepository",
]

# NOTE: Removed PersistenceLayer, get_persistence, and reset_persistence from __all__
# All code now uses AsyncPersistenceLayer from server.async_persistence
