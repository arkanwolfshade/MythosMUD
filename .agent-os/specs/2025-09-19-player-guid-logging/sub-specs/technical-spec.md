# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-09-19-player-guid-logging/spec.md

## Technical Requirements

### GUID Detection and Pattern Matching
- **UUID Regex Pattern**: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` (case-insensitive)
- **Player GUID Validation**: Only convert GUIDs that correspond to actual players in the system
- **Context Awareness**: Convert GUIDs in all log message contexts (connection events, game actions, errors, etc.)

### Player Data Integration
- **In-Memory Access**: Leverage existing player data structures already loaded in memory
- **Thread Safety**: Ensure GUID lookup operations are thread-safe for concurrent logging
- **Performance**: Minimize lookup overhead by using efficient data structures (O(1) or O(log n) lookup)

### Logging Formatter Enhancement
- **Integration Point**: Modify the existing `logging.Formatter` in `server/logging_config.py` (line 254-258)
- **Output-Level Processing**: Apply conversion at the formatter level, not at individual log statements
- **Format Preservation**: Maintain existing log format while enhancing GUID display
- **All Log Files**: Apply to all log categories (server, persistence, authentication, world, communications, commands, errors, access, console)

### Error Handling and Fallback
- **Unknown GUID Display**: Show `<UNKNOWN>: <GUID>` when player lookup fails
- **Error Logging**: Log lookup failures to `errors.log` with appropriate error level
- **Graceful Degradation**: System continues normal operation even if GUID conversion fails

### Performance Considerations
- **Minimal Overhead**: GUID conversion should add <1ms per log message
- **Memory Efficiency**: No additional caching beyond existing player data structures
- **Concurrent Safety**: Handle multiple threads logging simultaneously without race conditions

## Implementation Architecture

### Custom Logging Formatter
```python
class PlayerGuidFormatter(logging.Formatter):
    """
    Custom formatter that converts player GUIDs to "<name>: <GUID>" format.

    As noted in the Pnakotic Manuscripts, proper identification of entities
    is crucial for understanding the flow of events through our eldritch systems.
    """

    def __init__(self, player_service, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player_service = player_service
        self.uuid_pattern = re.compile(
            r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b',
            re.IGNORECASE
        )

    def format(self, record):
        # Get the original formatted message
        message = super().format(record)

        # Convert player GUIDs to "<name>: <GUID>" format
        enhanced_message = self._convert_player_guids(message)

        return enhanced_message

    def _convert_player_guids(self, message):
        """Convert player GUIDs in message to enhanced format."""
        def replace_guid(match):
            guid = match.group(0)
            player_name = self._get_player_name(guid)
            if player_name:
                return f"<{player_name}>: {guid}"
            else:
                # Log the lookup failure
                self._log_lookup_failure(guid)
                return f"<UNKNOWN>: {guid}"

        return self.uuid_pattern.sub(replace_guid, message)

    def _get_player_name(self, guid):
        """Get player name for GUID from in-memory data."""
        try:
            # Access existing player data structures
            player = self.player_service.get_player_by_id(guid)
            return player.name if player else None
        except Exception:
            return None

    def _log_lookup_failure(self, guid):
        """Log GUID lookup failure to errors.log."""
        error_logger = logging.getLogger('errors')
        error_logger.warning(f"Failed to resolve player name for GUID: {guid}")
```

### Integration Points
- **Player Service Access**: Inject `PlayerService` or `PersistenceLayer` into the formatter
- **Formatter Registration**: Replace existing formatter in `_setup_file_logging()` function
- **Error Logger**: Use existing `errors` logger for lookup failure tracking

### Configuration Updates
- **Logging Config**: Modify `server/logging_config.py` to use custom formatter
- **Player Service Integration**: Ensure formatter has access to player data
- **Testing**: Add unit tests for GUID conversion logic

## External Dependencies

No new external dependencies required. This enhancement leverages existing:
- `structlog` logging infrastructure
- `PlayerService`/`PersistenceLayer` for player data access
- Standard library `re` module for regex pattern matching
- Existing error logging mechanisms
