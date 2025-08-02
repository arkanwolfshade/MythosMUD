"""
MythosMUD Server Entry Point

This is the main entry point for the MythosMUD server application.
It creates and runs the FastAPI application with all necessary configuration.
"""

# Fix bcrypt warning by monkey patching before importing passlib
try:
    import bcrypt

    if not hasattr(bcrypt, "__about__"):
        bcrypt.__about__ = type("About", (), {"__version__": "4.3.0"})()

except ImportError:
    pass

from .app.factory import create_app
from .app.logging import setup_logging

# Setup logging
setup_logging()

# Create the FastAPI application
app = create_app()


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to MythosMUD!"}
