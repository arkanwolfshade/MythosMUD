# Redis to NATS Migration & Chat System Infrastructure Plan

*Academic Research into Forbidden Communications - Prof. Armitage's Notes*

## Overview

This document outlines the migration from Redis to NATS for the MythosMUD chat system, along with the implementation of all supporting infrastructure required for features that NATS doesn't support natively. This migration addresses the WSL networking issues we've encountered while providing a robust foundation for our comprehensive chat system.

## Migration Rationale

### Current Issues with Redis

- **WSL Networking Problems**: Redis running in WSL creates complex networking issues
- **Cross-platform Complexity**: Different connection methods for Windows vs Linux
- **Installation Overhead**: Redis requires separate server installation and configuration
- **Resource Usage**: Redis is more resource-intensive than needed for our use case

### Benefits of NATS

- **Native Windows Support**: No WSL networking complications
- **Lightweight**: Single binary, minimal resource usage
- **High Performance**: 10M+ messages/second capability
- **Simple Setup**: Easy installation and configuration
- **Perfect for Pub/Sub**: Designed specifically for messaging patterns we need

## Architecture Overview

### NATS Integration Layer

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Chat Service  │───▶│   NATS Server   │───▶│  WebSocket      │
│   (Business     │    │   (Messaging)   │    │  Clients        │
│    Logic)       │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   SQLite DB     │    │   Log Files     │    │   Rate Limiter  │
│   (Persistence) │    │   (Audit Trail) │    │   (In-Memory)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Subject Structure

```
chat.global                    # Global channel messages
chat.local.{room_id}          # Local channel messages per room
chat.say.{room_id}            # Say channel messages per room
chat.party.{party_id}         # Party channel messages
chat.whisper.{player_id}      # Whisper messages per player
chat.system                   # System announcements
chat.admin                    # Admin-only messages
```

## Implementation Phases

### Phase 1: NATS Infrastructure Setup

#### 1.1 NATS Server Installation

**Goal**: Install and configure NATS server on Windows

**Tasks**:

- [x] Download NATS server binary for Windows
- [x] Install NATS server in `E:\nats-server\`
- [x] Create NATS configuration file
- [x] Set up NATS as Windows service (optional)
- [x] Test NATS server connectivity

**Configuration**:

```yaml
# nats-server.conf
port: 4222
http_port: 8222
max_payload: 1048576  # 1MB max message size
debug: false
trace: false
logtime: true
```

#### 1.2 Python NATS Client Integration

**Goal**: Add NATS Python client to our dependencies

**Tasks**:

- [x] Add `nats-py` to `pyproject.toml`
- [x] Update `uv.lock` with new dependency
- [x] Create NATS service wrapper
- [x] Implement connection management
- [x] Add error handling and reconnection logic

**Code Structure**:

```python
# server/services/nats_service.py
class NATSService:
    def __init__(self, config):
        self.nc = None
        self.config = config

    async def connect(self):
        """Connect to NATS server"""

    async def publish(self, subject: str, data: dict):
        """Publish message to NATS subject"""

    async def subscribe(self, subject: str, callback):
        """Subscribe to NATS subject"""

    async def close(self):
        """Close NATS connection"""
```

#### 1.1.1 NATS Server Management Integration

**Goal**: Integrate NATS server management into existing server management scripts

**Tasks**:

- [x] Create NATS server management module (`scripts/nats_manager.ps1`)
- [x] Create NATS status checking script (`scripts/nats_status.ps1`)
- [x] Integrate NATS management into `start_server.ps1`
- [x] Integrate NATS management into `stop_server.ps1`
- [x] Update `start_dev.ps1` to inform users about automatic NATS startup
- [x] Test NATS server automatic start/stop functionality
- [x] Verify background operation and process management

#### 1.3 NATS Service Integration

**Goal**: Replace Redis service with NATS service

**Tasks**:

- [x] Create `server/services/nats_service.py`
- [x] Update `server/app/lifespan.py` to use NATS
- [x] Remove Redis service dependencies
- [x] Update configuration to use NATS settings
- [x] Test NATS connection in development environment

### Phase 2: Chat Service Migration

#### 2.1 Core Message Routing

**Goal**: Migrate chat message routing from Redis to NATS

**Tasks**:

- [x] Update `server/game/chat_service.py` to use NATS
- [x] Implement NATS message publishing
- [x] Implement NATS message subscription
- [x] Update message envelope structure
- [x] Test message routing functionality

**Code Changes**:

```python
# Before (Redis)
await redis_service.publish(f"chat:say:{room_id}", message_data)

# After (NATS)
await nats_service.publish(f"chat.say.{room_id}", message_data)
```

#### 2.2 Message Handler Migration

**Goal**: Update message handlers to use NATS

**Tasks**:

- [x] Update `server/realtime/redis_message_handler.py` → `nats_message_handler.py`
- [x] Implement NATS message processing
- [x] Update WebSocket broadcasting logic
- [x] Test real-time message delivery
- [x] Verify message ordering and delivery

#### 2.3 Error Handling and Fallbacks

**Goal**: Implement robust error handling for NATS

**Tasks**:

- [x] Add NATS connection monitoring
- [x] Implement automatic reconnection
- [x] Add fallback to direct WebSocket broadcasting
- [x] Create health check endpoints
- [x] Add logging for NATS operations

#### 2.4 Server-Side Message Filtering

**Goal**: Implement server-side filtering to reduce network traffic and client load

**Rationale**: Since we know what rooms players are in, we should do server-side filtering of outgoing messages on the "say" channel for the clients. We do not want to send all "say" messages to all clients and force them to filter to their room client-side. This would generate unnecessary network traffic and load on the client. This same behavior would be used for sub-zone/zone/plane communications as well.

**Tasks**:

- [x] Implement room-based message filtering in NATS message handler
- [ ] Add zone/subzone/plane-based filtering for broader communications
- [x] Update WebSocket broadcasting to only send relevant messages
- [ ] Add configuration for filtering granularity
- [x] Test filtering with multiple players in different rooms
- [ ] Verify network traffic reduction
- [ ] Add metrics for message filtering efficiency

**Implementation Strategy**:

```python
# In NATS message handler
async def _broadcast_by_channel_type(self, channel, chat_event, room_id, party_id, target_player_id, sender_id):
    if channel in ["say", "local"]:
        # Only broadcast to players in the same room
        await connection_manager.broadcast_to_room(room_id, chat_event, exclude_player=sender_id)
    elif channel == "zone":
        # Broadcast to players in the same zone
        await connection_manager.broadcast_to_zone(zone_id, chat_event, exclude_player=sender_id)
    elif channel == "subzone":
        # Broadcast to players in the same subzone
        await connection_manager.broadcast_to_subzone(subzone_id, chat_event, exclude_player=sender_id)
```

**Benefits**:
- **Reduced Network Traffic**: Only relevant messages sent to clients
- **Lower Client Load**: No client-side filtering required
- **Better Performance**: Faster message delivery to intended recipients
- **Scalability**: More efficient as player count increases

### Phase 3: Supporting Infrastructure Implementation

#### 3.1 Message Persistence System

**Goal**: Implement message history and persistence (NATS doesn't provide this)

**Tasks**:

- [x] Create `server/services/chat_logger.py` (AI-focused logging)
- [x] Design logfile-based persistence architecture
- [x] Implement structured JSON logging for AI processing
- [x] Add comprehensive moderation event logging
- [x] Implement daily log rotation with timestamp naming
- [x] Create log directories: logs/chat/, logs/moderation/, logs/system/
- [x] Integrate ChatLogger into ChatService and RealTimeEventHandler
- [x] Optimize for log shipping to external AI moderation systems

**Database Schema**:

```sql
-- Chat message history
CREATE TABLE chat_messages (
    id TEXT PRIMARY KEY,
    channel TEXT NOT NULL,
    sender_id TEXT NOT NULL,
    sender_name TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    room_id TEXT,
    party_id TEXT,
    filtered BOOLEAN DEFAULT FALSE,
    moderation_notes TEXT,
    FOREIGN KEY (sender_id) REFERENCES players(id)
);

-- Indexes for performance
CREATE INDEX idx_chat_messages_channel_timestamp ON chat_messages(channel, timestamp);
CREATE INDEX idx_chat_messages_sender ON chat_messages(sender_id);
CREATE INDEX idx_chat_messages_room ON chat_messages(room_id);
```

#### 3.2 Rate Limiting System

**Goal**: Implement per-user, per-channel rate limiting (NATS doesn't provide this)

**Tasks**:

- [ ] Create `server/services/rate_limiter.py`
- [ ] Implement sliding window rate limiting
- [ ] Add rate limit configuration
- [ ] Create rate limit middleware
- [ ] Add rate limit monitoring

**Rate Limiting Logic**:

```python
class RateLimiter:
    def __init__(self):
        self.limits = {
            'global': 10,    # messages per minute
            'local': 20,
            'say': 15,
            'party': 30,
            'whisper': 5
        }
        self.windows = {}  # In-memory storage

    async def check_rate_limit(self, player_id: str, channel: str) -> bool:
        """Check if player is within rate limits for channel"""

    async def record_message(self, player_id: str, channel: str):
        """Record a message for rate limiting"""
```

#### 3.3 User Management System

**Goal**: Implement user muting, channel muting, and permissions (NATS doesn't provide this)

**Tasks**:

- [ ] Create `server/models/chat_mutes.py`
- [ ] Implement mute/unmute functionality
- [ ] Add admin protection logic
- [ ] Create mute management endpoints
- [ ] Implement mute filtering in message processing

**Database Schema**:

```sql
-- Chat mute settings
CREATE TABLE chat_mutes (
    id TEXT PRIMARY KEY,
    player_id TEXT NOT NULL,
    target_type TEXT NOT NULL, -- 'channel' or 'player'
    target_id TEXT NOT NULL,   -- channel name or player id
    muted_until DATETIME,
    muted_by TEXT,
    reason TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (muted_by) REFERENCES players(id)
);

-- Indexes
CREATE INDEX idx_chat_mutes_player ON chat_mutes(player_id);
CREATE INDEX idx_chat_mutes_target ON chat_mutes(target_type, target_id);
```

#### 3.4 Content Filtering System

**Goal**: Implement message filtering and moderation (NATS doesn't provide this)

**Tasks**:

- [ ] Create `server/services/content_filter.py`
- [ ] Implement profanity filtering
- [ ] Add keyword detection
- [ ] Create moderation queue
- [ ] Add content filtering middleware

**Filtering Logic**:

```python
class ContentFilter:
    def __init__(self):
        self.profanity_list = self.load_profanity_list()
        self.keyword_patterns = self.load_keyword_patterns()

    async def filter_message(self, message: str) -> tuple[bool, str]:
        """Filter message content, return (is_clean, filtered_message)"""

    async def check_keywords(self, message: str) -> list[str]:
        """Check for concerning keywords"""
```

#### 3.5 Audit and Logging System

**Goal**: Implement comprehensive logging and audit trails (NATS doesn't provide this)

**Tasks**:

- [ ] Create `server/services/chat_logger.py`
- [ ] Implement structured logging
- [ ] Add audit trail functionality
- [ ] Create log rotation and cleanup
- [ ] Add log analysis tools

**Logging Structure**:

```python
class ChatLogger:
    async def log_message(self, message_data: dict):
        """Log chat message to file"""

    async def log_moderation_action(self, action_data: dict):
        """Log moderation actions"""

    async def log_rate_limit_violation(self, violation_data: dict):
        """Log rate limit violations"""
```

### Phase 4: API and Frontend Updates

#### 4.1 Chat API Endpoints

**Goal**: Update API endpoints to work with NATS and new infrastructure

**Tasks**:

- [ ] Update `server/api/chat.py` endpoints
- [ ] Add mute management endpoints
- [ ] Add rate limit status endpoints
- [ ] Add message history endpoints
- [ ] Update API documentation

**New Endpoints**:

```python
@router.post("/chat/send")
async def send_message(request: SendMessageRequest)

@router.get("/chat/history/{channel}")
async def get_chat_history(channel: str, limit: int = 50)

@router.post("/chat/mute/channel")
async def mute_channel(request: MuteChannelRequest)

@router.post("/chat/mute/player")
async def mute_player(request: MutePlayerRequest)

@router.get("/chat/rate-limit/status")
async def get_rate_limit_status(player_id: str)
```

#### 4.2 Frontend Integration

**Goal**: Update frontend to work with new NATS-based system

**Tasks**:

- [ ] Update `client/src/hooks/useChat.ts`
- [ ] Add mute/unmute UI components
- [ ] Add rate limit indicators
- [ ] Update message display logic
- [ ] Add channel management interface

### Phase 5: Testing and Validation

#### 5.1 Unit Testing

**Goal**: Comprehensive testing of all new components

**Tasks**:

- [ ] Test NATS service functionality
- [ ] Test rate limiting logic
- [ ] Test content filtering
- [ ] Test mute management
- [ ] Test message persistence

#### 5.2 Integration Testing

**Goal**: Test complete chat system workflows

**Tasks**:

- [ ] Test multi-player chat scenarios
- [ ] Test rate limit enforcement
- [ ] Test mute functionality
- [ ] Test message history
- [ ] Test error handling and fallbacks

#### 5.3 Performance Testing

**Goal**: Validate system performance under load

**Tasks**:

- [ ] Test message delivery latency
- [ ] Test concurrent user capacity
- [ ] Test rate limiting performance
- [ ] Test database performance
- [ ] Test memory usage

### Phase 6: Deployment and Monitoring

#### 6.1 Production Deployment

**Goal**: Deploy NATS-based chat system to production

**Tasks**:

- [ ] Install NATS server on production
- [ ] Configure production NATS settings
- [ ] Update production configuration
- [ ] Deploy updated application
- [ ] Monitor system health

#### 6.2 Monitoring and Alerting

**Goal**: Implement monitoring for the new chat system

**Tasks**:

- [ ] Add NATS connection monitoring
- [ ] Add rate limit violation alerts
- [ ] Add content filter alerts
- [ ] Add performance monitoring
- [ ] Create dashboard for chat metrics

## Technical Implementation Details

### NATS Service Implementation

```python
# server/services/nats_service.py
import asyncio
import json
import logging
from typing import Callable, Dict, Any
import nats

logger = logging.getLogger(__name__)

class NATSService:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.nc = None
        self.subscriptions = {}
        self.is_connected = False

    async def connect(self) -> bool:
        """Connect to NATS server"""
        try:
            self.nc = await nats.connect(
                self.config.get('nats_url', 'nats://localhost:4222'),
                reconnect_time_wait=1,
                max_reconnect_attempts=5
            )
            self.is_connected = True
            logger.info("Connected to NATS server")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to NATS: {e}")
            return False

    async def publish(self, subject: str, data: Dict[str, Any]) -> bool:
        """Publish message to NATS subject"""
        if not self.is_connected:
            logger.error("NATS not connected")
            return False

        try:
            message = json.dumps(data).encode()
            await self.nc.publish(subject, message)
            logger.debug(f"Published message to {subject}")
            return True
        except Exception as e:
            logger.error(f"Failed to publish message: {e}")
            return False

    async def subscribe(self, subject: str, callback: Callable) -> bool:
        """Subscribe to NATS subject"""
        if not self.is_connected:
            logger.error("NATS not connected")
            return False

        try:
            subscription = await self.nc.subscribe(subject, cb=callback)
            self.subscriptions[subject] = subscription
            logger.info(f"Subscribed to {subject}")
            return True
        except Exception as e:
            logger.error(f"Failed to subscribe to {subject}: {e}")
            return False

    async def close(self):
        """Close NATS connection"""
        if self.nc:
            await self.nc.close()
            self.is_connected = False
            logger.info("NATS connection closed")
```

### Rate Limiter Implementation

```python
# server/services/rate_limiter.py
import time
import asyncio
from typing import Dict, List, Tuple
from collections import defaultdict

class RateLimiter:
    def __init__(self):
        self.limits = {
            'global': 10,    # messages per minute
            'local': 20,
            'say': 15,
            'party': 30,
            'whisper': 5
        }
        self.windows = defaultdict(list)  # player_id:channel -> [timestamps]

    async def check_rate_limit(self, player_id: str, channel: str) -> Tuple[bool, int]:
        """Check if player is within rate limits for channel"""
        key = f"{player_id}:{channel}"
        now = time.time()
        window_start = now - 60  # 1 minute window

        # Clean old timestamps
        self.windows[key] = [ts for ts in self.windows[key] if ts > window_start]

        # Check limit
        current_count = len(self.windows[key])
        limit = self.limits.get(channel, 10)

        return current_count < limit, limit - current_count

    async def record_message(self, player_id: str, channel: str):
        """Record a message for rate limiting"""
        key = f"{player_id}:{channel}"
        self.windows[key].append(time.time())

    async def get_rate_limit_status(self, player_id: str) -> Dict[str, Dict[str, int]]:
        """Get rate limit status for all channels"""
        status = {}
        for channel in self.limits.keys():
            can_send, remaining = await self.check_rate_limit(player_id, channel)
            status[channel] = {
                'limit': self.limits[channel],
                'remaining': remaining,
                'can_send': can_send
            }
        return status
```

### Content Filter Implementation

```python
# server/services/content_filter.py
import re
from typing import List, Tuple

class ContentFilter:
    def __init__(self):
        self.profanity_patterns = [
            r'\b(bad_word_1)\b',
            r'\b(bad_word_2)\b',
            # Add more patterns
        ]
        self.keyword_patterns = [
            r'\b(harmful_keyword_1)\b',
            r'\b(harmful_keyword_2)\b',
            # Add more patterns
        ]

    async def filter_message(self, message: str) -> Tuple[bool, str, List[str]]:
        """Filter message content"""
        original_message = message
        filtered_message = message
        violations = []

        # Check profanity
        for pattern in self.profanity_patterns:
            if re.search(pattern, message, re.IGNORECASE):
                filtered_message = re.sub(pattern, '***', filtered_message, flags=re.IGNORECASE)
                violations.append('profanity')

        # Check harmful keywords
        for pattern in self.keyword_patterns:
            if re.search(pattern, message, re.IGNORECASE):
                violations.append('harmful_content')

        is_clean = len(violations) == 0
        return is_clean, filtered_message, violations
```

## Configuration Changes

### Server Configuration Updates

```yaml
# server/server_config.yaml
# Remove Redis configuration
# redis:
#   enabled: false

# Add NATS configuration
nats:
  enabled: true
  url: nats://localhost:4222
  max_payload: 1048576
  reconnect_time_wait: 1
  max_reconnect_attempts: 5

# Add chat system configuration
chat:
  rate_limiting:
    enabled: true
    global: 10
    local: 20
    say: 15
    party: 30
    whisper: 5

  content_filtering:
    enabled: true
    profanity_filter: true
    keyword_detection: true

  message_history:
    enabled: true
    retention_days: 30
    max_messages_per_channel: 1000
```

## Migration Checklist

### Pre-Migration Tasks

- [ ] Backup current Redis data (if any)
- [ ] Document current Redis configuration
- [ ] Test NATS server installation
- [ ] Validate NATS connectivity
- [ ] Create rollback plan

### Migration Tasks

- [ ] Install NATS server
- [ ] Update dependencies
- [ ] Implement NATS service
- [ ] Migrate chat service
- [ ] Implement supporting infrastructure
- [ ] Update configuration
- [ ] Test all functionality

### Post-Migration Tasks

- [ ] Remove Redis dependencies
- [ ] Update documentation
- [ ] Monitor system performance
- [ ] Validate all chat features
- [ ] Clean up old Redis configuration

## Risk Mitigation

### Technical Risks

- **NATS Connection Issues**: Implement robust reconnection logic
- **Message Loss**: Add message persistence and delivery guarantees
- **Performance Issues**: Monitor and optimize as needed
- **Data Migration**: Ensure no data loss during migration

### Operational Risks

- **Downtime**: Plan migration during low-usage periods
- **Rollback Complexity**: Maintain ability to revert to Redis if needed
- **Monitoring Gaps**: Implement comprehensive monitoring before migration

## Success Metrics

### Performance Metrics

- **Message Delivery Latency**: < 10ms (NATS target)
- **System Uptime**: > 99.9%
- **Concurrent Users**: 10-100 players
- **Message Volume**: 100-1000 messages per minute

### Functional Metrics

- **All Chat Channels**: Operational
- **Rate Limiting**: Effective enforcement
- **Content Filtering**: > 95% accuracy
- **User Management**: Mute/unmute functionality working

### User Experience Metrics

- **Message Delivery**: Real-time (sub-100ms)
- **Error Rate**: < 1%
- **User Satisfaction**: High adoption of chat features

## Timeline Estimate

### Development Timeline

- **Phase 1 (NATS Infrastructure)**: 1 week
- **Phase 2 (Chat Service Migration)**: 1 week
- **Phase 3 (Supporting Infrastructure)**: 2 weeks
- **Phase 4 (API and Frontend)**: 1 week
- **Phase 5 (Testing)**: 1 week
- **Phase 6 (Deployment)**: 1 week

**Total Estimated Duration**: 7 weeks

### Critical Path

1. NATS server installation and configuration
2. Chat service migration
3. Rate limiting implementation
4. User management system
5. Testing and validation
6. Production deployment

## Conclusion

This migration from Redis to NATS will provide MythosMUD with a robust, high-performance chat system that eliminates the WSL networking issues we've encountered. The comprehensive supporting infrastructure ensures that all Chat System features are properly implemented, even those not natively supported by NATS.

The phased approach allows for careful testing and validation at each step, ensuring a smooth transition with minimal risk. The result will be a chat system that is both technically superior and more maintainable than our current Redis-based approach.

*"The most merciful thing in the world, I think, is the inability of the human brain to correlate all its contents." - H.P. Lovecraft*

---

*Document prepared by Prof. Armitage, Miskatonic University Department of Occult Studies*
*Last updated: [Current Date]*
