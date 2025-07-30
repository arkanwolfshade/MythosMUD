"""
Mini-map renderer for room connectivity visualization.

This module provides visual representations of room connectivity graphs
for use in client mini-maps and debugging room layouts.
"""

from typing import Dict, List, Any


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

    def get_street_acronym(self, room_id: str) -> str:
        """
        Extract street acronym from room ID.

        Args:
            room_id: Full room ID (e.g., earth_arkham_city_campus_E_College_St_003)

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

    def render_ascii_map(self, minimap_data: Dict[str, Any], max_width: int = 80) -> str:
        """
        Render the mini-map as ASCII art.

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

        # Build the linear representation
        lines = []
        lines.append("🗺️  MINI-MAP OF ARKHAM CITY")
        lines.append("=" * max_width)
        lines.append(f"Starting Room: {minimap_data.get('starting_room', 'Unknown')}")
        lines.append(f"Total Rooms: {len(nodes)} | Total Connections: {len(edges)}")
        lines.append("=" * max_width)

        # Create a simple linear chain representation
        if len(nodes) <= 20:  # Only for small maps
            lines.append("\n📍 ROOM CONNECTIVITY:")
            lines.append("-" * 40)

            # Build connection chains
            room_connections = {}
            for edge in edges:
                if edge["from"] not in room_connections:
                    room_connections[edge["from"]] = []
                room_connections[edge["from"]].append(edge)

            # Find the starting room
            start_room = minimap_data.get("starting_room", "")
            if start_room and start_room in room_connections:
                chain = self._build_room_chain(start_room, room_connections, nodes)
                lines.append(chain)
            else:
                # Fallback to depth-based display
                lines.append(self._render_depth_based(nodes, edges))

        return "\n".join(lines)

    def _build_room_chain(self, start_room: str, room_connections: Dict, nodes: List) -> str:
        """Build a linear chain representation of connected rooms."""
        visited = set()
        used_acronyms = set()

        def traverse(room_id: str) -> str:
            if room_id in visited:
                return ""
            visited.add(room_id)

            # Get acronym for room
            acronym = self.get_street_acronym(room_id)
            used_acronyms.add(acronym)

            # Find next room
            if room_id in room_connections:
                for edge in room_connections[room_id]:
                    next_room = edge["to"]
                    if next_room not in visited:
                        return f"[{acronym}]<->{traverse(next_room)}"

            return f"[{acronym}]"

        chain = traverse(start_room)

        # Generate legend
        legend = self._generate_legend(used_acronyms)

        return f"{chain}\n\n{legend}"

    def _generate_legend(self, used_acronyms: set) -> str:
        """
        Generate a legend for the used acronyms.

        Args:
            used_acronyms: Set of acronyms used in the map

        Returns:
            Formatted legend string
        """
        legend_lines = ["📍 LEGEND:"]
        legend_lines.append("-" * 40)

        # Create reverse mapping from acronym to full name
        acronym_to_name = {}
        for full_name, acronym in self.street_acronyms.items():
            if acronym in used_acronyms:
                # Convert full_name to readable format
                readable_name = full_name.replace('_', ' ')
                acronym_to_name[acronym] = readable_name

        # Sort by acronym for consistent display
        for acronym in sorted(acronym_to_name.keys()):
            full_name = acronym_to_name[acronym]
            legend_lines.append(f"{acronym}: {full_name}")

        return "\n".join(legend_lines)

    def _render_depth_based(self, nodes: List, edges: List) -> str:
        """Fallback depth-based rendering for complex maps."""
        # Group nodes by depth
        depth_groups = {}
        for node in nodes:
            depth = node["depth"]
            if depth not in depth_groups:
                depth_groups[depth] = []
            depth_groups[depth].append(node)

        lines = []
        for depth in sorted(depth_groups.keys()):
            lines.append(f"\n📍 DEPTH {depth}:")
            lines.append("-" * 40)

            for node in depth_groups[depth]:
                # Find connections for this node
                connections = []
                for edge in edges:
                    if edge["from"] == node["id"]:
                        direction = edge["direction"]
                        symbol = self.direction_symbols.get(direction, direction)
                        connections.append(f"{symbol} {edge['to']}")

                # Format the room display
                room_display = f"🏠 {node['name']}"
                if node.get("is_start"):
                    room_display += " [START]"
                room_display += f" ({node['sub_zone']})"

                lines.append(room_display)

                if connections:
                    for conn in connections:
                        lines.append(f"  {conn}")
                else:
                    lines.append("  [No exits]")

        return "\n".join(lines)

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
