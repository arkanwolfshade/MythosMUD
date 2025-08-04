"""
Uvicorn logging configuration for MythosMUD.

This configuration provides environment-specific logging:
- Development: logs to server/logs/server.log
- Production: logs to logs/server.log (project root)
- Console output: Always enabled for development
"""

from pathlib import Path


# Determine log file based on environment
def get_log_file():
    """Get the appropriate log file path based on environment."""
    # Check if we're in development mode (has .env.local file)
    env_file = Path(".env.local")
    if env_file.exists():
        # Development: use server/logs/server.log
        return "server/logs/server.log"
    else:
        # Production: use logs/server.log (project root)
        return "logs/server.log"


# Ensure log directory exists
log_file = get_log_file()
log_path = Path(log_file)
log_path.parent.mkdir(parents=True, exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": log_file,
            "formatter": "default",
            "level": "INFO",
        },
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.error": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}
