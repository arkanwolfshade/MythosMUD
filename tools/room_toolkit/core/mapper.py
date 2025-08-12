"""
Room Mapper

Enhanced map building and rendering capabilities.
Consolidates functionality from the original mapbuilder.
"""

import json
from typing import Any

# Try optional imports
try:
    import tcod

    TCOD_AVAILABLE = True
except ImportError:
    tcod = None
    TCOD_AVAILABLE = False

try:
    from rich import print as rprint
    from rich.console import Console

    RICH_AVAILABLE = True
except ImportError:
    rprint = print
    Console = None
    RICH_AVAILABLE = False


# MythosMUD-specific tile palette for urban Arkham City
DEFAULT_TILE_MAP = {
    # Urban Streets
    "street_paved": {"glyph": "=", "fg": (128, 128, 128), "bg": (0, 0, 0)},
    "street_cobblestone": {"glyph": "≈", "fg": (100, 100, 100), "bg": (0, 0, 0)},
    "alley": {"glyph": "|", "fg": (80, 80, 80), "bg": (0, 0, 0)},
    "intersection": {"glyph": "+", "fg": (150, 150, 150), "bg": (0, 0, 0)},
    "plaza": {"glyph": "□", "fg": (120, 120, 120), "bg": (0, 0, 0)},
    # Buildings
    "building_exterior": {"glyph": "█", "fg": (139, 69, 19), "bg": (0, 0, 0)},
    "building_interior": {"glyph": "▒", "fg": (160, 82, 45), "bg": (0, 0, 0)},
    "institution": {"glyph": "▓", "fg": (105, 105, 105), "bg": (0, 0, 0)},
    "residential": {"glyph": "░", "fg": (184, 134, 11), "bg": (0, 0, 0)},
    "commercial": {"glyph": "▄", "fg": (139, 69, 19), "bg": (0, 0, 0)},
    # Natural Areas
    "park": {"glyph": "♠", "fg": (34, 139, 34), "bg": (0, 0, 0)},
    "cemetery": {"glyph": "†", "fg": (169, 169, 169), "bg": (0, 0, 0)},
    "waterfront": {"glyph": "~", "fg": (0, 0, 255), "bg": (0, 0, 0)},
    "hillside": {"glyph": "^", "fg": (139, 69, 19), "bg": (0, 0, 0)},
    # Special Areas
    "campus": {"glyph": "♣", "fg": (0, 100, 0), "bg": (0, 0, 0)},
    "docks": {"glyph": "⚓", "fg": (139, 69, 19), "bg": (0, 0, 0)},
    "industrial": {"glyph": "⚙", "fg": (105, 105, 105), "bg": (0, 0, 0)},
    "abandoned": {"glyph": "☠", "fg": (128, 128, 128), "bg": (0, 0, 0)},
    # Legacy Support
    "outdoors": {"glyph": ".", "fg": (100, 220, 100), "bg": (0, 0, 0)},
    "forest": {"glyph": ".", "fg": (0, 200, 0), "bg": (0, 0, 0)},
    "plains": {"glyph": ",", "fg": (100, 220, 100), "bg": (0, 0, 0)},
    "water": {"glyph": "~", "fg": (0, 0, 255), "bg": (0, 0, 0)},
    "wall": {"glyph": "#", "fg": (139, 69, 19), "bg": (0, 0, 0)},
    "cave": {"glyph": "^", "fg": (150, 150, 150), "bg": (0, 0, 0)},
    "default": {"glyph": "?", "fg": (255, 255, 255), "bg": (0, 0, 0)},
}


class RoomMapper:
    """Enhanced map building with validation integration"""

    def __init__(self):
        self.tile_map = DEFAULT_TILE_MAP

    def build_map(
        self, rooms: dict[str, dict[str, Any]], start_room: str
    ) -> tuple[dict[tuple[int, int], dict[str, Any]], dict[str, tuple[int, int]], list[str]]:
        """Build coordinate map with validation"""
        from .loader import RoomLoader

        # Use the loader's coordinate inference
        loader = RoomLoader("")  # Empty path since we already have rooms
        loader._room_cache = rooms  # Set the cache directly

        rooms_with_coords, coords, messages = loader.load_with_coordinates(start_room)

        # Build tile grid
        grid, rid_to_coord = self._build_tile_grid(rooms_with_coords, coords)

        return grid, rid_to_coord, messages

    def _build_tile_grid(
        self, rooms: dict[str, dict[str, Any]], coords: dict[str, tuple[int, int]]
    ) -> tuple[dict[tuple[int, int], dict[str, Any]], dict[str, tuple[int, int]]]:
        """Build coordinate -> tile mapping"""
        grid: dict[tuple[int, int], dict[str, Any]] = {}
        rid_to_coord: dict[str, tuple[int, int]] = {}

        for rid, room in rooms.items():
            if rid not in coords:
                continue

            c = coords[rid]
            rid_to_coord[rid] = c

            env = room.get("environment") or room.get("terrain")
            tile_def = self.tile_map.get(env, self.tile_map.get("default"))

            grid[c] = {
                "rid": rid,
                "glyph": tile_def["glyph"],
                "fg": tile_def["fg"],
                "bg": tile_def["bg"],
                "name": room.get("name", rid),
            }

        return grid, rid_to_coord

    def compute_bounds(self, grid: dict[tuple[int, int], Any]) -> tuple[int, int, int, int]:
        """Compute bounding box of the grid"""
        if not grid:
            return 0, 0, 0, 0

        xs = [x for x, y in grid.keys()]
        ys = [y for x, y in grid.keys()]
        return min(xs), max(xs), min(ys), max(ys)

    def render_map(
        self, grid: dict[tuple[int, int], dict[str, Any]], render_type: str, title: str = "MythosMUD Map"
    ) -> None:
        """Render map with multiple backends"""
        if render_type == "tcod":
            self._render_with_tcod(grid, title)
        elif render_type == "text":
            self._render_text(grid)
        else:
            raise ValueError(f"Unknown render type: {render_type}")

    def _render_with_tcod(self, grid: dict[tuple[int, int], dict[str, Any]], title: str) -> None:
        """Render using tcod (preferred)"""
        if not TCOD_AVAILABLE:
            raise RuntimeError("tcod not available; install with `pip install tcod`")

        min_x, max_x, min_y, max_y = self.compute_bounds(grid)
        width = max_x - min_x + 1
        height = max_y - min_y + 1

        # Load tileset with fallbacks
        tileset = None
        for tileset_name in ["dejavu10x10_gs_tc.png", "terminal.png"]:
            try:
                if tileset_name == "dejavu10x10_gs_tc.png":
                    tileset = tcod.tileset.load_tilesheet(tileset_name, 32, 8, tcod.tileset.CHARMAP_TCOD)
                else:
                    tileset = tcod.tileset.load_tilesheet(tileset_name, 16, 16, tcod.tileset.CHARMAP_TCOD)
                break
            except Exception:
                continue

        with tcod.context.new_terminal(columns=width, rows=height, tileset=tileset, title=title, vsync=True) as context:
            console = tcod.console.Console(width, height, order="F")
            console.clear()

            for (x, y), tile in grid.items():
                cx = x - min_x
                cy = y - min_y
                glyph = tile["glyph"]
                fg = tile["fg"]
                bg = tile["bg"]
                console.print(cx, cy, glyph, fg=fg, bg=bg)

            context.present(console)

            # Keep window open until user closes
            while True:
                for event in tcod.event.wait():
                    if event.type == "QUIT":
                        return
                    if event.type == "KEYDOWN":
                        if event.sym in (tcod.event.K_ESCAPE, ord("q")):
                            return

    def _render_text(self, grid: dict[tuple[int, int], dict[str, Any]]) -> None:
        """Fallback textual renderer"""
        if not grid:
            print("No tiles to render")
            return

        min_x, max_x, min_y, max_y = self.compute_bounds(grid)

        rows: list[str] = []
        for y in range(min_y, max_y + 1):
            row_chars = []
            for x in range(min_x, max_x + 1):
                tile = grid.get((x, y))
                if tile:
                    row_chars.append(tile["glyph"])
                else:
                    row_chars.append(" ")
            rows.append("".join(row_chars))

        if RICH_AVAILABLE:
            console = Console()
            console.print("\n".join(rows))
        else:
            print("\n".join(rows))

    def export_map(self, grid: dict[tuple[int, int], dict[str, Any]], format_type: str, output_path: str) -> None:
        """Export map in various formats"""
        if format_type == "ascii":
            self._export_ascii(grid, output_path)
        elif format_type == "json":
            self._export_json(grid, output_path)
        else:
            raise ValueError(f"Unknown export format: {format_type}")

    def _export_ascii(self, grid: dict[tuple[int, int], dict[str, Any]], output_path: str) -> None:
        """Export as ASCII text file"""
        min_x, max_x, min_y, max_y = self.compute_bounds(grid)

        with open(output_path, "w", encoding="utf-8") as f:
            for y in range(min_y, max_y + 1):
                line = ""
                for x in range(min_x, max_x + 1):
                    tile = grid.get((x, y))
                    line += tile["glyph"] if tile else " "
                f.write(line + "\n")

    def _export_json(self, grid: dict[tuple[int, int], dict[str, Any]], output_path: str) -> None:
        """Export as JSON file"""
        # Convert tuples to strings for JSON serialization
        json_grid = {}
        for coord, tile in grid.items():
            coord_str = f"{coord[0]},{coord[1]}"
            json_grid[coord_str] = tile

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_grid, f, indent=2, ensure_ascii=False)
