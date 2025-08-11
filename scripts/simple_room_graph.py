#!/usr/bin/env python3
"""
Simple Room Graph Visualization

This script creates a simplified visualization of all rooms in the Arkham City zone,
focusing only on room nodes and their connections, ignoring zone/subzone/plane metadata.
"""

import json
import os
from collections import defaultdict
from pathlib import Path


def load_room_data(zone_path: str) -> tuple[dict, dict, set]:
    """Load all room and intersection data from the zone directory."""
    rooms = {}
    intersections = {}
    connections = set()

    zone_dir = Path(zone_path)

    for subzone_dir in zone_dir.iterdir():
        if not subzone_dir.is_dir() or subzone_dir.name == '__pycache__':
            continue

        for file_path in subzone_dir.glob('*.json'):
            if file_path.name == 'subzone_config.json' or file_path.name == 'zone_config.json':
                continue

            try:
                with open(file_path, encoding='utf-8') as f:
                    data = json.load(f)

                room_id = data['id']
                room_name = data['name']
                exits = data.get('exits', {})

                # Determine if this is an intersection or regular room
                if 'intersection' in room_id:
                    intersections[room_id] = {
                        'name': room_name,
                        'exits': exits
                    }
                else:
                    rooms[room_id] = {
                        'name': room_name,
                        'exits': exits
                    }

                # Record connections
                for direction, target in exits.items():
                    if target:
                        connections.add((room_id, target, direction))

            except Exception as e:
                print(f"Error loading {file_path}: {e}")

    return rooms, intersections, connections

def generate_simple_dot_file(rooms: dict, intersections: dict, connections: set, output_path: str = "simple_room_graph.dot"):
    """Generate a simplified DOT file focusing only on room nodes."""
    print(f"Generating simple DOT file: {output_path}")

    with open(output_path, 'w') as f:
        f.write("digraph SimpleRoomGraph {\n")
        f.write("  rankdir=TB;\n")
        f.write("  node [shape=box, style=filled];\n\n")

        # Add room nodes (simplified names)
        for room_id, room_data in rooms.items():
            # Extract a simple name from the room ID
            simple_name = room_data['name']
            if len(simple_name) > 30:
                simple_name = simple_name[:27] + "..."

            f.write(f'  "{room_id}" [label="{simple_name}", fillcolor="lightblue"];\n')

        # Add intersection nodes (diamond shape)
        for intersection_id, intersection_data in intersections.items():
            simple_name = intersection_data['name']
            if len(simple_name) > 30:
                simple_name = simple_name[:27] + "..."

            f.write(f'  "{intersection_id}" [label="{simple_name}", fillcolor="lightyellow", shape=diamond];\n')

        f.write("\n")

        # Add edges (connections)
        for source, target, direction in connections:
            f.write(f'  "{source}" -> "{target}" [label="{direction}"];\n')

        f.write("}\n")

    print(f"Simple DOT file saved as {output_path}")

def generate_simple_html_visualization(rooms: dict, intersections: dict, connections: set, output_path: str = "simple_room_visualization.html"):
    """Generate a simplified HTML visualization."""

    # Generate node data for JavaScript (simplified)
    nodes = []
    for room_id, room_data in rooms.items():
        nodes.append({
            'id': room_id,
            'name': room_data['name'],
            'type': 'room',
            'color': '#4ecdc4'  # Single color for all rooms
        })

    for intersection_id, intersection_data in intersections.items():
        nodes.append({
            'id': intersection_id,
            'name': intersection_data['name'],
            'type': 'intersection',
            'color': '#ffd93d'  # Single color for all intersections
        })

    # Generate edge data for JavaScript
    edges = []
    for source, target, direction in connections:
        edges.append({
            'source': source,
            'target': target,
            'direction': direction
        })

    # Create HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Room Graph - Arkham City</title>
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
            <h1>🏛️ Simple Room Graph - Arkham City</h1>
            <p>A simplified visualization focusing only on rooms and their connections</p>
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
                <div class="stat-number">{len(rooms) + len(intersections)}</div>
                <div class="stat-label">Total Nodes</div>
            </div>
        </div>

        <div class="visualization">
            <div class="controls">
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
                <div class="legend-item"><div class="legend-color" style="background-color: #4ecdc4"></div><div class="legend-text">Rooms</div></div>
                <div class="legend-item"><div class="legend-color" style="background-color: #ffd93d"></div><div class="legend-text">Intersections</div></div>
            </div>
        </div>

        <div class="room-list">
            <h2>📋 All Rooms and Intersections</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div>
                    <h3>Rooms ({len(rooms)})</h3>
                    {chr(10).join(f'<div class="room-item"><div class="room-name">{room_data["name"]}</div><div class="room-id">{room_id}</div></div>' for room_id, room_data in sorted(rooms.items()))}
                </div>
                <div>
                    <h3>Intersections ({len(intersections)})</h3>
                    {chr(10).join(f'<div class="intersection-item"><div class="room-name">{intersection_data["name"]}</div><div class="room-id">{intersection_id}</div></div>' for intersection_id, intersection_data in sorted(intersections.items()))}
                </div>
            </div>
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
            const typeFilter = document.getElementById('node-type-filter').value;
            const showLabels = document.getElementById('show-labels').checked;

            // Filter nodes
            const filteredNodes = nodes.filter(node => {{
                const typeMatch = !typeFilter || node.type === typeFilter;
                return typeMatch;
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
        document.getElementById('node-type-filter').addEventListener('change', updateVisualization);
        document.getElementById('show-labels').addEventListener('change', updateVisualization);
    </script>
</body>
</html>"""

    # Write HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Simple HTML visualization saved as {output_path}")

def print_simple_statistics(rooms: dict, intersections: dict, connections: set):
    """Print simplified statistics about the room data."""
    print("\n=== Simple Room Graph Statistics ===")
    print(f"Total Rooms: {len(rooms)}")
    print(f"Total Intersections: {len(intersections)}")
    print(f"Total Connections: {len(connections)}")
    print(f"Total Nodes: {len(rooms) + len(intersections)}")

    # Count connections by direction
    direction_counts = defaultdict(int)
    for _, _, direction in connections:
        direction_counts[direction] += 1

    print("\nConnections by Direction:")
    for direction, count in sorted(direction_counts.items()):
        print(f"  {direction.title()}: {count}")

    # Find isolated nodes
    all_node_ids = set(rooms.keys()) | set(intersections.keys())
    connected_nodes = set()
    for source, target, _ in connections:
        connected_nodes.add(source)
        connected_nodes.add(target)

    isolated_nodes = all_node_ids - connected_nodes
    if isolated_nodes:
        print(f"\nIsolated Nodes ({len(isolated_nodes)}):")
        for node_id in sorted(isolated_nodes):
            if node_id in rooms:
                print(f"  - {rooms[node_id]['name']} (Room)")
            else:
                print(f"  - {intersections[node_id]['name']} (Intersection)")
    else:
        print("\nNo isolated nodes found - all nodes are connected!")

def main():
    """Main function to generate the simplified visualization."""
    zone_path = "data/rooms/earth/arkham_city"

    if not os.path.exists(zone_path):
        print(f"Error: Zone path {zone_path} not found!")
        return

    print("Loading Arkham City room data...")
    rooms, intersections, connections = load_room_data(zone_path)

    print("Generating simplified visualizations...")
    generate_simple_dot_file(rooms, intersections, connections)
    generate_simple_html_visualization(rooms, intersections, connections)

    print_simple_statistics(rooms, intersections, connections)

    print("\n=== Summary ===")
    print("Generated simplified visualizations:")
    print("- simple_room_graph.dot (DOT file for Graphviz)")
    print("- simple_room_visualization.html (Interactive HTML)")
    print("Focus: Only room nodes and connections, no zone/subzone metadata")

if __name__ == "__main__":
    main()
