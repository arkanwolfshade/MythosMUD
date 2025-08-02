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

### **Architectural Assessment: 7/10**

**Strengths:**
- Well-structured layered architecture with clear separation of concerns
- Excellent real-time communication design (SSE + WebSocket hybrid)
- Proper use of FastAPI dependency injection
- Good data persistence patterns with SQLAlchemy ORM
- Comprehensive test coverage (78% - above 70% requirement)

**Critical Issues:**
1. **Database Schema Mismatch** - Tests failing due to missing columns (`user_id`, `used_by_user_id`)
2. **Hardcoded Secrets** - JWT secrets in source code (partially addressed)
3. **Authentication System Inconsistencies** - Multiple auth implementations causing conflicts
4. **Missing Error Handling** - Incomplete exception handling in real-time connections
5. **Configuration Management** - Environment-specific logic embedded in code

### **Security Analysis**

**Critical Vulnerabilities:**
- Hardcoded secrets in `server/auth/users.py` (partially addressed)
- Database schema inconsistencies causing test failures
- Input validation gaps in command processing
- Overly permissive CORS configuration for production

**Medium Risk Issues:**
- Missing rate limiting on authentication endpoints
- Error information disclosure in some endpoints
- Incomplete input sanitization

### **Code Quality Metrics**

**Positive Indicators:**
- Test Coverage: 78% ✅
- Line Length Compliance: 120 chars max ✅
- Good documentation and README files
- Proper logging implementation

**Areas for Improvement:**
- Some functions exceed recommended complexity limits
- Code duplication in player data conversion
- Long files (main.py: 524 lines, command_handler.py: 602 lines)
- Missing type hints in some functions

### **Technical Debt Assessment**

**Immediate Actions Required:**
1. Fix database schema alignment issues
2. Move remaining hardcoded secrets to environment variables
3. Resolve authentication system inconsistencies
4. Fix failing test suite

**Short-term Improvements (1-2 weeks):**
1. Refactor large files into smaller, focused modules
2. Implement comprehensive error handling
3. Add rate limiting middleware
4. Improve input validation

**Long-term Refactoring (1-2 months):**
1. Implement proper service layer architecture
2. Add comprehensive security headers
3. Optimize database queries and add caching
4. Implement proper dependency injection patterns

### **Complexity Hotspots**

**High Complexity Functions:**
- `main.py` (524 lines) - Multiple responsibilities
- `command_handler.py` (602 lines) - Complex command processing
- `real_time.py` (455 lines) - Connection management complexity

**Recommended Refactoring:**
- Split main.py into focused route modules
- Extract command processing logic into separate services
- Create dedicated connection management classes

---

## Next Phase Priorities

### **Phase 1: Critical Fixes (Immediate - This Week)**
1. **Database Schema Alignment** - Fix schema inconsistencies causing test failures
2. **Security Hardening** - Move remaining secrets to environment variables
3. **Test Suite Repair** - Fix failing tests and ensure 80% coverage
4. **Authentication Consolidation** - Standardize on single auth approach

### **Phase 2: Code Quality (1-2 Weeks)**
1. **Architecture Refactoring** - Split large files into focused modules
2. **Error Handling** - Implement comprehensive exception handling
3. **Input Validation** - Enhance security validation patterns
4. **Rate Limiting** - Add protection against abuse

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

_This document will be updated as decisions are made and the project evolves._
