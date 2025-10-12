#!/usr/bin/env python3
"""
MythosMUD Server Startup Script

This script starts the uvicorn server with proper configuration,
avoiding PowerShell wildcard expansion issues by using Python's
uvicorn.run() function directly.
"""

import os
import sys
from pathlib import Path

import uvicorn


def main():
    """Start the MythosMUD server with uvicorn."""

    # Set working directory to project root
    project_root = Path(__file__).parent
    os.chdir(project_root)

    # Server configuration
    host = "0.0.0.0"
    port = 54731
    app_module = "server.main:app"

    # Reload configuration with test directory exclusion
    # Using glob patterns as documented in uvicorn settings
    reload_exclude_patterns = [
        "server/tests/*",
        "server/tests/data/*",
        "server/tests/logs/*",
        "server/tests/scripts/*",
        "server/tests/utils/*",
        "server/tests/__pycache__/*",
    ]

    print(f"Starting MythosMUD server on {host}:{port}")
    print(f"App module: {app_module}")
    print(f"Reload exclude patterns: {reload_exclude_patterns}")

    try:
        # Create uvicorn configuration
        # Note: reload_exclude functionality is temporarily disabled due to parameter naming issues
        # The server will still work with hot reload, but test directory changes may trigger restarts
        config = uvicorn.Config(
            app_module,
            host=host,
            port=port,
            reload=True,
            log_level="info",
            access_log=True,
            use_colors=True,
        )

        print("Note: Reload exclude patterns temporarily disabled - test directory changes may trigger restarts")

        # Start uvicorn server with configuration
        server = uvicorn.Server(config)
        server.run()
    except KeyboardInterrupt:
        print("\nServer shutdown requested by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
