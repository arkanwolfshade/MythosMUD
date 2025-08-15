# 🗺️ MythosMUD – Planning Document

This document outlines the vision, high-level architecture, technology stack, and required tools for the MythosMUD project.
If a decision is pending, it is marked as **TODO**.

---

## Vision

- Build a browser-accessible, text-based Multi-User Dungeon (MUD) inspired by the Cthulhu Mythos.
- Focus on collaborative storytelling, exploration, and light horror combat.
- Make the codebase beginner-friendly for contributors and maintainers.
- Support persistent multiplayer gameplay with real-time interactions.
- Prioritize modularity, readability, and extensibility.

---

## Architecture

### High-Level Overview

- **Client (Front-End):**
  - Web-based terminal interface for text commands and output.
  - Features: command history, triggers, aliases, highlighting, ASCII navigation map.
  - Communicates with the server via WebSockets or similar real-time protocol.

- **Server (Back-End):**
  - Real-time, tick-based event loop.
  - Handles game logic, world state, combat, chat, and persistence.
  - Modular design for rooms, NPCs, combat, sanity, quests, etc.
  - Exposes APIs for client communication and admin tools.

- **Persistence Layer:**
  - Stores character data, world state, inventory, quest progress, and sanity.
  - Database choice: **SQLite for MVP, PostgreSQL or AWS DynamoDB preferred for production**.

- **Hosting/Deployment:**
  - Cloud-based, cost-optimized (AWS preferred).
  - SSL/TLS for secure connections.
  - Invite-only authentication.

---

## Technology Stack

| Layer         | Technology (Preferred)         | Status   |
|---------------|-------------------------------|----------|
| Front-End     | React + TypeScript            | ✅ Implemented |
| Terminal UI   | xterm.js or similar           | ✅ Implemented |
| Back-End      | Python (FastAPI, Starlette)   | ✅ Implemented |
| Real-Time     | WebSockets                    | ✅ Implemented |
| Database      | SQLite (MVP), PostgreSQL or DynamoDB | ✅ SQLite Implemented |
| Hosting       | AWS EC2/Fargate, RDS/DynamoDB | TODO     |
| Static Assets | S3/CloudFront (if needed)     | TODO     |
| Auth          | Custom invite-only system     | ✅ Implemented |
| CI/CD         | GitHub Actions (optional)     | TODO     |

---

## Required Tools

- **Development**
  - Node.js & npm/yarn (for front-end and possibly back-end)
  - Python 3.x (if using Python back-end)
  - PostgreSQL or DynamoDB local emulator
  - Git & GitHub
  - VSCode or preferred code editor

- **Testing**
  - Jest (front-end/unit tests) **TODO**
  - Pytest or equivalent (if Python back-end) **✅ Implemented**
  - Cypress or Playwright (end-to-end tests) **TODO**

- **Deployment**
  - AWS CLI & SDKs
  - Docker (for local dev and deployment) **TODO**
  - Terraform or AWS CDK (for infrastructure as code) **TODO**

- **Documentation**
  - Markdown editors
  - Diagrams.net or similar for architecture diagrams **TODO**

---

## Recent Completed Work (Latest Session)

### Core Infrastructure ✅

- WebSocket real-time communication system
- Client terminal interface with React + TypeScript
- Basic command parser and handler (look, go, say, help)
- Room navigation and movement system
- Player authentication and session management
- SQLite database integration with proper schema management
- Comprehensive logging system with log rotation
- Room pathing validator utility

### Game Systems ✅

- Alias system for command shortcuts
- Help system with comprehensive command documentation
- Player connection handling with username integration
- Real-time room updates and player movement
- Basic inventory and stats commands
- Security improvements and automated testing

### User Management System ✅ (NEW - 2025-08-15)

- **Comprehensive Mute System**: Personal and global muting capabilities
- **Admin System**: Database-based admin privileges and persistence
- **Mute Commands**: `mute`, `unmute`, `mutes` commands with privacy protection
- **Server-Side Filtering**: Real-time message filtering based on mute status
- **JSON Persistence**: Individual player mute data stored in JSON files
- **Privacy Protection**: Players cannot see who has muted them
- **Real-Time Testing**: Verified with Playwright MCP using three players
- **Code Quality**: All linting issues resolved, comprehensive test coverage

### Development Tools ✅

- Enhanced testing infrastructure with mock persistence layer
- Development startup scripts (start/stop server)
- Pre-commit hooks with ruff linting
- Code coverage requirements (80% target)
- Room hierarchy validation and testing

---

## Current Status

**MVP Core Functionality: COMPLETE** ✅

The basic MUD functionality is now working:

- Server starts without errors
- Client connects to server via WebSocket
- Players can authenticate and create/load characters
- Room navigation works (look, go north/south/east/west)
- Real-time updates show room changes
- Basic MUD interface is functional
- Alias system allows command shortcuts
- Help system provides comprehensive documentation

**Ready for limited invite-only launch testing**

---

## 🏛️ Comprehensive Codebase Analysis

*As noted in the Pnakotic Manuscripts, a thorough examination of our eldritch artifacts has revealed both strengths and areas requiring immediate attention.*

### **Architectural Assessment: 7.5/10** ✅

**Strengths:**
- Well-structured layered architecture with clear separation of concerns
- Excellent real-time communication design (SSE + WebSocket hybrid)
- Proper use of FastAPI dependency injection
- Good data persistence patterns with SQLAlchemy ORM
- Comprehensive test coverage (88% - exceeds 70% requirement)
- Thread-safe singleton pattern for persistence layer
- Event-driven architecture with proper pub/sub system

**Critical Issues:**
1. **Single Responsibility Principle Violations** - Large files with multiple responsibilities
2. **Security Vulnerabilities** - Hardcoded secrets and missing rate limiting
3. **Architectural Inconsistencies** - Mixed abstraction levels in API endpoints
4. **Performance Concerns** - Memory usage in EventBus and database connection pooling
5. **Code Quality Issues** - Some functions exceed complexity limits

### **Security Analysis**

**Critical Vulnerabilities:**
- Hardcoded secrets in `server/auth/users.py` (line 90)
- Missing rate limiting on authentication endpoints
- Overly permissive CORS configuration for production
- Authentication tokens logged in plain text

**Medium Risk Issues:**
- Error information disclosure in some endpoints
- Incomplete input sanitization
- Missing security headers (CSP, HSTS, X-Frame-Options)

### **Code Quality Metrics**

**Positive Indicators:**
- Test Coverage: 88% ✅ (Excellent)
- Line Length Compliance: 120 chars max ✅
- Good documentation and README files
- Proper logging implementation
- Comprehensive test suite (669 passed, 3 skipped)

**Areas for Improvement:**
- Some functions exceed recommended complexity limits
- Code duplication in player data conversion
- Long files (command_handler.py: 711 lines, persistence.py: 364 lines)
- Missing type hints in some functions

### **Technical Debt Assessment**

**Immediate Actions Required:**
1. **Security Hardening** - Move hardcoded secrets to environment variables
2. **Architecture Refactoring** - Split large files into focused modules
3. **Rate Limiting Implementation** - Add protection against abuse
4. **Error Handling Standardization** - Implement consistent patterns

**Short-term Improvements (1-2 weeks):**
1. **Service Layer Enhancement** - Create dedicated service classes
2. **API Consistency** - Standardize response formats and error handling
3. **Input Validation** - Enhance security validation patterns
4. **Performance Optimization** - Add database connection pooling

**Long-term Refactoring (1-2 months):**
1. **Microservices Preparation** - Prepare for future scaling
2. **Event Sourcing Implementation** - Use events for state changes
3. **CQRS Pattern** - Separate read/write operations
4. **Advanced Monitoring** - Implement comprehensive metrics

### **Complexity Hotspots**

**High Complexity Functions:**
- `command_handler.py` (711 lines) - Multiple responsibilities
- `persistence.py` (364 lines) - Too many responsibilities
- `main.py` - Mixed concerns (app creation + route definitions)

**Recommended Refactoring:**
- Split command_handler.py into focused modules (commands/, services/)
- Extract persistence logic into domain-specific repositories
- Create dedicated service layer for business logic
- Implement proper dependency injection patterns

### **Performance & Scalability Analysis**

**Current Performance Metrics:**
- **Test Coverage**: 88% ✅ (Excellent)
- **Code Quality**: Good with ruff linting
- **Database**: SQLite for MVP (appropriate)

**Scalability Concerns:**
1. **Memory Usage**: EventBus keeps all events in memory
2. **Database**: SQLite will become bottleneck with concurrent users
3. **Connection Management**: No connection pooling for database

**Recommended Improvements:**
1. Implement database connection pooling
2. Add Redis for session management
3. Consider PostgreSQL for production
4. Implement caching layer for room data

---

## Next Phase Priorities

### **Phase 1: Critical Fixes (Immediate - This Week)**
1. **Security Hardening** - Move remaining secrets to environment variables
2. **Architecture Refactoring** - Split large files into focused modules
3. **Rate Limiting Implementation** - Add protection against abuse
4. **Error Handling Standardization** - Implement consistent patterns

### **Phase 1.5: User Management System (COMPLETED)** ✅
*As noted in the restricted archives of Miskatonic University, the user management system has been successfully implemented and tested, providing comprehensive muting capabilities and admin privileges.*

#### **User Management System Status: 100% Complete** ✅
- ✅ **Player Muting**: Personal mute functionality (player A mutes player B)
- ✅ **Global Muting**: Admin-only global mute functionality
- ✅ **Mute Persistence**: JSON file-based persistence per player
- ✅ **Admin System**: Database-based admin status persistence
- ✅ **Mute Commands**: `mute`, `unmute`, `mutes` commands implemented
- ✅ **Privacy Protection**: Players cannot see who has muted them
- ✅ **Server-Side Filtering**: Messages filtered on server before client delivery
- ✅ **Real-Time Testing**: Verified with Playwright MCP using three players
- ✅ **Code Quality**: All linting issues resolved, tests passing

#### **Completed Features**

**Mute System:**
- Personal mutes: Player A can mute Player B (only affects Player A's view)
- Global mutes: Admins can globally mute players (affects all non-admin players)
- Mute persistence: Stored in individual JSON files per player
- Mute commands: `mute <player>`, `unmute <player>`, `mutes` (view own mutes)
- Privacy protection: Players cannot see if they are muted by others

**Admin System:**
- Admin status stored in database (`is_admin` field)
- Admin privileges for global muting
- Admin status persistence across sessions

**Testing & Quality:**
- Comprehensive Playwright MCP testing with three players
- All linting issues resolved (ruff compliance)
- Test coverage maintained at 80%+
- Real-time functionality verified end-to-end

#### **Technical Implementation**

**Key Components:**
- `UserManager`: Core service for mute management and persistence
- `ChatService`: Interface between commands and UserManager
- `NatsMessageHandler`: Server-side message filtering
- JSON file persistence: Individual files per player for mute data
- Database integration: Admin status in players table

**Message Flow:**
```
1. Player A sends: "say Hello everyone!"
2. Server processes command → Creates ChatMessage
3. Server filters message based on mute status
4. Message sent only to unmuted players in room
5. Players receive filtered messages via WebSocket
```

#### **Testing Results (2025-08-15)**

**Three-Player Test Scenario:**
- **Players**: ArkanWolfshade, Ithaqua, Azathoth
- **Test**: ArkanWolfshade mutes Ithaqua, verifies Azathoth can still see Ithaqua's messages
- **Results**: ✅ All functionality working correctly
- **Mute/Unmute**: ✅ Successfully tested and verified
- **Privacy**: ✅ Players cannot see who has muted them
- **Real-time**: ✅ Messages filtered correctly in real-time



### **Phase 2: Code Quality (1-2 Weeks)**
1. **Service Layer Enhancement** - Create dedicated service classes
2. **API Consistency** - Standardize response formats and error handling
3. **Input Validation** - Enhance security validation patterns
4. **Performance Optimization** - Add database connection pooling

### **Phase 3: Feature Development (1-2 Months)**
1. **Content Creation** - Add more hand-authored zones and content
2. **Admin Tools** - Implement admin/moderator commands and tools
3. **UI/UX Polish** - Improve accessibility and user experience
4. **Performance** - Optimize for scalability
5. **Advanced Systems** - Implement magic/spellcasting, combat, death mechanics

---

## Task Tracking

All development tasks and priorities are now tracked through [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues). This provides better collaboration, tracking, and integration with GitHub's project management features.

For current development priorities and task status, please refer to the [Issues page](https://github.com/arkanwolfshade/MythosMUD/issues).

---

## 🎯 Long-Term Architectural Vision

### **Target Architecture**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Client Layer  │    │   API Gateway   │    │  Service Layer  │
│   (React/TS)    │◄──►│   (FastAPI)     │◄──►│  (Game Services)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │  Event Bus      │    │  Data Layer     │
                       │  (Redis/PubSub) │    │  (PostgreSQL)   │
                       └─────────────────┘    └─────────────────┘
```

### **Key Principles**
1. **Domain-Driven Design** - Organize by game domains
2. **Event Sourcing** - Use events for state changes
3. **CQRS Pattern** - Separate read/write operations
4. **Microservices Ready** - Prepare for future scaling

---

_This document will be updated as decisions are made and the project evolves._
