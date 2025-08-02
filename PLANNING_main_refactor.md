# Main.py Refactoring Plan

## Overview

The current `main.py` file has grown to 547 lines and handles multiple responsibilities, making it difficult to maintain and test. This document outlines a comprehensive refactoring plan to break it into logically grouped, focused modules.

## Current Issues

### 1. Mixed Responsibilities

- Application setup and configuration
- Logging configuration
- API route definitions
- Real-time communication handling
- Player management logic
- Game mechanics (sanity, fear, corruption)
- Authentication and authorization

### 2. Code Quality Issues

- **547 lines** in a single file
- Repeated player conversion logic
- Hard to test individual components
- Poor separation of concerns
- Difficult to navigate and understand

### 3. Maintenance Challenges

- Changes to one feature affect others
- Debugging requires understanding entire file
- New developers struggle to find relevant code
- Testing requires mocking large dependencies

## Proposed Architecture

### Directory Structure

```
server/
├── app/                    # Application setup and configuration
│   ├── __init__.py
│   ├── factory.py         # FastAPI app creation
│   ├── lifespan.py        # Application lifecycle
│   └── logging.py         # Logging configuration
├── api/                   # API route definitions
│   ├── __init__.py
│   ├── base.py           # Base router and dependencies
│   ├── players.py        # Player management endpoints
│   ├── game.py           # Game mechanics endpoints
│   ├── real_time.py      # WebSocket and SSE endpoints
│   └── rooms.py          # Room-related endpoints
├── game/                  # Game business logic
│   ├── __init__.py
│   ├── mechanics.py      # Sanity, fear, corruption logic
│   ├── player_service.py # Player business operations
│   └── room_service.py   # Room-related operations
├── realtime/             # Real-time communication
│   ├── __init__.py
│   ├── connection_manager.py # Connection management
│   ├── websocket_handler.py # WebSocket handling
│   └── sse_handler.py    # Server-Sent Events
├── utils/                # Utility functions
│   ├── __init__.py
│   ├── player_converter.py # Player model conversion
│   ├── authentication.py # Auth utilities
│   └── validation.py     # Input validation
└── main.py              # Simplified entry point
```

## Detailed Refactoring Plan

### Phase 1: Application Setup Extraction

#### 1.1 Create `app/logging.py`

**Responsibilities:**

- Logging configuration setup
- Log file rotation logic
- Uvicorn logging configuration

**Current Code to Move:**

```python
def setup_logging():
    """Setup logging configuration for the server."""
    # ... (lines 35-75)
```

#### 1.2 Create `app/lifespan.py`

**Responsibilities:**

- Application startup logic
- Application shutdown logic
- Game tick loop initialization

**Current Code to Move:**

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # ... (lines 95-105)

async def game_tick_loop(app: FastAPI):
    # ... (lines 125-140)
```

#### 1.3 Create `app/factory.py`

**Responsibilities:**

- FastAPI app creation
- Middleware configuration
- Router registration
- CORS setup

**Current Code to Move:**

```python
app = FastAPI(...)
app.add_middleware(CORSMiddleware, ...)
app.include_router(auth_router)
app.include_router(command_router)
```

### Phase 2: API Route Extraction

#### 2.1 Create `api/base.py`

**Responsibilities:**

- Common dependencies
- Base router setup
- Shared utilities for API endpoints

#### 2.2 Create `api/players.py`

**Responsibilities:**

- Player CRUD operations
- Player statistics endpoints

**Endpoints to Move:**

- `POST /players` - Create player
- `GET /players` - List players
- `GET /players/{player_id}` - Get player by ID
- `GET /players/name/{player_name}` - Get player by name
- `DELETE /players/{player_id}` - Delete player

#### 2.3 Create `api/game.py`

**Responsibilities:**

- Game mechanics endpoints
- Player status modifications

**Endpoints to Move:**

- `POST /players/{player_id}/sanity-loss`
- `POST /players/{player_id}/fear`
- `POST /players/{player_id}/corruption`
- `POST /players/{player_id}/occult-knowledge`
- `POST /players/{player_id}/heal`
- `POST /players/{player_id}/damage`

#### 2.4 Create `api/real_time.py`

**Responsibilities:**

- WebSocket endpoints
- Server-Sent Events endpoints
- Real-time communication setup

**Endpoints to Move:**

- `GET /events/{player_id}` - SSE stream
- `WebSocket /ws/{player_id}` - WebSocket connection

#### 2.5 Create `api/rooms.py`

**Responsibilities:**

- Room-related endpoints

**Endpoints to Move:**

- `GET /rooms/{room_id}` - Get room information

### Phase 3: Business Logic Extraction

#### 3.1 Create `game/player_service.py`

**Responsibilities:**

- Player business logic
- Player validation
- Player state management

**Functions to Extract:**

- Player creation logic
- Player retrieval logic
- Player deletion logic
- Player statistics management

#### 3.2 Create `game/mechanics.py`

**Responsibilities:**

- Game mechanics implementation
- Sanity, fear, corruption calculations
- Healing and damage logic

**Functions to Extract:**

- `apply_sanity_loss()`
- `apply_fear()`
- `apply_corruption()`
- `gain_occult_knowledge()`
- `heal_player()`
- `damage_player()`

#### 3.3 Create `game/room_service.py`

**Responsibilities:**

- Room-related business logic
- Room validation
- Room state management

### Phase 4: Real-time Communication Refactoring

#### 4.1 Refactor `realtime/connection_manager.py`

**Responsibilities:**

- Connection management (extract from current `real_time.py`)
- WebSocket connection tracking
- SSE connection tracking
- Rate limiting

#### 4.2 Create `realtime/websocket_handler.py`

**Responsibilities:**

- WebSocket message handling
- Command processing
- Real-time updates

#### 4.3 Create `realtime/sse_handler.py`

**Responsibilities:**

- Server-Sent Events handling
- Event streaming
- Connection management

### Phase 5: Utility Extraction

#### 5.1 Create `utils/player_converter.py`

**Responsibilities:**

- Convert between Player models and schemas
- Handle different player data formats

**Functions to Extract:**

```python
def convert_player_to_schema(player):
    # Repeated conversion logic from main.py
```

#### 5.2 Create `utils/authentication.py`

**Responsibilities:**

- Token validation
- User extraction from requests
- Authentication utilities

#### 5.3 Create `utils/validation.py`

**Responsibilities:**

- Input validation
- Command validation
- Data sanitization

## Implementation Strategy

### Step-by-Step Migration

#### Step 1: Create New Directory Structure

```bash
mkdir -p server/app server/api server/game server/realtime server/utils
touch server/app/__init__.py server/api/__init__.py server/game/__init__.py server/realtime/__init__.py server/utils/__init__.py
```

#### Step 2: Extract Application Setup

1. Move logging setup to `app/logging.py`
2. Move lifespan management to `app/lifespan.py`
3. Move app creation to `app/factory.py`
4. Update imports in `main.py`

#### Step 3: Extract API Routes

1. Create base router in `api/base.py`
2. Move player endpoints to `api/players.py`
3. Move game mechanics endpoints to `api/game.py`
4. Move real-time endpoints to `api/real_time.py`
5. Move room endpoints to `api/rooms.py`

#### Step 4: Extract Business Logic

1. Create player service in `game/player_service.py`
2. Create mechanics service in `game/mechanics.py`
3. Create room service in `game/room_service.py`
4. Update API routes to use services

#### Step 5: Extract Utilities

1. Create player converter in `utils/player_converter.py`
2. Create authentication utilities in `utils/authentication.py`
3. Create validation utilities in `utils/validation.py`

#### Step 6: Refactor Real-time Communication

1. Split `real_time.py` into focused modules
2. Move connection management to dedicated class
3. Separate WebSocket and SSE handling

#### Step 7: Update Main.py

1. Simplify `main.py` to only create and run the app
2. Remove all extracted code
3. Update imports to use new modules

### Testing Strategy

#### Unit Testing

- Test each extracted module independently
- Mock dependencies for isolated testing
- Ensure 80% code coverage maintained

#### Integration Testing

- Test API endpoints with new structure
- Verify real-time communication still works
- Test authentication flow

#### Regression Testing

- Run existing test suite
- Verify all functionality preserved
- Test performance characteristics

## Success Criteria

### Code Quality Metrics

- **File Size**: No file > 200 lines
- **Cyclomatic Complexity**: < 10 per function
- **Code Coverage**: Maintain 80% minimum
- **Import Dependencies**: Clear, logical dependencies

### Functionality Preservation

- All existing API endpoints work
- Real-time communication functions
- Authentication and authorization work
- Game mechanics function correctly
- Player management operations work

### Performance Requirements

- No performance degradation
- Same response times for API calls
- Real-time communication latency unchanged
- Memory usage similar to current implementation

## Risk Mitigation

### Potential Risks

1. **Breaking Changes**: Existing functionality might break
2. **Import Issues**: Circular imports or missing dependencies
3. **Testing Complexity**: More modules to test
4. **Performance Impact**: Additional function calls

### Mitigation Strategies

1. **Incremental Migration**: Move code piece by piece
2. **Comprehensive Testing**: Test each phase thoroughly
3. **Backup Strategy**: Keep original main.py until migration complete
4. **Rollback Plan**: Ability to revert if issues arise

## Timeline Estimate

### Phase 1: Application Setup (1-2 days)

- Create app/ directory structure
- Extract logging and lifespan management
- Update main.py imports

### Phase 2: API Routes (2-3 days)

- Create api/ directory structure
- Extract player endpoints
- Extract game mechanics endpoints
- Extract real-time endpoints
- Extract room endpoints

### Phase 3: Business Logic (2-3 days)

- Create game/ directory structure
- Extract player service
- Extract mechanics service
- Extract room service

### Phase 4: Real-time Communication (2-3 days)

- Refactor real_time.py
- Create focused realtime/ modules
- Update connection management

### Phase 5: Utilities (1-2 days)

- Create utils/ directory structure
- Extract player converter
- Extract authentication utilities
- Extract validation utilities

### Phase 6: Testing and Cleanup (2-3 days)

- Comprehensive testing
- Update documentation
- Clean up old code
- Performance verification

**Total Estimated Time: 10-16 days**

## Post-Refactoring Benefits

### Development Experience

- **Easier Navigation**: Related code grouped together
- **Faster Debugging**: Issues isolated to specific modules
- **Better Testing**: Smaller, focused modules easier to test
- **Improved Collaboration**: Multiple developers can work on different modules

### Code Quality

- **Single Responsibility**: Each module has one clear purpose
- **Reduced Coupling**: Modules depend only on what they need
- **Better Maintainability**: Changes affect only relevant modules
- **Enhanced Readability**: Clear structure and organization

### Future Development

- **Easier Feature Addition**: New features can be added to appropriate modules
- **Better Scalability**: Architecture supports growth
- **Improved Documentation**: Each module can be documented independently
- **Enhanced Reusability**: Utilities can be reused across modules

## Conclusion

This refactoring plan will transform the current monolithic `main.py` into a well-organized, maintainable codebase that follows FastAPI best practices and the project's academic theme. The new structure will make development more efficient and the codebase more sustainable for long-term growth.

The refactoring should be approached incrementally, with thorough testing at each phase to ensure no functionality is lost. The end result will be a much more maintainable and scalable codebase that better serves the MythosMUD project's needs.
