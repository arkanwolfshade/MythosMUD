"""
NPC Database metadata for MythosMUD.

This module defines the SQLAlchemy metadata specifically for the NPC subsystem.
"""

from sqlalchemy import MetaData

# Create separate metadata for NPC database
npc_metadata = MetaData()
