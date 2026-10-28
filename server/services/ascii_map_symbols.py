"""Symbol and colour tables for the ASCII map.

Pure configuration, split out of `ascii_map_renderer.py` to keep that module under its
length limit. `AsciiMapRenderer` assigns these to instance attributes in `__init__`, so
`renderer.symbols` and friends keep working exactly as before.
"""

from __future__ import annotations

# Room symbols per map style. `AsciiMapRenderer._get_room_symbol` falls back to these when
# a room has no stored `map_symbol`, which is the normal case - hard-coding a symbol on
# every room replaces this with a wall of identical marks.
SYMBOLS: dict[str, dict[str, str]] = {
    "world": {
        "default": ".",
        "room": ".",
        "intersection": "+",
        "building": "[",
        "player": "@",
    },
    "city": {
        "default": ".",
        "room": ".",
        "intersection": "+",
        "building": "[",
        "street": "-",
        "player": "@",
    },
    "interior": {
        "default": "#",
        "room": "#",
        "intersection": "+",
        "corridor": "-",
        "player": "@",
    },
}

EXIT_SYMBOLS: dict[str, str] = {
    "door": "D",
    "path": "-",
    "road": "-",
    "stairs": "/",
    "portal": "O",
}

STYLE_COLORS: dict[str, dict[str, str]] = {
    "world": {
        "room": "color: #8B7355;",  # Brown
        "player": "color: #FFD700; font-weight: bold;",  # Gold
        "exit": "color: #654321;",  # Dark brown
    },
    "city": {
        "room": "color: #696969;",  # Dim gray
        "player": "color: #FFD700; font-weight: bold;",  # Gold
        "exit": "color: #808080;",  # Gray
    },
    "interior": {
        "room": "color: #2F4F4F;",  # Dark slate gray
        "player": "color: #FFD700; font-weight: bold;",  # Gold
        "exit": "color: #708090;",  # Slate gray
    },
}
