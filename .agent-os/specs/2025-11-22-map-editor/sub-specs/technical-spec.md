# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-22-map-editor/spec.md

## Technical Requirements

**React Flow integration**: Install `reactflow` package (latest stable version) and configure with custom node types for rooms and intersections using React Flow's built-in customization features (Handle, custom shapes), custom edge types for directional exits with icon/badge indicators for flags, and grid-based layout algorithm.

**Component architecture**: Create modular component structure with `RoomMapViewer.tsx` as main container, `RoomNode.tsx` and `IntersectionNode.tsx` for custom nodes, `ExitEdge.tsx` for directional edges, `MapControls.tsx` toolbar, and `RoomDetailsPanel.tsx` sidebar, following existing React/TypeScript patterns in client codebase.

**Data transformation utilities**: Implement `mapUtils.ts` to convert room JSON structure (from existing Room interface) to React Flow format, handling exits dictionary (`{north: "room_id", south: null, ...}`) and exit objects with flags/description, merging both formats into single edges with flag metadata, room types, and using stored coordinates (map_x, map_y) from database when available.
- **Data loading hook**: Create `useRoomMapData.ts` hook to fetch room data from server API, transform to map format, handle loading/error states, and support filtering by zone/subzone with efficient data processing for large room sets (100+ rooms).
- **Layout management**: Implement `useMapLayout.ts` hook supporting multiple layout algorithms, auto-layout from coordinates if available, manual positioning persistence, and smooth layout updates with performance optimization (debouncing, memoization).
- **Edit mode functionality**: Create `useMapEditing.ts` hook for admin edit operations including node drag/reposition (with visual indicator for unsaved changes), edge creation via modal form/dialog (source room pre-selected, target from searchable dropdown, with preview and real-time validation), edge deletion, node property editing (all room schema properties, with tabs/sections, inline validation), and comprehensive validation (target room exists, valid direction, bidirectional pairing warnings, data integrity). All operations tracked in undo/redo system.
- **Server API endpoints**: Add `GET /api/rooms/list` endpoint requiring `plane` and `zone` parameters (with optional `subzone`), returning room data in same format as existing endpoints with exit relationships and map positions (map_x, map_y) when available. Positions stored directly in `rooms` table columns. Add exploration tracking via `player_exploration` junction table integrated with movement service.
- **Route integration**: Add `/map` route to main router configuration with `MapView.tsx` component wrapper, navigation link visible to all players (map content only shown if player has explored at least one room), and integration with existing player location tracking for pulsing/animated highlighting of current room.
- **Performance optimization**: Implement lazy loading for rooms outside viewport, debounced layout recalculations, and memoized node/edge rendering to maintain 60fps performance targets.
- **Theme and styling**: Apply consistent styling with existing client UI theme, support dark mode if applicable. Accessibility features deferred to future iteration.

## External Dependencies

**reactflow** - React-based graph visualization library for interactive node graphs

**Version**: Latest stable (^11.x recommended)

**Justification**: Modern, well-maintained library specifically designed for React interactive graph visualization with excellent TypeScript support, custom node/edge capabilities, and performance optimizations for large graphs
- **Alternative considered**: D3.js (already in project but more complex for this use case), Cytoscape.js (less React-integrated)

## Database Schema Changes

### Rooms Table Additions

Add `map_x` column (numeric/decimal, nullable) for admin layout X coordinate

- Add `map_y` column (numeric/decimal, nullable) for admin layout Y coordinate
- Migration script via PostgreSQL CLI, integrated into existing migration system

### Player Exploration Table (New)

`id` (uuid, primary key)

- `player_id` (uuid, foreign key to players table)
- `room_id` (uuid, foreign key to rooms table)
- `explored_at` (timestamp, when room was first explored)
- Unique constraint on `(player_id, room_id)`
- Index on `player_id` for fast player lookups
- Index on `room_id` for reverse lookups

### Exploration Tracking Integration

Automatically mark rooms as explored when player enters via movement service

- Called directly from movement service after successful move
- Error handling ensures exploration failures don't block movement
