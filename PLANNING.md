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
