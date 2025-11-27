# Spec Requirements Document

> Spec: React Flow Room Map Editor
> Created: 2025-11-22

## Overview

Implement an interactive room map visualization and editor using React Flow, providing both view-only mode for players to explore the world map and edit mode for admins to modify room connections and layouts. The feature will be a standalone route/page that loads room data from the server and provides a graph-based interface with custom nodes and edges representing rooms and their directional exits.

## User Stories

### Exploring the World Map

As a player, I want to view an interactive map of all rooms in the game world, so that I can understand spatial relationships and plan my exploration. When I navigate to the map view, I should see all rooms as nodes connected by directional edges showing exits, with the ability to zoom, pan, search for specific rooms, and click on nodes to view detailed room information. The map should highlight my current location and support filtering by zone or subzone.

### Admin Room Layout Editing

As an admin, I want to edit room connections and positions on the map, so that I can design and modify the game world layout efficiently. When I enable edit mode, I should be able to drag room nodes to reposition them, add new exit connections by linking nodes, delete exits, and modify room properties. All changes should be validated and saved to the server with undo/redo support.

## Spec Scope

1. **React Flow integration** - Install and configure reactflow library with custom node and edge components styled to represent rooms and directional exits with visual indicators for exit flags (hidden, locked, one-way).
2. **Standalone map route** - Create `/map` route accessible via navigation that renders the interactive map viewer with controls for zoom, pan, fit-to-view, filtering, and search.
3. **Room data transformation** - Implement utilities to convert existing room JSON structure (with exits dictionary) into React Flow nodes and edges format, handling room types, exit directions, and flags.
4. **View mode features** - Display all rooms as connected nodes with custom styling by subzone/environment, minimap for navigation, room details panel on selection, and player location highlighting.
5. **Admin edit mode** - Enable drag-and-drop node repositioning, edge creation/deletion for exits, property editing, layout persistence, and save/undo functionality with admin permission checks.
6. **Server API support** - Add bulk room data endpoint (`GET /api/rooms/list`) for efficient map loading with optional zone/subzone filtering, and optional layout persistence endpoints for saved positions.

## Out of Scope

- Real-time collaborative editing (multiple admins editing simultaneously)
- Pathfinding visualization (shortest path between rooms)
- Export map as image/PDF functionality
- 3D visualization or alternative view modes
- Mobile-optimized responsive design (desktop-first)
- Offline mode with cached data

## Expected Deliverable

1. Players can access `/map` route to view an interactive graph visualization of all rooms with smooth zoom/pan, search functionality, and detailed room information on node selection.
2. Admins can enable edit mode to modify room connections and positions, with changes validated and persisted to the server, and all operations testable through browser automation.
