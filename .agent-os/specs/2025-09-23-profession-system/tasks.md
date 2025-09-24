# Spec Tasks

## Tasks

- [ ] 1. Database Schema Implementation
  - [ ] 1.1 Write tests for profession model and database schema
  - [ ] 1.2 Create DDL script for professions table creation
  - [ ] 1.3 Add profession_id column to players table
  - [ ] 1.4 Seed MVP professions (Tramp and Gutter Rat) in database
  - [ ] 1.5 Add foreign key constraint after seeding
  - [ ] 1.6 Integrate schema changes into existing database initialization scripts
  - [ ] 1.7 Verify all database tests pass

- [ ] 2. Backend API Implementation
  - [ ] 2.1 Write tests for profession API endpoints
  - [ ] 2.2 Create Profession model with validation
  - [ ] 2.3 Implement GET /api/professions endpoint
  - [ ] 2.4 Implement GET /api/professions/{id} endpoint
  - [ ] 2.5 Write tests for modified stat rolling endpoint
  - [ ] 2.6 Modify POST /api/character/roll-stats to accept profession_id
  - [ ] 2.7 Implement weighted probability stat rolling algorithm
  - [ ] 2.8 Add profession requirements validation logic
  - [ ] 2.9 Verify all API tests pass

- [ ] 3. Frontend UI Components
  - [ ] 3.1 Write tests for profession selection screen
  - [ ] 3.2 Create profession card component
  - [ ] 3.3 Implement profession selection screen with card layout
  - [ ] 3.4 Add stat requirements display with highlighting
  - [ ] 3.5 Implement profession selection state management
  - [ ] 3.6 Add navigation between profession selection and stat rolling
  - [ ] 3.7 Verify all UI component tests pass

- [ ] 4. Character Creation Flow Integration
  - [ ] 4.1 Write integration tests for complete character creation flow
  - [ ] 4.2 Update character creation navigation to include profession selection
  - [ ] 4.3 Integrate profession API calls into character creation flow
  - [ ] 4.4 Implement back/next navigation between screens
  - [ ] 4.5 Add error handling for profession selection and stat rolling
  - [ ] 4.6 Implement loading states during API calls
  - [ ] 4.7 Verify all integration tests pass

- [ ] 5. End-to-End Testing and Validation
  - [ ] 5.1 Write E2E tests for complete profession selection workflow
  - [ ] 5.2 Test profession selection with different profession choices
  - [ ] 5.3 Test stat rolling with profession requirements validation
  - [ ] 5.4 Test navigation flow between all character creation screens
  - [ ] 5.5 Test error handling and edge cases
  - [ ] 5.6 Verify profession choice persistence to database
  - [ ] 5.7 Run full test suite and ensure all tests pass
  - [ ] 5.8 Perform manual testing of complete user journey
