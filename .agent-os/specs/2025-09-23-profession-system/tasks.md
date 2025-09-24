# Spec Tasks

## Tasks

- [x] 1. Database Schema Implementation
  - [x] 1.1 Write tests for profession model and database schema
  - [x] 1.2 Create DDL script for professions table creation
  - [x] 1.3 Add profession_id column to players table
  - [x] 1.4 Seed MVP professions (Tramp and Gutter Rat) in database
  - [x] 1.5 Add foreign key constraint after seeding
  - [x] 1.6 Integrate schema changes into existing database initialization scripts
  - [x] 1.7 Verify all database tests pass

- [x] 2. Backend API Implementation
  - [x] 2.1 Write tests for profession API endpoints
  - [x] 2.2 Create Profession model with validation
  - [x] 2.3 Implement GET /api/professions endpoint
  - [x] 2.4 Implement GET /api/professions/{id} endpoint
  - [x] 2.5 Write tests for modified stat rolling endpoint
  - [x] 2.6 Modify POST /api/character/roll-stats to accept profession_id
  - [x] 2.7 Implement weighted probability stat rolling algorithm
  - [x] 2.8 Add profession requirements validation logic
  - [x] 2.9 Verify all API tests pass

- [x] 3. Frontend UI Components
  - [x] 3.1 Write tests for profession selection screen
  - [x] 3.2 Create profession card component
  - [x] 3.3 Implement profession selection screen with card layout
  - [x] 3.4 Add stat requirements display with highlighting
  - [x] 3.5 Implement profession selection state management
  - [x] 3.6 Add navigation between profession selection and stat rolling
  - [x] 3.7 Verify all UI component tests pass

- [x] 4. Character Creation Flow Integration
  - [x] 4.1 Write integration tests for complete character creation flow
  - [x] 4.2 Update character creation navigation to include profession selection
  - [x] 4.3 Integrate profession API calls into character creation flow
  - [x] 4.4 Implement back/next navigation between screens
  - [x] 4.5 Add error handling for profession selection and stat rolling
  - [x] 4.6 Implement loading states during API calls
  - [x] 4.7 Verify all integration tests pass

- [x] 5. End-to-End Testing and Validation
  - [x] 5.1 Write E2E tests for complete profession selection workflow
  - [x] 5.2 Test profession selection with different profession choices
  - [x] 5.3 Test stat rolling with profession requirements validation
  - [x] 5.4 Test navigation flow between all character creation screens
  - [x] 5.5 Test error handling and edge cases
  - [x] 5.6 Verify profession choice persistence to database
  - [x] 5.7 Run full test suite and ensure all tests pass
  - [x] 5.8 Perform manual testing of complete user journey
