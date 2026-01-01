# Backend APIs for Room Editor

Based on the frontend implementation in `client/src/components/map/utils/saveMapChanges.ts`, the following backend APIs need to be implemented to fully support the room editor functionality.

## Current Status

### Already Implemented

- `POST /api/rooms/{room_id}/position` - Updates room map coordinates (map_x, map_y)
  - Location: `server/api/rooms.py`
  - Status: ✅ Fully functional

### Missing APIs

## 1. Room Property Update API

**Endpoint**: `PUT /api/rooms/{room_id}`

**Purpose**: Update room properties (name, description, zone, sub_zone, environment) edited in the RoomEditModal.

**Request Body** (Pydantic model):

```python
class RoomUpdateRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    zone: str | None = None
    sub_zone: str | None = None
    environment: str | None = None
```

**Database Updates**:

- Update `rooms.name`
- Update `rooms.description`
- Update `rooms.attributes` JSONB field (for environment)
- Update zone/subzone (requires looking up subzone_id from zone/subzone names)

**Implementation Files**:

- `server/api/rooms.py` - Add new endpoint
- `server/persistence/repositories/room_repository.py` - Add async method to update room in database
- `server/game/room_service.py` - May need method to update room and invalidate cache

**Key Requirements**:

- Admin authentication required (similar to position update)
- Validate room exists
- Validate zone/subzone exist if provided
- Update database using SQLAlchemy async session
- Invalidate room cache after update
- Handle JSONB attributes field for environment

## 2. Exit/Edge Management APIs

**Purpose**: Create, update, and delete room exits (edges) that connect rooms on the map.

### 2a. Create Exit API

**Endpoint**: `POST /api/rooms/{room_id}/exits`

**Request Body**:

```python
class ExitCreateRequest(BaseModel):
    direction: str  # e.g., 'north', 'south', 'east', etc.
    target_room_id: str  # stable_id of target room
    flags: list[str] | None = None  # ['one_way', 'hidden', 'locked', 'self_reference']
    description: str | None = None  # Custom exit description
```

**Database Operations**:

- Insert into `room_links` table
- Convert room stable_ids to UUIDs (from_room_id, to_room_id)
- Store flags and description in `attributes` JSONB field
- Validate target room exists
- Enforce UNIQUE constraint (from_room_id, direction)

### 2b. Update Exit API

**Endpoint**: `PUT /api/rooms/{room_id}/exits/{direction}`

**Request Body**:

```python
class ExitUpdateRequest(BaseModel):
    target_room_id: str | None = None  # Can change target room
    flags: list[str] | None = None
    description: str | None = None
```

**Database Operations**:

- Update `room_links.to_room_id` if target_room_id provided
- Update `room_links.attributes` JSONB field (flags, description)
- Validate target room exists if provided

### 2c. Delete Exit API

**Endpoint**: `DELETE /api/rooms/{room_id}/exits/{direction}`

**Database Operations**:

- Delete from `room_links` table
- CASCADE delete will handle cleanup

**Implementation Files**:

- `server/api/rooms.py` - Add three new endpoints
- `server/persistence/repositories/room_repository.py` - Add methods for exit CRUD operations
- Consider creating a `RoomLinkRepository` or `ExitRepository` if logic becomes complex

**Key Requirements**:

- Admin authentication required
- Validate source and target rooms exist
- Convert stable_ids to UUIDs for database operations
- Handle JSONB attributes field for flags and description
- Invalidate room cache for both source and target rooms after changes
- Handle bidirectional exit relationships (create reverse exit if not one_way flag)
- Validate direction is valid (north, south, east, west, up, down, northeast, etc.)

## Database Schema Reference

From `db/schema/01_world_and_calendar.sql`:

**rooms table**:

- `id` (uuid, PK)
- `stable_id` (text, unique per subzone)
- `name` (text)
- `description` (text)
- `attributes` (jsonb) - stores environment and other metadata
- `subzone_id` (uuid, FK to subzones)
- `map_x`, `map_y` (float, nullable) - map coordinates

**room_links table**:

- `id` (uuid, PK)
- `from_room_id` (uuid, FK to rooms.id)
- `to_room_id` (uuid, FK to rooms.id)
- `direction` (text)
- `attributes` (jsonb) - stores flags and description
- UNIQUE constraint: (from_room_id, direction)

## Implementation Notes

1. **Authentication**: All endpoints should use `get_current_user` and admin permission checks similar to `_validate_room_position_update()` in `server/api/rooms.py`

2. **Error Handling**: Use `LoggedHTTPException` pattern from existing code

3. **Cache Invalidation**: After any room or exit update, invalidate the room cache using `room_service.room_cache.invalidate_room()`

4. **Transaction Management**: Use async database sessions with proper commit/rollback handling

5. **Room ID Conversion**: Need to convert between stable_id (string) used in frontend and UUID (database id) for database operations. This likely requires queries to `rooms` table using `stable_id`.

6. **Zone/Subzone Updates**: Changing zone or sub_zone requires updating `subzone_id` FK, which means looking up the subzone UUID from the zone/subzone names.

## Frontend Integration

The frontend is already calling these APIs (or will call them) through:

- `saveRoomUpdates()` in `client/src/components/map/utils/saveMapChanges.ts` - expects `PUT /api/rooms/{room_id}`
- `saveEdgeChanges()` in `client/src/components/map/utils/saveMapChanges.ts` - expects the exit CRUD endpoints

## Testing Considerations

- Unit tests for repository methods
- Integration tests for API endpoints
- Test admin authentication
- Test validation (non-existent rooms, invalid directions, etc.)
- Test cache invalidation
- Test JSONB attribute handling
