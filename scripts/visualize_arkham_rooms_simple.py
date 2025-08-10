#!/usr/bin/env python3
"""
Simple Arkham City Rooms Graph Visualization

This script creates a visual representation of all rooms in the Arkham City zone,
saving it as a PNG file without interactive display.
"""

import json
import os
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
from typing import Dict, List, Tuple, Set

# Color scheme for different subzones
SUBZONE_COLORS = {
    'campus': '#2E8B57',        # Sea Green
    'northside': '#8B0000',     # Dark Red
    'downtown': '#4169E1',      # Royal Blue
    'merchant': '#FF8C00',      # Dark Orange
    'lower_southside': '#800080', # Purple
    'uptown': '#32CD32',        # Lime Green
    'east_town': '#FF1493',     # Deep Pink
    'river_town': '#00CED1',    # Dark Turquoise
    'french_hill': '#FFD700',   # Gold
    'intersection': '#696969'   # Dim Gray
}

def load_room_data(zone_path: str) -> Tuple[Dict, Dict, Set]:
    """Load all room and intersection data from the zone directory."""
    rooms = {}
    intersections = {}
    connections = set()
    
    zone_dir = Path(zone_path)
    
    for subzone_dir in zone_dir.iterdir():
        if not subzone_dir.is_dir() or subzone_dir.name == '__pycache__':
            continue
            
        subzone = subzone_dir.name
        print(f"Processing subzone: {subzone}")
        
        for file_path in subzone_dir.glob('*.json'):
            if file_path.name == 'subzone_config.json' or file_path.name == 'zone_config.json':
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                room_id = data['id']
                room_name = data['name']
                exits = data.get('exits', {})
                
                # Determine if this is an intersection or regular room
                if 'intersection' in room_id:
                    intersections[room_id] = {
                        'name': room_name,
                        'subzone': subzone,
                        'exits': exits
                    }
                else:
                    rooms[room_id] = {
                        'name': room_name,
                        'subzone': subzone,
                        'exits': exits
                    }
                
                # Record connections
                for direction, target in exits.items():
                    if target:
                        connections.add((room_id, target, direction))
                        
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
    
    return rooms, intersections, connections

def create_graph(rooms: Dict, intersections: Dict, connections: Set) -> nx.Graph:
    """Create a NetworkX graph from the room data."""
    G = nx.Graph()
    
    # Add nodes
    for room_id, room_data in rooms.items():
        G.add_node(room_id, 
                  name=room_data['name'],
                  subzone=room_data['subzone'],
                  type='room')
    
    for intersection_id, intersection_data in intersections.items():
        G.add_node(intersection_id,
                  name=intersection_data['name'],
                  subzone=intersection_data['subzone'],
                  type='intersection')
    
    # Add edges
    for source, target, direction in connections:
        if source in G.nodes and target in G.nodes:
            G.add_edge(source, target, direction=direction)
    
    return G

def visualize_graph(G: nx.Graph, output_path: str = "arkham_city_rooms_graph.png"):
    """Create a visual representation of the graph."""
    plt.figure(figsize=(20, 16))
    
    # Use spring layout for better visualization
    pos = nx.spring_layout(G, k=3, iterations=50, seed=42)
    
    # Draw nodes by subzone
    for subzone in SUBZONE_COLORS:
        # Get nodes for this subzone
        subzone_nodes = [node for node, data in G.nodes(data=True) 
                        if data.get('subzone') == subzone]
        
        if subzone_nodes:
            nx.draw_networkx_nodes(G, pos, 
                                 nodelist=subzone_nodes,
                                 node_color=SUBZONE_COLORS[subzone],
                                 node_size=300,
                                 alpha=0.8)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color='gray')
    
    # Draw labels (only for intersections to avoid clutter)
    intersection_labels = {node: data['name'] for node, data in G.nodes(data=True) 
                          if data.get('type') == 'intersection'}
    nx.draw_networkx_labels(G, pos, intersection_labels, font_size=8, font_weight='bold')
    
    # Create legend
    legend_elements = []
    for subzone, color in SUBZONE_COLORS.items():
        if any(data.get('subzone') == subzone for _, data in G.nodes(data=True)):
            legend_elements.append(mpatches.Patch(color=color, label=subzone.title()))
    
    plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    plt.title('Arkham City Zone - Room Connections', fontsize=16, fontweight='bold')
    plt.axis('off')
    
    # Save the plot
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory
    
    print(f"Graph saved as {output_path}")

def print_statistics(rooms: Dict, intersections: Dict, connections: Set):
    """Print statistics about the room data."""
    print("\n=== Arkham City Zone Statistics ===")
    print(f"Total Rooms: {len(rooms)}")
    print(f"Total Intersections: {len(intersections)}")
    print(f"Total Connections: {len(connections)}")
    
    # Count by subzone
    subzone_counts = {}
    for room_data in rooms.values():
        subzone = room_data['subzone']
        subzone_counts[subzone] = subzone_counts.get(subzone, 0) + 1
    
    for intersection_data in intersections.values():
        subzone = intersection_data['subzone']
        subzone_counts[subzone] = subzone_counts.get(subzone, 0) + 1
    
    print("\nRooms by Subzone:")
    for subzone, count in sorted(subzone_counts.items()):
        print(f"  {subzone.title()}: {count}")
    
    # Count connections by direction
    direction_counts = {}
    for _, _, direction in connections:
        direction_counts[direction] = direction_counts.get(direction, 0) + 1
    
    print("\nConnections by Direction:")
    for direction, count in sorted(direction_counts.items()):
        print(f"  {direction.title()}: {count}")

def main():
    """Main function to generate the visualization."""
    zone_path = "data/rooms/earth/arkham_city"
    
    if not os.path.exists(zone_path):
        print(f"Error: Zone path {zone_path} not found!")
        return
    
    print("Loading Arkham City room data...")
    rooms, intersections, connections = load_room_data(zone_path)
    
    print("Creating graph...")
    G = create_graph(rooms, intersections, connections)
    
    print("Generating visualization...")
    visualize_graph(G)
    
    print_statistics(rooms, intersections, connections)
    
    # Print some sample room names for reference
    print("\n=== Sample Rooms by Subzone ===")
    for subzone in sorted(set(room['subzone'] for room in rooms.values())):
        subzone_rooms = [room for room in rooms.values() if room['subzone'] == subzone]
        print(f"\n{subzone.title()}:")
        for room in subzone_rooms[:3]:  # Show first 3 rooms
            print(f"  - {room['name']}")

if __name__ == "__main__":
    main()
