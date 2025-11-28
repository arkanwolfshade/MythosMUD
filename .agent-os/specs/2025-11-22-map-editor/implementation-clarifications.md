# Implementation Clarifications

This document captures all clarifying questions and answers from the spec review process to ensure nothing is forgotten during implementation.

## Exit Data Handling

**Q:** How should exits be transformed to React Flow edges?
**A:** Handle both cases (string room IDs and object with target/flags/description) and merge them. Create a single edge with all flag information as metadata.

## Exit Flag Visualization

**Q:** How should exit flags be visualized?
**A:** Use icons/badges on the edge to indicate flags (hidden, locked, one-way, self_reference).

## Room Node Styling

**Q:** How should rooms be visually distinguished by subzone/environment?
**A:** Use different shapes (circle, square, diamond, etc.) based on subzone/environment type.

## Player Location Highlighting

**Q:** How should the player's current location be highlighted?
**A:** Use pulsing/animated highlighting to draw attention to the current room node.

## Search Functionality

**Q:** What should be searchable in the map viewer?
**A:** All of the following: room names, room IDs, room descriptions, zone/subzone names.

## Filter Controls

**Q:** What UI pattern should be used for zone/subzone filters?
**A:** Use dropdown selection menus for zone and subzone filtering.

## Layout Persistence Storage

**Q:** Where should map positions be stored?
**A:** Store positions in PostgreSQL database, linked to the existing rooms table. Add columns `map_x` (numeric/decimal, nullable) and `map_y` (numeric/decimal, nullable) directly to the `rooms` table to keep it normalized. Support both admin and player views.

## Admin vs Player View

**Q:** How should admin and player views work?
**A:**
- Admins see all rooms regardless of view type
- Players only see the "player_view" layout (only explored rooms)
- Admin view is the only editable view
- Player view is instanced per player based on explored rooms (tracked via `player_exploration` junction table)
- Exploration is automatically marked when a player enters a room via the movement service

## Database Schema - Player Exploration

**Q:** What should the player_exploration table structure be?
**A:**
- Separate `id` column as primary key
- Unique constraint on `(player_id, room_id)`
- Index on `player_id` for fast lookups of all explored rooms for a player
- Index on `room_id` for queries like "which players have explored this room"
- Fields: `player_id` (uuid FK to players), `room_id` (uuid FK to rooms), `explored_at` (timestamp)

## Movement System Integration

**Q:** How should exploration tracking integrate with movement?
**A:** Call exploration tracking directly from the movement service after a successful move, with error handling that doesn't block movement. This keeps it simple, maintains ACID properties, and ensures exploration failures don't affect movement.

## Exit Creation Interface

**Q:** How should admins create/edit exits?
**A:** Use a modal dialog that appears when clicking an edge or a "Create Exit" button. The form should:
- Pre-select the source room as the currently selected/clicked room
- Select the target room from a searchable/filterable dropdown
- Show a preview of the exit relationship on the map while editing
- Include validation feedback (e.g., "Target room does not exist") in real-time
- Allow editing exit properties (flags, descriptions) through the same interface

## Undo/Redo System

**Q:** What operations should be tracked in undo/redo?
**A:** All operations should be tracked: node position changes, edge (exit) creation/deletion/modification, and room property edits.

## Layout Algorithm

**Q:** What layout algorithm should be used?
**A:** Grid-based layout. Admins should be able to set what zone and subzone the nodes are in.

## Room Details Panel

**Q:** What information should be displayed in the room details panel?
**A:** All of the following: room name, ID, description, zone, subzone, plane, environment, current occupants/players in the room, exit list with directions and targets.

## Minimap

**Q:** What should the minimap show?
**A:** Small overview of a 7x7 grid of rooms with the player at the center.

## Map Route Access

**Q:** When and to whom should the map route be accessible?
**A:** Map link should be visible to all players, but the map should only show if they have explored at least one room.

## Exit Validation

**Q:** What validation rules should be enforced for exit creation/editing?
**A:** All of the following:
- Validate that the target room exists in the database
- Validate that the direction is valid (north, south, east, west, up, down)
- Validate that bidirectional exits are properly paired (warning, not requirement - one-way exits are allowed)
- Prevent creating exits to non-existent rooms

## Performance Optimization

**Q:** What performance optimization approach should be prioritized?
**A:** Use lazy loading for handling large numbers of rooms.

## Accessibility

**Q:** What accessibility features should be implemented?
**A:** None for now (deferred to future iteration).

## Save Functionality

**Q:** How should admin edits be saved?
**A:**
- Saved only when the admin clicks a "Save" button
- Saved with a confirmation dialog to prevent accidental saves
- Positions only saved when admin clicks "Save" (along with other changes)
- Show visual indicator (node color/border change) that position has changed but not been saved yet
- Allow admins to reset positions to auto-layout if they don't like manual positioning

## Room Property Editing

**Q:** Which room properties should be editable?
**A:** All room properties from the room schema should be editable. The form should:
- Allow editing all properties at once, or have tabs/sections for different property groups
- Show validation errors inline (e.g., "Room ID format invalid")
- Appear when clicking an "Edit Room" button in the room details panel

## Custom Node Components

**Q:** What functionality should custom node components provide?
**A:**
- Use React Flow's built-in node customization features (Handle, custom shapes)
- Support click events to open the room details panel

## Map Controls

**Q:** What controls should be included?
**A:**
- Use React Flow's built-in controls
- Include a "Reset View" button to return to default zoom/position

## Error Handling

**Q:** How should errors be displayed?
**A:** Show errors in a dedicated error banner at the top of the map. Use the existing error handling system in the client if one exists.

## Exit Object Handling

**Q:** How should complex exit objects be handled in visual representation?
**A:** Create a single edge with all flag information as metadata.

## Player View - Unexplored Rooms

**Q:** How should unexplored rooms be handled in the player's map view?
**A:** Only show rooms they have personally explored. No indication that other rooms exist.

## Node Position Changes

**Q:** How should node position changes be handled in the edit workflow?
**A:**
- Only save positions when the admin clicks "Save" (along with other changes)
- Show visual indicator that position has changed but not been saved yet
- Allow admins to reset positions to auto-layout if they don't like manual positioning

## Database Migration

**Q:** How should database schema changes be handled?
**A:** Create a migration script that can be run via PostgreSQL CLI. Add the migration to the existing database migration system.

## API Endpoint - GET /api/rooms/list

**Q:** What should be the default behavior and response format?
**A:**
- Require filter parameters of `plane` and `zone`, with `subzone` optional
- Return room data in the same format as existing room endpoints (for consistency)
- Include exit relationships in a format that's easy to convert to React Flow edges
- Include room positions (map_x, map_y) if they exist in the database

## Navigation Link Placement

**Q:** Where should the map navigation link be placed?
**A:** TBD - To be clarified during Task 7.4 implementation (Route Integration and Navigation)
