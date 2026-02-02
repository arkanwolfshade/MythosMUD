"""
Dependency Injection Container for MythosMUD.

Re-exports ApplicationContainer and factory functions from the main container module.
Preserves backward compatibility for imports: from server.container import ApplicationContainer.
"""

# Expose submodules for static analysis (pylint E0611). Order: utils, bundles, then main.
import server.container.bundles  # noqa: F401
import server.container.main  # noqa: F401
import server.container.utils  # noqa: F401
from server.container.main import (
    ApplicationContainer,
    get_container,
    reset_container,
)

__all__ = ["ApplicationContainer", "get_container", "reset_container"]
