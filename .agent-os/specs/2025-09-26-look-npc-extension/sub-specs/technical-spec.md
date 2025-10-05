# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-09-26-look-npc-extension/spec.md

## Technical Requirements

- **Command Parsing Enhancement** - Modify `handle_look_command` in `server/commands/exploration_commands.py` to check for NPC targets before direction targets
- **NPC Matching Logic** - Implement case-insensitive partial string matching against NPC names in the current room
- **NPC Data Retrieval** - Use existing room `get_npcs()` method to retrieve NPC instances in the current room
- **NPC Information Formatting** - Display NPC name, description, and flavor text in a consistent format
- **Multiple Match Handling** - When multiple NPCs match, return a list of matching NPC names
- **Error Message Standardization** - Return "You don't see anyone like that here." for no matches
- **Command Priority Implementation** - Check NPC matches first, then fall back to direction look if no NPCs match
- **NPC Instance Access** - Retrieve NPC instances from the persistence layer using the NPC IDs returned by `room.get_npcs()`

## Implementation Details

### Command Flow
1. Extract target from `command_data.get("target")` or `command_data.get("direction")`
2. Get current room and retrieve NPC list using `room.get_npcs()`
3. For each NPC ID, retrieve NPC instance from persistence layer
4. Perform case-insensitive partial matching on NPC names
5. If single match: display NPC information
6. If multiple matches: display list of matching names
7. If no matches: check for direction look as fallback
8. If no direction match: return error message

### NPC Information Display Format
```
NPC Name
NPC Description
NPC Flavor Text
```

### Multiple Match Display Format
```
You see several people here:
- NPC Name 1
- NPC Name 2
- NPC Name 3
```

### Error Handling
- No NPCs in room: "You don't see anyone like that here."
- No matching NPCs: "You don't see anyone like that here."
- Invalid room: Use existing room error handling
- Missing persistence: Use existing persistence error handling
