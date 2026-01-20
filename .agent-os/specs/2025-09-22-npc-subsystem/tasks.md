# Spec Tasks

## Recent Completion Summary

### ✅ Database Separation and Environment Configuration (Completed)

**NPC Database Separation**: Successfully separated NPC data into dedicated `npcs.db` database

**Production Database**: Created `/data/npcs/npcs.db` with complete schema and all indexes

**Test Database**: Created `/server/tests/data/npcs/test_npcs.db` with same schema
- **Database Models**: Updated NPC models to use separate database metadata and session management
- **Environment Configuration**: Added `NPC_DATABASE_URL` to both production and test configurations
- **IDE Configuration**: Updated Cursor workspace settings to allow access to non-production environment files
- **Git Configuration**: Updated `.gitignore` to allow test and example environment files while blocking production files
- **Test Suite**: All 18 NPC model tests passing with separate database architecture
- **Application Integration**: Updated application lifespan to initialize NPC database on startup

### Database Architecture

**Tables**: `npc_definitions`, `npc_spawn_rules`, `npc_relationships`

**Indexes**: Complete indexing strategy for performance optimization

**Constraints**: Foreign key relationships and unique constraints properly enforced
- **Environment Variables**:
  - Production: `NPC_DATABASE_URL=sqlite+aiosqlite:///../../data/npcs/npcs.db`
  - Tests: `NPC_DATABASE_URL=sqlite+aiosqlite:///server/tests/data/npcs/test_npcs.db`

## Tasks

[x] 1. Database Schema and NPC Data Models ✅ COMPLETED

- [x] 1.1 Write tests for NPC database models and schema validation ✅
- [x] 1.2 Create SQL DDL files for NPC tables (npc_definitions, npc_spawn_rules, npc_relationships) ✅
- [x] 1.3 Implement NPC database models and repository classes ✅
- [x] 1.4 Create database initialization and verification scripts ✅
- [x] 1.5 Add sample NPC data for testing and development ✅
- [x] 1.6 Verify all database tests pass ✅

- [x] 2. NPC Threading and Message Queue Infrastructure ✅ COMPLETED
  - [x] 2.1 Write tests for NPC thread management and message queue operations ✅
  - [x] 2.2 Implement NPC thread manager and message queue system ✅
  - [x] 2.3 Create NPC action message types and serialization ✅
  - [x] 2.4 Implement thread-safe communication between NPC and main game threads ✅
  - [x] 2.5 Add NPC thread lifecycle management (start, stop, restart) ✅
  - [x] 2.6 Verify all threading and message queue tests pass ✅

- [x] 3. Basic NPC Types and Core Behaviors ✅ COMPLETED
  - [x] 3.1 Write tests for NPC base classes and behavior engines ✅
  - [x] 3.2 Implement NPC base class with common functionality (stats, inventory, communication) ✅
  - [x] 3.3 Create behavior engine framework with deterministic rule system ✅
  - [x] 3.4 Implement shopkeeper NPC type with buy/sell interactions ✅
  - [x] 3.5 Implement passive mob NPC type with wandering and response behaviors ✅
  - [x] 3.6 Implement aggressive mob NPC type with hunting and territorial behaviors ✅
  - [x] 3.7 Add AI integration stubs for future enhancement ✅
  - [x] 3.8 Verify all NPC behavior tests pass ✅

- [x] 4. NPC Integration with Existing Systems ✅ COMPLETED
  - [x] 4.1 Write integration tests for NPC movement system integration ✅
  - [x] 4.2 Implement NPC integration with existing movement system ✅
  - [x] 4.3 Write integration tests for NPC combat system integration ✅
  - [x] 4.4 Implement NPC integration with existing combat system ✅
  - [x] 4.5 Write integration tests for NPC communication system integration ✅
  - [x] 4.6 Implement NPC integration with existing chat/whisper systems ✅
  - [x] 4.7 Add NPC event subscription and reaction system ✅
  - [x] 4.8 Verify all integration tests pass ✅

- [x] 5. NPC Population Management and Zone Integration ✅
  - [x] 5.1 Write tests for NPC spawning and population management ✅
  - [x] 5.2 Implement sub-zone-based NPC population control system ✅
  - [x] 5.3 Create NPC spawning logic with required/optional population rules ✅
  - [x] 5.4 Implement NPC lifecycle management (spawn, despawn, respawn) ✅
  - [x] 5.5 Add NPC-to-NPC interaction and relationship system ✅
  - [x] 5.6 Verify all population management tests pass ✅

- [x] 6. Basic Admin API for NPC Management ✅
  - [x] 6.1 Write tests for NPC admin API endpoints ✅
  - [x] 6.2 Implement basic CRUD API endpoints for NPC definitions ✅
  - [x] 6.3 Create NPC instance management endpoints (spawn, despawn, list) ✅
  - [x] 6.4 Add NPC population monitoring and zone statistics endpoints ✅
  - [x] 6.5 Implement API authentication and authorization for admin endpoints ✅
  - [x] 6.6 Verify all API tests pass ✅

- [ ] 7. Admin Slash Commands for NPC Management
  - [x] 7.1 Write tests for admin slash command parsing and validation ✅
  - [x] 7.2 Implement slash command framework for admin NPC management ✅
  - [x] 7.3 Create NPC definition management commands (/npc create, /npc edit, /npc delete, /npc list) ✅
  - [x] 7.4 Implement NPC instance control commands (/npc spawn, /npc despawn, /npc move, /npc stats) ✅
  - [x] 7.5 Add NPC population monitoring commands (/npc population, /npc zones, /npc status) ✅
  - [x] 7.6 Create NPC behavior control commands (/npc behavior, /npc react, /npc stop) ✅
  - [x] 7.7 Implement command help system and error handling ✅
  - [x] 7.8 Verify all slash command tests pass ✅
