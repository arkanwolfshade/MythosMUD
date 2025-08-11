"""
MythosMUD Map Builder & Renderer
--------------------------------

Single-file utility that:
- Loads per-room JSON files from a directory
- Optionally validates each room using a user-provided validator function
- Assigns coordinates to rooms (uses explicit coords if present; otherwise
  attempts to lay out rooms by walking exits from a start room using a
  direction-to-delta mapping)
- Detects coordinate conflicts and missing connectivity
- Builds a coordinate -> tile mapping
- Renders the map using `tcod` (preferred) or falls back to a terminal
  text renderer using `rich`.

How to use
----------
1. Put room JSON files in a directory. Each file should contain at least an
   `id` and `exits` map. `coords` are optional—if absent the tool will do a
   BFS from a chosen start room to infer coordinates.

   Minimal room example (room_001.json):
   {
     "id": "room_001",
     "coords": [0, 0],              # optional
     "environment": "forest",
     "exits": {"north": "room_002", "east": "room_010"}
   }

2. Run:
   python mythosmud_map_builder.py --rooms-dir rooms/ --start-room room_001 --render tcod

Dependencies
------------
- python 3.8+
- optional: tcod (`pip install tcod`) for authentic roguelike rendering
- optional: rich (`pip install rich`) as a fallback textual renderer

The script is organized into functions so you can import pieces into your
validator/test harness if you like.

"""

from __future__ import annotations
import argparse
import json
import os
import glob
from collections import deque, defaultdict
from dataclasses import dataclass
from typing import Dict, Tuple, Optional, Any, Callable, List

# Try optional imports
try:
    import tcod
    TCOD_AVAILABLE = True
except Exception:
    tcod = None
    TCOD_AVAILABLE = False

try:
    from rich import print as rprint
    from rich.console import Console
    RICH_AVAILABLE = True
except Exception:
    rprint = print
    Console = None
    RICH_AVAILABLE = False


# --- Types ---
Coord = Tuple[int, int]
RoomID = str


# Direction -> delta mapping. 2D only (x, y). Y increases downward for rendering
DIRECTION_DELTAS: Dict[str, Coord] = {
    "north": (0, -1),
    "n": (0, -1),
    "south": (0, 1),
    "s": (0, 1),
    "east": (1, 0),
    "e": (1, 0),
    "west": (-1, 0),
    "w": (-1, 0),
    "up": (0, -1),    # if you want 3D, replace this or extend
    "down": (0, 1),
}


# Basic tile palette you can expand
DEFAULT_TILE_MAP = {
    "forest": {"glyph": ".", "fg": (0, 200, 0), "bg": (0, 0, 0)},
    "plains": {"glyph": ",", "fg": (100, 220, 100), "bg": (0, 0, 0)},
    "water": {"glyph": "~", "fg": (0, 0, 255), "bg": (0, 0, 0)},
    "wall": {"glyph": "#", "fg": (139, 69, 19), "bg": (0, 0, 0)},
    "cave": {"glyph": "^", "fg": (150, 150, 150), "bg": (0, 0, 0)},
    "default": {"glyph": "?", "fg": (255, 255, 255), "bg": (0, 0, 0)},
}


# --- Data classes ---
@dataclass
class Room:
    id: RoomID
    exits: Dict[str, RoomID]
    environment: Optional[str] = None
    coords: Optional[Coord] = None
    raw: Dict[str, Any] = None


# --- Loading rooms ---

def load_rooms_from_dir(rooms_dir: str) -> Dict[RoomID, Room]:
    """Load all .json files in a directory and return a map of RoomID -> Room"""
    rooms: Dict[RoomID, Room] = {}
    for fname in sorted(glob.glob(os.path.join(rooms_dir, "*.json"))):
        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Failed to load {fname}: {e}")
            continue

        rid = data.get("id") or os.path.splitext(os.path.basename(fname))[0]
        exits = data.get("exits") or {}
        env = data.get("environment")
        coords = tuple(data["coords"]) if data.get("coords") else None
        room = Room(id=rid, exits=dict(exits), environment=env, coords=coords, raw=data)
        rooms[rid] = room
    return rooms


# --- Validation hook ---

def run_validator_on_rooms(rooms: Dict[RoomID, Room], validator: Optional[Callable[[Room], List[str]]] = None) -> Dict[RoomID, List[str]]:
    """Run user-provided validator function over rooms. It should return a list
    of error strings for each room (empty list if valid). If validator is None,
    returns empty lists."""
    results: Dict[RoomID, List[str]] = {}
    for rid, room in rooms.items():
        if validator:
            try:
                results[rid] = validator(room)
            except Exception as e:
                results[rid] = [f"validator exception: {e}"]
        else:
            results[rid] = []
    return results


# --- Coordinate inference ---

def infer_coordinates(rooms: Dict[RoomID, Room], start_room: Optional[RoomID] = None) -> Tuple[Dict[RoomID, Coord], List[str]]:
    """
    If rooms have coords already, those are used. If some rooms lack coords and
    start_room is provided, do a BFS from start_room following exits to assign
    coordinates using DIRECTION_DELTAS. Returns mapping and a list of conflict/warning messages.
    """
    coords: Dict[RoomID, Coord] = {}
    messages: List[str] = []

    # First, record explicit coords
    for rid, room in rooms.items():
        if room.coords is not None:
            coords[rid] = room.coords

    # If no start room provided, pick any room if needed
    if start_room is None:
        # if all rooms already have coords, we're done
        if len(coords) == len(rooms):
            return coords, messages
        start_room = next(iter(rooms.keys()))
        messages.append(f"No start_room provided; using {start_room} as seed")

    if start_room not in rooms:
        messages.append(f"Start room {start_room} not found in rooms")
        return coords, messages

    # BFS queue seeded with start_room (use its explicit coords if present, else (0,0))
    queue = deque()
    if start_room in coords:
        queue.append(start_room)
    else:
        coords[start_room] = (0, 0)
        queue.append(start_room)

    visited = set(queue)

    while queue:
        cur = queue.popleft()
        cur_coord = coords[cur]
        room = rooms[cur]
        for dir_, dest in room.exits.items():
            if dest not in rooms:
                messages.append(f"Room {cur} has exit to unknown room id {dest}")
                continue
            delta = DIRECTION_DELTAS.get(dir_.lower())
            if delta is None:
                # Unknown direction; don't move coordinates but still connect
                # You could map arbitrary directions to coordinates here
                messages.append(f"Unknown direction '{dir_}' in room {cur}; treating as non-spatial connection")
                # mark dest as visited but don't assign coords if it already has none
                if dest not in coords:
                    coords[dest] = (cur_coord[0], cur_coord[1])
                if dest not in visited:
                    visited.add(dest)
                    queue.append(dest)
                continue

            nx = cur_coord[0] + delta[0]
            ny = cur_coord[1] + delta[1]
            new_coord = (nx, ny)

            if dest in coords:
                if coords[dest] != new_coord:
                    messages.append(f"Coordinate conflict for {dest}: existing {coords[dest]} vs computed {new_coord} from {cur}->{dir_}")
                # still continue BFS from dest if not visited
                if dest not in visited:
                    visited.add(dest)
                    queue.append(dest)
                continue
            else:
                # if coordinate already claimed by another room id, that's a problem
                holder = next((r for r, c in coords.items() if c == new_coord), None)
                if holder is not None:
                    messages.append(f"Spatial collision: {dest} would be placed at {new_coord}, but {holder} already occupies it")
                    # still assign but mark the issue
                    # choose not to overwrite holder
                    # assign dest to new_coord with a suffix? For now, assign and record.
                    coords[dest] = new_coord
                else:
                    coords[dest] = new_coord
                if dest not in visited:
                    visited.add(dest)
                    queue.append(dest)

    # After BFS, there may be rooms with no coords (disconnected). Leave them absent.
    disconnected = [rid for rid in rooms.keys() if rid not in coords]
    if disconnected:
        messages.append(f"{len(disconnected)} rooms disconnected (no coords assigned). Example: {disconnected[:5]}")

    return coords, messages


# --- Build grid mapping ---

def build_tile_grid(rooms: Dict[RoomID, Room], coords: Dict[RoomID, Coord], tile_map: Dict[str, Dict[str, Any]] = None) -> Tuple[Dict[Coord, Dict[str, Any]], Dict[str, Coord]]:
    """Return coord->tile info and roomid->coord mapping"""
    tile_map = tile_map or DEFAULT_TILE_MAP
    grid: Dict[Coord, Dict[str, Any]] = {}
    rid_to_coord: Dict[str, Coord] = {}

    for rid, room in rooms.items():
        if rid not in coords:
            continue
        c = coords[rid]
        rid_to_coord[rid] = c
        env = room.environment or room.raw.get("terrain") if room.raw else None
        tile_def = tile_map.get(env, tile_map.get("default"))
        grid[c] = {
            "rid": rid,
            "glyph": tile_def["glyph"],
            "fg": tile_def["fg"],
            "bg": tile_def["bg"],
            "name": room.raw.get("name") if room.raw else rid,
        }
    return grid, rid_to_coord


# --- Rendering ---

def compute_bounds(grid: Dict[Coord, Any]) -> Tuple[int, int, int, int]:
    xs = [x for x, y in grid.keys()]
    ys = [y for x, y in grid.keys()]
    return min(xs), max(xs), min(ys), max(ys)


def render_with_tcod(grid: Dict[Coord, Dict[str, Any]], title: str = "Map") -> None:
    if not TCOD_AVAILABLE:
        raise RuntimeError("tcod not available; install with `pip install tcod`")

    min_x, max_x, min_y, max_y = compute_bounds(grid)
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Load a tileset. tcod ships with a sample, but we try to use a bundled font.
    # If not available, tcod can render ASCII fonts from system fonts but that is
    # platform dependent. We'll try a typical fallback that often works.
    try:
        tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    except Exception:
        # Fallback to builtin font if present
        try:
            tileset = tcod.tileset.get_default()
        except Exception:
            tileset = None

    with tcod.context.new_terminal(width, height, tileset=tileset, title=title, vsync=True) as context:
        console = tcod.Console(width, height, order="F")
        console.clear()
        for (x, y), tile in grid.items():
            cx = x - min_x
            cy = y - min_y
            glyph = tile["glyph"]
            fg = tile["fg"]
            bg = tile["bg"]
            console.print(cx, cy, glyph, fg=fg, bg=bg)
        context.present(console)
        # keep window open until user closes
        while True:
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    return
                if event.type == "KEYDOWN":
                    if event.sym in (tcod.event.K_ESCAPE, ord("q")):
                        return


def render_text(grid: Dict[Coord, Dict[str, Any]]) -> None:
    """Fallback textual renderer using simple printing or rich if available."""
    if not grid:
        print("No tiles to render")
        return
    min_x, max_x, min_y, max_y = compute_bounds(grid)
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    rows: List[str] = []
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


# --- Utility outputs for debugging ---

def dump_ascii_to_file(grid: Dict[Coord, Dict[str, Any]], out_path: str) -> None:
    min_x, max_x, min_y, max_y = compute_bounds(grid)
    with open(out_path, "w", encoding="utf-8") as f:
        for y in range(min_y, max_y + 1):
            line = ""
            for x in range(min_x, max_x + 1):
                tile = grid.get((x, y))
                line += tile["glyph"] if tile else " "
            f.write(line + "\n")


# --- CLI glue ---

def example_validator(room: Room) -> List[str]:
    """A tiny example validator; replace with your own validator hook."""
    errors = []
    if not room.id:
        errors.append("missing id")
    if not isinstance(room.exits, dict):
        errors.append("exits must be a dict")
    # add more rules as required
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build and render an ASCII map from per-room JSON files")
    parser.add_argument("--rooms-dir", required=True, help="Directory containing room JSON files")
    parser.add_argument("--start-room", help="Room ID to use as BFS seed when inferring coords")
    parser.add_argument("--render", choices=["tcod", "text", "none"], default="tcod", help="Rendering backend")
    parser.add_argument("--dump-ascii", help="Write ASCII map to a file")
    parser.add_argument("--validate", action="store_true", help="Run example validator on rooms and print summary")
    args = parser.parse_args(argv)

    rooms = load_rooms_from_dir(args.rooms_dir)
    if not rooms:
        print(f"No rooms loaded from {args.rooms_dir}")
        return

    if args.validate:
        results = run_validator_on_rooms(rooms, example_validator)
        bad = {rid: errs for rid, errs in results.items() if errs}
        if bad:
            print(f"Validator found issues in {len(bad)} rooms:")
            for rid, errs in bad.items():
                print(f" - {rid}: {errs}")
        else:
            print("Validator found no problems (example validator).")

    coords_map, messages = infer_coordinates(rooms, start_room=args.start_room)
    if messages:
        print("Info/Warnings from layout:")
        for m in messages:
            print(" - ", m)

    grid, rid_to_coord = build_tile_grid(rooms, coords_map)

    if args.dump_ascii:
        dump_ascii_to_file(grid, args.dump_ascii)
        print(f"Wrote ASCII map to {args.dump_ascii}")

    if args.render == "tcod":
        if TCOD_AVAILABLE:
            print("Launching tcod renderer. Close window or press q/ESC to exit.")
            render_with_tcod(grid, title="MythosMUD Map")
        else:
            print("tcod not installed — falling back to text renderer.")
            render_text(grid)
    elif args.render == "text":
        render_text(grid)
    else:
        print("No rendering requested. Map built in memory.")


if __name__ == "__main__":
    main()
