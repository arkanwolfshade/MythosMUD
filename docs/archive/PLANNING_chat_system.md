# Chat System Implementation Plan

_Academic Research into Forbidden Communications - Prof. Armitage's Notes_

## Current Status (Updated: August 14, 2025)

### ✅ **Phase 1: Core Infrastructure - COMPLETED**

**NATS Integration**: Successfully migrated from Redis to NATS for real-time messaging

**Server-Side Architecture**: NATS service, message handler, and WebSocket integration working

**Cross-Player Chat**: Demonstrated working chat between ArkanWolfshade and Ithaqua

- **Real-Time Communication**: Messages delivered instantly via NATS → WebSocket pipeline

### 🔄 **Phase 2: Chat Channels - IN PROGRESS**

**Say Channel**: ✅ **COMPLETED** - Working cross-player communication in same room

**Local Channel**: ⏳ **PENDING** - Area-wide communication (room + adjacent)

**Global Channel**: ⏳ **PENDING** - System-wide communication

- **Party Channel**: ⏳ **PENDING** - Group communication
- **Whisper Channel**: ⏳ **PENDING** - Private messaging

### ⏳ **Phase 3: Advanced Features - PENDING**

**Server-Side Filtering**: ⏳ **PENDING** - Room/zone-based message filtering

**Rate Limiting**: ⏳ **PENDING** - Per-user, per-channel rate limiting

**Content Filtering**: ⏳ **PENDING** - Profanity and keyword detection

- **Muting System**: ⏳ **PENDING** - Player and channel muting
- **Message Persistence**: ⏳ **PENDING** - Chat history and audit trail

### 🎯 **Next Priority**: Server-Side Message Filtering

Implement room-based filtering to reduce network traffic and improve performance.

## Overview

This document outlines the implementation of a comprehensive chat system for MythosMUD, addressing both the core chat channels (Issue #18) and the full chat system with moderation features (Issue #58). The system will enable players to communicate across multiple channels while maintaining the eldritch atmosphere of our Miskatonic University setting.

## Implementation Strategy: Tracer Bullet Approach

### Tracer Bullet Philosophy

The implementation follows a **tracer bullet** approach, using the `say` channel as the initial target to validate the entire system architecture quickly. This allows us to:

**Validate architecture**: Test all subsystems with minimal implementation

**Rapid feedback**: Get working chat functionality in 1-2 weeks

**Iterative development**: Build on validated foundation

- **Risk mitigation**: Identify issues early in the development cycle

### MVP Definition

**Minimum Viable Product**: A working `say` channel that allows players in the same room to communicate in real-time.

**Success Criteria**:

- Players can use `/say <message>` command
- Messages appear instantly for all players in the same room
- Basic chat interface displays messages
- System architecture supports future expansion

## Requirements Analysis

### Core Chat Channels (Issue #18)

**Global Channel**: System-wide communication accessible to all players

**Local Channel**: Area-wide communication (current room + adjacent areas)

**Party Channel**: Group communication for players in the same party

- **Say Channel**: Direct speech within the current room only
- **Whisper Channel**: Private communication between specific players

### Advanced Features (Issue #58)

**Communication Controls**: Mute, filters, and channel preferences

**Moderation System**: Profanity filtering, harm-related keyword detection

**Admin Tools**: Moderator commands and administrative oversight

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

**Automatic Subscription**: Players are automatically subscribed based on context

**Say/Local**: Automatically active when in rooms

**Global**: Always available (but can be muted)

- **Party**: Automatically joined when in a party
- **Whisper**: Always available for private communication
- **No Manual Join/Leave**: Use mute/unmute instead for better UX

### Player Muting Rules

**Player Muting**: Users can mute specific players across all channels

**Admin Protection**: Admins and moderators cannot be muted by regular users

**Self-Muting**: Players cannot mute themselves

- **Cross-Channel**: Muted players are hidden from all channels (global, local, party, say)
- **Whisper Exception**: Muted players can still send whispers (for emergency communication)
- **Admin Override**: Admins can mute/unmute any player, including other admins

### Rate Limiting Strategy

**Per-User Limits**: Rate limiting is applied per user, not globally

**Sliding Window**: Uses sliding window algorithm for accurate rate tracking

**Channel-Specific**: Different limits for different channels based on usage patterns

- **Admin Bypass**: Admins and moderators are exempt from rate limiting

#### Rate Limits (Per User Per Minute)

```
Global Channel: 10 messages per minute per user
Local Channel: 20 messages per minute per user
Party Channel: 30 messages per minute per user
Say Channel: 15 messages per minute per user
Whisper Channel: 5 messages per minute per user
```

#### Rate Limiting Implementation

**Storage**: In-memory cache with Redis for distributed deployments

**Algorithm**: Sliding window with 1-minute buckets

**Response**: Graceful degradation with user feedback

- **Monitoring**: Rate limit violations logged for moderation review

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

**Channel Muting**: Messages from muted channels are completely hidden

**Player Muting**: Messages from muted players are hidden in all channels except whispers

**Admin Messages**: Cannot be muted by regular users (system protection)

- **Whisper Exception**: Muted players can still send whispers for emergency communication
- **Cross-Session**: Mute settings persist across game sessions

## Technical Architecture

### Redis Pub/Sub System

#### Redis Channels Structure

```
chat:global          - Global channel messages
chat:local:{room_id} - Local channel messages per room
chat:party:{party_id} - Party channel messages
chat:say:{room_id}   - Say channel messages per room
chat:whisper:{player_id} - Whisper messages per player
chat:system          - System announcements
```

#### Redis Data Structures

```redis
# Session message history (TTL: 24 hours)

HSET chat:session:{player_id}:{channel} {message_id} {message_json}

# Rate limiting (TTL: 1 minute)

INCR chat:rate:{player_id}:{channel}
EXPIRE chat:rate:{player_id}:{channel} 60

# Mute settings (persistent)

HSET chat:mutes:{player_id} {target_type}:{target_id} {mute_data_json}

# Online players per channel

SADD chat:online:{channel} {player_id}
SREM chat:online:{channel} {player_id}
```

#### Performance Benefits

**Message Delivery**: < 1ms latency

**Concurrent Users**: 100+ supported (optimized for 10-100 range)

**Message Volume**: 1000+ messages per minute capacity

- **Memory Usage**: Efficient session storage
- **Scalability**: Horizontal scaling with Redis Cluster
- **Reliability**: Message persistence and delivery guarantees

### Backend Components

#### 1. Chat Service (`server/game/chat_service.py`)

```python
class ChatService:
    """Manages chat message routing, filtering, and delivery using Redis"""

    def __init__(self, redis_client):
        self.redis = redis_client
        self.channels = {}  # Channel registry
        self.filters = []   # Message filters
        self.moderators = set()  # Admin/moderator list

    async def send_message(self, player_id: str, channel: str, message: str) -> bool
    async def publish_message(self, channel: str, message_data: dict) -> bool
    async def subscribe_to_channel(self, player_id: str, channel: str) -> bool
    async def unsubscribe_from_channel(self, player_id: str, channel: str) -> bool
    async def get_session_history(self, player_id: str, channel: str, limit: int = 50) -> list
    async def mute_channel(self, player_id: str, channel: str, duration: int = None) -> bool
    async def unmute_channel(self, player_id: str, channel: str) -> bool
    async def mute_player(self, muter_id: str, target_id: str, duration: int = None) -> bool
    async def unmute_player(self, unmuter_id: str, target_id: str) -> bool
    async def is_player_muted(self, player_id: str, by_player_id: str) -> bool
    async def is_channel_muted(self, player_id: str, channel: str) -> bool
    async def check_rate_limit(self, player_id: str, channel: str) -> bool
    async def record_message_sent(self, player_id: str, channel: str) -> None
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

class RateLimitInfo(BaseModel):
    """Rate limiting information for a user-channel combination"""
    player_id: str
    channel: str
    message_count: int
    window_start: datetime
    last_message_time: datetime
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

**Desktop-optimized**: Designed for desktop web browsers

**Channel tabs**: Switching between chat types

**Message input**: Full keyboard support with send button

- **Message history**: Scrollable message display
- **User list**: Current channel participants
- **Mute/unmute controls**: Channel and player management
- **Keyboard shortcuts**: Hotkeys for common actions

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

**Location**: `logs/chat/` directory

**Format**: JSON-structured logs for AI integration

**Rotation**: Daily log files with timestamp naming

- **Retention**: 30 days by default, configurable

### Redis Pub/Sub Architecture

**Message Broker**: Redis for real-time message distribution

**Session History**: In-memory session storage with Redis

**Performance**: Sub-millisecond message delivery

- **Scalability**: Support for 1000+ concurrent users
- **Reliability**: Message persistence and delivery guarantees

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

````

## Prerequisites: System Infrastructure Requirements

### Critical Infrastructure Fixes (Required Before Chat Implementation)

#### 1. Multiplayer Configuration Fix

**Issue**: `allow_multiplay: false` in production config blocks multiplayer functionality
**Fix Required**:
```yaml
# server/server_config.yaml

allow_multiplay: true  # Enable multiplayer for chat functionality
````

**Impact**: Without this fix, only one player can connect at a time, making chat impossible.

#### 2. Room Adjacency Logic Implementation

**Issue**: `get_adjacent_rooms()` returns empty list, needed for local channel
**Fix Required**: Complete implementation in `server/game/room_service.py`

```python
def get_adjacent_rooms(self, room_id: str) -> list[dict[str, Any]]:
    """Get rooms adjacent to the specified room for local chat scope."""
    # Implementation needed for local channel functionality

```

**Impact**: Local channel cannot function without room adjacency logic.

#### 3. Player Name Resolution System

**Issue**: Inconsistent player lookup between ID and name
**Fix Required**: Robust player name resolution for whisper commands

```python
def resolve_player_name(self, identifier: str) -> Player | None:
    """Resolve player by ID or name with consistent behavior."""
    # Implementation needed for whisper functionality

```

**Impact**: Whisper commands cannot function without reliable player name resolution.

### Deferred Infrastructure (Part of Chat Implementation)

#### 4. Admin/Moderator System

**Timing**: Implemented as part of Chat System Phase 4 (Advanced Features)
**Scope**: Admin protection, moderator commands, chat moderation

#### 5. Real-time Event Types

**Timing**: Implemented as part of Chat System development
**Scope**: `chat_message`, `chat_mute`, `chat_unmute` event types

#### 6. Party System

**Timing**: Implemented when adding `/party` channel in Phase 3
**Scope**: Party management, party chat functionality. See
[docs/PLANNING_ephemeral_grouping.md](../PLANNING_ephemeral_grouping.md) for consolidated
ephemeral grouping plan.

## Implementation Phases

### Phase 0: Infrastructure Prerequisites (REQUIRED FIRST)

**Goal**: Fix critical system infrastructure before any chat development.

#### 0.1 Multiplayer Configuration

Enable `allow_multiplay: true` in server config

- Test multiple player connections
- Verify room occupant tracking works

#### 0.2 Room Adjacency Implementation

Complete `get_adjacent_rooms()` method

- Add room adjacency validation
- Test adjacency logic with room data

#### 0.3 Player Name Resolution

Implement robust player lookup system

- Add player name validation
- Test whisper command resolution

### Phase 1: Tracer Bullet - Say Channel MVP

**Goal**: Implement minimal `say` channel functionality as quickly as possible to validate the entire system architecture.

#### 1.1 Minimal Chat Service

Basic message routing (no Redis initially)

- Room-based message delivery
- Simple in-memory message storage
- Basic WebSocket integration

#### 1.2 Minimal Database Schema

Basic mute settings table (simplified)

- No moderation logs initially
- Minimal migration scripts

#### 1.3 Minimal API Endpoints

`/say` command endpoint

- Basic message delivery
- No channel management initially

#### 1.4 Minimal Frontend

Basic chat interface for say messages

- Simple message display
- Basic input handling
- No channel tabs initially

### Phase 2: Core Infrastructure Completion

1. **Redis Integration**
   - Redis pub/sub setup and configuration
   - Message broker implementation
   - Session history storage
   - Rate limiting with Redis

2. **Chat Service Enhancement**
   - Full message routing with Redis
   - Complete channel management
   - Enhanced WebSocket integration
   - Log file management

3. **Database Schema Completion**
   - Complete mute settings table
   - Add moderation logs table
   - Full migration scripts

4. **API Endpoints Completion**
   - All channel endpoints
   - Mute/unmute functionality
   - Channel status queries

### Phase 3: Additional Channels

1. **Global Channel**
   - System-wide messaging
   - Player list integration

2. **Local Channel**
   - Area-wide messaging (room + adjacent areas)
   - Location awareness and room adjacency logic (requires Phase 0.2)

3. **Whisper Channel**
   - Private messaging
   - Player targeting (requires Phase 0.3)

4. **Party Channel**
   - Group messaging
   - Party management integration (requires new Party System)

### Phase 4: Advanced Features

1. **Admin/Moderator System** (Deferred from Phase 0)
   - Admin protection from muting
   - Moderator commands and tools
   - Chat moderation capabilities
   - Player reporting system

2. **Moderation System**
   - Profanity filtering
   - Basic moderation tools
   - Player reporting system

3. **Enhanced UI**
   - Channel tabs
   - Advanced chat interface
   - Notification system

4. **Performance Optimization**
   - Redis integration completion
   - Rate limiting implementation
   - Session management

### Phase 5: Future Enhancements

1. **Advanced Moderation**
   - AI-powered content analysis
   - Progressive warning system
   - Enhanced moderator tools

2. **Game Integration**
   - Item and room linking
   - Spell casting integration
   - Lovecraftian atmosphere effects
   - NPC interaction system

3. **Social Features**
   - Friends list system
   - Event announcements
   - Achievement sharing

4. **Advanced UI Features**
   - Message formatting
   - Emote system
   - Advanced notifications

### Phase 6: Polish and Optimization

1. **Performance Tuning**
   - Message delivery optimization
   - Database query optimization
   - Memory usage optimization

2. **User Experience Polish**
   - Accessibility improvements
   - Mobile responsiveness
   - Advanced keyboard shortcuts

3. **Monitoring and Analytics**
   - Performance monitoring
   - Usage analytics
   - Error tracking and reporting

## Infrastructure Dependencies

### Critical Dependencies (Must Complete First)

**Phase 0.1**: Multiplayer configuration must be enabled before any chat development

**Phase 0.2**: Room adjacency logic required for local channel functionality

- **Phase 0.3**: Player name resolution required for whisper commands

### Feature Dependencies

**Say Channel**: Requires Phase 0.1 (multiplayer enabled)

**Local Channel**: Requires Phase 0.1 + Phase 0.2 (multiplayer + adjacency)

- **Whisper Channel**: Requires Phase 0.1 + Phase 0.3 (multiplayer + name resolution)
- **Party Channel**: Requires new Party System (implemented in Phase 3)
- **Admin Features**: Requires Admin/Moderator System (implemented in Phase 4)

### Risk Mitigation

**Phase 0**: Complete all infrastructure fixes before starting chat development

**Testing**: Each phase must be fully tested before proceeding to next phase

- **Rollback Plan**: Infrastructure changes can be reverted if issues arise

## Testing Strategy

### Unit Tests

Chat service functionality

- Message filtering logic
- Channel management
- Player muting logic
- Admin protection rules
- API endpoint validation

### Integration Tests

WebSocket message delivery

- Database persistence
- Real-time communication
- Multi-player scenarios

### End-to-End Tests

Complete chat workflows

- Moderation features
- UI interactions
- Performance under load

## Security Considerations

### Message Security

Input validation and sanitization

- XSS prevention
- SQL injection protection
- Rate limiting

### Access Control

Channel permissions

- Player muting permissions
- Admin protection from muting
- Moderator privileges
- Admin authentication
- Audit trail maintenance

### Privacy Protection

Message encryption (future enhancement)

- Data retention policies
- User consent management
- GDPR compliance considerations

## Performance Requirements

### Scalability Targets

**Concurrent Users**: 10-100 players

**Message Volume**: 100-1000 messages per minute (10 messages per player per minute average)

- **Message Delivery**: Sub-100ms latency
- **Uptime**: 99.9% availability
- **Peak Load**: Handle burst traffic up to 2000 messages per minute

### Optimization Strategies

Message queuing and batching

- Database indexing
- Caching strategies
- Connection pooling
- Per-user rate limiting with sliding windows

## Integration Points

### Existing Systems

**Player Service**: User authentication and management

**Room Service**: Location-based messaging

- **Party System**: Group communication
- **WebSocket Handler**: Real-time delivery
- **Event Bus**: System-wide notifications
- **Redis**: Message broker and session storage

### Future Enhancements

**Voice Chat**: Audio communication

**File Sharing**: Image and document exchange

- **Emoji Support**: Enhanced expression
- **Chat Bots**: Automated responses
- **Translation**: Multi-language support

## Success Metrics

### Functional Requirements

All chat channels operational

- Real-time message delivery
- Effective moderation tools
- Intuitive user interface

### Performance Metrics

**Message delivery latency**: < 100ms

**System uptime**: > 99.9%

- **Concurrent users**: 10-100 players
- **Message volume**: 100-1000 messages per minute
- **Successful message filtering**: > 95%
- **Peak load handling**: Up to 2000 messages per minute

### User Experience

User satisfaction scores

- Feature adoption rates
- Support ticket reduction
- Community engagement metrics

## Risk Mitigation

### Technical Risks

**WebSocket Scalability**: Implement connection pooling and load balancing

**Database Performance**: Optimize queries and implement caching

- **Message Loss**: Implement reliable delivery mechanisms
- **Security Vulnerabilities**: Regular security audits and penetration testing

### Operational Risks

**Moderation Burden**: Automated filtering and community tools

**User Abuse**: Rate limiting and administrative oversight

- **System Overload**: Monitoring and auto-scaling capabilities
- **Data Loss**: Regular backups and disaster recovery procedures

## Timeline Estimate

### Development Timeline

**Phase 0 (Infrastructure Prerequisites)**: 1 week (Critical fixes)

**Phase 1 (Tracer Bullet)**: 1-2 weeks (Say channel MVP)

- **Phase 2 (Core Infrastructure)**: 2-3 weeks (Redis, full chat service)
- **Phase 3 (Additional Channels)**: 2-3 weeks (Global, local, whisper, party)
- **Phase 4 (Advanced Features)**: 2-3 weeks (Admin/moderator, moderation, enhanced UI)
- **Phase 5 (Future Enhancements)**: 4-6 weeks (Game integration, social features)
- **Phase 6 (Polish)**: 1-2 weeks (Optimization, monitoring)

**Total Estimated Duration**: 13-20 weeks

### Phase 0 Success Criteria

Multiple players can connect simultaneously

- Room adjacency logic works correctly
- Player name resolution is reliable
- System ready for chat implementation

### MVP Success Criteria

Players can use `/say` command successfully

- Messages appear in real-time for players in same room
- Basic chat interface is functional
- System architecture is validated and extensible

## Conclusion

This chat system implementation will provide MythosMUD with a comprehensive communication platform that enhances player interaction while maintaining the atmospheric integrity of our eldritch setting. The phased approach ensures steady progress while allowing for iterative refinement based on user feedback and testing results.

_"The most merciful thing in the world, I think, is the inability of the human brain to correlate all its contents." - H.P. Lovecraft_

---

_Document prepared by Prof. Armitage, Miskatonic University Department of Occult Studies_
_Last updated: [Current Date]_
