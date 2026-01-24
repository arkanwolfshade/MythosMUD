# Dual Connection System Client Integration Guide

## Overview

This guide provides comprehensive documentation for integrating the dual WebSocket/SSE connection system into React applications. The system provides enhanced reliability and performance through simultaneous WebSocket and Server-Sent Events connections.

## Table of Contents

1. [Installation and Setup](#installation-and-setup)
2. [useGameConnection Hook](#usegameconnection-hook)
3. [Connection Management](#connection-management)
4. [Session Management](#session-management)
5. [Error Handling](#error-handling)
6. [Performance Monitoring](#performance-monitoring)
7. [Best Practices](#best-practices)
8. [Examples](#examples)
9. [Troubleshooting](#troubleshooting)

## Installation and Setup

### Prerequisites

React 16.8+ (for hooks support)

- TypeScript 4.0+ (recommended)
- Node.js 16+ and npm/yarn

### Dependencies

The dual connection system requires the following dependencies:

```json
{
  "dependencies": {
    "react": "^18.0.0",
    "typescript": "^4.9.0"
  }
}
```

### Project Structure

```
src/
├── hooks/
│   └── useGameConnection.ts
├── components/
│   ├── GameTerminal.tsx
│   ├── ConnectionPanel.tsx
│   └── MonitoringPanel.tsx
└── types/
    └── connection.ts
```

## useGameConnection Hook

### Basic Usage

```typescript
import { useGameConnection } from './hooks/useGameConnection';

function GameComponent() {
  const {
    isConnected,
    isConnecting,
    error,
    connect,
    disconnect,
    sendCommand
  } = useGameConnection({
    playerId: 'your_player_id',
    authToken: 'your_auth_token'
  });

  return (
    <div>
      <p>Status: {isConnected ? 'Connected' : 'Disconnected'}</p>
      <button onClick={connect} disabled={isConnecting}>
        {isConnecting ? 'Connecting...' : 'Connect'}
      </button>
    </div>
  );
}
```

### Advanced Usage with Session Management

```typescript
import { useGameConnection } from './hooks/useGameConnection';

function AdvancedGameComponent() {
  const {
    // Connection state
    isConnected,
    isConnecting,
    websocketConnected,
    sseConnected,

    // Session management
    sessionId,
    createNewSession,
    switchToSession,

    // Connection health
    connectionHealth,
    connectionMetadata,

    // Actions
    connect,
    disconnect,
    sendCommand,
    getConnectionInfo
  } = useGameConnection({
    playerId: 'test_player',
    authToken: 'auth_token_123',

    // Callbacks
    onSessionChange: (newSessionId) => {
      console.log('Session changed to:', newSessionId);
    },
    onConnectionHealthUpdate: (health) => {
      console.log('Connection health updated:', health);
    },
    onMessage: (message) => {
      console.log('Received message:', message);
    },
    onError: (error) => {
      console.error('Connection error:', error);
    }
  });

  const handleNewGame = async () => {
    const newSession = await createNewSession();
    console.log('Created new session:', newSession);
  };

  const handleSwitchSession = async () => {
    await switchToSession('new_session_id');
  };

  return (
    <div>
      <div>
        <h3>Connection Status</h3>
        <p>Overall: {isConnected ? 'Connected' : 'Disconnected'}</p>
        <p>WebSocket: {websocketConnected ? 'Connected' : 'Disconnected'}</p>
        <p>SSE: {sseConnected ? 'Connected' : 'Disconnected'}</p>
        <p>Session: {sessionId}</p>
      </div>

      <div>
        <h3>Actions</h3>
        <button onClick={connect} disabled={isConnecting}>
          Connect
        </button>
        <button onClick={disconnect}>
          Disconnect
        </button>
        <button onClick={handleNewGame}>
          New Game Session
        </button>
        <button onClick={handleSwitchSession}>
          Switch Session
        </button>
      </div>

      <div>
        <h3>Connection Health</h3>
        <p>Status: {connectionHealth}</p>
        <pre>{JSON.stringify(connectionMetadata, null, 2)}</pre>
      </div>
    </div>
  );
}
```

## Connection Management

### Connection State

The hook provides comprehensive connection state information:

```typescript
interface GameConnectionState {
  // Basic connection state
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;

  // Dual connection state
  websocketConnected: boolean;
  sseConnected: boolean;

  // Session information
  sessionId: string | null;

  // Connection health
  connectionHealth: 'unknown' | 'healthy' | 'degraded' | 'unhealthy';
  connectionMetadata: ConnectionMetadata | null;

  // Player information
  playerName: string;
  authToken: string;
}
```

### Connection Lifecycle

```typescript
function ConnectionLifecycleExample() {
  const connection = useGameConnection({
    playerId: 'test_player',
    authToken: 'auth_token'
  });

  // Connection establishment
  useEffect(() => {
    if (!connection.isConnected && !connection.isConnecting) {
      connection.connect();
    }
  }, []);

  // Connection monitoring
  useEffect(() => {
    if (connection.isConnected) {
      console.log('Connection established');
      console.log('WebSocket:', connection.websocketConnected);
      console.log('SSE:', connection.sseConnected);
    }
  }, [connection.isConnected]);

  // Error handling
  useEffect(() => {
    if (connection.error) {
      console.error('Connection error:', connection.error);
      // Implement error recovery logic
    }
  }, [connection.error]);

  return <div>Connection Status: {connection.isConnected ? 'Connected' : 'Disconnected'}</div>;
}
```

### Manual Connection Control

```typescript
function ManualConnectionControl() {
  const connection = useGameConnection({
    playerId: 'test_player',
    authToken: 'auth_token'
  });

  const handleConnect = async () => {
    try {
      await connection.connect();
      console.log('Connection successful');
    } catch (error) {
      console.error('Connection failed:', error);
    }
  };

  const handleDisconnect = () => {
    connection.disconnect();
    console.log('Disconnected');
  };

  return (
    <div>
      <button onClick={handleConnect} disabled={connection.isConnecting}>
        Connect
      </button>
      <button onClick={handleDisconnect} disabled={!connection.isConnected}>
        Disconnect
      </button>
    </div>
  );
}
```

## Session Management

### Session Creation

```typescript
function SessionManagementExample() {
  const connection = useGameConnection({
    playerId: 'test_player',
    authToken: 'auth_token'
  });

  const createNewGameSession = async () => {
    try {
      const newSessionId = await connection.createNewSession();
      console.log('New session created:', newSessionId);

      // The hook will automatically update the sessionId state
      // and establish new connections with the new session
    } catch (error) {
      console.error('Failed to create new session:', error);
    }
  };

  const switchToExistingSession = async (sessionId: string) => {
    try {
      await connection.switchToSession(sessionId);
      console.log('Switched to session:', sessionId);
    } catch (error) {
      console.error('Failed to switch session:', error);
    }
  };

  return (
    <div>
      <p>Current Session: {connection.sessionId}</p>
      <button onClick={createNewGameSession}>
        New Game Session
      </button>
      <button onClick={() => switchToExistingSession('existing_session_id')}>
        Switch to Existing Session
      </button>
    </div>
  );
}
```

### Session Callbacks

```typescript
function SessionCallbackExample() {
  const connection = useGameConnection({
    playerId: 'test_player',
    authToken: 'auth_token',

    onSessionChange: (newSessionId, previousSessionId) => {
      console.log('Session changed from', previousSessionId, 'to', newSessionId);

      // Update UI to reflect new session
      // Clear any session-specific state
      // Notify other components of session change
    }
  });

  return <div>Session: {connection.sessionId}</div>;
}
```

## Error Handling

### Error Types

The hook provides comprehensive error handling for various scenarios:

```typescript
interface ConnectionError {
  type: 'connection' | 'authentication' | 'session' | 'network' | 'system';
  message: string;
  details?: any;
  timestamp: string;
}
```

### Error Handling Strategies

```typescript
function ErrorHandlingExample() {
  const connection = useGameConnection({
    playerId: 'test_player',
    authToken: 'auth_token',

    onError: (error) => {
      console.error('Connection error:', error);

      switch (error.type) {
        case 'connection':
          // Handle connection-specific errors
          console.log('Connection error - attempting reconnection');
          setTimeout(() => connection.connect(), 5000);
          break;

        case 'authentication':
          // Handle authentication errors
          console.log('Authentication error - redirect to login');
          // Redirect to login page
          break;

        case 'session':
          // Handle session errors
          console.log('Session error - creating new session');
          connection.createNewSession();
          break;

        case 'network':
          // Handle network errors
          console.log('Network error - retrying connection');
          setTimeout(() => connection.connect(), 10000);
          break;

        default:
          console.log('Unknown error type:', error.type);
      }
    }
  });

  return (
    <div>
      {connection.error && (
        <div className="error-message">
          Error: {connection.error}
        </div>
      )}
    </div>
  );
}
```

### Automatic Error Recovery

```typescript
function AutomaticRecoveryExample() {
  const connection = useGameConnection({
    playerId: 'test_player',
    authToken: 'auth_token',

    // Enable automatic reconnection
    autoReconnect: true,
    reconnectInterval: 5000,
    maxReconnectAttempts: 10,

    onError: (error) => {
      // Log error for monitoring
      console.error('Connection error:', error);
    }
  });

  return <div>Connection: {connection.isConnected ? 'Connected' : 'Disconnected'}</div>;
}
```

## Performance Monitoring

### Connection Health Monitoring

```typescript
function HealthMonitoringExample() {
  const connection = useGameConnection({
    playerId: 'test_player',
    authToken: 'auth_token',

    onConnectionHealthUpdate: (health, metadata) => {
      console.log('Health update:', health);
      console.log('Metadata:', metadata);

      // Update UI based on health status
      if (health === 'unhealthy') {
        // Show warning to user
        // Attempt to recover connection
      }
    }
  });

  const getConnectionInfo = () => {
    const info = connection.getConnectionInfo();
    console.log('Connection info:', info);
  };

  return (
    <div>
      <h3>Connection Health</h3>
      <p>Status: {connection.connectionHealth}</p>
      <button onClick={getConnectionInfo}>
        Get Connection Info
      </button>
    </div>
  );
}
```

### Performance Metrics

```typescript
function PerformanceMetricsExample() {
  const connection = useGameConnection({
    playerId: 'test_player',
    authToken: 'auth_token'
  });

  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const response = await fetch('/monitoring/performance');
        const data = await response.json();
        setMetrics(data);
      } catch (error) {
        console.error('Failed to fetch metrics:', error);
      }
    }, 30000); // Update every 30 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h3>Performance Metrics</h3>
      {metrics && (
        <div>
          <p>Total Connections: {metrics.connection_establishment.total_connections}</p>
          <p>Avg WebSocket Time: {metrics.connection_establishment.avg_websocket_establishment_ms}ms</p>
          <p>Avg SSE Time: {metrics.connection_establishment.avg_sse_establishment_ms}ms</p>
        </div>
      )}
    </div>
  );
}
```

## Best Practices

### Connection Management

1. **Initialize connections early**: Establish connections when the component mounts
2. **Handle connection states**: Always check connection state before sending messages
3. **Implement reconnection logic**: Handle network interruptions gracefully
4. **Monitor connection health**: Use health callbacks to detect issues early

### Session Management

1. **Create sessions appropriately**: Use new sessions for new game instances
2. **Handle session changes**: Implement callbacks for session transitions
3. **Clean up old sessions**: Prevent resource leaks by cleaning up unused sessions
4. **Validate session state**: Check session validity before critical operations

### Error Handling

1. **Implement comprehensive error handling**: Handle all error types appropriately
2. **Provide user feedback**: Inform users of connection issues
3. **Log errors for debugging**: Use proper logging for troubleshooting
4. **Implement retry logic**: Automatically retry failed operations

### Performance Optimization

1. **Limit connection attempts**: Prevent excessive connection attempts
2. **Monitor performance metrics**: Track connection performance
3. **Implement connection pooling**: Reuse connections when possible
4. **Use health checks**: Regular health monitoring for early issue detection

## Examples

### Complete Game Component

```typescript
import React, { useEffect, useState } from 'react';
import { useGameConnection } from './hooks/useGameConnection';

interface GameComponentProps {
  playerId: string;
  authToken: string;
}

function GameComponent({ playerId, authToken }: GameComponentProps) {
  const [messages, setMessages] = useState<string[]>([]);
  const [inputValue, setInputValue] = useState('');

  const connection = useGameConnection({
    playerId,
    authToken,

    onMessage: (message) => {
      setMessages(prev => [...prev, message.content]);
    },

    onSessionChange: (newSessionId) => {
      console.log('New session:', newSessionId);
      setMessages([]); // Clear messages for new session
    },

    onConnectionHealthUpdate: (health) => {
      if (health === 'unhealthy') {
        console.warn('Connection health degraded');
      }
    },

    onError: (error) => {
      console.error('Connection error:', error);
      // Implement error recovery
    }
  });

  // Auto-connect on mount
  useEffect(() => {
    if (!connection.isConnected && !connection.isConnecting) {
      connection.connect();
    }
  }, []);

  const sendMessage = async () => {
    if (inputValue.trim() && connection.isConnected) {
      try {
        await connection.sendCommand(inputValue);
        setInputValue('');
      } catch (error) {
        console.error('Failed to send message:', error);
      }
    }
  };

  const startNewGame = async () => {
    try {
      await connection.createNewSession();
    } catch (error) {
      console.error('Failed to start new game:', error);
    }
  };

  return (
    <div className="game-component">
      <div className="connection-status">
        <h3>Connection Status</h3>
        <p>Overall: {connection.isConnected ? 'Connected' : 'Disconnected'}</p>
        <p>WebSocket: {connection.websocketConnected ? 'Connected' : 'Disconnected'}</p>
        <p>SSE: {connection.sseConnected ? 'Connected' : 'Disconnected'}</p>
        <p>Session: {connection.sessionId}</p>
        <p>Health: {connection.connectionHealth}</p>
      </div>

      <div className="game-actions">
        <button onClick={startNewGame} disabled={connection.isConnecting}>
          New Game
        </button>
        <button onClick={connection.disconnect} disabled={!connection.isConnected}>
          Disconnect
        </button>
      </div>

      <div className="game-messages">
        <h3>Game Messages</h3>
        <div className="message-list">
          {messages.map((message, index) => (
            <div key={index} className="message">
              {message}
            </div>
          ))}
        </div>
      </div>

      <div className="message-input">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          disabled={!connection.isConnected}
          placeholder="Enter command..."
        />
        <button onClick={sendMessage} disabled={!connection.isConnected || !inputValue.trim()}>
          Send
        </button>
      </div>

      {connection.error && (
        <div className="error-message">
          Error: {connection.error}
        </div>
      )}
    </div>
  );
}

export default GameComponent;
```

### Connection Monitoring Dashboard

```typescript
import React, { useEffect, useState } from 'react';
import { useGameConnection } from './hooks/useGameConnection';

function ConnectionDashboard() {
  const [stats, setStats] = useState(null);

  const connection = useGameConnection({
    playerId: 'monitor_player',
    authToken: 'monitor_token'
  });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await fetch('/monitoring/dual-connections');
        const data = await response.json();
        setStats(data);
      } catch (error) {
        console.error('Failed to fetch stats:', error);
      }
    };

    fetchStats();
    const interval = setInterval(fetchStats, 10000); // Update every 10 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="connection-dashboard">
      <h2>Connection Dashboard</h2>

      <div className="connection-overview">
        <h3>Connection Overview</h3>
        <p>Status: {connection.isConnected ? 'Connected' : 'Disconnected'}</p>
        <p>Health: {connection.connectionHealth}</p>
        <p>Session: {connection.sessionId}</p>
      </div>

      {stats && (
        <div className="system-stats">
          <h3>System Statistics</h3>
          <div className="stats-grid">
            <div className="stat-item">
              <h4>Total Players</h4>
              <p>{stats.connection_distribution.total_players}</p>
            </div>
            <div className="stat-item">
              <h4>Dual Connections</h4>
              <p>{stats.connection_distribution.dual_connection_players}</p>
            </div>
            <div className="stat-item">
              <h4>Health Percentage</h4>
              <p>{stats.connection_health.health_percentage}%</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default ConnectionDashboard;
```

## Troubleshooting

### Common Issues

1. **Connection Not Establishing**

   - Check network connectivity
   - Verify server status
   - Validate authentication token
   - Check browser console for errors

2. **Messages Not Received**

   - Verify connection state
   - Check message handlers
   - Review server logs
   - Test with different connection types

3. **Session Management Issues**

   - Ensure session ID format is correct
   - Check session validation logic
   - Verify session cleanup
   - Review session callbacks

4. **Performance Issues**

   - Monitor connection health
   - Check for connection leaks
   - Review message frequency
   - Analyze network conditions

### Debugging Tools

```typescript
// Enable debug logging
const connection = useGameConnection({
  playerId: 'test_player',
  authToken: 'auth_token',
  debug: true, // Enable debug logging
});

// Get detailed connection info
const connectionInfo = connection.getConnectionInfo();
console.log('Connection info:', connectionInfo);

// Monitor connection health
connection.onConnectionHealthUpdate = (health, metadata) => {
  console.log('Health update:', { health, metadata });
};
```

### Performance Monitoring

```typescript
// Monitor connection performance
useEffect(() => {
  const startTime = Date.now();

  const handleConnect = () => {
    const connectionTime = Date.now() - startTime;
    console.log(`Connection established in ${connectionTime}ms`);
  };

  connection.onConnect = handleConnect;
}, []);
```

## Support

For technical support or questions about the client integration:

1. Check the browser console for error messages
2. Review the connection state and health
3. Test with different connection configurations
4. Consult the server logs for additional context
5. Contact the development team for advanced issues

---

*This guide is maintained as part of the MythosMUD dual connection system implementation. Last updated: 2025-01-06*
