"""
Mini-map renderer for room connectivity visualization.

This module provides visual representations of room connectivity graphs
for use in client mini-maps and debugging room layouts.
"""

from typing import Dict, List, Any, Tuple


class MinimapRenderer:
    """
    Renders room connectivity graphs in various visual formats.

    Implements the dimensional mapping visualization techniques described
    in the Pnakotic Manuscripts for eldritch architecture analysis.
    """

    def __init__(self):
        """Initialize the mini-map renderer."""
        self.direction_symbols = {
            "north": "↑",
            "south": "↓",
            "east": "→",
            "west": "←",
            "up": "↗",
            "down": "↘"
        }

        # Street name to acronym mapping
        self.street_acronyms = {
            "E_College_St": "ECS",
            "W_College_St": "WCS",
            "W_Church_St": "WCS",
            "West_St": "WS",
            "Main_St": "MS",
            "Federal_St": "FS",
            "Garrison_St": "GS",
            "Boundary_St": "BS",
            "Peabody_Ave": "PA",
            "Pickman_St": "PS",
            "Washington_St": "WS",
            "Miskatonic_Ave": "MA",
            "Saltonstall_St": "SS",
            "High_St": "HS",
            "East_St": "ES",
            "West_St": "WS",
            "North_St": "NS",
            "South_St": "SS",
            "Church_St": "CS",
            "Curwen_St": "CS",
            "Jenkin_St": "JS",
            "Whateley_St": "WS",
            "Armitage_St": "AS",
            "River_St": "RS",
            "Water_St": "WS",
            "Sentinel_St": "SS",
            "New_St": "NS",
            "Crane_St": "CS",
            "N_French_Hill_St": "NFHS",
            "S_Parsonage_St": "SPS",
            "E_High_St": "EHS",
            "E_Miskatonic_Ave": "EMA",
            "E_Pickman_St": "EPS",
            "E_Saltonstall_St": "ESS",
            "E_Washington_St": "EWS",
            "E_River_St": "ERS",
            "E_Water_St": "EWS",
            "W_High_St": "WHS",
            "W_Miskatonic_Ave": "WMA",
            "W_Pickman_St": "WPS",
            "W_Saltonstall_St": "WSS",
            "W_Washington_St": "WWS",
            "W_River_St": "WRS",
            "W_Water_St": "WWS",
            "S_Peabody_St": "SPS",
            "Powder_Mill_St": "PMS",
            "Walnut_St": "WS",
            "intersection": "INT"
        }

        # Color codes for different streets (ANSI color codes)
        self.street_colors = {
            "E_College_St": "\033[32m",        # Green
            "W_College_St": "\033[36m",        # Cyan
            "W_Church_St": "\033[35m",         # Magenta
            "West_St": "\033[91m",             # Bright Red
            "Main_St": "\033[33m",             # Yellow
            "Federal_St": "\033[35m",          # Magenta
            "Garrison_St": "\033[34m",         # Blue
            "Boundary_St": "\033[31m",         # Red
            "Peabody_Ave": "\033[37m",         # White
            "Pickman_St": "\033[90m",          # Dark Gray
            "Washington_St": "\033[95m",       # Bright Magenta
            "Miskatonic_Ave": "\033[94m",      # Bright Blue
            "Saltonstall_St": "\033[96m",      # Bright Cyan
            "High_St": "\033[93m",             # Bright Yellow
            "East_St": "\033[92m",             # Bright Green
            "West_St": "\033[91m",             # Bright Red
            "North_St": "\033[97m",            # Bright White
            "South_St": "\033[30m",            # Black
            "Church_St": "\033[33m",           # Yellow
            "Curwen_St": "\033[35m",           # Magenta
            "Jenkin_St": "\033[36m",           # Cyan
            "Whateley_St": "\033[32m",         # Green
            "Armitage_St": "\033[34m",         # Blue
            "River_St": "\033[94m",            # Bright Blue
            "Water_St": "\033[96m",            # Bright Cyan
            "Sentinel_St": "\033[95m",         # Bright Magenta
            "New_St": "\033[93m",              # Bright Yellow
            "Crane_St": "\033[92m",            # Bright Green
            "N_French_Hill_St": "\033[90m",    # Dark Gray
            "S_Parsonage_St": "\033[37m",      # White
            "E_High_St": "\033[33m",           # Yellow
            "E_Miskatonic_Ave": "\033[94m",    # Bright Blue
            "E_Pickman_St": "\033[90m",        # Dark Gray
            "E_Saltonstall_St": "\033[96m",    # Bright Cyan
            "E_Washington_St": "\033[95m",     # Bright Magenta
            "E_River_St": "\033[94m",          # Bright Blue
            "E_Water_St": "\033[96m",          # Bright Cyan
            "W_High_St": "\033[33m",           # Yellow
            "W_Miskatonic_Ave": "\033[94m",    # Bright Blue
            "W_Pickman_St": "\033[90m",        # Dark Gray
            "W_Saltonstall_St": "\033[96m",    # Bright Cyan
            "W_Washington_St": "\033[95m",     # Bright Magenta
            "W_River_St": "\033[94m",          # Bright Blue
            "W_Water_St": "\033[96m",          # Bright Cyan
            "S_Peabody_St": "\033[37m",        # White
            "Powder_Mill_St": "\033[90m",      # Dark Gray
            "Walnut_St": "\033[33m",           # Yellow
            "intersection": "\033[93m"         # Bright Yellow
        }

        # Reset color code
        self.color_reset = "\033[0m"

    def get_street_acronym(self, room_id: str) -> str:
        """
        Extract street acronym from room ID.

        Args:
            room_id: Full room ID (e.g., earth_arkham_city_campus_W_College_St_003)

        Returns:
            Street acronym (e.g., ECS)
        """
        # Extract the street name from the room ID
        parts = room_id.split('_')
        if len(parts) >= 4:
            # Look for street name patterns
            for i in range(len(parts) - 1):
                potential_street = '_'.join(parts[i:i+2])
                if potential_street in self.street_acronyms:
                    return self.street_acronyms[potential_street]

                # Try with more parts for longer street names
                if i + 2 < len(parts):
                    potential_street = '_'.join(parts[i:i+3])
                    if potential_street in self.street_acronyms:
                        return self.street_acronyms[potential_street]

        # Fallback: return first 3 letters of the last part
        return parts[-1][:3].upper()

    def get_street_name(self, room_id: str) -> str:
        """
        Extract street name from room ID.

        Args:
            room_id: Full room ID

        Returns:
            Street name (e.g., W_College_St)
        """
        parts = room_id.split('_')
        if len(parts) >= 4:
            # Look for street name patterns
            for i in range(len(parts) - 1):
                potential_street = '_'.join(parts[i:i+2])
                if potential_street in self.street_acronyms:
                    return potential_street

                # Try with more parts for longer street names
                if i + 2 < len(parts):
                    potential_street = '_'.join(parts[i:i+3])
                    if potential_street in self.street_acronyms:
                        return potential_street

        return "unknown"

    def get_street_color(self, room_id: str) -> str:
        """
        Get color code for a street.

        Args:
            room_id: Full room ID

        Returns:
            ANSI color code for the street
        """
        street_name = self.get_street_name(room_id)
        # Default to white
        return self.street_colors.get(street_name, "\033[37m")

    def render_ascii_map(self, minimap_data: Dict[str, Any], max_width: int = 80) -> str:
        """
        Render the mini-map as ASCII art with grid-based visualization.

        Args:
            minimap_data: Mini-map graph data from PathValidator
            max_width: Maximum width for the display

        Returns:
            ASCII representation of the room connectivity
        """
        if "error" in minimap_data:
            return f"Error: {minimap_data['error']}"

        nodes = minimap_data.get("nodes", [])
        edges = minimap_data.get("edges", [])

        if not nodes:
            return "No rooms found in mini-map"

        # Build the grid-based representation
        lines = []
        lines.append("🗺️  MINI-MAP OF ARKHAM CITY")
        lines.append("=" * max_width)
        lines.append(f"Starting Room: {minimap_data.get('starting_room', 'Unknown')}")
        lines.append(f"Total Rooms: {len(nodes)} | Total Connections: {len(edges)}")
        lines.append("=" * max_width)

        # Create grid-based visualization
        grid_map = self._create_grid_map(nodes, edges, minimap_data.get("starting_room", ""))
        lines.append("\n📍 GRID VISUALIZATION:")
        lines.append("-" * 40)
        lines.append(grid_map)

        # Add legend
        legend = self._generate_color_legend(nodes)
        lines.append("\n" + legend)

        return "\n".join(lines)

    def _create_grid_map(self, nodes: List, edges: List, start_room: str) -> str:
        """
        Create a grid-based map visualization.

        Args:
            nodes: List of room nodes
            edges: List of connections
            start_room: Starting room ID

        Returns:
            Grid-based ASCII map
        """
        # Create coordinate system
        coords = self._assign_coordinates(nodes, edges, start_room)

        # Find grid boundaries
        min_x = min(coord[0] for coord in coords.values()) if coords else 0
        max_x = max(coord[0] for coord in coords.values()) if coords else 0
        min_y = min(coord[1] for coord in coords.values()) if coords else 0
        max_y = max(coord[1] for coord in coords.values()) if coords else 0

        # Create grid
        grid_width = max_x - min_x + 1
        grid_height = max_y - min_y + 1

        # Initialize grid with empty spaces
        grid = [[' ' for _ in range(grid_width * 3)] for _ in range(grid_height * 2)]

        # Place rooms in grid
        for room_id, (x, y) in coords.items():
            grid_x = (x - min_x) * 3
            grid_y = (y - min_y) * 2

            # Get room info
            room_info = next((n for n in nodes if n["id"] == room_id), None)
            if room_info:
                color = self.get_street_color(room_id)

                # Determine room symbol
                symbol = "□"
                if room_id == start_room:
                    symbol = "★"  # Starting point
                elif "intersection" in room_id.lower():
                    symbol = "◆"  # Intersection

                # Place room in grid
                if 0 <= grid_y < len(grid) and 0 <= grid_x < len(grid[0]):
                    grid[grid_y][grid_x] = f"{color}{symbol}{self.color_reset}"

        # Add connections
        for edge in edges:
            from_room = edge["from"]
            to_room = edge["to"]
            direction = edge["direction"]

            if from_room in coords and to_room in coords:
                from_x, from_y = coords[from_room]
                to_x, to_y = coords[to_room]

                # Calculate grid positions
                grid_from_x = (from_x - min_x) * 3
                grid_from_y = (from_y - min_y) * 2
                grid_to_x = (to_x - min_x) * 3
                grid_to_y = (to_y - min_y) * 2

                # Draw connection line
                self._draw_connection(grid, grid_from_x, grid_from_y, grid_to_x, grid_to_y, direction)

        # Convert grid to string
        lines = []
        for row in grid:
            line = ''.join(row)
            if line.strip():  # Only add non-empty lines
                lines.append(line)

        return '\n'.join(lines)

    def _assign_coordinates(self, nodes: List, edges: List, start_room: str) -> Dict[str, Tuple[int, int]]:
        """
        Assign grid coordinates to rooms based on connectivity.

        Args:
            nodes: List of room nodes
            edges: List of connections
            start_room: Starting room ID

        Returns:
            Dictionary mapping room IDs to (x, y) coordinates
        """
        coords = {}
        visited = set()

        if not start_room or start_room not in [n["id"] for n in nodes]:
            # Use first room as starting point
            start_room = nodes[0]["id"] if nodes else ""

        if not start_room:
            return coords

        # Start with the starting room at (0, 0)
        coords[start_room] = (0, 0)
        visited.add(start_room)

        # Build adjacency list
        adjacency = {}
        for edge in edges:
            if edge["from"] not in adjacency:
                adjacency[edge["from"]] = []
            adjacency[edge["from"]].append((edge["to"], edge["direction"]))

            if edge["to"] not in adjacency:
                adjacency[edge["to"]] = []
            adjacency[edge["to"]].append((edge["from"], self._reverse_direction(edge["direction"])))

        # BFS to assign coordinates
        queue = [(start_room, 0, 0)]
        while queue:
            room_id, x, y = queue.pop(0)

            if room_id in adjacency:
                for next_room, direction in adjacency[room_id]:
                    if next_room not in visited:
                        # Calculate new coordinates based on direction
                        new_x, new_y = self._get_next_coordinates(x, y, direction)
                        coords[next_room] = (new_x, new_y)
                        visited.add(next_room)
                        queue.append((next_room, new_x, new_y))

        return coords

    def _get_next_coordinates(self, x: int, y: int, direction: str) -> Tuple[int, int]:
        """
        Get coordinates for the next room based on direction.

        Args:
            x: Current x coordinate
            y: Current y coordinate
            direction: Direction to move

        Returns:
            New (x, y) coordinates
        """
        if direction == "north":
            return (x, y - 1)
        elif direction == "south":
            return (x, y + 1)
        elif direction == "east":
            return (x + 1, y)
        elif direction == "west":
            return (x - 1, y)
        else:
            return (x, y)  # No change for up/down

    def _reverse_direction(self, direction: str) -> str:
        """
        Reverse a direction.

        Args:
            direction: Original direction

        Returns:
            Reversed direction
        """
        direction_map = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east",
            "up": "down",
            "down": "up"
        }
        return direction_map.get(direction, direction)

    def _draw_connection(self, grid: List[List[str]], x1: int, y1: int, x2: int, y2: int, direction: str):
        """
        Draw a connection line between two rooms.

        Args:
            grid: The grid to draw on
            x1, y1: Coordinates of first room
            x2, y2: Coordinates of second room
            direction: Direction of connection
        """
        # Determine connection symbol based on direction
        if direction == "north":
            symbol = "↑"
        elif direction == "south":
            symbol = "↓"
        elif direction == "east":
            symbol = "→"
        elif direction == "west":
            symbol = "←"
        else:
            symbol = "·"

        # Place connection symbol between rooms
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2

        if 0 <= mid_y < len(grid) and 0 <= mid_x < len(grid[0]):
            grid[mid_y][mid_x] = symbol

    def _generate_color_legend(self, nodes: List) -> str:
        """
        Generate a color-coded legend for the streets and special symbols.

        Args:
            nodes: List of room nodes

        Returns:
            Formatted legend string
        """
        legend_lines = ["📍 COLOR LEGEND:"]
        legend_lines.append("-" * 40)

        # Collect unique streets
        streets_used = set()
        for node in nodes:
            street_name = self.get_street_name(node["id"])
            if street_name != "unknown":
                streets_used.add(street_name)

        # Sort streets for consistent display
        for street_name in sorted(streets_used):
            acronym = self.street_acronyms.get(street_name, street_name[:3].upper())
            color = self.street_colors.get(street_name, "\033[37m")
            readable_name = street_name.replace('_', ' ')

            legend_lines.append(f"{color}■{self.color_reset} {acronym}: {readable_name}")

        # Add special symbols legend
        legend_lines.append("")
        legend_lines.append("📍 SPECIAL SYMBOLS:")
        legend_lines.append("-" * 40)
        legend_lines.append("★ Starting Point")
        legend_lines.append("◆ Intersection")
        legend_lines.append("□ Regular Room")
        legend_lines.append("")
        legend_lines.append("📍 DIRECTIONAL MARKERS:")
        legend_lines.append("-" * 40)
        legend_lines.append("↑ North  ↓ South  → East  ← West")

        return "\n".join(legend_lines)

    def render_json_summary(self, minimap_data: Dict[str, Any]) -> str:
        """
        Render a JSON summary of the mini-map data.

        Args:
            minimap_data: Mini-map graph data from PathValidator

        Returns:
            JSON string representation
        """
        import json

        # Create a simplified summary
        summary = {
            "metadata": {
                "total_nodes": minimap_data.get("total_nodes", 0),
                "total_edges": minimap_data.get("total_edges", 0),
                "max_depth": minimap_data.get("max_depth", 0),
                "starting_room": minimap_data.get("starting_room", "")
            },
            "sub_zones": {},
            "connections_by_depth": {}
        }

        # Group by sub-zones
        for node in minimap_data.get("nodes", []):
            sub_zone = node["sub_zone"]
            if sub_zone not in summary["sub_zones"]:
                summary["sub_zones"][sub_zone] = []
            summary["sub_zones"][sub_zone].append({
                "id": node["id"],
                "name": node["name"],
                "depth": node["depth"],
                "is_start": node.get("is_start", False)
            })

        # Group connections by depth
        for edge in minimap_data.get("edges", []):
            # Find the depth of the source node
            source_depth = 0
            for node in minimap_data.get("nodes", []):
                if node["id"] == edge["from"]:
                    source_depth = node["depth"]
                    break

            if source_depth not in summary["connections_by_depth"]:
                summary["connections_by_depth"][source_depth] = []

            summary["connections_by_depth"][source_depth].append({
                "from": edge["from"],
                "to": edge["to"],
                "direction": edge["direction"]
            })

        return json.dumps(summary, indent=2)

    def render_connectivity_stats(self, minimap_data: Dict[str, Any]) -> str:
        """
        Render connectivity statistics for the mini-map.

        Args:
            minimap_data: Mini-map graph data from PathValidator

        Returns:
            Formatted statistics string
        """
        nodes = minimap_data.get("nodes", [])
        edges = minimap_data.get("edges", [])

        if not nodes:
            return "No connectivity data available"

        # Calculate statistics
        sub_zone_counts = {}
        depth_counts = {}
        connection_counts = {}

        for node in nodes:
            sub_zone = node["sub_zone"]
            depth = node["depth"]

            sub_zone_counts[sub_zone] = sub_zone_counts.get(sub_zone, 0) + 1
            depth_counts[depth] = depth_counts.get(depth, 0) + 1

        for edge in edges:
            from_room = edge["from"]
            for node in nodes:
                if node["id"] == from_room:
                    depth = node["depth"]
                    connection_counts[depth] = connection_counts.get(depth, 0) + 1
                    break

        # Build the statistics display
        lines = []
        lines.append("📊 MINI-MAP CONNECTIVITY STATISTICS")
        lines.append("=" * 50)
        lines.append(f"Total Rooms: {len(nodes)}")
        lines.append(f"Total Connections: {len(edges)}")
        lines.append(f"Average Connections per Room: {len(edges) / len(nodes):.2f}")
        lines.append("")

        lines.append("📍 ROOMS BY SUB-ZONE:")
        for sub_zone, count in sorted(sub_zone_counts.items()):
            lines.append(f"  {sub_zone}: {count} rooms")

        lines.append("")
        lines.append("📏 ROOMS BY DEPTH:")
        for depth in sorted(depth_counts.keys()):
            lines.append(f"  Depth {depth}: {depth_counts[depth]} rooms")

        lines.append("")
        lines.append("🔗 CONNECTIONS BY DEPTH:")
        for depth in sorted(connection_counts.keys()):
            lines.append(f"  Depth {depth}: {connection_counts[depth]} connections")

        return "\n".join(lines)
