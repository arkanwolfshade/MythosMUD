# Dual Connection System Troubleshooting Guide

## Overview

This guide provides comprehensive troubleshooting information for the dual WebSocket/SSE connection system. It covers common issues, diagnostic procedures, and resolution strategies.

## Table of Contents

1. [Quick Diagnostic Checklist](#quick-diagnostic-checklist)
2. [Connection Issues](#connection-issues)
3. [Message Delivery Problems](#message-delivery-problems)
4. [Session Management Issues](#session-management-issues)
5. [Performance Problems](#performance-problems)
6. [Error Handling Issues](#error-handling-issues)
7. [Client-Side Issues](#client-side-issues)
8. [Server-Side Issues](#server-side-issues)
9. [Database Issues](#database-issues)
10. [Network and Infrastructure Issues](#network-and-infrastructure-issues)
11. [Monitoring and Debugging Tools](#monitoring-and-debugging-tools)

## Quick Diagnostic Checklist

### System Health Check

```bash
# 1. Check server status
curl -f http://localhost:8000/health

# 2. Check connection statistics
curl http://localhost:8000/api/connections/stats

# 3. Check monitoring endpoints
curl http://localhost:8000/monitoring/dual-connections
curl http://localhost:8000/monitoring/performance
curl http://localhost:8000/monitoring/connection-health

# 4. Check error statistics
curl http://localhost:8000/monitoring/errors

# 5. Check server logs
tail -f logs/mythos.log | grep -E "(ERROR|WARNING|CRITICAL)"
```

### Client Health Check

```javascript
// Check connection state
console.log('Connection state:', {
  isConnected: connection.isConnected,
  websocketConnected: connection.websocketConnected,
  sseConnected: connection.sseConnected,
  sessionId: connection.sessionId,
  connectionHealth: connection.connectionHealth
});

// Check connection info
const info = connection.getConnectionInfo();
console.log('Connection info:', info);

// Test message sending
try {
  await connection.sendCommand('test');
  console.log('Message sent successfully');
} catch (error) {
  console.error('Message send failed:', error);
}
```

## Connection Issues

### Issue: Connections Not Establishing

**Symptoms:**
- Client shows "Connecting..." indefinitely
- WebSocket connection fails
- SSE connection fails
- No connection events in logs

**Diagnostic Steps:**

1. **Check Network Connectivity:**
```bash
# Test basic connectivity
ping yourdomain.com
telnet yourdomain.com 8000

# Test WebSocket connectivity
<!-- nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket -->
<!-- This is documentation showing example WebSocket URLs, not production code -->
wscat -c ws://yourdomain.com/ws/test_player

# Test SSE connectivity
curl -N http://yourdomain.com/sse/test_player
```

2. **Check Server Status:**
```bash
# Check if server is running
ps aux | grep uvicorn
netstat -tlnp | grep :8000

# Check server logs
tail -f logs/mythos.log | grep -E "(WebSocket|SSE|connection)"
```

3. **Check Authentication:**
```bash
# Test authentication endpoint
curl -H "Authorization: Bearer your_token" http://localhost:8000/api/auth/verify

# Check authentication logs
grep "authentication" logs/mythos.log | tail -20
```

**Resolution:**

1. **Network Issues:**
```bash
# Check firewall settings
sudo ufw status
sudo iptables -L

# Check DNS resolution
nslookup yourdomain.com
dig yourdomain.com
```

2. **Server Issues:**
```bash
# Restart server
sudo systemctl restart mythos
# or
docker-compose restart mythos-server

# Check server configuration
cat .env | grep -E "(DEBUG|LOG_LEVEL|DATABASE_URL)"
```

3. **Authentication Issues:**
```bash
# Verify token format
echo "your_token" | base64 -d

# Check token expiration
curl -H "Authorization: Bearer your_token" http://localhost:8000/api/auth/verify
```

### Issue: Connections Dropping Frequently

**Symptoms:**
- Connections establish but drop quickly
- Frequent reconnection attempts
- "Connection lost" messages
- High error rates in logs

**Diagnostic Steps:**

1. **Check Connection Health:**
```bash
# Check connection health statistics
curl http://localhost:8000/monitoring/connection-health | jq '.overall_health'

# Check for unhealthy connections
curl http://localhost:8000/monitoring/connection-health | jq '.connection_type_health'
```

2. **Check Network Stability:**
```bash
# Monitor network latency
ping -c 100 yourdomain.com | tail -1

# Check for packet loss
mtr --report --report-cycles 100 yourdomain.com
```

3. **Check Server Resources:**
```bash
# Check memory usage
free -h
ps aux --sort=-%mem | head -10

# Check CPU usage
top -p $(pgrep -f uvicorn)

# Check disk space
df -h
```

**Resolution:**

1. **Network Issues:**
```bash
# Increase connection timeout
export CONNECTION_TIMEOUT=600

# Configure keep-alive
echo 'net.ipv4.tcp_keepalive_time = 600' >> /etc/sysctl.conf
sysctl -p
```

2. **Server Resource Issues:**
```bash
# Increase memory limits
export MAX_CONNECTIONS_PER_PLAYER=2

# Optimize garbage collection
export PYTHONOPTIMIZE=1

# Restart with more resources
docker-compose up -d --scale mythos-server=2
```

3. **Application Issues:**
```python
# Increase health check frequency
HEALTH_CHECK_INTERVAL = 15  # seconds

# Reduce cleanup interval
CLEANUP_INTERVAL = 30  # seconds

# Enable connection pooling
CONNECTION_POOL_SIZE = 2000
```

### Issue: Multiple Connections Not Working

**Symptoms:**
- Only one connection type works
- Dual connections not established
- Session conflicts
- Connection replacement instead of addition

**Diagnostic Steps:**

1. **Check Connection Manager State:**
```bash
# Check connection statistics
curl http://localhost:8000/api/connections/stats | jq '.connection_distribution'

# Check specific player connections
curl http://localhost:8000/api/connections/test_player | jq '.connections'
```

2. **Check Session Management:**
```bash
# Check session information
curl http://localhost:8000/api/connections/test_player/session

# Check session statistics
curl http://localhost:8000/monitoring/dual-connections | jq '.session_analytics'
```

3. **Check Client Configuration:**
```javascript
// Verify client is attempting dual connections
console.log('Connection URLs:', {
  websocket: `ws://localhost:8000/ws/test_player?session_id=${sessionId}`,
  sse: `http://localhost:8000/sse/test_player?session_id=${sessionId}`
});
```

**Resolution:**

1. **Server Configuration:**
```python
# Ensure dual connections are enabled
MAX_CONNECTIONS_PER_PLAYER = 4  # Allow multiple connections

# Check connection manager logic
# Verify connect_websocket and connect_sse don't disconnect existing connections
```

2. **Client Configuration:**
```typescript
// Ensure client establishes both connections
const connection = useGameConnection({
  playerId: 'test_player',
  authToken: 'token',
  // Enable dual connections
  enableDualConnections: true
});
```

3. **Session Management:**
```python
# Ensure session tracking is working
# Check that session_id is properly passed to connection methods
# Verify session validation logic
```

## Message Delivery Problems

### Issue: Messages Not Delivered

**Symptoms:**
- Messages sent but not received
- Partial message delivery
- Message delivery failures
- High delivery failure rates

**Diagnostic Steps:**

1. **Check Message Delivery Statistics:**
```bash
# Check delivery statistics
curl http://localhost:8000/monitoring/performance | jq '.message_delivery'

# Check specific player delivery
curl http://localhost:8000/api/connections/test_player | jq '.message_delivery_stats'
```

2. **Check Connection State:**
```bash
# Verify connections are active
curl http://localhost:8000/api/connections/test_player | jq '.connections'

# Check connection health
curl http://localhost:8000/monitoring/connection-health | jq '.overall_health'
```

3. **Check Message Logs:**
```bash
# Check message delivery logs
grep "Message delivered" logs/mythos.log | tail -20

# Check message failure logs
grep "Message delivery failed" logs/mythos.log | tail -20
```

**Resolution:**

1. **Connection Issues:**
```python
# Check connection health before sending
if not connection_manager.check_connection_health(player_id):
    logger.warning(f"Unhealthy connections for player {player_id}")
    # Attempt to recover connections

# Implement retry logic
async def send_with_retry(player_id, message, max_retries=3):
    for attempt in range(max_retries):
        try:
            return await connection_manager.send_personal_message(player_id, message)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
```

2. **Message Format Issues:**
```python
# Validate message format
def validate_message(message):
    required_fields = ['type', 'content']
    for field in required_fields:
        if field not in message:
            raise ValueError(f"Missing required field: {field}")

    # Check message size
    if len(str(message)) > MAX_MESSAGE_SIZE:
        raise ValueError("Message too large")
```

3. **Network Issues:**
```bash
# Check network connectivity
ping -c 10 yourdomain.com

# Check for packet loss
mtr --report --report-cycles 100 yourdomain.com

# Test message delivery manually
curl -X POST http://localhost:8000/api/messages \
  -H "Content-Type: application/json" \
  -d '{"player_id": "test_player", "message": {"type": "test", "content": "hello"}}'
```

### Issue: Duplicate Messages

**Symptoms:**
- Messages received multiple times
- Duplicate message delivery
- Message deduplication not working

**Diagnostic Steps:**

1. **Check Message Logs:**
```bash
# Check for duplicate message logs
grep "Message delivered" logs/mythos.log | grep "test_player" | tail -20

# Check message IDs
grep "message_id" logs/mythos.log | tail -20
```

2. **Check Client State:**
```javascript
// Check if client is receiving duplicates
let messageCount = 0;
connection.onMessage = (message) => {
  messageCount++;
  console.log(`Message ${messageCount}:`, message);
};
```

**Resolution:**

1. **Implement Message Deduplication:**
```python
# Add message ID tracking
import hashlib
import time

def generate_message_id(message, player_id):
    content = f"{player_id}:{message['type']}:{message['content']}:{time.time()}"
    return hashlib.md5(content.encode()).hexdigest()

# Track delivered messages
delivered_messages = set()

async def send_personal_message(self, player_id, message):
    message_id = generate_message_id(message, player_id)

    if message_id in delivered_messages:
        logger.warning(f"Duplicate message detected: {message_id}")
        return

    delivered_messages.add(message_id)
    # ... send message logic
```

2. **Client-Side Deduplication:**
```typescript
// Implement client-side deduplication
const receivedMessages = new Set();

connection.onMessage = (message) => {
  const messageId = message.id || `${message.type}:${message.content}:${message.timestamp}`;

  if (receivedMessages.has(messageId)) {
    console.warn('Duplicate message received:', message);
    return;
  }

  receivedMessages.add(messageId);
  // Process message
};
```

## Session Management Issues

### Issue: Session Conflicts

**Symptoms:**
- Multiple sessions for same player
- Session validation failures
- Connection disconnections on session change
- Session state inconsistencies

**Diagnostic Steps:**

1. **Check Session State:**
```bash
# Check player session
curl http://localhost:8000/api/connections/test_player/session

# Check session statistics
curl http://localhost:8000/monitoring/dual-connections | jq '.session_analytics'
```

2. **Check Session Logs:**
```bash
# Check session management logs
grep "session" logs/mythos.log | tail -20

# Check session validation logs
grep "session validation" logs/mythos.log | tail -20
```

**Resolution:**

1. **Session Validation:**
```python
# Implement proper session validation
def validate_session(player_id, session_id):
    current_session = connection_manager.get_player_session(player_id)

    if current_session is None:
        # First session for player
        return True

    if current_session == session_id:
        # Same session
        return True

    # Different session - need to handle session switch
    return False

# Handle session switching
async def handle_new_game_session(player_id, new_session_id):
    current_session = connection_manager.get_player_session(player_id)

    if current_session == new_session_id:
        logger.info(f"Player {player_id} already in session {new_session_id}")
        return

    # Disconnect existing connections
    await connection_manager.force_disconnect_player(player_id)

    # Update session
    connection_manager.player_sessions[player_id] = new_session_id

    logger.info(f"Player {player_id} switched from {current_session} to {new_session_id}")
```

2. **Client Session Management:**
```typescript
// Ensure proper session handling
const connection = useGameConnection({
  playerId: 'test_player',
  authToken: 'token',
  onSessionChange: (newSessionId, previousSessionId) => {
    console.log(`Session changed from ${previousSessionId} to ${newSessionId}`);
    // Handle session change
  }
});

// Create new session when needed
const createNewGame = async () => {
  try {
    const newSessionId = await connection.createNewSession();
    console.log('New session created:', newSessionId);
  } catch (error) {
    console.error('Failed to create new session:', error);
  }
};
```

### Issue: Session Persistence Problems

**Symptoms:**
- Sessions lost on server restart
- Session data not persisted
- Session recovery failures
- Inconsistent session state

**Diagnostic Steps:**

1. **Check Database State:**
```bash
# Check session data in database (PostgreSQL)
psql $DATABASE_URL -c "SELECT * FROM sessions WHERE player_id = 'test_player';"

# Check connection data
psql $DATABASE_URL -c "SELECT * FROM connections WHERE player_id = 'test_player';"
```

2. **Check Persistence Logs:**
```bash
# Check persistence logs
grep "persistence" logs/mythos.log | tail -20

# Check database connection logs
grep "database" logs/mythos.log | tail -20
```

**Resolution:**

1. **Database Configuration:**
```python
# Ensure proper database connection (PostgreSQL)
DATABASE_URL = "postgresql://user:password@localhost:5432/mythosmud"

# Implement session persistence
async def save_session_data(player_id, session_id, connection_data):
    async with database.transaction():
        await database.execute(
            "INSERT OR REPLACE INTO sessions (player_id, session_id, data, created_at) VALUES (?, ?, ?, ?)",
            player_id, session_id, json.dumps(connection_data), datetime.utcnow()
        )

async def load_session_data(player_id):
    result = await database.fetch_one(
        "SELECT session_id, data FROM sessions WHERE player_id = ? ORDER BY created_at DESC LIMIT 1",
        player_id
    )
    return result
```

2. **Session Recovery:**
```python
# Implement session recovery on startup
async def recover_sessions():
    sessions = await database.fetch_all("SELECT player_id, session_id, data FROM sessions")

    for session in sessions:
        player_id = session['player_id']
        session_id = session['session_id']
        data = json.loads(session['data'])

        # Restore session state
        connection_manager.player_sessions[player_id] = session_id

        logger.info(f"Recovered session {session_id} for player {player_id}")
```

## Performance Problems

### Issue: Slow Connection Establishment

**Symptoms:**
- Long connection times
- Timeout errors
- High connection establishment latency
- Poor user experience

**Diagnostic Steps:**

1. **Check Performance Metrics:**
```bash
# Check connection establishment times
curl http://localhost:8000/monitoring/performance | jq '.connection_establishment'

# Check system performance
curl http://localhost:8000/monitoring/performance | jq '.system_performance'
```

2. **Check Server Resources:**
```bash
# Check CPU usage
top -p $(pgrep -f uvicorn)

# Check memory usage
free -h
ps aux --sort=-%mem | head -10

# Check disk I/O
iostat -x 1 5
```

**Resolution:**

1. **Server Optimization:**
```python
# Optimize connection establishment
CONNECTION_POOL_SIZE = 1000
MAX_CONNECTIONS_PER_PLAYER = 2
CONNECTION_TIMEOUT = 180

# Use connection pooling
import asyncio
from asyncio import Queue

class ConnectionPool:
    def __init__(self, max_size=1000):
        self.pool = Queue(maxsize=max_size)
        self.active_connections = set()

    async def get_connection(self):
        if not self.pool.empty():
            return await self.pool.get()
        return await self.create_new_connection()

    async def return_connection(self, connection):
        if connection.is_healthy():
            await self.pool.put(connection)
        else:
            await connection.close()
```

2. **Database Optimization:**
```sql
-- Add indexes for better performance
CREATE INDEX CONCURRENTLY idx_connections_player_id ON connections(player_id);
CREATE INDEX CONCURRENTLY idx_connections_session_id ON connections(session_id);
CREATE INDEX CONCURRENTLY idx_connections_created_at ON connections(created_at);

-- Optimize queries
EXPLAIN ANALYZE SELECT * FROM connections WHERE player_id = 'test_player';
```

3. **Network Optimization:**
```bash
# Optimize TCP settings
echo 'net.core.rmem_max = 16777216' >> /etc/sysctl.conf
echo 'net.core.wmem_max = 16777216' >> /etc/sysctl.conf
echo 'net.ipv4.tcp_rmem = 4096 87380 16777216' >> /etc/sysctl.conf
echo 'net.ipv4.tcp_wmem = 4096 65536 16777216' >> /etc/sysctl.conf
sysctl -p
```

### Issue: High Memory Usage

**Symptoms:**
- Memory usage growing over time
- Out of memory errors
- Slow performance
- System instability

**Diagnostic Steps:**

1. **Check Memory Usage:**
```bash
# Check overall memory usage
free -h
cat /proc/meminfo

# Check process memory usage
ps aux --sort=-%mem | head -10

# Check memory usage over time
sar -r 1 60
```

2. **Check for Memory Leaks:**
```bash
# Use memory profiler
python -m memory_profiler server/main.py

# Check for memory leaks in logs
grep "memory" logs/mythos.log | tail -20
```

**Resolution:**

1. **Memory Management:**
```python
# Implement proper cleanup
import gc
import weakref

class ConnectionManager:
    def __init__(self):
        self.connections = weakref.WeakValueDictionary()
        self.cleanup_interval = 60  # seconds
        self.max_connections = 1000

    async def cleanup_old_connections(self):
        current_time = time.time()
        cutoff_time = current_time - CONNECTION_TIMEOUT

        # Remove old connections
        old_connections = [
            conn_id for conn_id, conn in self.connections.items()
            if conn.last_activity < cutoff_time
        ]

        for conn_id in old_connections:
            await self.disconnect_connection(conn_id)

        # Force garbage collection
        gc.collect()

        logger.info(f"Cleaned up {len(old_connections)} old connections")
```

2. **Resource Limits:**
```python
# Set resource limits
MAX_CONNECTIONS_PER_PLAYER = 2
MAX_TOTAL_CONNECTIONS = 1000
CONNECTION_TIMEOUT = 300
CLEANUP_INTERVAL = 60

# Monitor memory usage
import psutil

def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > 85:
        logger.warning(f"High memory usage: {memory.percent}%")
        # Trigger cleanup
        asyncio.create_task(connection_manager.cleanup_old_connections())
```

## Error Handling Issues

### Issue: Errors Not Being Caught

**Symptoms:**
- Unhandled exceptions
- Application crashes
- Error logs not appearing
- Poor error recovery

**Diagnostic Steps:**

1. **Check Error Logs:**
```bash
# Check for unhandled exceptions
grep "Traceback" logs/mythos.log | tail -20

# Check error statistics
curl http://localhost:8000/monitoring/errors | jq '.error_breakdown'
```

2. **Check Error Handling:**
```python
# Test error handling
try:
    # Trigger an error
    await connection_manager.connect_websocket(None, "test_player")
except Exception as e:
    print(f"Error caught: {e}")
```

**Resolution:**

1. **Comprehensive Error Handling:**
```python
# Implement comprehensive error handling
import logging
from functools import wraps

def handle_errors(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ConnectionError as e:
            logger.error(f"Connection error in {func.__name__}: {e}")
            # Handle connection errors
        except AuthenticationError as e:
            logger.error(f"Authentication error in {func.__name__}: {e}")
            # Handle authentication errors
        except Exception as e:
            logger.error(f"Unexpected error in {func.__name__}: {e}", exc_info=True)
            # Handle unexpected errors
    return wrapper

@handle_errors
async def connect_websocket(self, websocket, player_id, session_id=None):
    # Connection logic
    pass
```

2. **Error Recovery:**
```python
# Implement error recovery
class ErrorRecovery:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        self.retry_attempts = {}
        self.max_retries = 3

    async def recover_from_error(self, error_type, player_id, error_details):
        if error_type == "connection_error":
            await self.recover_connection(player_id)
        elif error_type == "session_error":
            await self.recover_session(player_id)
        elif error_type == "authentication_error":
            await self.recover_authentication(player_id)

    async def recover_connection(self, player_id):
        # Attempt to reconnect
        try:
            await self.connection_manager.force_disconnect_player(player_id)
            # Wait before reconnecting
            await asyncio.sleep(5)
            # Attempt to reconnect
        except Exception as e:
            logger.error(f"Failed to recover connection for {player_id}: {e}")
```

## Client-Side Issues

### Issue: React Hook Not Working

**Symptoms:**
- Hook not initializing
- State not updating
- Connection not establishing
- Error in browser console

**Diagnostic Steps:**

1. **Check Browser Console:**
```javascript
// Check for JavaScript errors
console.error('Check browser console for errors');

// Check hook state
console.log('Hook state:', {
  isConnected: connection.isConnected,
  isConnecting: connection.isConnecting,
  error: connection.error
});
```

2. **Check Network Requests:**
```javascript
// Check network tab in browser dev tools
// Look for failed requests to /ws/ and /sse/ endpoints
```

**Resolution:**

1. **Hook Configuration:**
```typescript
// Ensure proper hook configuration
const connection = useGameConnection({
  playerId: 'test_player',
  authToken: 'valid_token',
  // Add error handling
  onError: (error) => {
    console.error('Connection error:', error);
  },
  // Add debug logging
  debug: true
});
```

2. **State Management:**
```typescript
// Check state updates
useEffect(() => {
  console.log('Connection state changed:', {
    isConnected: connection.isConnected,
    websocketConnected: connection.websocketConnected,
    sseConnected: connection.sseConnected
  });
}, [connection.isConnected, connection.websocketConnected, connection.sseConnected]);
```

### Issue: WebSocket Connection Fails

**Symptoms:**
- WebSocket connection not establishing
- WebSocket errors in console
- Fallback to SSE only
- Connection timeout

**Diagnostic Steps:**

1. **Check WebSocket URL:**
```javascript
// Verify WebSocket URL
const wsUrl = `ws://localhost:8000/ws/test_player?session_id=${sessionId}`;
console.log('WebSocket URL:', wsUrl);

// Test WebSocket connection manually
const ws = new WebSocket(wsUrl);
ws.onopen = () => console.log('WebSocket connected');
ws.onerror = (error) => console.error('WebSocket error:', error);
ws.onclose = (event) => console.log('WebSocket closed:', event);
```

2. **Check Server WebSocket Endpoint:**
```bash
# Test WebSocket endpoint
wscat -c ws://localhost:8000/ws/test_player

# Check WebSocket logs
grep "WebSocket" logs/mythos.log | tail -20
```

**Resolution:**

1. **WebSocket Configuration:**
```typescript
// Ensure proper WebSocket configuration
const connection = useGameConnection({
  playerId: 'test_player',
  authToken: 'token',
  // WebSocket-specific options
  websocketOptions: {
    protocols: ['mythos-protocol'],
    timeout: 10000
  }
});
```

2. **Error Handling:**
```typescript
// Handle WebSocket errors
connection.onError = (error) => {
  if (error.type === 'websocket_error') {
    console.error('WebSocket error:', error);
    // Attempt to reconnect or fallback to SSE
  }
};
```

## Server-Side Issues

### Issue: Server Not Starting

**Symptoms:**
- Server fails to start
- Port already in use
- Configuration errors
- Dependency issues

**Diagnostic Steps:**

1. **Check Server Logs:**
```bash
# Check startup logs
tail -f logs/mythos.log

# Check system logs
journalctl -u mythos -f
```

2. **Check Port Usage:**
```bash
# Check if port is in use
netstat -tlnp | grep :8000
lsof -i :8000
```

**Resolution:**

1. **Port Issues:**
```bash
# Kill process using port
sudo kill -9 $(lsof -t -i:8000)

# Use different port
export PORT=8001
uvicorn server.main:app --port 8001
```

2. **Configuration Issues:**
```bash
# Check configuration
cat .env
python -c "import server.config; print(server.config.DATABASE_URL)"

# Validate configuration
python server/scripts/validate_config.py
```

### Issue: Database Connection Problems

**Symptoms:**
- Database connection errors
- Query failures
- Data not persisting
- Database locks

**Diagnostic Steps:**

1. **Check Database Connectivity:**
```bash
# Test database connection
python -c "import psycopg2; print(psycopg2.connect(os.environ['DATABASE_URL']).cursor().execute('SELECT 1').fetchone())"

# For PostgreSQL
psql -h localhost -U mythos_user -d mythos_prod -c "SELECT 1;"
```

2. **Check Database Logs:**
```bash
# Check database logs
grep "database" logs/mythos.log | tail -20

# Check for database errors
grep "postgresql\|database" logs/mythos.log | tail -20
```

**Resolution:**

1. **Database Configuration:**
```python
# Ensure proper database URL
DATABASE_URL = "postgresql://user:password@localhost:5432/mythosmud"

# For PostgreSQL
DATABASE_URL = "postgresql://user:password@localhost:5432/mythos_prod"

# Test database connection
async def test_database_connection():
    try:
        await database.fetch_one("SELECT 1")
        logger.info("Database connection successful")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
```

2. **Database Optimization:**
```sql
-- Check database locks
SELECT * FROM pg_locks WHERE NOT granted;

-- Check active connections
SELECT * FROM pg_stat_activity WHERE state = 'active';

-- Optimize database
VACUUM ANALYZE;
```

## Network and Infrastructure Issues

### Issue: Load Balancer Problems

**Symptoms:**
- Connections not distributed
- Sticky sessions not working
- Connection drops
- Performance issues

**Diagnostic Steps:**

1. **Check Load Balancer Configuration:**
```bash
# Check nginx configuration
nginx -t
cat /etc/nginx/nginx.conf

# Check load balancer logs
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

2. **Check Server Distribution:**
```bash
# Check which server is handling requests
curl -H "X-Forwarded-For: test" http://yourdomain.com/api/connections/stats
```

**Resolution:**

1. **Nginx Configuration:**
```nginx
# Configure WebSocket load balancing
upstream mythos_websocket {
    ip_hash;  # Sticky sessions
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
}

# WebSocket proxy configuration
location /ws/ {
    proxy_pass http://mythos_websocket;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_read_timeout 86400;
}
```

2. **Session Affinity:**
```python
# Implement session affinity
def get_server_for_session(session_id):
    # Use consistent hashing
    hash_value = hash(session_id) % len(servers)
    return servers[hash_value]
```

## Monitoring and Debugging Tools

### Debug Mode

**Enable Debug Mode:**
```bash
# Set debug environment variable
export DEBUG=true
export LOG_LEVEL=DEBUG

# Start server in debug mode
uvicorn server.main:app --reload --log-level debug
```

**Debug Logging:**
```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Add debug statements
logger.debug(f"Connection state: {connection_state}")
logger.debug(f"Message content: {message}")
logger.debug(f"Session ID: {session_id}")
```

### Performance Profiling

**CPU Profiling:**
```bash
# Install profiling tools
pip install py-spy

# Profile running server
py-spy top --pid $(pgrep -f uvicorn)

# Generate flame graph
py-spy record -o profile.svg --pid $(pgrep -f uvicorn)
```

**Memory Profiling:**
```bash
# Install memory profiler
pip install memory-profiler

# Profile memory usage
python -m memory_profiler server/main.py

# Monitor memory usage
python -c "
import psutil
import time
while True:
    memory = psutil.virtual_memory()
    print(f'Memory: {memory.percent}%')
    time.sleep(5)
"
```

### Network Debugging

**Network Analysis:**
```bash
# Monitor network connections
netstat -an | grep :8000

# Check network traffic
tcpdump -i any port 8000

# Monitor WebSocket traffic
wireshark -f "port 8000"
```

**Connection Testing:**
```bash
# Test WebSocket connection
wscat -c ws://localhost:8000/ws/test_player

# Test SSE connection
curl -N http://localhost:8000/sse/test_player

# Test API endpoints
curl -v http://localhost:8000/api/connections/stats
```

### Log Analysis

**Error Analysis:**
```bash
# Count errors by type
grep "ERROR" logs/mythos.log | jq -r '.error_type' | sort | uniq -c

# Find recent errors
grep "ERROR" logs/mythos.log | tail -50

# Analyze error patterns
grep "connection_error" logs/mythos.log | jq -r '.player_id' | sort | uniq -c
```

**Performance Analysis:**
```bash
# Check connection establishment times
grep "WebSocket connected" logs/mythos.log | jq -r '.establishment_time_ms' | sort -n

# Check message delivery times
grep "Message delivered" logs/mythos.log | jq -r '.delivery_time_ms' | sort -n

# Check for slow operations
grep "establishment_time_ms" logs/mythos.log | jq 'select(.establishment_time_ms > 1000)'
```

---

*This troubleshooting guide is maintained as part of the MythosMUD dual connection system implementation. Last updated: 2025-01-06*
