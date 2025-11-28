# Spec Tasks

## Tasks

- [x] 1. React Flow Integration and Setup
  - [x] 1.1 Write tests for React Flow installation and configuration
  - [x] 1.2 Install reactflow package (latest stable version ^11.x)
  - [x] 1.3 Configure React Flow with custom node types using built-in customization (Handle, custom shapes)
  - [x] 1.4 Configure React Flow with custom edge types (ExitEdge with icon/badge indicators for flags)
  - [x] 1.5 Set up grid-based layout algorithm (admins can set zone/subzone for nodes)
  - [x] 1.6 Verify all tests pass

- [x] 2. Data Transformation Utilities
  - [x] 2.1 Write tests for room data transformation utilities
  - [x] 2.2 Implement mapUtils.ts to convert room JSON to React Flow format
  - [x] 2.3 Handle exits dictionary transformation (handle both string room IDs and object format with target/flags/description, merge into single edges)
  - [x] 2.4 Handle room types and environment-based styling (different shapes: circle, square, diamond, etc.)
  - [x] 2.5 Use stored coordinates (map_x, map_y) from database when available, fallback to grid layout
  - [x] 2.6 Verify all tests pass

- [x] 3. Server API Endpoints
  - [x] 3.1 Write tests for GET /api/rooms/list endpoint
  - [x] 3.2 Implement GET /api/rooms/list with required plane/zone parameters and optional subzone
  - [x] 3.3 Return room data in same format as existing endpoints, include map_x/map_y when available
  - [x] 3.4 Add include_exits parameter support (default: true)
  - [x] 3.5 Write tests for room position updates (saving to rooms.map_x/map_y columns)
  - [x] 3.6 Implement room position update endpoint (admin only, saves to rooms table)
  - [x] 3.7 Add admin permission checks for edit endpoints
  - [x] 3.8 Verify all tests pass

- [x] 4. Data Loading and State Management
  - [x] 4.1 Write tests for useRoomMapData hook
  - [x] 4.2 Implement useRoomMapData hook for fetching room data (requires plane/zone, optional subzone)
  - [x] 4.3 Add loading/error state handling (error banner at top of map)
  - [x] 4.4 Implement zone/subzone filtering support (dropdown selection)
  - [x] 4.5 Write tests for useMapLayout hook
  - [x] 4.6 Implement useMapLayout hook for grid-based layout management
  - [x] 4.7 Use stored coordinates (map_x, map_y) from database when available
  - [x] 4.8 Implement manual positioning persistence (save on button click with confirmation)
  - [x] 4.9 Add performance optimizations (debouncing, memoization, lazy loading)
  - [x] 4.10 Verify all tests pass

- [x] 5. Map Viewer Component (View Mode)
  - [x] 5.1 Write tests for RoomMapViewer component
  - [x] 5.2 Create RoomMapViewer.tsx main container component
  - [x] 5.3 Implement custom RoomNode component using React Flow Handle/custom shapes (different shapes by subzone/environment)
  - [x] 5.4 Implement custom IntersectionNode component
  - [x] 5.5 Implement custom ExitEdge component with icon/badge indicators for flags (hidden, locked, one-way, self_reference)
  - [x] 5.6 Add click events on nodes to open room details panel
  - [x] 5.7 Create MapControls component (React Flow built-in controls, reset view button, dropdown filters, search)
  - [x] 5.8 Implement minimap showing 7x7 grid centered on player
  - [x] 5.9 Create RoomDetailsPanel component (room name, ID, description, zone, subzone, plane, environment, occupants, exits)
  - [x] 5.10 Implement pulsing/animated highlighting for player's current location
  - [x] 5.11 Implement search functionality (room names, IDs, descriptions, zone/subzone names)
  - [x] 5.12 Verify all tests pass

- [ ] 6. Admin Edit Mode
  - [x] 6.1 Write tests for useMapEditing hook
  - [x] 6.2 Implement useMapEditing hook for admin edit operations
  - [x] 6.3 Add node drag/reposition functionality (visual indicator for unsaved changes via color/border)
  - [x] 6.4 Implement edge creation via modal form/dialog (source pre-selected, target from searchable dropdown, preview on map, real-time validation)
  - [x] 6.5 Add edge deletion functionality
  - [x] 6.6 Implement edge editing (flags, descriptions) via same modal form
  - [x] 6.7 Implement room property editing (all schema properties, tabs/sections, inline validation, triggered from "Edit Room" button in details panel)
  - [x] 6.8 Add comprehensive validation (target room exists, valid direction, bidirectional pairing warnings, data integrity)
  - [x] 6.9 Implement undo/redo support (track all operations: positions, edges, properties)
  - [x] 6.10 Add save functionality (save button with confirmation dialog, reset to auto-layout option)
  - [x] 6.11 Verify all tests pass

- [x] 7. Route Integration and Navigation
  - [x] 7.1 Write tests for /map route integration
  - [x] 7.2 Add /map route to main router configuration (Note: App uses state-based navigation, map integrated via modal)
  - [x] 7.3 Create MapView.tsx component wrapper
  - [x] 7.4 Add navigation link visible to all players (map content only shown if player has explored at least one room)
    - **RESOLVED:** Map navigation link placed in ESC modal menu (MainMenuModal)
  - [x] 7.5 Integrate with existing player location tracking (use player.position from gameStore)
  - [x] 7.6 Verify all tests pass

- [x] 8. Performance Optimization
  - [x] 8.1 Write tests for lazy loading
  - [x] 8.2 Implement lazy loading for rooms outside viewport (React Flow onlyRenderVisibleElements)
  - [x] 8.3 Optimize layout recalculations with debouncing
  - [x] 8.4 Add memoized node/edge rendering
  - [x] 8.5 Verify 60fps performance targets (performance monitor added)
  - [x] 8.6 Verify all tests pass

- [x] 9. Theme and Styling
  - [x] 9.1 Write tests for theme integration
  - [x] 9.2 Apply consistent styling with existing client UI theme (all components use mythos-terminal-* classes)
  - [x] 9.3 Support dark mode if applicable (ThemeContext supports dark/light/terminal themes)
  - [x] 9.4 Verify all tests pass (accessibility deferred to future iteration)

- [ ] 10. Database Schema and Exploration Tracking
  - [x] 10.1 Write migration script for adding map_x/map_y columns to rooms table
  - [x] 10.2 Write migration script for creating player_exploration table
  - [x] 10.3 Add migrations to existing migration system (PostgreSQL CLI)
  - [x] 10.4 Write tests for exploration service
  - [x] 10.5 Implement exploration service (mark room as explored)
  - [x] 10.6 Integrate exploration tracking into movement service (call after successful move, error handling)
  - [x] 10.7 Write tests for player view filtering (only show explored rooms)
  - [x] 10.8 Implement player view filtering in useRoomMapData hook
  - [x] 10.9 Verify all tests pass

- [ ] 11. Integration Testing and Documentation
  - [x] 11.1 Write E2E tests for map viewer (view mode)
  - [x] 11.2 Write E2E tests for admin edit mode
  - [x] 11.3 Test with large room sets (500+ rooms)
  - [x] 11.4 Test performance benchmarks
  - [x] 11.5 Update documentation
  - [ ] 11.6 Verify all tests pass
