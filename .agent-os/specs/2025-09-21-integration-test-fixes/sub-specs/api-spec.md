# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-09-21-integration-test-fixes/spec.md

## Endpoints

### POST /auth/login

**Purpose:** Mock authentication endpoint for integration tests
**Parameters:**
- username (string): Test username
- password (string): Test password (ignored in mock)
**Response:**
```json
{
  "access_token": "test-token",
  "has_character": true,
  "character_name": "username",
  "refresh_token": "test-refresh-token"
}
```
**Errors:** None (always succeeds in mock)

### GET /motd

**Purpose:** Mock MOTD (Message of the Day) endpoint for integration tests
**Parameters:** None
**Response:**
```json
{
  "title": "Welcome to MythosMUD",
  "content": "Welcome to the realm of eldritch knowledge..."
}
```
**Errors:** None (always succeeds in mock)

### GET /api/game/state

**Purpose:** Mock initial game state endpoint for integration tests
**Parameters:** None
**Response:**
```json
{
  "player": {
    "name": "username",
    "current_room_id": "arkham_001"
  },
  "room": {
    "id": "arkham_001",
    "name": "Arkham Streets",
    "description": "Dark streets of Arkham",
    "zone": "arkham",
    "sub_zone": "downtown",
    "exits": {
      "north": "arkham_002",
      "south": "arkham_003"
    },
    "occupants": ["username"],
    "occupant_count": 1
  }
}
```
**Errors:** None (always succeeds in mock)

### POST /api/commands/move

**Purpose:** Mock movement command endpoint for integration tests
**Parameters:**
- direction (string): Movement direction (north, south, east, west)
**Response:**
```json
{
  "success": true,
  "message": "You move east",
  "new_room": {
    "id": "arkham_002",
    "name": "Arkham Library",
    "description": "Ancient library",
    "occupants": ["username"],
    "occupant_count": 1
  }
}
```
**Errors:** None (always succeeds in mock)

### POST /api/commands/say

**Purpose:** Mock chat command endpoint for integration tests
**Parameters:**
- message (string): Chat message content
**Response:**
```json
{
  "success": true,
  "message": "You say: Hello world"
}
```
**Errors:** None (always succeeds in mock)

### POST /api/commands/who

**Purpose:** Mock who command endpoint for integration tests
**Parameters:** None
**Response:**
```json
{
  "success": true,
  "players": [
    {
      "name": "Player1",
      "location": "Arkham Streets"
    },
    {
      "name": "Player2",
      "location": "Arkham Library"
    }
  ]
}
```
**Errors:** None (always succeeds in mock)

## Mock Implementation Strategy

### Route Interception
All API endpoints will be intercepted using Playwright's `page.route()` method to provide consistent mock responses:

```typescript
await page.route('**/auth/login', async route => {
  await route.fulfill({
    status: 200,
    contentType: 'application/json',
    body: JSON.stringify(mockLoginResponse)
  });
});
```

### Response Consistency
- All mock responses return HTTP 200 status
- Content-Type is always 'application/json'
- Response structure matches actual server responses
- No authentication required for mock endpoints

### Test Isolation
- Each test sets up its own mock routes
- Mock responses are isolated per test context
- No shared state between test runs
- Cleanup of routes after each test
