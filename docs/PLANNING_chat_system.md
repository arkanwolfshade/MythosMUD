# Chat System Implementation Plan

*Academic Research into Forbidden Communications - Prof. Armitage's Notes*

## Overview

This document outlines the implementation of a comprehensive chat system for MythosMUD, addressing both the core chat channels (Issue #18) and the full chat system with moderation features (Issue #58). The system will enable players to communicate across multiple channels while maintaining the eldritch atmosphere of our Miskatonic University setting.

## Requirements Analysis

### Core Chat Channels (Issue #18)

- **Global Channel**: System-wide communication accessible to all players
- **Local Channel**: Area-wide communication (current room + adjacent areas)
- **Party Channel**: Group communication for players in the same party
- **Say Channel**: Direct speech within the current room only
- **Whisper Channel**: Private communication between specific players

### Advanced Features (Issue #58)

- **Communication Controls**: Mute, filters, and channel preferences
- **Moderation System**: Profanity filtering, harm-related keyword detection
- **Admin Tools**: Moderator commands and administrative oversight
- **Chat Logging**: Audit trail and message history
- **Real-time Delivery**: WebSocket-based instant messaging
- **User Interface**: Intuitive chat interface components

## User Experience & Commands

### Chat Commands

```
/global <message>      - System-wide communication
/local <message>       - Area-wide communication (current room + adjacent)
/say <message>         - Room-only speech
/party <message>       - Group communication
/whisper <player> <msg> - Private messaging
/tell <player> <msg>   - Alternative private messaging
```

### Channel Management Commands

```
/mute <channel>        - Mute specific channel (global, local, party)
/unmute <channel>      - Unmute specific channel
/mute <player>         - Mute specific player across all channels
/unmute <player>       - Unmute specific player
/mute all              - Mute all channels except whispers
/unmute all            - Unmute all channels
/channels              - Show current channel status
/channels muted        - Show muted channels
/channels active       - Show active channels
/muted players         - Show list of muted players
```

### Channel Subscription Model

- **Automatic Subscription**: Players are automatically subscribed based on context
- **Say/Local**: Automatically active when in rooms
- **Global**: Always available (but can be muted)
- **Party**: Automatically joined when in a party
- **Whisper**: Always available for private communication
- **No Manual Join/Leave**: Use mute/unmute instead for better UX

### Player Muting Rules

- **Player Muting**: Users can mute specific players across all channels
- **Admin Protection**: Admins and moderators cannot be muted by regular users
- **Self-Muting**: Players cannot mute themselves
- **Cross-Channel**: Muted players are hidden from all channels (global, local, party, say)
- **Whisper Exception**: Muted players can still send whispers (for emergency communication)
- **Admin Override**: Admins can mute/unmute any player, including other admins

### Message Display Format

```
[Global] Prof. Armitage: Welcome to Miskatonic University
[Local] Dr. Wilmarth: Is anyone in the library complex?
Prof. Armitage says, "The restricted section is this way."
[Party] Prof. Armitage: Let's investigate the basement together
Prof. Armitage whispers to you, "I found something disturbing..."
```

### Muting Examples

```
/mute global              - Mute global channel
/mute Ithaqua             - Mute player "Ithaqua" across all channels
/unmute local             - Unmute local channel
/unmute Yog-Sothoth       - Unmute player "Yog-Sothoth"
/muted players            - Show: "Muted players: Ithaqua, Cthulhu"
/channels muted           - Show: "Muted channels: global"
```

### Muting Behavior

- **Channel Muting**: Messages from muted channels are completely hidden
- **Player Muting**: Messages from muted players are hidden in all channels except whispers
- **Admin Messages**: Cannot be muted by regular users (system protection)
- **Whisper Exception**: Muted players can still send whispers for emergency communication
- **Cross-Session**: Mute settings persist across game sessions

## Technical Architecture

### Backend Components

#### 1. Chat Service (`server/game/chat_service.py`)

```python
class ChatService:
    """Manages chat message routing, filtering, and delivery"""

    def __init__(self):
        self.channels = {}  # Channel registry
        self.filters = []   # Message filters
        self.moderators = set()  # Admin/moderator list

    async def send_message(self, player_id: str, channel: str, message: str) -> bool
    async def mute_channel(self, player_id: str, channel: str, duration: int = None) -> bool
    async def unmute_channel(self, player_id: str, channel: str) -> bool
    async def mute_player(self, muter_id: str, target_id: str, duration: int = None) -> bool
    async def unmute_player(self, unmuter_id: str, target_id: str) -> bool
    async def is_player_muted(self, player_id: str, by_player_id: str) -> bool
    async def is_channel_muted(self, player_id: str, channel: str) -> bool
    async def filter_message(self, message: str) -> tuple[bool, str]
```

#### 2. Chat Models (`server/models/chat.py`)

```python
class ChatMessage(BaseModel):
    """Represents a chat message in the system"""
    id: str
    sender_id: str
    channel: str
    content: str
    timestamp: datetime
    filtered: bool = False
    moderation_notes: Optional[str] = None

class ChatChannel(BaseModel):
    """Represents a chat channel"""
    name: str
    type: str  # global, local, party, say, whisper
    participants: set[str]
    moderators: set[str]
    settings: dict
```

#### 3. Chat API Endpoints (`server/api/chat.py`)

```python
@router.post("/chat/send")
async def send_message(request: SendMessageRequest)

@router.post("/chat/join")
async def join_channel(request: JoinChannelRequest)

@router.post("/chat/leave")
async def leave_channel(request: LeaveChannelRequest)

@router.get("/chat/history/{channel}")
async def get_chat_history(channel: str, limit: int = 50)

@router.post("/chat/mute/channel")
async def mute_channel(request: MuteChannelRequest)

@router.post("/chat/unmute/channel")
async def unmute_channel(request: UnmuteChannelRequest)

@router.post("/chat/mute/player")
async def mute_player(request: MutePlayerRequest)

@router.post("/chat/unmute/player")
async def unmute_player(request: UnmutePlayerRequest)

@router.get("/chat/muted/channels")
async def get_muted_channels(player_id: str)

@router.get("/chat/muted/players")
async def get_muted_players(player_id: str)
```

### Frontend Components

#### 1. Chat Interface (`client/src/components/ChatInterface.tsx`)

- Channel tabs for switching between chat types
- Message input with send button
- Message history display with scrolling
- User list for current channel
- Mute/unmute controls

#### 2. Chat Hook (`client/src/hooks/useChat.ts`)

```typescript
interface UseChatReturn {
  messages: ChatMessage[];
  sendMessage: (channel: string, content: string) => Promise<void>;
  joinChannel: (channel: string) => Promise<void>;
  leaveChannel: (channel: string) => Promise<void>;
  isConnected: boolean;
}
```

## Chat Logging & Storage

### Chat Log Files

- **Location**: `logs/chat/` directory
- **Format**: JSON-structured logs for AI integration
- **Rotation**: Daily log files with timestamp naming
- **Retention**: 30 days by default, configurable

### Log File Structure

```json
{
  "timestamp": "2025-01-27T10:30:00Z",
  "channel": "global",
  "sender_id": "player_123",
  "sender_name": "Prof. Armitage",
  "content": "Welcome to Miskatonic University",
  "room_id": "arkham_campus_001",
  "filtered": false,
  "moderation_notes": null
}
```

### Database Schema (Minimal - Only for Mute Settings)

```sql
-- Chat mute settings (persistent across sessions)
CREATE TABLE chat_mute_settings (
    player_id TEXT NOT NULL,
    target_type TEXT NOT NULL, -- 'channel' or 'player'
    target_id TEXT NOT NULL,   -- channel name or player id
    muted_until DATETIME,
    muted_by TEXT, -- moderator who applied mute
    reason TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (player_id, target_type, target_id),
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (muted_by) REFERENCES players(id)
);
```

-- Chat moderation logs (for admin oversight)
CREATE TABLE chat_moderation_logs (
    id TEXT PRIMARY KEY,
    moderator_id TEXT NOT NULL,
    target_id TEXT NOT NULL,
    action TEXT NOT NULL, -- mute, unmute, ban, etc.
    reason TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (moderator_id) REFERENCES players(id),
    FOREIGN KEY (target_id) REFERENCES players(id)
);

```

## Implementation Phases

### Phase 1: Core Chat Infrastructure

1. **Chat Service Implementation**
   - Basic message routing
   - Channel management
   - WebSocket integration
   - Log file management

2. **Database Schema**
   - Create mute settings table
   - Create moderation logs table
   - Migration scripts

3. **Basic API Endpoints**
   - Send/receive messages
   - Mute/unmute channels
   - Channel status queries

### Phase 2: Channel Implementation

1. **Global Channel**
   - System-wide messaging
   - Player list integration

2. **Local Channel**
   - Area-wide messaging (room + adjacent areas)
   - Location awareness and room adjacency logic

3. **Party Channel**
   - Group messaging
   - Party management integration

4. **Say Channel**
   - Room-only speech
   - NPC interaction support

5. **Whisper Channel**
   - Private messaging
   - Player targeting

### Phase 3: Moderation & Controls

1. **Message Filtering**
   - Profanity detection
   - Harm-related keyword filtering
   - Custom filter lists

2. **Communication Controls**
   - Channel mute/unmute functionality
   - Player mute/unmute functionality
   - Admin protection and override rules
   - Message rate limiting

3. **Admin Tools**
   - Moderator commands
   - Administrative oversight
   - Audit logging

### Phase 4: User Interface

1. **Chat Interface Components**
   - Channel tabs
   - Message display
   - Input controls

2. **Real-time Updates**
   - WebSocket integration
   - Message delivery
   - Status indicators

3. **User Experience**
   - Responsive design
   - Accessibility features
   - Performance optimization

## Testing Strategy

### Unit Tests

- Chat service functionality
- Message filtering logic
- Channel management
- Player muting logic
- Admin protection rules
- API endpoint validation

### Integration Tests

- WebSocket message delivery
- Database persistence
- Real-time communication
- Multi-player scenarios

### End-to-End Tests

- Complete chat workflows
- Moderation features
- UI interactions
- Performance under load

## Security Considerations

### Message Security

- Input validation and sanitization
- XSS prevention
- SQL injection protection
- Rate limiting

### Access Control

- Channel permissions
- Player muting permissions
- Admin protection from muting
- Moderator privileges
- Admin authentication
- Audit trail maintenance

### Privacy Protection

- Message encryption (future enhancement)
- Data retention policies
- User consent management
- GDPR compliance considerations

## Performance Requirements

### Scalability Targets

- Support 100+ concurrent users
- Handle 1000+ messages per minute
- Sub-100ms message delivery
- 99.9% uptime

### Optimization Strategies

- Message queuing and batching
- Database indexing
- Caching strategies
- Connection pooling

## Integration Points

### Existing Systems

- **Player Service**: User authentication and management
- **Room Service**: Location-based messaging
- **Party System**: Group communication
- **WebSocket Handler**: Real-time delivery
- **Event Bus**: System-wide notifications

### Future Enhancements

- **Voice Chat**: Audio communication
- **File Sharing**: Image and document exchange
- **Emoji Support**: Enhanced expression
- **Chat Bots**: Automated responses
- **Translation**: Multi-language support

## Success Metrics

### Functional Requirements

- All chat channels operational
- Real-time message delivery
- Effective moderation tools
- Intuitive user interface

### Performance Metrics

- Message delivery latency < 100ms
- System uptime > 99.9%
- Support for 100+ concurrent users
- Successful message filtering > 95%

### User Experience

- User satisfaction scores
- Feature adoption rates
- Support ticket reduction
- Community engagement metrics

## Risk Mitigation

### Technical Risks

- **WebSocket Scalability**: Implement connection pooling and load balancing
- **Database Performance**: Optimize queries and implement caching
- **Message Loss**: Implement reliable delivery mechanisms
- **Security Vulnerabilities**: Regular security audits and penetration testing

### Operational Risks

- **Moderation Burden**: Automated filtering and community tools
- **User Abuse**: Rate limiting and administrative oversight
- **System Overload**: Monitoring and auto-scaling capabilities
- **Data Loss**: Regular backups and disaster recovery procedures

## Timeline Estimate

### Development Timeline

- **Phase 1**: 2-3 weeks (Core infrastructure)
- **Phase 2**: 3-4 weeks (Channel implementation)
- **Phase 3**: 2-3 weeks (Moderation features)
- **Phase 4**: 2-3 weeks (User interface)
- **Testing & Polish**: 1-2 weeks

**Total Estimated Duration**: 10-15 weeks

## Conclusion

This chat system implementation will provide MythosMUD with a comprehensive communication platform that enhances player interaction while maintaining the atmospheric integrity of our eldritch setting. The phased approach ensures steady progress while allowing for iterative refinement based on user feedback and testing results.

*"The most merciful thing in the world, I think, is the inability of the human brain to correlate all its contents." - H.P. Lovecraft*

---

*Document prepared by Prof. Armitage, Miskatonic University Department of Occult Studies*
*Last updated: [Current Date]*
