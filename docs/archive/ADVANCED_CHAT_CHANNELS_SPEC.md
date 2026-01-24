# Advanced Chat Channels Specification

**Document Version:** 1.0
**Date:** 2025-08-27
**Author:** Miskatonic University Development Team
**Status:** Draft Specification

## Executive Summary

This specification defines the implementation of Advanced Chat Channels for MythosMUD, extending the existing NATS-based "say" system to support multiple communication channels with enhanced user experience and moderation capabilities.

## 1. Feature Overview

### 1.1 Purpose

Implement a comprehensive chat channel system that provides players with multiple communication options while maintaining the existing "say" command functionality. The system will support local, global, whisper, and system channels with appropriate access controls and moderation features.

### 1.2 Scope

**Local Channel**: Sub-zone based communication

**Global Channel**: Server-wide communication with level restrictions

**Whisper Channel**: Player-to-player private communication with reply functionality
- **System Channel**: Admin announcements (unmutable)
- **Integration**: Extends existing NATS-based "say" system
- **UI Support**: Both command-line and graphical interface options

### 1.3 Success Criteria

All channels function reliably with real-time messaging

- Player preferences persist across sessions
- Admin moderation tools are effective
- System integrates seamlessly with existing chat infrastructure
- Performance remains acceptable under normal load

## 2. Technical Architecture

### 2.1 System Integration

The new channel system will extend the existing NATS-based messaging infrastructure:

```
Existing "say" system
├── NATS Service (server/services/nats_service.py)
├── Chat Service (server/game/chat_service.py)
├── Rate Limiter (server/services/rate_limiter.py)
├── User Manager (server/services/user_manager.py)
└── Message Handler (server/realtime/nats_message_handler.py)

New Channel Extensions
├── Enhanced Chat Service (extended methods)
├── Channel Management Service (new)
├── Player Preferences Service (new)
├── Admin Moderation Service (new)
└── UI Channel Selector (client-side)
```

### 2.2 NATS Subject Patterns

Extend existing NATS subject patterns for new channels:

```python
# Existing patterns

"chat.say.{room_id}"           # Room-based say messages

# New patterns

"chat.local.{sub_zone_id}"     # Sub-zone based local messages
"chat.global"                  # Global server messages
"chat.whisper.{receiver_id}"   # Whisper messages to specific player
"chat.system"                  # System announcements
```

### 2.3 Database Schema Extensions

#### Player Channel Preferences Table

```sql
CREATE TABLE player_channel_preferences (
    player_id TEXT PRIMARY KEY,
    default_channel TEXT NOT NULL DEFAULT 'local',
    muted_channels TEXT,  -- JSON array of muted channel names
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(id)
);
```

**Note**: Channel muting will be handled through the existing JSON-based mute system in `server/data/user_management/`, while player preferences (default channel, etc.) will be stored in the database.

#### Channel Messages Table (for history)

**Note**: Chat messages will be logged to files in the `chat/` directory rather than stored in the database. Each channel type will have its own log file with structured logging format.

```python
# Log file structure

chat/
├── local_<subzone>.log    # Local channel messages per sub-zone
├── global.log             # Global channel messages
├── whisper.log            # Whisper messages
├── system.log             # System announcements
└── combined.log           # All channel messages (for moderation)

# Example sub-zone log files
# local_arkhamcity.log
# local_sanitarium.log
# local_miskatonic_university.log

```

#### Admin Channel Mutes Table

**Note**: Admin channel mutes will be handled using the existing JSON-based mute system in `server/data/user_management/`. The existing mute files already support channel-level muting through the `channel_mutes` field.

```json
// Example: server/data/user_management/mutes_player.json
{
  "player_id": "player",
  "last_updated": "2025-08-27T12:00:00.000000+00:00",
  "player_mutes": {},
  "channel_mutes": {
    "global": {
      "muted_by": "admin",
      "reason": "Spam",
      "muted_at": "2025-08-27T12:00:00.000000+00:00",
      "expires_at": "2025-08-28T12:00:00.000000+00:00"
    }
  },
  "global_mutes": {},
  "is_admin": false
}
```

## 3. Channel Specifications

### 3.1 Local Channel

#### 3.1.1 Scope

**Range**: Sub-zone based (all players in the same sub-zone)

**Dynamic**: Automatically updates as players move between sub-zones

**Subscription**: Players automatically subscribe to local channel of current sub-zone

#### 3.1.2 Implementation

```python
class LocalChannelStrategy:
    def get_subscribers(self, player_id: str) -> List[str]:
        """Get all players in the same sub-zone as the sender."""
        player = player_service.get_player_by_id(player_id)
        sub_zone = get_sub_zone_from_room(player.current_room_id)
        return get_players_in_sub_zone(sub_zone)

    def get_nats_subject(self, player_id: str) -> str:
        """Get NATS subject for local channel."""
        player = player_service.get_player_by_id(player_id)
        sub_zone = get_sub_zone_from_room(player.current_room_id)
        return f"chat.local.{sub_zone}"
```

#### 3.1.3 Commands

`/local <message>` - Send message to local channel

- `/l <message>` - Short form for local channel

### 3.2 Global Channel

#### 3.2.1 Scope

**Range**: Server-wide (all online players)

**Access**: Minimum level requirement (configurable, default: level 1)

**Rate Limiting**: Stricter than local channel

#### 3.2.2 Configuration

```yaml
# server_config.yaml additions

chat:
  global:
    min_level: 1  # Configurable minimum level
    rate_limit: 10  # messages per minute
```

#### 3.2.3 Implementation

```python
class GlobalChannelStrategy:
    def get_subscribers(self, player_id: str) -> List[str]:
        """Get all online players meeting level requirements."""
        min_level = config.get("chat.global.min_level", 1)
        return get_online_players_with_min_level(min_level)

    def get_nats_subject(self, player_id: str) -> str:
        """Get NATS subject for global channel."""
        return "chat.global"

    def check_access(self, player_id: str) -> bool:
        """Check if player can access global channel."""
        player = player_service.get_player_by_id(player_id)
        min_level = config.get("chat.global.min_level", 1)
        return player.level >= min_level
```

#### 3.2.4 Commands

`/global <message>` - Send message to global channel

- `/g <message>` - Short form for global channel

### 3.3 Whisper Channel

#### 3.3.1 Scope

**Range**: Player-to-player only

**Distance**: No distance limitations

**Reply**: Support for `/reply` command to respond to last whisper

#### 3.3.2 Implementation

```python
class WhisperChannelStrategy:
    def send_whisper(self, sender_id: str, receiver_name: str, message: str) -> dict:
        """Send whisper to specific player."""
        receiver = player_service.get_player_by_name(receiver_name)
        if not receiver:
            return {"success": False, "error": "You whisper into the aether."}

        # Check if receiver has muted sender

        if user_manager.is_player_muted(receiver.id, sender_id):
            return {"success": True, "message": "Message sent."}  # No error indicator

        # Store last whisper for reply functionality

        self.store_last_whisper(sender_id, receiver.id)

        # Send via NATS

        subject = f"chat.whisper.{receiver.id}"
        return self.publish_whisper(subject, sender_id, receiver.id, message)

    def reply_to_whisper(self, player_id: str, message: str) -> dict:
        """Reply to the last whisper received."""
        last_whisper = self.get_last_whisper(player_id)
        if not last_whisper:
            return {"success": False, "error": "No one has whispered to you recently."}

        return self.send_whisper(player_id, last_whisper.sender_name, message)
```

#### 3.3.3 Commands

`/whisper <player> <message>` - Whisper to specific player

- `/w <player> <message>` - Short form for whisper
- `/reply <message>` - Reply to last whisper received

### 3.4 System Channel

#### 3.4.1 Scope

**Range**: Server-wide (all online players)

**Access**: Admin-only for sending, all players receive

**Muting**: Players cannot mute system channel

#### 3.4.2 Implementation

```python
class SystemChannelStrategy:
    def send_system_message(self, admin_id: str, message: str) -> dict:
        """Send system announcement."""
        if not user_manager.is_admin(admin_id):
            return {"success": False, "error": "Admin access required."}

        subject = "chat.system"
        return self.publish_system_message(subject, admin_id, message)

    def get_subscribers(self, player_id: str) -> List[str]:
        """Get all online players (system messages cannot be muted)."""
        return get_all_online_players()
```

#### 3.4.3 Commands

`/system <message>` - Send system announcement (admin only)

## 4. User Interface

### 4.1 Command-Line Interface

#### 4.1.1 Channel Commands

```bash
# Local channel

/local <message>    # Send to local channel
/l <message>        # Short form

# Global channel

/global <message>   # Send to global channel
/g <message>        # Short form

# Whisper channel

/whisper <player> <message>  # Whisper to player
/w <player> <message>        # Short form
/reply <message>             # Reply to last whisper

# System channel (admin only)

/system <message>   # Send system announcement
```

#### 4.1.2 Channel Management Commands

```bash
/channel local       # Switch to local channel
/channel global      # Switch to global channel
/channel default     # Set default channel
/mute local          # Mute local channel
/unmute local        # Unmute local channel
/mutes               # Show muted channels
```

### 4.2 Graphical Interface

#### 4.2.1 Channel Selector

Dropdown menu for channel selection

- Visual indicators for active channel
- Mute/unmute toggles for each channel
- Channel-specific color coding

#### 4.2.2 Message Display

Color-coded messages by channel type

- Channel prefixes: `[Local]`, `[Global]`, `[Whisper]`, `[System]`
- Whisper format: `<playername> whispers to you: <message>`
- Real-time streaming with backscrolling for limited history

#### 4.2.3 Preferences Panel

Default channel selection

- Channel subscription toggles
- Mute management interface
- Visual feedback for rate limiting

## 5. Message Formatting

### 5.1 Channel Prefixes

```typescript
interface ChannelFormatting {
  local: {
    prefix: "[Local]",
    color: "#4CAF50",  // Green
    format: "[Local] <playername>: <message>"
  },
  global: {
    prefix: "[Global]",
    color: "#2196F3",  // Blue
    format: "[Global] <playername>: <message>"
  },
  whisper: {
    prefix: "[Whisper]",
    color: "#9C27B0",  // Purple
    format: "<playername> whispers to you: <message>"
  },
  system: {
    prefix: "[System]",
    color: "#FF9800",  // Orange
    format: "[System] <message>"
  }
}
```

### 5.2 Error Messages

```typescript
const ErrorMessages = {
  rateLimited: "You are being rate limited. Please wait before sending another message.",
  muted: "You are muted in this channel.",
  globalMuted: "You are globally muted and cannot send messages.",
  invalidChannel: "Invalid channel name. Available channels: local, global, whisper",
  playerNotFound: "You whisper into the aether.",
  noReplyTarget: "No one has whispered to you recently.",
  accessDenied: "You do not have access to this channel.",
  adminRequired: "Admin access required for this command."
};
```

## 6. Rate Limiting

### 6.1 Configuration

```yaml
# server_config.yaml

chat:
  rate_limiting:
    local: 20      # messages per minute
    global: 10     # messages per minute
    whisper: 30     # messages per minute
    system: 60     # messages per minute (admin)
```

### 6.2 Implementation

Extend existing rate limiter to support new channels:

```python
class RateLimiter:
    def check_rate_limit(self, player_id: str, channel: str, player_name: str) -> bool:
        """Check rate limit for specific channel."""
        limits = config.get("chat.rate_limiting", {})
        channel_limit = limits.get(channel, 15)  # Default fallback

        return self._check_limit(player_id, channel, channel_limit)
```

## 7. Player Preferences

### 7.1 Default Channel

Players can set their preferred default channel

- Stored in database and persists across sessions
- Default: "local" for new players

### 7.2 Channel Subscriptions

Players can subscribe/unsubscribe from channels

- Local channel automatically updates based on sub-zone
- Preferences stored in database

### 7.3 Mute Management

Channel-level muting (except system channel) - using existing JSON mute system

- Player-level muting (existing functionality)
- Admin channel mutes (using existing UserManager)

## 8. Admin Moderation

### 8.1 Channel Muting

```python
class AdminModerationService:
    def mute_player_from_channel(self, admin_id: str, player_id: str, channel: str, reason: str = None, duration: int = None) -> dict:
        """Mute player from specific channel using existing JSON mute system."""
        if not user_manager.is_admin(admin_id):
            return {"success": False, "error": "Admin access required."}

        # Use existing UserManager to handle channel muting

        expires_at = None
        if duration:
            expires_at = datetime.now() + timedelta(minutes=duration)

        return user_manager.mute_player_in_channel(player_id, channel, admin_id, reason, expires_at)

    def unmute_player_from_channel(self, admin_id: str, player_id: str, channel: str) -> dict:
        """Unmute player from specific channel using existing JSON mute system."""
        if not user_manager.is_admin(admin_id):
            return {"success": False, "error": "Admin access required."}

        return user_manager.unmute_player_from_channel(player_id, channel)
```

### 8.2 System Announcements

```python
def send_system_announcement(self, admin_id: str, message: str) -> dict:
    """Send system-wide announcement."""
    if not user_manager.is_admin(admin_id):
        return {"success": False, "error": "Admin access required."}

    return self.system_channel.send_system_message(admin_id, message)
```

### 8.3 Admin Commands

```bash
/mute <player> <channel> [duration] [reason]  # Mute player from channel
/unmute <player> <channel>                    # Unmute player from channel
/announce <message>                           # Send system announcement
/channelmutes                                 # List channel mutes
```

## 9. Implementation Phases

### Phase 1: Local Channel

**Duration**: 1-2 weeks
**Deliverables**:

- Local channel implementation
- Sub-zone detection and subscription
- Basic UI channel selector
- Database schema for preferences
- Unit tests for local channel

**Success Criteria**:

- Players can send/receive local messages
- Messages are limited to sub-zone
- Channel switching works via UI and commands
- Preferences persist across sessions

### Phase 2: Global Channel

**Duration**: 1-2 weeks
**Deliverables**:

- Global channel implementation
- Level-based access control
- Enhanced rate limiting
- Admin system announcements
- Integration tests

**Success Criteria**:

- Players can send/receive global messages
- Level restrictions work correctly
- System announcements function
- Admin moderation tools work

### Phase 3: Whisper Channel

**Duration**: 1-2 weeks
**Deliverables**:

- Whisper channel implementation
- Reply functionality
- Player-to-player messaging
- Enhanced error handling
- UI/UX tests

**Success Criteria**:

- Players can whisper to each other
- Reply command works correctly
- Error messages are user-friendly
- No distance limitations apply

## 10. Testing Strategy

### 10.1 Unit Tests

```python
class TestLocalChannel:
    def test_local_message_sub_zone_scope(self):
        """Test that local messages only reach players in same sub-zone."""

    def test_local_channel_subscription_update(self):
        """Test that local subscription updates when player moves sub-zones."""

class TestGlobalChannel:
    def test_global_message_level_restriction(self):
        """Test that global messages respect level requirements."""

    def test_global_channel_rate_limiting(self):
        """Test rate limiting for global channel."""

class TestWhisperChannel:
    def test_whisper_player_to_player(self):
        """Test player-to-player whisper functionality."""

    def test_whisper_reply_functionality(self):
        """Test reply to last whisper functionality."""

    def test_whisper_offline_player(self):
        """Test whispering to offline player returns appropriate message."""
```

### 10.2 Integration Tests

```python
class TestChannelIntegration:
    def test_cross_channel_functionality(self):
        """Test that different channels work together properly."""

    def test_channel_preferences_persistence(self):
        """Test that channel preferences persist across sessions."""

    def test_admin_moderation_integration(self):
        """Test admin moderation features across channels."""
```

### 10.3 UI/UX Tests

```python
class TestChannelUI:
    def test_channel_selector_functionality(self):
        """Test channel selector dropdown works correctly."""

    def test_message_formatting_display(self):
        """Test that messages display with correct formatting."""

    def test_mute_toggle_functionality(self):
        """Test mute/unmute toggles work correctly."""
```

## 11. Performance Considerations

### 11.1 Message Volume

Local channel: Moderate volume (sub-zone limited)

- Global channel: High volume (server-wide)
- Whisper channel: Low volume (player-to-player)
- System channel: Very low volume (admin only)

### 11.2 NATS Optimization

Use appropriate NATS subjects for message routing

- Implement message filtering on client side
- Consider message compression for high-volume channels

### 11.3 Log File Management

Implement log rotation for chat files

- Archive old chat logs with timestamps
- Maintain log file size limits
- Implement log cleanup for old history

## 12. Security Considerations

### 12.1 Input Validation

All message content validated for length and content

- Channel names validated against allowed list
- Player names validated for whisper commands

### 12.2 Access Control

Level-based access for global channel

- Admin-only access for system channel
- Player mute checks for all channels

### 12.3 Rate Limiting

Per-channel rate limiting to prevent spam

- Exponential backoff for repeated violations
- Admin override capabilities

## 13. Documentation Requirements

### 13.1 API Documentation

New endpoint specifications

- Message format documentation
- Error code documentation
- Rate limiting documentation

### 13.2 User Guide

Channel usage instructions

- Command reference
- UI navigation guide
- Troubleshooting section

### 13.3 Admin Guide

Moderation tool usage

- System announcement procedures
- Channel management procedures
- Security best practices

### 13.4 Technical Implementation Notes

Architecture decisions

- Integration patterns
- Performance considerations
- Future enhancement possibilities

## 14. Future Enhancements

### 14.1 Party Channel

Group-based communication

- Party formation and management
- Shared party features

### 14.2 Combat Channel

Combat-specific messaging

- Automatic combat notifications
- Tactical communication

### 14.3 Advanced Moderation

Automated content filtering

- AI-powered moderation
- Advanced reporting system

### 14.4 Channel Customization

Custom channel creation

- Channel-specific permissions
- Advanced channel management

## 15. Conclusion

This specification provides a comprehensive framework for implementing Advanced Chat Channels in MythosMUD. The phased approach ensures manageable development while delivering value incrementally. The system extends the existing NATS infrastructure while providing enhanced user experience and moderation capabilities.

The implementation will provide players with multiple communication options while maintaining the existing "say" command functionality. Admin tools will enable effective moderation, and the system will be designed for future enhancements.

---

**Document Control**

**Version**: 1.0

**Last Updated**: 2025-01-27

**Next Review**: After Phase 1 completion
- **Approval**: Pending Professor Wolfshade review
