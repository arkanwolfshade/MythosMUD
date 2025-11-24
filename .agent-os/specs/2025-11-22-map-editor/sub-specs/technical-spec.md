# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-22-map-editor/spec.md

## Technical Requirements

- **React Flow integration**: Install `reactflow` package (latest stable version) and configure with custom node types for rooms and intersections, custom edge types for directional exits, and layout algorithms (force-directed, hierarchical, or custom grid-based).
- **Component architecture**: Create modular component structure with `RoomMapViewer.tsx` as main container, `RoomNode.tsx` and `IntersectionNode.tsx` for custom nodes, `ExitEdge.tsx` for directional edges, `MapControls.tsx` toolbar, and `RoomDetailsPanel.tsx` sidebar, following existing React/TypeScript patterns in client codebase.
- **Data transformation utilities**: Implement `mapUtils.ts` to convert room JSON structure (from existing Room interface) to React Flow format, handling exits dictionary (`{north: "room_id", south: null, ...}`), exit objects with flags, room types, and coordinate inference from exit relationships.
- **Data loading hook**: Create `useRoomMapData.ts` hook to fetch room data from server API, transform to map format, handle loading/error states, and support filtering by zone/subzone with efficient data processing for large room sets (100+ rooms).
- **Layout management**: Implement `useMapLayout.ts` hook supporting multiple layout algorithms, auto-layout from coordinates if available, manual positioning persistence, and smooth layout updates with performance optimization (debouncing, memoization).
- **Edit mode functionality**: Create `useMapEditing.ts` hook for admin edit operations including node drag/reposition, edge creation via drag-and-drop, edge deletion, node property editing, and validation ensuring exit targets exist and data integrity.
- **Server API endpoints**: Add `GET /api/rooms/list` endpoint supporting query parameters for zone/subzone filtering, returning room data optimized for map visualization with exit relationships, and optional `POST /api/map/layout` endpoint for saving node positions separately from room definitions.
- **Route integration**: Add `/map` route to main router configuration with `MapView.tsx` component wrapper, navigation link/menu item (conditionally shown for admins), and integration with existing player location tracking for highlighting current room.
- **Performance optimization**: Implement virtual rendering for large room sets (500+ rooms), lazy loading for rooms outside viewport, debounced layout recalculations, and memoized node/edge rendering to maintain 60fps performance targets.
- **Theme and styling**: Apply consistent styling with existing client UI theme, support dark mode if applicable, and ensure accessibility with keyboard navigation, screen reader compatibility, and high contrast mode support.

## External Dependencies

- **reactflow** - React-based graph visualization library for interactive node graphs
  - **Version**: Latest stable (^11.x recommended)
  - **Justification**: Modern, well-maintained library specifically designed for React interactive graph visualization with excellent TypeScript support, custom node/edge capabilities, and performance optimizations for large graphs
  - **Alternative considered**: D3.js (already in project but more complex for this use case), Cytoscape.js (less React-integrated)
