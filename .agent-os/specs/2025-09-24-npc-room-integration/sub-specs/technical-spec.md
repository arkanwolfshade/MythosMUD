# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-09-24-npc-room-integration/spec.md

## Technical Requirements

- **Event Handler Implementation** - Create NPCEnteredRoom and NPCLeftRoom event handlers in the persistence layer or event handler to process NPC room entry/exit events
- **Room Integration** - Modify room occupant tracking to call `room.npc_entered(npc_id)` and `room.npc_left(npc_id)` when NPC events are processed
- **Data Transformation** - Update room data processing to combine `room.get_players()`, `room.get_npcs()`, and `room.get_objects()` into a unified `occupants` array for client consumption
- **NPC Name Resolution** - Implement NPC ID to display name mapping using the NPC lifecycle manager's active NPC registry or NPC instance service
- **Real-time Broadcasting** - Ensure room occupant updates are broadcast to all connected players when NPCs enter/leave rooms
- **Client Data Structure** - Maintain existing client interface expectations (occupants as string array) while supporting both player names and NPC names
- **Event Subscription** - Subscribe to NPCEnteredRoom and NPCLeftRoom events in the appropriate service (persistence layer or real-time event handler)
- **Error Handling** - Implement proper error handling for cases where NPC IDs cannot be resolved to names or rooms cannot be found

## Integration Points

- **NPC Lifecycle Manager** - Source of NPCEnteredRoom/NPCLeftRoom events when NPCs spawn/despawn
- **Room Model** - Target for NPC occupant tracking via `npc_entered()`/`npc_left()` methods
- **Real-time Event Handler** - Potential location for event subscription and room occupant broadcasting
- **Persistence Layer** - Alternative location for event subscription and room data management
- **Connection Manager** - Broadcasting mechanism for room occupant updates to connected players
- **Room Info Panel** - Client component that will display the integrated occupant data

## Performance Considerations

- **Event Processing** - NPC room events should be processed efficiently without blocking the main game loop
- **Memory Usage** - NPC name resolution should use existing in-memory NPC registries to avoid database lookups
- **Broadcasting Efficiency** - Room occupant updates should only be sent to players currently in the affected room
- **Data Consistency** - Ensure room occupant data remains consistent across all connected players
