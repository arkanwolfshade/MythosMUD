# Spec Requirements Document

> Spec: NPC-Room Integration
> Created: 2025-09-24

## Overview

Integrate the NPC spawning system with the room occupant tracking system to make spawned NPCs visible in the Room Info panel. This feature will bridge the dimensional barrier between the NPC lifecycle management and room display systems, allowing players to see NPCs as room occupants alongside other players.

## User Stories

### Player Room Awareness

As a player, I want to see all NPCs present in my current room in the Room Info panel, so that I can be aware of the game world's inhabitants and interact with them appropriately.

**Detailed Workflow:**
1. Player enters a room that contains spawned NPCs
2. Room Info panel displays both players and NPCs in the occupants list
3. Player can see NPC names and types (shopkeeper, quest giver, etc.)
4. Occupant count accurately reflects total entities (players + NPCs) in the room

### NPC Visibility During Spawning

As a player, I want to see NPCs appear in the room occupants list when they spawn, so that the game world feels dynamic and alive.

**Detailed Workflow:**
1. NPC spawns in a room due to server startup or dynamic spawning
2. NPCEnteredRoom event is processed by the room system
3. NPC is added to room's occupant tracking
4. All players in the room receive updated occupant list
5. Room Info panel reflects the new NPC presence

## Spec Scope

1. **Event Handler Integration** - Create event handler to process NPCEnteredRoom events and add NPCs to room occupant tracking
2. **Room Data Transformation** - Modify room data processing to combine player and NPC data into unified occupants array for client consumption
3. **NPC Name Resolution** - Implement mapping from NPC IDs to display names for UI presentation
4. **Real-time Updates** - Ensure room occupant updates are broadcast to all players when NPCs enter/leave rooms

## Out of Scope

- NPC movement between rooms (handled by existing movement system)
- NPC interaction commands (separate feature)
- NPC behavior modifications (existing system sufficient)
- Room Info panel UI changes (current design accommodates mixed occupants)

## Expected Deliverable

1. Spawned NPCs appear in Room Info panel occupants list alongside players
2. Real-time occupant updates when NPCs enter/leave rooms during gameplay
3. Accurate occupant count reflecting both players and NPCs
4. NPCs display with proper names and are distinguishable from players in the UI
