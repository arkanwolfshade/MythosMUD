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

# Re-export get_persistence and reset_persistence from the module file (server/persistence.py)
# Modern Python pattern: Package re-exports functions from module file for backward compatibility
# This allows both "from server.persistence import get_persistence" (package) and
# direct module access to work correctly
try:
    # Load the module file directly using importlib.util to avoid package/module name conflict
    import importlib.util
    import sys
    from pathlib import Path

    # Get the parent directory (server/)
    _parent_dir = Path(__file__).parent.parent
    _module_file = _parent_dir / "persistence.py"

    if _module_file.exists():
        # Load the module with a unique name to avoid conflicts with this package
        _module_name = "server._persistence_module"
        _spec = importlib.util.spec_from_file_location(_module_name, _module_file)
        if _spec and _spec.loader:
            _persistence_module = importlib.util.module_from_spec(_spec)
            # Set __package__ so relative imports in persistence.py work correctly
            _persistence_module.__package__ = "server"
            _persistence_module.__name__ = _module_name
            sys.modules[_module_name] = _persistence_module
            _spec.loader.exec_module(_persistence_module)

            # Re-export the functions
            if hasattr(_persistence_module, "get_persistence"):
                get_persistence = _persistence_module.get_persistence
            if hasattr(_persistence_module, "reset_persistence"):
                reset_persistence = _persistence_module.reset_persistence
            if hasattr(_persistence_module, "PersistenceLayer"):
                PersistenceLayer = _persistence_module.PersistenceLayer
except Exception as e:
    # If import fails, log the error for debugging but don't fail the package import
    # This allows the package to be imported even if the module file has issues
    import traceback
    import warnings

    # Log the full traceback for debugging
    error_msg = f"Could not import get_persistence from server.persistence module: {type(e).__name__}: {e}"
    warnings.warn(error_msg, ImportWarning, stacklevel=2)
    # Also print to stderr for immediate visibility during test runs
    import sys

    print(f"WARNING: {error_msg}", file=sys.stderr)
    print(f"Traceback: {''.join(traceback.format_exception(type(e), e, e.__traceback__))}", file=sys.stderr)

__all__ = [
    "ContainerData",
    "create_container",
    "get_container",
    "get_containers_by_room_id",
    "get_containers_by_entity_id",
    "get_decayed_containers",
    "update_container",
    "delete_container",
    "create_item_instance",
    "ensure_item_instance",
    "get_item_instance",
    "item_instance_exists",
]

# Add re-exported functions to __all__ if they were successfully imported
if "get_persistence" in globals():
    __all__.append("get_persistence")
if "reset_persistence" in globals():
    __all__.append("reset_persistence")
if "PersistenceLayer" in globals():
    __all__.append("PersistenceLayer")
