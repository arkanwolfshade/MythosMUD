"""
ASCII map renderer for MythosMUD.

This module provides server-side rendering of ASCII maps with context-aware
styling. Maps are rendered as HTML strings with CSS colors for display in
the client.

As documented in the Pnakotic Manuscripts, proper spatial visualization
is essential for navigating the eldritch architecture of our world.
"""

# pylint: disable=too-few-public-methods,too-many-locals,too-many-arguments,too-many-positional-arguments  # Reason: Renderer class with focused responsibility, minimal public interface, and complex rendering logic requiring many parameters

from collections.abc import Mapping
from typing import Any, NamedTuple, cast

from ..structured_logging.enhanced_logging_config import get_logger
from . import ascii_map_exits, ascii_map_symbols

logger = get_logger(__name__)

# Characters used to continue an exit across cells that hold no room. These match
# the bidirectional glyphs _horizontal_exit_char_between / _vertical_exit_char_between
# already use, so a spanning exit is indistinguishable from an ordinary one.
_BRIDGE_HORIZONTAL = "—"
_BRIDGE_VERTICAL = "|"

# Marks an exit leading out of the area currently drawn - into another sub-zone or zone.
# A map request is scoped to one sub-zone, so the room on the far side is not loaded and
# cannot be plotted; without this the only way into a building like the Sanitarium simply
# does not appear, and the street corner looks like a dead end.
_DEPARTURE = "*"
_NO_DEPARTURES: dict[tuple[int, int], frozenset[str]] = {}

# Hoisted so it is not a call inside a default-argument expression.
_NO_BRIDGES: frozenset[tuple[int, int]] = frozenset()


class _RoomRowContext(NamedTuple):
    """Viewport and style context for horizontal room row rendering."""

    # Reason: SERIALIZATION_BOUNDARY - grid mirrors _ExitRowContext's identical, unsuppressed
    # field just below (both hold the same grid-cell shape used throughout this module).
    # Appropriate because: a cell is a dict of ad hoc rendering fields (symbol, is_player,
    # room_name), not a schema; matches the module's existing rooms: list[dict[str, Any]].
    grid: dict[tuple[int, int], dict[str, Any] | str]  # pyright: ignore[reportExplicitAny]
    # Reason: SERIALIZATION_BOUNDARY - exit_from mirrors _ExitRowContext's identical,
    # unsuppressed field just below (the same exit-lookup shape used throughout this module).
    # Appropriate because: an exit entry is an ad hoc dict (target coords, bidirectional
    # flag), not a schema; matches the module's existing rooms: list[dict[str, Any]].
    exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]]  # pyright: ignore[reportExplicitAny]
    map_style: str
    viewport_x: int
    viewport_width: int
    # Cells between two rooms joined by one exit; see _build_exit_bridges.
    horizontal_bridges: frozenset[tuple[int, int]] = _NO_BRIDGES
    vertical_bridges: frozenset[tuple[int, int]] = _NO_BRIDGES
    # Rooms with an exit leaving the loaded area; see ascii_map_exits.build_departures.
    departures: dict[tuple[int, int], frozenset[str]] = _NO_DEPARTURES


class _ExitRowContext(NamedTuple):
    """Viewport and style context for vertical exit row rendering."""

    grid: dict[tuple[int, int], dict[str, Any] | str]
    exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]]
    map_style: str
    viewport_x: int
    viewport_width: int
    viewport_y: int
    viewport_height: int
    # Cells between two rooms joined by one exit; see _build_exit_bridges.
    vertical_bridges: frozenset[tuple[int, int]] = _NO_BRIDGES
    # Rooms with an exit leaving the loaded area; see ascii_map_exits.build_departures.
    departures: dict[tuple[int, int], frozenset[str]] = _NO_DEPARTURES


class AsciiMapRenderer:
    """
    Renders ASCII maps from room coordinate data.

    Supports multiple map styles (world, city, interior) with context-aware
    symbol assignment and exit representation.
    """

    def __init__(self) -> None:
        """Initialize the ASCII map renderer."""
        # Tables live in ascii_map_symbols; bound here so `renderer.symbols` still resolves.
        self.symbols = ascii_map_symbols.SYMBOLS
        self.exit_symbols = ascii_map_symbols.EXIT_SYMBOLS
        self.style_colors = ascii_map_symbols.STYLE_COLORS

    def _exit_is_bidirectional(
        self,
        target_room: dict[str, Any],
        direction: str,
        from_room_id: Any,
    ) -> bool:
        """True if target room has a reverse exit back to from_room_id."""
        target_exits = target_room.get("exits", {})
        reverse_dir = self._get_reverse_direction(direction)
        return reverse_dir in target_exits and target_exits[reverse_dir] == from_room_id

    def _resolve_exit_target(
        self,
        rooms: list[dict[str, Any]],
        target_id: Any,
        direction: str,
        from_room_id: Any,
    ) -> tuple[tuple[int, int], bool] | None:
        """
        Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if invalid.
        """
        target_id_str = str(target_id) if target_id else ""
        target_room = next(
            (r for r in rooms if str(r.get("id") or r.get("stable_id", "")) == target_id_str),
            None,
        )
        if not target_room:
            return None
        target_x = target_room.get("map_x")
        target_y = target_room.get("map_y")
        if target_x is None or target_y is None:
            return None
        tx, ty = int(target_x), int(target_y)
        is_bidirectional = self._exit_is_bidirectional(target_room, direction, from_room_id)
        return ((tx, ty), is_bidirectional)

    def _get_exit_entries_for_room(
        self,
        room: dict[str, Any],
        rooms: list[dict[str, Any]],
    ) -> list[tuple[str, tuple[int, int], bool]]:
        """
        Return list of (direction, (target_x, target_y), is_bidirectional) for exits
        from this room that have valid target coordinates.
        """
        room_id = room.get("id") or room.get("stable_id", "")
        exits = room.get("exits", {})
        entries: list[tuple[str, tuple[int, int], bool]] = []
        for direction, target_id in exits.items():
            resolved = self._resolve_exit_target(rooms, target_id, direction, room_id)
            if resolved:
                entries.append((direction, resolved[0], resolved[1]))
        return entries

    def _build_exit_lookup(self, rooms: list[dict[str, Any]]) -> dict[tuple[int, int], dict[str, dict[str, Any]]]:
        """Build exit lookup map from room data."""
        exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]] = {}
        for room in rooms:
            map_x = room.get("map_x")
            map_y = room.get("map_y")
            if map_x is None or map_y is None:
                continue
            x, y = int(map_x), int(map_y)
            for direction, target_coords, is_bidirectional in self._get_exit_entries_for_room(room, rooms):
                if (x, y) not in exit_from:
                    exit_from[(x, y)] = {}
                exit_from[(x, y)][direction] = {
                    "target": target_coords,
                    "is_bidirectional": is_bidirectional,
                }
        return exit_from

    def _build_exit_bridges(
        self, exit_from: Mapping[tuple[int, int], Mapping[str, Mapping[str, object]]]
    ) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
        """Cells lying strictly between two rooms joined by a single exit."""
        return ascii_map_exits.build_exit_bridges(exit_from)

    def _auto_center_viewport(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Viewport centering requires many parameters for context and viewport calculations
        self,
        current_room_id: str | None,
        room_positions: dict[str, tuple[int, int]],
        viewport_width: int,
        viewport_height: int,
        viewport_x: int,
        viewport_y: int,
    ) -> tuple[int, int]:
        """Center viewport on the character's current room so the player is in the middle of the minimap."""
        current_id_str = str(current_room_id) if current_room_id else None
        if current_id_str and current_id_str in room_positions:
            player_x, player_y = room_positions[current_id_str]
            return player_x - viewport_width // 2, player_y - viewport_height // 2
        return viewport_x, viewport_y

    def _render_room_cell_with_room(
        self, x: int, y: int, cell: dict[str, Any], ctx: _RoomRowContext, exit_span: str
    ) -> str:
        """Render one grid cell that holds a room, plus its east-facing exit marker."""
        # cell is built by _build_grid with these exact keys/types (str, bool, str).
        symbol = cast(str, cell.get("symbol", " "))
        is_player = cast(bool, cell.get("is_player", False))
        room_name = cast(str, cell.get("room_name", ""))
        # Use class so client SafeHtml (ALLOWED_ATTR: ['class']) preserves styling
        room_class = "ascii-map-player" if is_player else f"ascii-map-room ascii-map-room-{ctx.map_style}"
        title_attr = f' title="{room_name}"' if room_name else ""
        cell_html = f'<span class="{room_class}"{title_attr}>{symbol}</span>'

        exit_char = self._get_horizontal_exit_char(x, y, ctx.exit_from, ctx.grid, ctx.viewport_x, ctx.viewport_width)
        if not exit_char and (x + 1, y) in ctx.horizontal_bridges:
            # The next cell is not a room but the exit continues through it.
            exit_char = _BRIDGE_HORIZONTAL
        if not exit_char and "east" in ctx.departures.get((x, y), frozenset()):
            exit_char = _DEPARTURE
        exit_html = f"{exit_span}{exit_char}</span>" if exit_char else " "
        return cell_html + exit_html

    def _render_room_cell(self, x: int, y: int, ctx: _RoomRowContext) -> str:
        """Render one cell of a room row: a room, a bridge span, a departure marker, or blank."""
        cell = ctx.grid.get((x, y), " ")
        exit_span = f'<span class="ascii-map-exit ascii-map-exit-{ctx.map_style}">'
        if isinstance(cell, dict):
            return self._render_room_cell_with_room(x, y, cell, ctx, exit_span)
        if (x, y) in ctx.horizontal_bridges:
            # Empty cell inside an east/west span: draw straight through it.
            return f"{exit_span}{_BRIDGE_HORIZONTAL}</span>{exit_span}{_BRIDGE_HORIZONTAL}</span>"
        if (x, y) in ctx.vertical_bridges:
            return f"{exit_span}{_BRIDGE_VERTICAL}</span> "
        if "west" in ctx.departures.get((x + 1, y), frozenset()):
            # The room to the right leaves westward; mark the square beside it.
            return f" {exit_span}{_DEPARTURE}</span>"
        return "  "

    def _render_room_row(self, y: int, ctx: _RoomRowContext) -> str:
        """Render a single row of rooms with horizontal exits."""
        return "".join(
            self._render_room_cell(x, y, ctx) for x in range(ctx.viewport_x, ctx.viewport_x + ctx.viewport_width)
        )

    def _render_exit_row(self, y: int, ctx: _ExitRowContext) -> str:
        """Render a single row of vertical exits between room rows."""
        if y >= ctx.viewport_y + ctx.viewport_height - 1:
            return ""
        exit_line: list[str] = []
        for x in range(ctx.viewport_x, ctx.viewport_x + ctx.viewport_width):
            cell = ctx.grid.get((x, y), " ")
            next_cell = ctx.grid.get((x, y + 1), " ")
            bridged = (x, y) in ctx.vertical_bridges or (x, y + 1) in ctx.vertical_bridges
            # The room above leaving southward, or the room below leaving northward:
            # either way the door sits on this line.
            departing = "south" in ctx.departures.get((x, y), frozenset()) or "north" in ctx.departures.get(
                (x, y + 1), frozenset()
            )
            if isinstance(cell, dict) and isinstance(next_cell, dict):
                exit_char = self._get_vertical_exit_char(
                    x, y, ctx.exit_from, ctx.grid, ctx.viewport_y, ctx.viewport_height
                )
                if exit_char:
                    exit_line.append(f'<span class="ascii-map-exit ascii-map-exit-{ctx.map_style}">{exit_char}</span>')
                    exit_line.append(" ")
                else:
                    exit_line.append("  ")
            elif departing:
                exit_line.append(f'<span class="ascii-map-exit ascii-map-exit-{ctx.map_style}">{_DEPARTURE}</span>')
                exit_line.append(" ")
            elif bridged:
                # One side is an empty cell inside a north/south span - keep the line whole.
                exit_line.append(
                    f'<span class="ascii-map-exit ascii-map-exit-{ctx.map_style}">{_BRIDGE_VERTICAL}</span>'
                )
                exit_line.append(" ")
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
        h_bridges, v_bridges = self._build_exit_bridges(exit_from)
        departures = ascii_map_exits.build_departures(rooms)
        horizontal_bridges = frozenset(h_bridges)
        vertical_bridges = frozenset(v_bridges)

        html_lines = []
        html_lines.append('<div class="ascii-map">')
        room_row_ctx = _RoomRowContext(
            grid, exit_from, map_style, viewport_x, viewport_width, horizontal_bridges, vertical_bridges, departures
        )

        for y in range(viewport_y, viewport_y + viewport_height):
            html_lines.append(self._render_room_row(y, room_row_ctx))
            exit_row = self._render_exit_row(
                y,
                _ExitRowContext(
                    grid,
                    exit_from,
                    map_style,
                    viewport_x,
                    viewport_width,
                    viewport_y,
                    viewport_height,
                    vertical_bridges,
                    departures,
                ),
            )
            if exit_row:
                html_lines.append(exit_row)

        html_lines.append("</div>")
        return "\n".join(html_lines)

    def _horizontal_exit_char_between(
        self,
        east_exit: dict[str, Any] | None,
        west_exit_back: dict[str, Any] | None,
        next_x: int,
        y: int,
        x: int,
    ) -> str | None:
        """Return the horizontal exit character (em dash, >, or <), or None."""
        return ascii_map_exits.horizontal_exit_char_between(east_exit, west_exit_back, next_x, y, x)

    def _get_horizontal_exit_char(
        self,
        x: int,
        y: int,
        exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]],
        grid: dict[tuple[int, int], dict[str, Any] | str],
        viewport_x: int,
        viewport_width: int,
    ) -> str | None:
        """Exit character shown immediately after the room at (x, y), or None."""
        return ascii_map_exits.get_horizontal_exit_char(x, y, exit_from, grid, viewport_x, viewport_width)

    def _vertical_exit_char_between(
        self,
        south_exit: dict[str, Any] | None,
        north_exit_back: dict[str, Any] | None,
        next_y: int,
        x: int,
        y: int,
    ) -> str | None:
        """Return the vertical exit character (|, v, or ^), or None."""
        return ascii_map_exits.vertical_exit_char_between(south_exit, north_exit_back, next_y, x, y)

    def _get_vertical_exit_char(
        self,
        x: int,
        y: int,
        exit_from: dict[tuple[int, int], dict[str, dict[str, Any]]],
        grid: dict[tuple[int, int], dict[str, Any] | str],
        viewport_y: int,
        viewport_height: int,
    ) -> str | None:
        """Exit character shown on the row below the room at (x, y), or None."""
        return ascii_map_exits.get_vertical_exit_char(x, y, exit_from, grid, viewport_y, viewport_height)

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
            # When multiple rooms share the same (x,y), later one overwrites; preserve player
            # highlight so the current room is always shown (log evidence: in_room_positions
            # true but any_is_player false when duplicate coords overwrote the cell).
            existing = grid.get((x, y))
            if isinstance(existing, dict) and existing.get("is_player"):
                is_player = True

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
        """Reverse of `direction`, for checking bidirectional exits."""
        return ascii_map_exits.reverse_direction(direction)

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
        html_lines.append('<div class="ascii-map">')
        for _ in range(height):
            html_lines.append(" " * width)
        html_lines.append("</div>")
        return "\n".join(html_lines)
