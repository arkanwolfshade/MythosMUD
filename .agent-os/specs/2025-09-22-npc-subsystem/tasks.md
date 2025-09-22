# Spec Tasks

## Recent Completion Summary

### ✅ Database Separation and Environment Configuration (Completed)

- **NPC Database Separation**: Successfully separated NPC data into dedicated `npcs.db` database
- **Production Database**: Created `/data/npcs/npcs.db` with complete schema and all indexes
- **Test Database**: Created `/server/tests/data/npcs/test_npcs.db` with same schema
- **Database Models**: Updated NPC models to use separate database metadata and session management
- **Environment Configuration**: Added `NPC_DATABASE_URL` to both production and test configurations
- **IDE Configuration**: Updated Cursor workspace settings to allow access to non-production environment files
- **Git Configuration**: Updated `.gitignore` to allow test and example environment files while blocking production files
- **Test Suite**: All 18 NPC model tests passing with separate database architecture
- **Application Integration**: Updated application lifespan to initialize NPC database on startup

### Database Architecture

- **Tables**: `npc_definitions`, `npc_spawn_rules`, `npc_relationships`
- **Indexes**: Complete indexing strategy for performance optimization
- **Constraints**: Foreign key relationships and unique constraints properly enforced
- **Environment Variables**:
  - Production: `NPC_DATABASE_URL=sqlite+aiosqlite:///../../data/npcs/npcs.db`
  - Tests: `NPC_DATABASE_URL=sqlite+aiosqlite:///server/tests/data/npcs/test_npcs.db`

## Tasks

- [x] 1. Database Schema and NPC Data Models ✅ COMPLETED
  - [x] 1.1 Write tests for NPC database models and schema validation ✅
  - [x] 1.2 Create SQL DDL files for NPC tables (npc_definitions, npc_spawn_rules, npc_relationships) ✅
  - [x] 1.3 Implement NPC database models and repository classes ✅
  - [x] 1.4 Create database initialization and verification scripts ✅
  - [x] 1.5 Add sample NPC data for testing and development ✅
  - [x] 1.6 Verify all database tests pass ✅

- [ ] 2. NPC Threading and Message Queue Infrastructure
  - [ ] 2.1 Write tests for NPC thread management and message queue operations
  - [ ] 2.2 Implement NPC thread manager and message queue system
  - [ ] 2.3 Create NPC action message types and serialization
  - [ ] 2.4 Implement thread-safe communication between NPC and main game threads
  - [ ] 2.5 Add NPC thread lifecycle management (start, stop, restart)
  - [ ] 2.6 Verify all threading and message queue tests pass

- [ ] 3. Basic NPC Types and Core Behaviors
  - [ ] 3.1 Write tests for NPC base classes and behavior engines
  - [ ] 3.2 Implement NPC base class with common functionality (stats, inventory, communication)
  - [ ] 3.3 Create behavior engine framework with deterministic rule system
  - [ ] 3.4 Implement shopkeeper NPC type with buy/sell interactions
  - [ ] 3.5 Implement passive mob NPC type with wandering and response behaviors
  - [ ] 3.6 Implement aggressive mob NPC type with hunting and territorial behaviors
  - [ ] 3.7 Add AI integration stubs for future enhancement
  - [ ] 3.8 Verify all NPC behavior tests pass

- [ ] 4. NPC Integration with Existing Systems
  - [ ] 4.1 Write integration tests for NPC movement system integration
  - [ ] 4.2 Implement NPC integration with existing movement system
  - [ ] 4.3 Write integration tests for NPC combat system integration
  - [ ] 4.4 Implement NPC integration with existing combat system
  - [ ] 4.5 Write integration tests for NPC communication system integration
  - [ ] 4.6 Implement NPC integration with existing chat/whisper systems
  - [ ] 4.7 Add NPC event subscription and reaction system
  - [ ] 4.8 Verify all integration tests pass

- [ ] 5. NPC Population Management and Zone Integration
  - [ ] 5.1 Write tests for NPC spawning and population management
  - [ ] 5.2 Implement sub-zone-based NPC population control system
  - [ ] 5.3 Create NPC spawning logic with required/optional population rules
  - [ ] 5.4 Implement NPC lifecycle management (spawn, despawn, respawn)
  - [ ] 5.5 Add NPC-to-NPC interaction and relationship system
  - [ ] 5.6 Verify all population management tests pass

- [ ] 6. Basic Admin API for NPC Management
  - [ ] 6.1 Write tests for NPC admin API endpoints
  - [ ] 6.2 Implement basic CRUD API endpoints for NPC definitions
  - [ ] 6.3 Create NPC instance management endpoints (spawn, despawn, list)
  - [ ] 6.4 Add NPC population monitoring and zone statistics endpoints
  - [ ] 6.5 Implement API authentication and authorization for admin endpoints
  - [ ] 6.6 Verify all API tests pass
