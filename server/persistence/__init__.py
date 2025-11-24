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

# Re-export get_persistence and reset_persistence from the module file (server/persistence.py)
# Modern Python pattern: Package re-exports functions from module file for backward compatibility
# This allows both "from server.persistence import get_persistence" (package) and
# direct module access to work correctly
try:
    # Import the module file as a submodule to handle relative imports correctly
    import importlib.util
    import sys
    from pathlib import Path

    # Get the parent directory (server/)
    _parent_dir = Path(__file__).parent.parent
    _module_file = _parent_dir / "persistence.py"

    if _module_file.exists():
        # Load the module with proper package context so relative imports work
        _spec = importlib.util.spec_from_file_location(
            "server.persistence_module", _module_file, submodule_search_locations=[str(_parent_dir)]
        )
        if _spec and _spec.loader:
            # Set package context for relative imports
            if hasattr(_spec.loader, "name"):
                _spec.loader.name = "server.persistence_module"
            _persistence_module = importlib.util.module_from_spec(_spec)
            # Set __package__ so relative imports work
            _persistence_module.__package__ = "server"
            _persistence_module.__name__ = "server.persistence_module"
            sys.modules["server.persistence_module"] = _persistence_module
            _spec.loader.exec_module(_persistence_module)

            # Re-export the functions
            if hasattr(_persistence_module, "get_persistence"):
                get_persistence = _persistence_module.get_persistence
            if hasattr(_persistence_module, "reset_persistence"):
                reset_persistence = _persistence_module.reset_persistence
            if hasattr(_persistence_module, "PersistenceLayer"):
                PersistenceLayer = _persistence_module.PersistenceLayer
except (ImportError, AttributeError, FileNotFoundError):
    # If import fails, functions won't be available - this is OK for some contexts
    pass

__all__ = [
    "ContainerData",
    "create_container",
    "get_container",
    "get_containers_by_room_id",
    "get_containers_by_entity_id",
    "get_decayed_containers",
    "update_container",
    "delete_container",
]

# Add re-exported functions to __all__ if they were successfully imported
if "get_persistence" in globals():
    __all__.append("get_persistence")
if "reset_persistence" in globals():
    __all__.append("reset_persistence")
if "PersistenceLayer" in globals():
    __all__.append("PersistenceLayer")
