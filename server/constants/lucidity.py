"""
Shared lucidity values.

Kept free of project imports so persistence, models and game code can all use it without import cycles.
"""

# Lucidity (LCD) a character starts with, and the value used when they have no player_lucidity record yet.
STARTING_LCD: int = 100
