# Spec Tasks

## Tasks

- [ ] 1. Implement NATSSubjectManager Core System
  - [ ] 1.1 Write comprehensive unit tests for NATSSubjectManager class
  - [ ] 1.2 Create `server/services/nats_subject_manager.py` with pattern registry infrastructure
  - [ ] 1.3 Implement `build_subject()` method with parameter validation
  - [ ] 1.4 Implement `validate_subject()` method with pattern matching
  - [ ] 1.5 Implement `register_pattern()` and `get_pattern_info()` methods
  - [ ] 1.6 Add predefined subject patterns (chat_say_room, chat_local_subzone, etc.)
  - [ ] 1.7 Implement comprehensive error handling for validation failures
  - [ ] 1.8 Verify all tests pass with 90%+ coverage

- [ ] 2. Integrate Subject Manager with Chat Services
  - [ ] 2.1 Write integration tests for ChatService migration
  - [ ] 2.2 Update ChatService to inject NATSSubjectManager dependency
  - [ ] 2.3 Migrate say command subject construction to use pattern `chat_say_room`
  - [ ] 2.4 Migrate local channel subject construction to use pattern `chat_local_subzone`
  - [ ] 2.5 Migrate whisper command subject construction to use pattern `chat_whisper_player`
  - [ ] 2.6 Migrate global channel subject construction to use pattern `chat_global`
  - [ ] 2.7 Migrate emote/pose commands to use standardized patterns
  - [ ] 2.8 Verify all integration tests pass and chat functionality works correctly

- [ ] 3. Add Subject Validation to NATS Message Publishing
  - [ ] 3.1 Write tests for NATSService subject validation integration
  - [ ] 3.2 Update NATSService to inject NATSSubjectManager dependency
  - [ ] 3.3 Add pre-publish subject validation in `publish()` method
  - [ ] 3.4 Implement logging for validation failures with correlation IDs
  - [ ] 3.5 Add configuration option to enable/disable strict validation
  - [ ] 3.6 Update message handlers to use standardized subscription patterns
  - [ ] 3.7 Add performance monitoring for subject validation operations
  - [ ] 3.8 Verify all tests pass and message publishing remains reliable

- [ ] 4. Implement Admin API Endpoints for Subject Management
  - [ ] 4.1 Write API tests for SubjectController endpoints
  - [ ] 4.2 Create `server/api/controllers/subject_controller.py` with route definitions
  - [ ] 4.3 Implement GET `/api/health/nats/subjects` endpoint for statistics
  - [ ] 4.4 Implement POST `/api/admin/nats/subjects/validate` endpoint
  - [ ] 4.5 Implement GET `/api/admin/nats/subjects/patterns` endpoint
  - [ ] 4.6 Implement POST `/api/admin/nats/subjects/patterns` endpoint (admin-only)
  - [ ] 4.7 Add admin permission validation and error handling
  - [ ] 4.8 Verify all API tests pass and endpoints return correct responses

- [ ] 5. Performance Optimization and Documentation
  - [ ] 5.1 Write performance tests for pattern caching and validation
  - [ ] 5.2 Implement pattern caching for compiled patterns
  - [ ] 5.3 Implement validation result caching for repeated subjects
  - [ ] 5.4 Add performance metrics collection and logging
  - [ ] 5.5 Create comprehensive documentation in `docs/NATS_SUBJECT_PATTERNS.md`
  - [ ] 5.6 Add usage examples and migration guide to documentation
  - [ ] 5.7 Update existing chat service documentation with standardized patterns
  - [ ] 5.8 Verify all tests pass, performance targets met, and documentation complete
