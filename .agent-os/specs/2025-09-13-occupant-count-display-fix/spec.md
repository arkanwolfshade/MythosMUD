# Spec Requirements Document

> Spec: Occupant Count Display Fix
> Created: 2025-09-13

## Overview

Fix the occupant count display issue in the multiplayer game client by implementing proper event handling for real-time room occupant updates. This will ensure accurate occupant counts are displayed immediately when players join or leave rooms during gameplay.

## User Stories

### Real-Time Occupant Visibility

As a player, I want to see accurate occupant counts in real-time when other players join or leave my room, so that I can be aware of who is present and have a better multiplayer experience.

When a player moves into or out of my current room, I should see the occupant count update immediately without needing to refresh or perform any other action. The count should reflect the actual number of players currently in the room.

### Consistent Multiplayer State

As a player, I want all clients to show the same occupant count for the same room, so that there's no confusion about who is present during multiplayer sessions.

When multiple players are in the same room, all connected clients should display the identical occupant count and occupant list, ensuring synchronized multiplayer state across all participants.

## Spec Scope

1. **Server-Side Event Broadcasting** - Add event listeners in connection manager for PlayerEnteredRoom/PlayerLeftRoom events and broadcast room_occupants events during player movement
2. **Client-Side Event Handling** - Add room_occupants event handler in GameTerminalWithPanels.tsx to process occupant updates from server
3. **Real-Time State Synchronization** - Ensure occupant count updates are applied immediately to the client state and UI display

## Out of Scope

- Modifying the existing UI components (RoomInfoPanel.tsx, RoomInfo.tsx) as they already handle occupant display correctly
- Changing the database schema or persistence layer
- Implementing new occupant-related features beyond fixing the display issue
- Performance optimizations for high-frequency occupant updates

## Expected Deliverable

1. Server broadcasts room_occupants events when players move between rooms (not just on disconnect)
2. Client processes room_occupants events and updates occupant count in real-time
3. All connected clients show synchronized occupant counts when players join/leave rooms
