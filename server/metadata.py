"""
Shared SQLAlchemy metadata for MythosMUD models.

This module provides the shared metadata instance that all models
use to avoid circular imports between database.py and models.
"""

from sqlalchemy import MetaData

# Shared metadata for all models
metadata = MetaData()
