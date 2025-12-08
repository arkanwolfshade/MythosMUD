# Client Layout Baseline

**Date:** 2025-11-25
**Status:** ✅ Verified and Working

This document serves as the baseline reference for the game client panel layout. All future layout changes should reference this document and maintain consistency with this established design.

## Layout Overview

The game client uses a three-column layout with five draggable panels:

- **Left Column:** Chat Panel (top) + Room Info Panel (bottom)
- **Middle Column:** Game Log Panel (full height, wider)
- **Right Column:** Status Panel (top) + Commands Panel (bottom)

## Panel Configuration

### Chat Panel

- **Position:** `x: 50, y: 80`
- **Size:** `width: 450, height: 650`
- **Z-Index:** `1001`
- **Variant:** `eldritch`
- **Location:** Left column, top
- **Purpose:** Chat messages, channel selection, activity indicators

### Game Log Panel

- **Position:** `x: 520, y: 80`
- **Size:** `width: 550, height: 900` (with `autoSize={true}`)
- **Z-Index:** `1000` (lowest, middle column)
- **Variant:** `default`
- **Location:** Middle column, full height
- **Purpose:** Game events, room descriptions, game ticks, searchable log

### Room Info Panel

- **Position:** `x: 50, y: 780`
- **Size:** `width: 450, height: 200`
- **Z-Index:** `1002`
- **Variant:** `default`
- **Location:** Left column, bottom
- **Purpose:** Current room information, zone, subzone, occupants

### Status Panel

- **Position:** `x: 1090, y: 80`
- **Size:** `width: 350, height: 650`
- **Z-Index:** `1004` (highest, right column top)
- **Variant:** `default`
- **Location:** Right column, top
- **Purpose:** Player stats, health, lucidity, attributes, profession

### Commands Panel

- **Position:** `x: 1090, y: 780`
- **Size:** `width: 350, height: 200`
- **Z-Index:** `1003`
- **Variant:** `elevated`
- **Location:** Right column, bottom
- **Purpose:** Command input, recent commands, logout

## Header Configuration

- **Position:** `fixed top-0 left-0 right-0`
- **Z-Index:** `z-[9999]` (highest, always on top)
- **Content:** Connection status, player name, Mythos Time HUD
- **Styling:** Dark background with semi-transparent overlay (`bg-mythos-terminal-surface/95`)

## Z-Index Hierarchy

Z-index values ensure proper layering when panels overlap:

1. **Header:** `9999` (always on top)
2. **Status Panel:** `1004` (right column, top)
3. **Commands Panel:** `1003` (right column, bottom)
4. **Room Info Panel:** `1002` (left column, bottom)
5. **Chat Panel:** `1001` (left column, top)
6. **Game Log Panel:** `1000` (middle column, lowest)

## Key Implementation Details

### Positioning System

- All panels use **absolute positioning** with explicit `position: 'absolute'` in inline styles
- Default positions are in **absolute pixels** (not relative percentages)
- Panels are **draggable and resizable** but positions reset to defaults on page refresh (no localStorage persistence)

### Panel Styling

- **Background:** `bg-mythos-terminal-surface` (solid, opaque)
- **Overflow:** `overflow-hidden` on panel container, `overflow-auto` on content area
- **Content Area:** Has `relative` positioning and background to prevent content bleeding
- **Borders:** Thin gray borders with rounded corners

### Viewport Considerations

- Header height: ~60px (panels start at `y: 80` to account for header)
- Default viewport assumption: 1920x1080, but layout adapts to actual viewport
- Panels are clamped to viewport bounds with 50px padding

## File Locations

- **Main Layout Component:** `client/src/components/GameTerminal.tsx`
- **Panel Component:** `client/src/components/DraggablePanel.tsx`
- **Panel Components:**
  - Chat: `client/src/components/panels/ChatPanel.tsx`
  - Game Log: `client/src/components/panels/GameLogPanel.tsx`
  - Commands: `client/src/components/panels/CommandPanel.tsx`
  - Room Info: `client/src/components/RoomInfoPanel.tsx`
  - Status: Inline in `GameTerminal.tsx`

## Layout Validation

✅ All panels are fully visible on screen
✅ No content bleeding between panels
✅ Proper z-index layering prevents overlap issues
✅ Header is fully visible at top of viewport
✅ Panels maintain consistent spacing and alignment
✅ Layout matches wireframe design specification

## Notes for Future Development

1. **Position Persistence:** Currently disabled (localStorage removed). If re-implementing, ensure validation prevents off-screen positions.

2. **Responsive Design:** Layout uses absolute pixels. For responsive design, consider viewport-relative positioning or media queries.

3. **Panel Ordering:** Z-index values are critical. When adding new panels, assign appropriate z-index values based on desired layering.

4. **Header Height:** If header height changes, update panel `defaultPosition.y` values accordingly (currently `y: 80`).

5. **Content Overflow:** Content areas use `overflow-auto` for scrolling. Ensure content doesn't overflow panel boundaries.

## Visual Reference

The layout matches the wireframe specification:

- Left column: Two stacked panels (Chat large, Room Info small)
- Middle column: One large panel (Game Log, full height)
- Right column: Two stacked panels (Status large, Commands small)
- All panels aligned at top (`y: 80`) and bottom (`y: 780`) edges
- Consistent spacing between columns

---

**Last Updated:** 2025-11-25
**Verified By:** Playwright MCP testing with account Ithaqua/Cthulhu1
