"""
ASCII map renderer for MythosMUD.

This module provides server-side rendering of ASCII maps with context-aware
styling. Maps are rendered as HTML strings with CSS colors for display in
the client.

As documented in the Pnakotic Manuscripts, proper spatial visualization
is essential for navigating the eldritch architecture of our world.
"""

# pylint: disable=too-few-public-methods,too-many-locals,too-many-arguments,too-many-positional-arguments  # Reason: Renderer class with focused responsibility, minimal public interface, and complex rendering logic requiring many parameters

from typing import Any, cast

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class AsciiMapRenderer:
    """
    Renders ASCII maps from room coordinate data.

    Supports multiple map styles (world, city, interior) with context-aware
    symbol assignment and exit representation.
    """

    def __init__(self):
        """Initialize the ASCII map renderer."""
        # Symbol sets for different environments
        self.symbols = {
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

        # Exit type symbols
        self.exit_symbols = {
            "door": "D",
            "path": "-",
            "road": "-",
            "stairs": "/",
            "portal": "O",
        }

        # CSS color classes for different styles
        self.style_colors = {
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

    def _build_exit_lookup(self, rooms: list[dict[str, Any]]) -> dict[tuple[int, int], dict[str, dict[str, Any]]]:
        """Build exit lookup map from room data."""
        exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]] = {}
        for room in rooms:
            room_id = room.get("id") or room.get("stable_id", "")
            map_x = room.get("map_x")
            map_y = room.get("map_y")
            if map_x is None or map_y is None:
                continue
            x = int(map_x)
            y = int(map_y)
            exits = room.get("exits", {})
            for direction, target_id in exits.items():
                target_id_str = str(target_id) if target_id else ""
                target_room = next(
                    (r for r in rooms if str(r.get("id") or r.get("stable_id", "")) == target_id_str), None
                )
                if target_room:
                    target_x = target_room.get("map_x")
                    target_y = target_room.get("map_y")
                    if target_x is not None and target_y is not None:
                        tx, ty = int(target_x), int(target_y)
                        target_exits = target_room.get("exits", {})
                        reverse_dir = self._get_reverse_direction(direction)
                        is_bidirectional = reverse_dir in target_exits and target_exits[reverse_dir] == room_id
                        if (x, y) not in exit_from:
                            exit_from[(x, y)] = {}
                        exit_from[(x, y)][direction] = {"target": (tx, ty), "is_bidirectional": is_bidirectional}
        return exit_from

    def _auto_center_viewport(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Viewport centering requires many parameters for context and viewport calculations
        self,
        current_room_id: str | None,
        room_positions: dict[str, tuple[int, int]],
        viewport_width: int,
        viewport_height: int,
        viewport_x: int,
        viewport_y: int,
    ) -> tuple[int, int]:
        """Auto-center viewport on current room if provided."""
        current_id_str = str(current_room_id) if current_room_id else None
        if current_id_str and current_id_str in room_positions:
            player_x, player_y = room_positions[current_id_str]
            return player_x - viewport_width // 2, player_y - viewport_height // 2
        return viewport_x, viewport_y

    def _render_room_row(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Room row rendering requires many parameters for context and rendering logic
        self,
        y: int,
        grid: dict[tuple[int, int], dict[str, Any] | str],
        exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]],
        map_style: str,
        viewport_x: int,
        viewport_width: int,
    ) -> str:
        """Render a single row of rooms with horizontal exits."""
        line = []
        for x in range(viewport_x, viewport_x + viewport_width):
            cell = grid.get((x, y), " ")
            if isinstance(cell, dict):
                symbol = cell.get("symbol", " ")
                is_player = cell.get("is_player", False)
                room_name = cell.get("room_name", "")
                style = self.style_colors[map_style]["player"] if is_player else self.style_colors[map_style]["room"]
                title_attr = f' title="{room_name}"' if room_name else ""
                line.append(f'<span style="{style}"{title_attr}>{symbol}</span>')
                exit_char = self._get_horizontal_exit_char(x, y, exit_from, grid, viewport_x, viewport_width)
                if exit_char:
                    exit_style = self.style_colors[map_style]["exit"]
                    line.append(f'<span style="{exit_style}">{exit_char}</span>')
                else:
                    line.append(" ")
            else:
                line.append("  ")
        return "".join(line)

    def _render_exit_row(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Exit row rendering requires many parameters for context and rendering logic
        self,
        y: int,
        grid: dict[tuple[int, int], dict[str, Any] | str],
        exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]],
        map_style: str,
        viewport_x: int,
        viewport_width: int,
        viewport_y: int,
        viewport_height: int,
    ) -> str:
        """Render a single row of vertical exits between room rows."""
        if y >= viewport_y + viewport_height - 1:
            return ""
        exit_line = []
        for x in range(viewport_x, viewport_x + viewport_width):
            cell = grid.get((x, y), " ")
            next_cell = grid.get((x, y + 1), " ")
            if isinstance(cell, dict) and isinstance(next_cell, dict):
                exit_char = self._get_vertical_exit_char(x, y, exit_from, grid, viewport_y, viewport_height)
                if exit_char:
                    exit_style = self.style_colors[map_style]["exit"]
                    exit_line.append(f'<span style="{exit_style}">{exit_char}</span>')
                    exit_line.append(" ")
                else:
                    exit_line.append("  ")
            else:
                exit_line.append("  ")
        return "".join(exit_line)

    def render_map(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Map rendering requires many parameters for context and rendering logic
        self,
        rooms: list[dict[str, Any]],
        current_room_id: str | None = None,
        viewport_width: int = 80,
        viewport_height: int = 24,
        viewport_x: int = 0,
        viewport_y: int = 0,
    ) -> str:
        """
        Render an ASCII map as HTML.

        Args:
            rooms: List of room dictionaries with coordinates and metadata
            current_room_id: ID of the current room (for player marker)
            viewport_width: Width of viewport in characters (default 80)
            viewport_height: Height of viewport in lines (default 24)
            viewport_x: X offset for viewport (default 0, auto-center if current_room_id provided)
            viewport_y: Y offset for viewport (default 0, auto-center if current_room_id provided)

        Returns:
            HTML string with ASCII map rendered in monospace font
        """
        if not rooms:
            return self._render_empty_map(viewport_width, viewport_height)

        map_style = self._determine_map_style(rooms)
        grid, room_positions = self._build_grid(rooms, current_room_id)
        viewport_x, viewport_y = self._auto_center_viewport(
            current_room_id, room_positions, viewport_width, viewport_height, viewport_x, viewport_y
        )
        exit_from = self._build_exit_lookup(rooms)

        html_lines = []
        html_lines.append('<div class="ascii-map" style="font-family: monospace; white-space: pre; line-height: 1.2;">')

        for y in range(viewport_y, viewport_y + viewport_height):
            html_lines.append(self._render_room_row(y, grid, exit_from, map_style, viewport_x, viewport_width))
            exit_row = self._render_exit_row(
                y, grid, exit_from, map_style, viewport_x, viewport_width, viewport_y, viewport_height
            )
            if exit_row:
                html_lines.append(exit_row)

        html_lines.append("</div>")
        return "\n".join(html_lines)

    def _get_horizontal_exit_char(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Exit character calculation requires many parameters for context and character selection
        self,
        x: int,
        y: int,
        exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]],
        grid: dict[tuple[int, int], dict[str, Any] | str],
        viewport_x: int,
        viewport_width: int,
    ) -> str | None:
        """
        Get exit character to display after a room for horizontal (east/west) exits.

        Args:
            x, y: Current position
            exit_from: Map of exits from each position
            grid: Grid dictionary
            viewport_x: Viewport X offset
            viewport_width: Viewport width

        Returns:
            Exit character to display, or None
        """
        room_exits = exit_from.get((x, y), {})

        # Check for east exit (room to the right)
        next_x = x + 1
        if next_x < viewport_x + viewport_width:
            next_cell = grid.get((next_x, y))
            if isinstance(next_cell, dict):  # There's a room to the east
                # Check if current room has east exit
                east_exit = room_exits.get("east")
                # Check if next room has west exit back
                next_exits = exit_from.get((next_x, y), {})
                west_exit_back = next_exits.get("west")

                if east_exit and east_exit["target"] == (next_x, y):
                    # Current room has east exit
                    if west_exit_back and west_exit_back["target"] == (x, y):
                        # Bidirectional
                        return "—"  # em dash
                    # One-way east
                    return ">"
                if west_exit_back and west_exit_back["target"] == (x, y):
                    # Next room has west exit (one-way west)
                    return "<"

        return None

    def _get_vertical_exit_char(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Exit character calculation requires many parameters for context and character selection
        self,
        x: int,
        y: int,
        exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]],
        grid: dict[tuple[int, int], dict[str, Any] | str],
        viewport_y: int,
        viewport_height: int,
    ) -> str | None:
        """
        Get exit character to display between rows for vertical (north/south) exits.

        Args:
            x, y: Current position (upper room)
            exit_from: Map of exits from each position
            grid: Grid dictionary
            viewport_y: Viewport Y offset
            viewport_height: Viewport height

        Returns:
            Exit character to display, or None
        """
        room_exits = exit_from.get((x, y), {})
        next_y = y + 1

        if next_y < viewport_y + viewport_height:
            next_cell = grid.get((x, next_y), " ")
            if isinstance(next_cell, dict):  # There's a room to the south
                # Check if current room has south exit
                south_exit = room_exits.get("south")
                # Check if next room has north exit back
                next_exits = exit_from.get((x, next_y), {})
                north_exit_back = next_exits.get("north")

                if south_exit and south_exit["target"] == (x, next_y):
                    # Current room has south exit
                    if north_exit_back and north_exit_back["target"] == (x, y):
                        # Bidirectional
                        return "|"
                    # One-way south
                    return "v"
                if north_exit_back and north_exit_back["target"] == (x, y):
                    # Next room has north exit (one-way north)
                    return "^"

        return None

    def _determine_map_style(self, rooms: list[dict[str, Any]]) -> str:
        """
        Determine map style from room data.

        Args:
            rooms: List of room dictionaries

        Returns:
            Style name: "world", "city", or "interior"
        """
        if not rooms:
            return "world"

        # Check for explicit map_style
        for room in rooms:
            map_style = room.get("map_style")
            if map_style is not None and map_style in self.symbols:
                return str(map_style)

        # Check environment
        for room in rooms:
            environment = room.get("environment", "outdoors")
            if environment == "indoors":
                return "interior"
            if environment in ("city", "town"):
                return "city"

        # Default to world
        return "world"

    def _build_grid(
        self, rooms: list[dict[str, Any]], current_room_id: str | None
    ) -> tuple[dict[tuple[int, int], dict[str, Any] | str], dict[str, tuple[int, int]]]:
        """
        Build a coordinate grid from room data.

        Args:
            rooms: List of room dictionaries with map_x, map_y
            current_room_id: ID of current room for player marker

        Returns:
            Tuple of (grid dict, room_positions dict)
        """
        grid: dict[tuple[int, int], dict[str, Any] | str] = {}
        room_positions: dict[str, tuple[int, int]] = {}

        map_style = self._determine_map_style(rooms)

        for room in rooms:
            # Get room ID - try both id and stable_id, convert to string for comparison
            room_id = room.get("id") or room.get("stable_id", "")
            if room_id:
                room_id = str(room_id)  # Ensure string for comparison
            map_x = room.get("map_x")
            map_y = room.get("map_y")

            if map_x is None or map_y is None:
                continue

            x = int(map_x)
            y = int(map_y)
            room_positions[room_id] = (x, y)

            # Determine symbol
            symbol = self._get_room_symbol(room, map_style)
            # Compare with current_room_id (convert to string if needed)
            current_id_str = str(current_room_id) if current_room_id else ""
            is_player = room_id == current_id_str

            grid[(x, y)] = {
                "symbol": symbol,
                "is_player": is_player,
                "room_id": room_id,
                "room_name": room.get("name", ""),
            }

            # Exits are now handled during rendering, not in grid building

        return grid, room_positions

    def _get_room_symbol(self, room: dict[str, Any], map_style: str) -> str:
        """
        Get ASCII symbol for a room.

        Args:
            room: Room dictionary
            map_style: Current map style

        Returns:
            ASCII character for the room
        """
        # Use admin-set symbol if available
        map_symbol: str | None = cast(str | None, room.get("map_symbol"))
        if map_symbol:
            return map_symbol

        # Auto-assign based on room type and style
        room_name = room.get("name", "").lower()
        stable_id = room.get("stable_id", "").lower()

        # Check for intersection
        if "intersection" in room_name or "intersection" in stable_id:
            return self.symbols[map_style].get("intersection", "+")

        # Check for building
        if "building" in room_name or any(
            building_word in room_name for building_word in ["house", "shop", "store", "inn"]
        ):
            return self.symbols[map_style].get("building", "[")

        # Default symbol
        return self.symbols[map_style].get("default", ".")

    def _get_reverse_direction(self, direction: str) -> str:
        """
        Get reverse direction for checking bidirectional exits.

        Args:
            direction: Exit direction

        Returns:
            Reverse direction name
        """
        direction_lower = direction.lower()
        reverse_map = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east",
            "northeast": "southwest",
            "northwest": "southeast",
            "southeast": "northwest",
            "southwest": "northeast",
            "up": "down",
            "down": "up",
            "in": "out",
            "out": "in",
        }
        return reverse_map.get(direction_lower, "")

    def _render_empty_map(self, width: int, height: int) -> str:
        """
        Render an empty map.

        Args:
            width: Viewport width
            height: Viewport height

        Returns:
            HTML string with empty map
        """
        html_lines = []
        html_lines.append('<div class="ascii-map" style="font-family: monospace; white-space: pre; line-height: 1.2;">')
        for _ in range(height):
            html_lines.append(" " * width)
        html_lines.append("</div>")
        return "\n".join(html_lines)
