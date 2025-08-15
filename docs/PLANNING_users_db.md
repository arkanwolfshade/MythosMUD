# 🗺️ MythosMUD – FastAPI Users Migration Planning

## Overview

This document outlines the migration from our current custom invite-only authentication system to FastAPI Users with SQLite database authentication. This migration will provide a more robust, scalable authentication system while maintaining our existing functionality.

---

## Current State Analysis

### Existing Authentication System

- **File-based storage**: `users.json` and `invites.json`
- **Custom invite-only system**: Manual invite code validation
- **JWT tokens**: Custom token generation and validation
- **Player data**: Stored separately in individual JSON files
- **Security**: Recent path injection fixes implemented
- **Invite generation**: `generate_invites.py` utility for creating invite codes

### Current Dependencies

- `argon2-cffi` for password hashing
- `python-jose` for JWT handling
- `bcrypt` for password security
- Custom `auth_utils.py` and `security_utils.py`

---

## Migration Goals

### Primary Objectives

1. **Replace custom auth with FastAPI Users**
2. **Migrate to SQLite database for user storage**
3. **Maintain invite-only functionality**
4. **Preserve existing player data structure**
5. **Ensure backward compatibility during transition**
6. **Update invite generation utility for database storage**

### Success Criteria

- [ ] All existing authentication endpoints work
- [ ] Invite-only registration still functions
- [ ] New player system functions correctly
- [ ] Tests pass with new system
- [ ] Performance is maintained or improved
- [ ] Security is enhanced
- [ ] `generate_invites.py` utility works with database
- [ ] Test database mirrors production schema
- [ ] All test fixtures use new database structure

---

## Technical Architecture

### Database Schema Design

#### Users Table (FastAPI Users)

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_superuser BOOLEAN DEFAULT FALSE,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Invites Table (Custom Extension)

```sql
CREATE TABLE invites (
    id UUID PRIMARY KEY,
    invite_code VARCHAR(50) UNIQUE NOT NULL,
    created_by UUID REFERENCES users(id),
    used_by UUID REFERENCES users(id),
    is_used BOOLEAN DEFAULT FALSE,
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Players Table (Game Data)

```sql
CREATE TABLE players (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id) UNIQUE,
    name VARCHAR(50) UNIQUE NOT NULL,
    stats TEXT NOT NULL, -- JSON serialized as TEXT for SQLite
    inventory TEXT DEFAULT '[]', -- JSON serialized as TEXT for SQLite
    status_effects TEXT DEFAULT '[]', -- JSON serialized as TEXT for SQLite
    current_room_id VARCHAR(50) DEFAULT 'arkham_001',
    experience_points INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### File Structure Changes

```
server/
├── database.py          # NEW: Database configuration and session management
├── models/
│   ├── __init__.py
│   ├── user.py          # NEW: FastAPI Users user model
│   ├── player.py        # REFACTORED: Player model with database fields
│   └── invite.py        # NEW: Invite model
├── schemas/
│   ├── __init__.py
│   ├── user.py          # NEW: User Pydantic schemas
│   ├── player.py        # REFACTORED: Player schemas
│   └── invite.py        # NEW: Invite schemas
├── auth/
│   ├── __init__.py
│   ├── users.py         # NEW: FastAPI Users configuration
│   ├── invites.py       # NEW: Invite management
│   └── dependencies.py  # NEW: Authentication dependencies
├── migrations/          # NEW: Alembic migrations
│   ├── versions/
│   └── alembic.ini
├── generate_invites.py  # UPDATED: Database-based invite generation
└── auth.py              # DEPRECATED: Will be replaced by auth/ module

server/tests/
├── data/
│   ├── test_users.db    # NEW: Test database with users, players, invites tables
│   ├── test_players.db  # UPDATED: Test database with new schema
│   └── test_persistence.log
├── init_test_db.py      # UPDATED: Initialize test database with new schema
├── verify_test_db.py    # UPDATED: Verify test database structure
└── test_auth.py         # UPDATED: Test new authentication system
```

---

## Implementation Plan

### Phase 1: Database Setup and Models (1-2 hours)

1. **Install new dependencies**
   - FastAPI Users
   - SQLAlchemy
   - aiosqlite
   - Alembic

2. **Create database configuration**
   - Database connection setup
   - Session management
   - Migration configuration

3. **Define database models**
   - User model (FastAPI Users)
   - Player model (refactored)
   - Invite model (custom)

4. **Create Pydantic schemas**
   - User schemas
   - Player schemas
   - Invite schemas

5. **Update test infrastructure**
   - Create test database with new schema (`test_users.db`)
   - Update `init_test_db.py` for new tables (users, players, invites)
   - Update `verify_test_db.py` for schema validation
   - Update test fixtures to use new database structure
   - Ensure test data isolation from production

### Phase 2: FastAPI Users Integration (2-3 hours)

1. **Configure FastAPI Users**
   - User model configuration
   - Authentication backend setup
   - Password hashing configuration

2. **Create authentication endpoints**
   - Register endpoint (with invite validation)
   - Login endpoint
   - User management endpoints

3. **Implement invite system**
   - Invite creation and validation
   - Registration with invite requirement
   - Invite tracking and cleanup

### Phase 3: Player Data Migration (1-2 hours)

1. **Drop and recreate players table**
   - Drop existing players table
   - Create new table with updated schema
   - No data migration needed

2. **Update player management**
   - Database-based player operations
   - Maintain existing API compatibility
   - Update persistence layer

3. **Test new player system**
   - Test player creation and management
   - Test existing functionality
   - Performance validation

### Phase 4: Integration and Testing (1-2 hours)

1. **Update existing endpoints**
   - Replace auth dependencies
   - Update WebSocket authentication
   - Maintain API compatibility

2. **Update utility scripts**
   - **Update `generate_invites.py`** for database storage
   - Create database-based invite management
   - Maintain CLI interface compatibility

3. **Comprehensive testing**
   - Unit tests for new auth system
   - Integration tests for full flow
   - Performance testing
   - Test database schema validation
   - Test data isolation verification

4. **Documentation updates**
   - Update API documentation
   - Migration guides
   - Development setup instructions
   - Test infrastructure documentation

---

## Migration Strategy

### Data Migration Approach

1. **Drop and recreate players table**: No existing data migration needed
2. **Switchover**: Update all endpoints to use new system
3. **Cleanup**: Remove old file-based storage

### Implementation Strategy

- Drop existing players table and recreate with new schema
- No rollback procedures needed - clean slate approach
- Feature flags for gradual rollout of new authentication system
- Keep existing `auth.py` as backup during transition

### Testing Strategy

- **Unit tests**: New auth components
- **Integration tests**: Full authentication flow
- **Security tests**: Authentication and authorization testing
- **Performance tests**: Database query optimization
- **Test database setup**: Mirror production schema in test environment
- **Test data isolation**: Ensure tests use separate test database
- **Schema validation tests**: Verify database schema matches requirements

---

## Security Considerations

### Enhanced Security Features

- **Database-level constraints**: Unique constraints, foreign keys
- **SQL injection prevention**: Parameterized queries
- **Password security**: Enhanced hashing with FastAPI Users
- **Session management**: Improved token handling
- **Audit logging**: Database-based activity tracking

### Security Audit Requirements

- **Pre-migration security review**: Audit new authentication system
- **Penetration testing**: Test for common vulnerabilities
- **Input validation testing**: Verify all user inputs are properly validated
- **Token security testing**: Validate JWT token handling
- **Database security testing**: Test SQL injection prevention
- **API security testing**: Verify rate limiting and CORS configuration

---

## Performance Considerations

### Database Optimization

- **Indexing**: Proper indexes on frequently queried fields
- **Connection pooling**: Efficient database connections
- **Query optimization**: Minimize N+1 queries
- **Caching**: Redis integration for future scalability

### System Performance

- **Connection pooling**: Efficient database connections
- **Query optimization**: Minimize N+1 queries
- **Resource management**: Memory and CPU optimization

---

## Dependencies and Configuration

### New Dependencies

```toml
fastapi-users[sqlalchemy]==12.1.3
sqlalchemy==2.0.27
aiosqlite==0.20.0
alembic==1.13.1
```

### Configuration Changes

- **Database URL**: SQLite file path configuration
- **Migration settings**: Alembic configuration
- **Environment variables**: Database connection settings
- **Logging**: Database operation logging
- **Test configuration**: Separate test database setup
- **Test fixtures**: Updated to use new database schema

---

## Risk Assessment

### High Risk

- **Authentication downtime**: Mitigated by gradual rollout
- **Performance degradation**: Mitigated by testing and optimization

### Medium Risk

- **API compatibility issues**: Mitigated by comprehensive testing
- **Security vulnerabilities**: Mitigated by security review
- **System complexity**: Mitigated by phased approach

### Low Risk

- **Dependency conflicts**: Mitigated by version pinning
- **Configuration issues**: Mitigated by documentation

---

## Error Handling Strategy

### Database Connection Failures

- Implement connection pooling and retry logic
- Graceful degradation when database unavailable
- Comprehensive logging of database errors

### Authentication Service Outages

- Fallback authentication mechanism
- Token validation error handling
- User session management during outages

### Data Corruption Prevention

- Input validation on all database operations
- JSON serialization/deserialization error handling
- Data integrity checks on critical operations

### WebSocket Authentication Failures

- Graceful connection termination on auth failure
- Token refresh mechanism for long-running connections
- Reconnection logic with proper authentication

---

## Success Metrics

### Technical Metrics

- [ ] All tests pass (maintain 70%+ coverage)
- [ ] Authentication response time < 100ms
- [ ] Database query performance maintained
- [ ] New player system functions correctly

### Functional Metrics

- [ ] All existing features work unchanged
- [ ] Invite system functions correctly
- [ ] Player creation and management works
- [ ] Admin tools work with new system
- [ ] `generate_invites.py` utility works with database
- [ ] Test database contains all required tables
- [ ] Test fixtures properly isolate test data
- [ ] Schema validation tests pass

---

## Timeline Estimate

**Total Estimated Time: 5-9 hours**

- **Phase 1**: 1-2 hours (Database setup)
- **Phase 2**: 2-3 hours (FastAPI Users integration)
- **Phase 3**: 1-2 hours (Player system setup)
- **Phase 4**: 1-2 hours (Integration and testing)

**Recommended Approach**: Implement in phases with testing between each phase to ensure stability.

---

## Next Steps

1. **Review this plan** and provide feedback
2. **Approve dependencies** and configuration changes
3. **Begin Phase 1** implementation
4. **Regular check-ins** during development
5. **Comprehensive testing** before deployment
6. **Security audit** before production deployment

---

*This migration represents a significant step toward a more robust and scalable authentication system, worthy of the restricted archives of Miskatonic University's digital collections.*
