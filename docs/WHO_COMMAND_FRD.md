# 🕵️ Who Command Feature Requirements Document (FRD)

**Document Version**: 1.0
**Date**: 2025-01-27
**Author**: Professor of Occult Studies
**Status**: Ready for Implementation
**Priority**: High

---

## 📋 **Feature Overview**

### **Purpose**

Enhance the existing "who" command to provide a standard level of detail for listing online players, including names, levels, and locations with basic filtering capabilities.

### **Background**

The current "who" command implementation provides basic functionality but lacks the detailed information and filtering capabilities common in MUD systems. This enhancement will improve the social experience by allowing players to easily locate and identify other investigators in the eldritch corridors of MythosMUD.

---

## 🎯 **Requirements**

### **Core Requirements**

#### **R1: Standard Information Display**

- **Requirement**: Display player name, level, and location for all online players
- **Format**: `PlayerName [Level] - Zone: Sub-zone: Room`
- **Example**: `Alice [5] - Arkham: University: Library`

#### **R2: Basic Filtering**

- **Requirement**: Support `who <name>` for searching specific players
- **Behavior**: Case-insensitive partial matching
- **Example**: `who al` finds "Alice", "Albert", "Malcolm"

#### **R3: Admin Indicators**

- **Requirement**: Show admin status for administrators
- **Format**: `PlayerName [Level] [ADMIN] - Zone: Sub-zone: Room`
- **Example**: `Alice [5] [ADMIN] - Arkham: University: Library`

#### **R4: Helpful Error Messages**

- **Requirement**: Provide guidance when no matches found
- **Format**: "No players found matching 'xyz'. Try 'who' to see all online players."

#### **R5: Simple List Format**

- **Requirement**: Display results in a clean, comma-separated list
- **Format**: `Online players (3): Alice [5] - Arkham: University: Library, Bob [3] - Miskatonic: River: Bridge`

### **Technical Requirements**

#### **TR1: Performance**

- **Requirement**: Response time under 100ms for up to 100 online players
- **Constraint**: Must not impact other game systems

#### **TR2: Data Consistency**

- **Requirement**: Use real-time player data from persistence layer
- **Constraint**: Must handle concurrent player updates

#### **TR3: Error Handling**

- **Requirement**: Graceful handling of persistence layer failures
- **Fallback**: Return appropriate error message

#### **TR4: Security**

- **Requirement**: No sensitive player information exposure
- **Constraint**: Only show publicly visible information

---

## 🏗️ **System Architecture**

### **Current Implementation**

```python
# Current basic implementation in server/commands/utility_commands.py
async def handle_who_command(args, current_user, request, alias_storage, player_name):
    # Basic online player listing
    # 5-minute activity threshold
    # Simple comma-separated output
```

### **Enhanced Implementation**

```python
# Enhanced implementation with filtering and formatting
async def handle_who_command(args, current_user, request, alias_storage, player_name):
    # Parse filter arguments
    # Apply case-insensitive partial matching
    # Format with level and location
    # Add admin indicators
    # Return formatted results
```

### **Data Flow**

1. **Command Input**: Player enters `who` or `who <filter>`
2. **Argument Parsing**: Extract filter term if provided
3. **Player Lookup**: Query persistence layer for online players
4. **Filtering**: Apply case-insensitive partial matching
5. **Formatting**: Format results with level and location
6. **Admin Check**: Add admin indicators where appropriate
7. **Response**: Return formatted list to player

---

## 📊 **User Interface**

### **Command Syntax**

```
who                    # List all online players
who <name>            # Filter players by name
```

### **Output Examples**

#### **All Players (No Filter)**

```
Online players (3): Alice [5] - Arkham: University: Library, Bob [3] - Miskatonic: River: Bridge, Charlie [7] [ADMIN] - Innsmouth: Harbor: Docks
```

#### **Filtered Results**

```
Players matching 'al' (2): Alice [5] - Arkham: University: Library, Malcolm [4] - Arkham: Sanitarium: Ward
```

#### **No Matches**

```
No players found matching 'xyz'. Try 'who' to see all online players.
```

#### **No Players Online**

```
No players are currently online.
```

---

## 🔧 **Implementation Details**

### **File Modifications**

#### **Primary Changes**

- `server/commands/utility_commands.py` - Enhanced who command handler
- `server/help/help_content.py` - Add who command documentation

#### **Supporting Changes**

- `server/tests/test_utility_commands.py` - Enhanced test coverage
- `server/utils/command_parser.py` - Update command parsing if needed

### **Key Functions**

#### **Enhanced Who Handler**

```python
async def handle_who_command(args, current_user, request, alias_storage, player_name):
    """
    Enhanced who command with filtering and detailed formatting.

    Args:
        args: Command arguments (optional filter term)
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Formatted who command result
    """
```

#### **Player Filtering**

```python
def filter_players_by_name(players, filter_term):
    """
    Filter players by case-insensitive partial name matching.

    Args:
        players: List of player objects
        filter_term: Search term

    Returns:
        list: Filtered player list
    """
```

#### **Location Formatting**

```python
def format_player_location(player):
    """
    Format player location as Zone: Sub-zone: Room.

    Args:
        player: Player object

    Returns:
        str: Formatted location string
    """
```

### **Data Structures**

#### **Player Information**

```python
class PlayerInfo:
    name: str
    level: int
    location: str
    is_admin: bool
    last_active: datetime
```

---

## 🧪 **Testing Strategy**

### **Unit Tests**

#### **Core Functionality**

- Test basic who command (no filter)
- Test filtering with exact matches
- Test filtering with partial matches
- Test case-insensitive matching
- Test admin indicator display

#### **Edge Cases**

- Test empty filter results
- Test special characters in names
- Test very long player lists
- Test persistence layer failures

#### **Performance Tests**

- Test with 100+ online players
- Test response time under load
- Test memory usage

### **Integration Tests**

- Test with real player data
- Test concurrent player updates
- Test with admin privileges

---

## 📈 **Success Criteria**

### **Functional Criteria**

- [ ] `who` command displays all online players with level and location
- [ ] `who <name>` filters players by case-insensitive partial matching
- [ ] Admin players show [ADMIN] indicator
- [ ] Helpful error messages for no matches
- [ ] Clean, readable output format

### **Performance Criteria**

- [ ] Response time under 100ms for typical usage
- [ ] No impact on other game systems
- [ ] Graceful handling of persistence failures

### **Quality Criteria**

- [ ] 100% test coverage for new functionality
- [ ] No regression in existing who command behavior
- [ ] Proper error handling and logging
- [ ] Documentation updated

---

## 🚀 **Implementation Plan**

### **Phase 1: Core Enhancement (1-2 days)**

1. Enhance `handle_who_command` function
2. Add filtering logic
3. Implement location formatting
4. Add admin indicators

### **Phase 2: Testing & Documentation (1 day)**

1. Update unit tests
2. Add integration tests
3. Update help documentation
4. Performance testing

### **Phase 3: Deployment & Validation (1 day)**

1. Code review and testing
2. Deploy to development environment
3. User acceptance testing
4. Monitor for issues

---

## 🔒 **Security Considerations**

### **Information Exposure**

- Only display publicly visible player information
- No sensitive stats or personal data
- Admin status is intentionally visible for transparency

### **Input Validation**

- Validate filter terms for injection attempts
- Sanitize output to prevent XSS
- Rate limit who command usage

### **Privacy**

- Respect player privacy settings (future enhancement)
- Log who command usage for moderation purposes

---

## 📚 **References**

### **Related Documents**

- `docs/COMMAND_HANDLER_PATTERNS.md` - Command system patterns
- `docs/COMMAND_SECURITY_GUIDE.md` - Security guidelines
- `server/commands/utility_commands.py` - Current implementation

### **Technical References**

- FastAPI command handling patterns
- Pydantic data validation
- SQLite persistence layer documentation

---

## 📝 **Notes**

### **Future Enhancements**

- Status effect indicators (AFK, Busy, etc.)
- Advanced filtering (by level, zone, etc.)
- Player titles and achievements
- Guild/clan affiliations

### **Performance Considerations**

- Consider caching for large player lists
- Optimize database queries for filtering
- Monitor memory usage with many online players

---

*"In the vast corridors of our digital Arkham, the ability to locate one's fellow investigators is not merely a convenience—it is a necessity for survival and collaboration in the face of the unknown."* - Professor of Occult Studies
