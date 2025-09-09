#!/usr/bin/env python3
"""
Generate HTML Visualization for Arkham City Rooms (Fixed Version)

This script creates an interactive HTML visualization of all rooms in the Arkham City zone.
"""

import json
import os
from pathlib import Path


def load_room_data(zone_path: str) -> tuple[dict, dict, set]:
    """Load all room and intersection data from the zone directory."""
    rooms = {}
    intersections = {}
    connections = set()

    zone_dir = Path(zone_path)

    for subzone_dir in zone_dir.iterdir():
        if not subzone_dir.is_dir() or subzone_dir.name == "__pycache__":
            continue

        subzone = subzone_dir.name

        for file_path in subzone_dir.glob("*.json"):
            if file_path.name == "subzone_config.json" or file_path.name == "zone_config.json":
                continue

            try:
                with open(file_path, encoding="utf-8") as f:
                    data = json.load(f)

                room_id = data["id"]
                room_name = data["name"]
                exits = data.get("exits", {})

                # Determine if this is an intersection or regular room
                if "intersection" in room_id:
                    intersections[room_id] = {"name": room_name, "subzone": subzone, "exits": exits}
                else:
                    rooms[room_id] = {"name": room_name, "subzone": subzone, "exits": exits}

                # Record connections
                for direction, target in exits.items():
                    if target:
                        connections.add((room_id, target, direction))

            except Exception as e:
                print(f"Error loading {file_path}: {e}")

    return rooms, intersections, connections


def generate_html_visualization(
    rooms: dict, intersections: dict, connections: set, output_path: str = "arkham_city_visualization.html"
):
    """Generate an HTML visualization of the room network."""

    # Color scheme for subzones
    subzone_colors = {
        "campus": "#2E8B57",
        "northside": "#8B0000",
        "downtown": "#4169E1",
        "merchant": "#FF8C00",
        "lower_southside": "#800080",
        "uptown": "#32CD32",
        "east_town": "#FF1493",
        "river_town": "#00CED1",
        "french_hill": "#FFD700",
    }

    # Generate node data for JavaScript
    nodes = []
    for room_id, room_data in rooms.items():
        nodes.append(
            {
                "id": room_id,
                "name": room_data["name"],
                "subzone": room_data["subzone"],
                "type": "room",
                "color": subzone_colors.get(room_data["subzone"], "#CCCCCC"),
            }
        )

    for intersection_id, intersection_data in intersections.items():
        nodes.append(
            {
                "id": intersection_id,
                "name": intersection_data["name"],
                "subzone": intersection_data["subzone"],
                "type": "intersection",
                "color": subzone_colors.get(intersection_data["subzone"], "#CCCCCC"),
            }
        )

    # Generate edge data for JavaScript
    edges = []
    for source, target, direction in connections:
        edges.append({"source": source, "target": target, "direction": direction})

    # Generate subzone options for dropdown
    all_subzones = sorted(
        {room["subzone"] for room in rooms.values()}
        | {intersection["subzone"] for intersection in intersections.values()}
    )
    subzone_options = "\n".join(f'<option value="{subzone}">{subzone.title()}</option>' for subzone in all_subzones)

    # Generate legend items
    legend_items = []
    for subzone, color in subzone_colors.items():
        legend_items.append(
            f'<div class="legend-item"><div class="legend-color" style="background-color: {color}"></div><div class="legend-text">{subzone.title()}</div></div>'
        )
    legend_html = "\n".join(legend_items)

    # Generate room listing by subzone
    room_listing_html = ""
    for subzone in sorted(all_subzones):
        room_listing_html += '<div class="subzone-section">\n'
        room_listing_html += f'<div class="subzone-title">{subzone.upper()}</div>\n'

        # Add rooms for this subzone
        subzone_rooms = [(rid, rdata) for rid, rdata in rooms.items() if rdata["subzone"] == subzone]
        for room_id, room_data in sorted(subzone_rooms):
            exits = [f"{dir}: {target}" for dir, target in room_data["exits"].items() if target]
            exits_str = ", ".join(exits) if exits else "None"
            room_listing_html += '<div class="room-item">\n'
            room_listing_html += f'<div class="room-name">{room_data["name"]}</div>\n'
            room_listing_html += f'<div class="room-id">{room_id}</div>\n'
            room_listing_html += f'<div class="room-exits">Exits: {exits_str}</div>\n'
            room_listing_html += "</div>\n"

        # Add intersections for this subzone
        subzone_intersections = [(iid, idata) for iid, idata in intersections.items() if idata["subzone"] == subzone]
        for intersection_id, intersection_data in sorted(subzone_intersections):
            exits = [f"{dir}: {target}" for dir, target in intersection_data["exits"].items() if target]
            exits_str = ", ".join(exits) if exits else "None"
            room_listing_html += '<div class="intersection-item">\n'
            room_listing_html += f'<div class="room-name">{intersection_data["name"]}</div>\n'
            room_listing_html += f'<div class="room-id">{intersection_id}</div>\n'
            room_listing_html += f'<div class="room-exits">Exits: {exits_str}</div>\n'
            room_listing_html += "</div>\n"

        room_listing_html += "</div>\n"

    # Create HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arkham City Zone Visualization</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #1a1a1a;
            color: #ffffff;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .header h1 {{
            color: #ff6b6b;
            margin-bottom: 10px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: #2d2d2d;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #4ecdc4;
        }}
        .stat-label {{
            color: #b0b0b0;
            margin-top: 5px;
        }}
        .visualization {{
            background: #2d2d2d;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        .controls {{
            margin-bottom: 20px;
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }}
        .control-group {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .control-group label {{
            color: #b0b0b0;
        }}
        .control-group select, .control-group input {{
            background: #404040;
            border: 1px solid #555;
            color: #ffffff;
            padding: 5px 10px;
            border-radius: 4px;
        }}
        .legend {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 20px;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .legend-color {{
            width: 20px;
            height: 20px;
            border-radius: 3px;
        }}
        .legend-text {{
            color: #b0b0b0;
        }}
        .room-list {{
            background: #2d2d2d;
            border-radius: 8px;
            padding: 20px;
        }}
        .subzone-section {{
            margin-bottom: 20px;
        }}
        .subzone-title {{
            color: #4ecdc4;
            font-size: 1.2em;
            margin-bottom: 10px;
            border-bottom: 1px solid #404040;
            padding-bottom: 5px;
        }}
        .room-item {{
            background: #404040;
            margin: 5px 0;
            padding: 10px;
            border-radius: 4px;
            border-left: 4px solid #4ecdc4;
        }}
        .room-name {{
            font-weight: bold;
            color: #ffffff;
        }}
        .room-id {{
            color: #b0b0b0;
            font-size: 0.9em;
            margin-top: 5px;
        }}
        .room-exits {{
            color: #ff6b6b;
            font-size: 0.9em;
            margin-top: 5px;
        }}
        .intersection-item {{
            background: #404040;
            margin: 5px 0;
            padding: 10px;
            border-radius: 4px;
            border-left: 4px solid #ffd93d;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏛️ Arkham City Zone Visualization</h1>
            <p>A comprehensive map of all locations and connections in the MythosMUD Arkham City zone</p>
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{len(rooms)}</div>
                <div class="stat-label">Rooms</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(intersections)}</div>
                <div class="stat-label">Intersections</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(connections)}</div>
                <div class="stat-label">Connections</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(all_subzones)}</div>
                <div class="stat-label">Subzones</div>
            </div>
        </div>

        <div class="visualization">
            <div class="controls">
                <div class="control-group">
                    <label for="subzone-filter">Filter by Subzone:</label>
                    <select id="subzone-filter">
                        <option value="">All Subzones</option>
                        {subzone_options}
                    </select>
                </div>
                <div class="control-group">
                    <label for="node-type-filter">Filter by Type:</label>
                    <select id="node-type-filter">
                        <option value="">All Types</option>
                        <option value="room">Rooms Only</option>
                        <option value="intersection">Intersections Only</option>
                    </select>
                </div>
                <div class="control-group">
                    <label for="show-labels">Show Labels:</label>
                    <input type="checkbox" id="show-labels" checked>
                </div>
            </div>

            <div id="graph-container" style="width: 100%; height: 600px; border: 1px solid #404040; border-radius: 4px;"></div>

            <div class="legend">
                {legend_html}
                <div class="legend-item"><div class="legend-color" style="background-color: #ffd93d"></div><div class="legend-text">Intersections</div></div>
            </div>
        </div>

        <div class="room-list">
            <h2>📋 Detailed Room Listing</h2>
            {room_listing_html}
        </div>
    </div>

    <script>
        // Data
        const nodes = {json.dumps(nodes, indent=8)};
        const edges = {json.dumps(edges, indent=8)};

        // Setup
        const width = document.getElementById('graph-container').offsetWidth;
        const height = 600;

        const svg = d3.select('#graph-container')
            .append('svg')
            .attr('width', width)
            .attr('height', height);

        const g = svg.append('g');

        // Create force simulation
        const simulation = d3.forceSimulation(nodes)
            .force('link', d3.forceLink(edges).id(d => d.id).distance(100))
            .force('charge', d3.forceManyBody().strength(-300))
            .force('center', d3.forceCenter(width / 2, height / 2))
            .force('collision', d3.forceCollide().radius(30));

        // Create links
        const link = g.append('g')
            .selectAll('line')
            .data(edges)
            .enter().append('line')
            .attr('stroke', '#666')
            .attr('stroke-width', 1)
            .attr('opacity', 0.6);

        // Create nodes
        const node = g.append('g')
            .selectAll('circle')
            .data(nodes)
            .enter().append('circle')
            .attr('r', d => d.type === 'intersection' ? 8 : 6)
            .attr('fill', d => d.color)
            .attr('stroke', '#fff')
            .attr('stroke-width', 2)
            .call(d3.drag()
                .on('start', dragstarted)
                .on('drag', dragged)
                .on('end', dragended));

        // Create labels
        const label = g.append('g')
            .selectAll('text')
            .data(nodes)
            .enter().append('text')
            .text(d => d.name.length > 20 ? d.name.substring(0, 20) + '...' : d.name)
            .attr('font-size', '10px')
            .attr('fill', '#fff')
            .attr('text-anchor', 'middle')
            .attr('dy', '0.35em');

        // Update positions on simulation tick
        simulation.on('tick', () => {{
            link
                .attr('x1', d => d.source.x)
                .attr('y1', d => d.source.y)
                .attr('x2', d => d.target.x)
                .attr('y2', d => d.target.y);

            node
                .attr('cx', d => d.x)
                .attr('cy', d => d.y);

            label
                .attr('x', d => d.x)
                .attr('y', d => d.y);
        }});

        // Drag functions
        function dragstarted(event, d) {{
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }}

        function dragged(event, d) {{
            d.fx = event.x;
            d.fy = event.y;
        }}

        function dragended(event, d) {{
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }}

        // Filtering functionality
        function updateVisualization() {{
            const subzoneFilter = document.getElementById('subzone-filter').value;
            const typeFilter = document.getElementById('node-type-filter').value;
            const showLabels = document.getElementById('show-labels').checked;

            // Filter nodes
            const filteredNodes = nodes.filter(node => {{
                const subzoneMatch = !subzoneFilter || node.subzone === subzoneFilter;
                const typeMatch = !typeFilter || node.type === typeFilter;
                return subzoneMatch && typeMatch;
            }});

            const filteredNodeIds = new Set(filteredNodes.map(n => n.id));
            const filteredEdges = edges.filter(edge =>
                filteredNodeIds.has(edge.source.id || edge.source) &&
                filteredNodeIds.has(edge.target.id || edge.target)
            );

            // Update simulation
            simulation.nodes(filteredNodes);
            simulation.force('link').links(filteredEdges);
            simulation.alpha(1).restart();

            // Update visual elements
            link.data(filteredEdges)
                .join('line')
                .attr('stroke', '#666')
                .attr('stroke-width', 1)
                .attr('opacity', 0.6);

            node.data(filteredNodes)
                .join('circle')
                .attr('r', d => d.type === 'intersection' ? 8 : 6)
                .attr('fill', d => d.color)
                .attr('stroke', '#fff')
                .attr('stroke-width', 2);

            label.data(filteredNodes)
                .join('text')
                .text(d => d.name.length > 20 ? d.name.substring(0, 20) + '...' : d.name)
                .attr('font-size', '10px')
                .attr('fill', '#fff')
                .attr('text-anchor', 'middle')
                .attr('dy', '0.35em')
                .style('display', showLabels ? 'block' : 'none');
        }}

        // Add event listeners
        document.getElementById('subzone-filter').addEventListener('change', updateVisualization);
        document.getElementById('node-type-filter').addEventListener('change', updateVisualization);
        document.getElementById('show-labels').addEventListener('change', updateVisualization);
    </script>
</body>
</html>"""

    # Write HTML file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML visualization saved as {output_path}")
    print(f"Open {output_path} in your web browser to view the interactive visualization")


def main():
    """Main function to generate the HTML visualization."""
    zone_path = "data/rooms/earth/arkham_city"

    if not os.path.exists(zone_path):
        print(f"Error: Zone path {zone_path} not found!")
        return

    print("Loading Arkham City room data...")
    rooms, intersections, connections = load_room_data(zone_path)

    print("Generating HTML visualization...")
    generate_html_visualization(rooms, intersections, connections)

    print("\n=== Summary ===")
    print("Generated interactive HTML visualization with:")
    print(f"- {len(rooms)} rooms")
    print(f"- {len(intersections)} intersections")
    print(f"- {len(connections)} connections")
    print(
        f"- {len({room['subzone'] for room in rooms.values()} | {intersection['subzone'] for intersection in intersections.values()})} subzones"
    )


if __name__ == "__main__":
    main()
