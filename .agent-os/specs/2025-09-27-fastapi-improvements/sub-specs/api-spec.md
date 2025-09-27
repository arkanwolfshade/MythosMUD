# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-09-27-fastapi-improvements/spec.md

## Endpoints

### No New Endpoints

**Purpose:** This specification focuses on improving existing endpoints rather than adding new ones
**Changes:** All existing endpoints will maintain their current API contracts while improving internal implementation
**Security:** All endpoints will receive enhanced security headers and improved error handling

## Middleware Changes

### Security Headers Middleware

**Purpose:** Add comprehensive security headers to all HTTP responses
**Implementation:** Custom middleware class that adds security headers to response objects
**Headers Added:**
- Strict-Transport-Security: max-age=31536000; includeSubDomains
- X-Frame-Options: DENY
- X-Content-Type-Options: nosniff
- Referrer-Policy: strict-origin-when-cross-origin
- Content-Security-Policy: default-src 'self'

### CORS Middleware Updates

**Purpose:** Replace permissive CORS configuration with secure, environment-based settings
**Current Configuration:**
```python
allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"]
allow_methods=["*"]
allow_headers=["*"]
```
**New Configuration:**
```python
allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
allow_methods=["GET", "POST", "PUT", "DELETE"]
allow_headers=["Authorization", "Content-Type"]
```

## Service Layer Integration

### Dependency Injection Updates

**Purpose:** Replace direct database access with proper service layer dependency injection
**Current Pattern:**
```python
@player_router.post("/{player_id}/heal")
def heal_player(player_id: str, amount: int, request: Request = None):
    persistence = request.app.state.persistence  # Direct access
    player = persistence.get_player(player_id)   # Business logic in route
```

**New Pattern:**
```python
@player_router.post("/{player_id}/heal")
async def heal_player(
    player_id: str,
    amount: int,
    player_service: PlayerService = Depends(get_player_service)
):
    return await player_service.heal_player(player_id, amount)
```

## Error Handling

### LoggedHTTPException Preservation

**Purpose:** Maintain existing comprehensive error handling while fixing middleware issues
**Changes:** Remove duplicate ErrorLoggingMiddleware registration while preserving error logging functionality
**Implementation:** Consolidate error logging into single ComprehensiveLoggingMiddleware

## Performance Improvements

### Async Route Handlers

**Purpose:** Ensure all I/O operations are non-blocking
**Changes:** Convert synchronous route handlers to async where database operations occur
**Implementation:** Use async/await patterns for all persistence layer interactions
