# SSE Authentication System

## Overview

The Server-Sent Events (SSE) authentication system provides secure, real-time communication for the MythosMUD game. This document describes the authentication mechanisms, security features, and implementation details.

## Architecture

### Authentication Flow

1. **Client Authentication**: Clients obtain JWT tokens through the `/auth/login` endpoint
2. **Token Validation**: SSE and WebSocket connections validate tokens before establishing connections
3. **Rate Limiting**: Connection attempts are rate-limited to prevent abuse
4. **Security Headers**: SSE responses include comprehensive security headers

### Components

- **Token Validation**: `validate_sse_token()` function in `auth.py`
- **Security Headers**: `get_sse_auth_headers()` function in `auth.py`
- **Rate Limiting**: Built into `ConnectionManager` class in `real_time.py`
- **SSE Endpoint**: `/events/{player_id}` with token validation
- **WebSocket Endpoint**: `/ws/{player_id}` with token validation

## Authentication Mechanisms

### JWT Token Validation

SSE and WebSocket connections require valid JWT tokens that can be provided in two ways:

1. **Query Parameter**: `?token=<jwt_token>`
2. **Authorization Header**: `Authorization: Bearer <jwt_token>`

```python
# Token validation example
def validate_sse_token(token: str, users_file: str = None) -> dict:
    """
    Validate JWT token for SSE and WebSocket connections.

    Args:
        token: The JWT token to validate
        users_file: Optional path to users file for additional validation

    Returns:
        dict: User information if token is valid

    Raises:
        HTTPException: If token is invalid, expired, or user not found
    """
```

### Security Features

#### Rate Limiting

- **Max Attempts**: 5 connection attempts per minute per player
- **Time Window**: 60 seconds
- **Per-Player**: Rate limits are tracked separately for each player
- **Automatic Reset**: Limits reset after the time window expires

```python
# Rate limiting configuration
self.max_connection_attempts = 5  # Max attempts per minute
self.connection_window = 60  # Time window in seconds
```

#### Security Headers

SSE responses include comprehensive security headers:

```python
def get_sse_auth_headers() -> dict:
    return {
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "X-XSS-Protection": "1; mode=block",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Content-Security-Policy": "default-src 'self'; script-src 'self' 'unsafe-inline'",
    }
```

## API Endpoints

### SSE Endpoint

**URL**: `GET /events/{player_id}`

**Authentication**: Required via token parameter or Authorization header

**Parameters**:
- `player_id` (path): The player ID to connect for
- `token` (query): JWT authentication token

**Headers**:
- `Accept: text/event-stream` (required)
- `Authorization: Bearer <token>` (alternative to query parameter)

**Response**:
- **200 OK**: Connection established, SSE stream begins
- **401 Unauthorized**: Invalid or missing token
- **403 Forbidden**: Token doesn't match player ID

**Example**:
```bash
curl -H "Accept: text/event-stream" \
     "http://localhost:54731/events/testuser?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
```

### WebSocket Endpoint

**URL**: `WS /ws/{player_id}`

**Authentication**: Required via token query parameter

**Parameters**:
- `player_id` (path): The player ID to connect for
- `token` (query): JWT authentication token

**Response**:
- **Connection Established**: Valid token and matching player ID
- **4001 Close Code**: Missing authentication token
- **4001 Close Code**: Invalid authentication token
- **4003 Close Code**: Token doesn't match player ID

**Example**:
```javascript
const ws = new WebSocket(
    `ws://localhost:54731/ws/testuser?token=${jwtToken}`
);
```

## Error Handling

### Authentication Errors

- **No Token**: Returns 401 with "Authentication token required"
- **Invalid Token**: Returns 401 with "Invalid authentication token"
- **Token Mismatch**: Returns 403 with "Access denied: token does not match player ID"

### Rate Limiting Errors

When rate limits are exceeded, SSE connections return an error event:

```json
{
    "event_type": "error",
    "sequence_number": 123,
    "player_id": "testuser",
    "data": {
        "error": "rate_limited",
        "message": "Too many connection attempts",
        "rate_limit_info": {
            "attempts": 5,
            "max_attempts": 5,
            "window_seconds": 60,
            "attempts_remaining": 0,
            "reset_time": 1640995200.0
        }
    }
}
```

## Testing

### Test Coverage

The SSE authentication system includes comprehensive tests:

- **Token Validation**: Tests for valid, invalid, and missing tokens
- **Security Headers**: Verification of all security headers
- **Rate Limiting**: Tests for rate limit enforcement and reset
- **Integration**: End-to-end authentication flow testing

### Running Tests

```bash
# Run all SSE authentication tests
python -m pytest tests/test_sse_auth.py -v

# Run specific test categories
python -m pytest tests/test_sse_auth.py::TestSSETokenValidation -v
python -m pytest tests/test_sse_auth.py::TestRateLimiting -v
python -m pytest tests/test_sse_auth.py::TestSSEEndpointAuthentication -v
```

## Security Considerations

### Token Security

- **Expiration**: JWT tokens expire after 60 minutes
- **Algorithm**: Uses HS256 for token signing
- **Secret Key**: Stored in environment variable `MYTHOSMUD_SECRET_KEY`
- **Validation**: Tokens are validated on every connection attempt

### Connection Security

- **HTTPS Required**: Production deployments should use HTTPS
- **CORS**: Configured for specific origins only
- **Rate Limiting**: Prevents connection flooding attacks
- **Security Headers**: Comprehensive protection against common attacks

### Best Practices

1. **Token Storage**: Store tokens securely on the client side
2. **Token Refresh**: Implement token refresh mechanisms for long-running sessions
3. **Error Handling**: Handle authentication errors gracefully
4. **Monitoring**: Monitor rate limiting and authentication failures
5. **Logging**: Log authentication events for security auditing

## Implementation Notes

### Dependencies

- **python-jose**: JWT token handling
- **passlib**: Password hashing and verification
- **bcrypt**: Password hashing algorithm
- **fastapi**: Web framework with WebSocket support

### Configuration

Key configuration values can be adjusted in the code:

```python
# In auth_utils.py
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"

# In real_time.py
self.max_connection_attempts = 5
self.connection_window = 60
```

### Future Enhancements

1. **Token Refresh**: Implement automatic token refresh for long sessions
2. **Session Management**: Add session tracking and management
3. **Advanced Rate Limiting**: Implement IP-based rate limiting
4. **Audit Logging**: Add comprehensive security audit logging
5. **Multi-Factor Authentication**: Support for additional authentication factors

## Troubleshooting

### Common Issues

1. **Token Expired**: Check token expiration time and implement refresh
2. **Rate Limited**: Wait for rate limit window to reset or reduce connection frequency
3. **CORS Errors**: Ensure proper CORS configuration for your domain
4. **WebSocket Connection Failed**: Verify token is provided in query parameter

### Debug Information

Enable debug logging to troubleshoot authentication issues:

```python
import logging
logging.getLogger('server.auth').setLevel(logging.DEBUG)
logging.getLogger('server.real_time').setLevel(logging.DEBUG)
```

## References

- [JWT RFC 7519](https://tools.ietf.org/html/rfc7519)
- [Server-Sent Events W3C Specification](https://www.w3.org/TR/eventsource/)
- [WebSocket RFC 6455](https://tools.ietf.org/html/rfc6455)
- [OWASP Security Headers](https://owasp.org/www-project-secure-headers/)
