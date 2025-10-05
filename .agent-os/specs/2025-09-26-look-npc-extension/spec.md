# Spec Requirements Document

> Spec: Look NPC Extension
> Created: 2025-09-26

## Overview

Extend the existing `look` command to accept an optional NPC target, allowing players to examine NPCs in their current room by name. This feature will enhance player immersion and provide detailed information about NPCs including their name, description, and flavor text.

## User Stories

### NPC Examination

As a player, I want to examine NPCs in my current room by typing `look <npc_name>`, so that I can learn more about the characters around me and make informed decisions about interactions.

When I type `look guard`, the system should find NPCs in my current room whose names contain "guard" (case-insensitive) and display their detailed information. If multiple NPCs match, I should see a list of matching names to choose from. If no NPCs match, I should receive a clear error message.

## Spec Scope

1. **NPC Target Parsing** - Extend look command to accept NPC names as targets
2. **Case-Insensitive Partial Matching** - Match NPC names using case-insensitive partial string matching
3. **Multiple Match Handling** - Display list of matching NPC names when multiple matches found
4. **NPC Information Display** - Show NPC name, description, and flavor text in formatted output
5. **Command Priority** - Check for NPC matches before direction matches
6. **Error Handling** - Provide clear error messages for no matches found

## Out of Scope

- Looking at NPCs in other rooms
- Looking at NPCs by type or other attributes
- Interactive NPC dialogue or actions
- NPC inventory or equipment display
- NPC stat display beyond basic information
- Looking directions/exits
- Looking at players (PCs)

## Expected Deliverable

1. Players can type `look <npc_name>` and receive detailed NPC information
2. Multiple NPC matches display as a list of names for player selection
3. No matches return the error message "You don't see anyone like that here."
4. NPC look takes priority over direction look when both are possible
