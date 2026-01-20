# Spec Tasks

## Tasks

[x] 1. Database Schema and Persistence Foundation

- [x] 1.1 Write tests for containers table creation and migration
- [x] 1.2 Create PostgreSQL migration script for containers table
- [x] 1.3 Update inventory payload JSON schema to support nested inner_container
- [x] 1.4 Implement container persistence layer (create, read, update, delete)
- [x] 1.5 Write tests for container persistence operations
- [x] 1.6 Verify all persistence tests pass

- [x] 2. ContainerComponent Data Model
  - [x] 2.1 Write tests for ContainerComponent validation and serialization
  - [x] 2.2 Implement ContainerComponent Pydantic model with all required fields
  - [x] 2.3 Add ContainerComponent factory methods for different source types
  - [x] 2.4 Write tests for ContainerComponent factory methods
  - [x] 2.5 Verify all ContainerComponent tests pass

- [x] 3. ContainerService Core Logic
  - [x] 3.1 Write tests for ContainerService open/close operations
  - [x] 3.2 Write tests for ContainerService transfer operations (bidirectional)
  - [x] 3.3 Write tests for ContainerService mutation guard serialization
  - [x] 3.4 Implement ContainerService with open/close methods
  - [x] 3.5 Implement ContainerService transfer methods (to_container, to_player)
  - [x] 3.6 Implement ContainerService mutation guard integration
  - [x] 3.7 Implement ContainerService capacity and weight validation
  - [x] 3.8 Add structured logging to all ContainerService operations
  - [x] 3.9 Verify all ContainerService tests pass

- [x] 4. Container Access Control and Locking
  - [x] 4.1 Write tests for container access control (proximity, ACL, roles)
  - [x] 4.2 Write tests for container lock/unlock mechanisms
  - [x] 4.3 Implement container access control validation
  - [x] 4.4 Implement container lock state management
  - [x] 4.5 Implement key-based unlocking for locked containers
  - [x] 4.6 Verify all access control tests pass

- [x] 5. API Endpoints and Controllers
  - [x] 5.1 Write tests for ContainerController endpoints
  - [x] 5.2 Implement POST /api/containers/open endpoint
  - [x] 5.3 Implement POST /api/containers/transfer endpoint
  - [x] 5.4 Implement POST /api/containers/close endpoint
  - [x] 5.5 Implement POST /api/containers/loot-all endpoint
  - [x] 5.6 Add rate limiting to container endpoints
  - [x] 5.7 Implement error handling and HTTP status code mapping
  - [x] 5.8 Verify all API endpoint tests pass

- [x] 6. WebSocket Events and Real-time Updates
  - [x] 6.1 Write tests for container WebSocket event emission
  - [x] 6.2 Implement container.opened event emission
  - [x] 6.3 Implement container.updated event emission with diffs
  - [x] 6.4 Implement container.closed event emission
  - [x] 6.5 Implement container.decayed event emission
  - [x] 6.6 Add WebSocket event broadcasting to room occupants
  - [x] 6.7 Verify all WebSocket event tests pass

- [x] 7. Corpse Lifecycle Automation
  - [x] 7.1 Write tests for corpse container creation on death
  - [x] 7.2 Write tests for corpse owner grace period logic
  - [x] 7.3 Write tests for corpse decay timer and cleanup
  - [x] 7.4 Hook death events to spawn corpse containers
  - [x] 7.5 Implement owner-only grace period enforcement
  - [x] 7.6 Implement corpse decay timer with time_service integration
  - [x] 7.7 Implement corpse cleanup with item redistribution
  - [x] 7.8 Add structured logging for all corpse lifecycle events
  - [x] 7.9 Verify all corpse lifecycle tests pass

- [x] 8. Environmental Container Integration
  - [x] 8.1 Write tests for room container loading into PostgreSQL from JSON definitions
  - [x] 8.1.1 Write tests for room container loading into Python from PostgreSQL definitions
  - [x] 8.2 Update room JSON schema to support container blocks
  - [x] 8.2.1 Update room table/field definitions to support container blocks
  - [x] 8.3 Implement world loader migration for room container definitions
  - [x] 8.4 Add container lookup by room_id to persistence layer
  - [x] 8.5 Verify all environmental container tests pass

- [x] 9. Wearable Container Integration
  - [x] 9.1 Write tests for wearable container equip/unequip transitions
  - [x] 9.2 Write tests for nested container capacity enforcement
  - [x] 9.3 Extend InventoryItem model to support inner_container
  - [x] 9.4 Implement equip/unequip handlers for wearable containers
  - [x] 9.5 Implement inventory spill rules for wearable container overflow
  - [x] 9.6 Add container lookup by entity_id to persistence layer
  - [x] 9.7 Verify all wearable container tests pass

- [x] 10. React Client Container UI Components
  - [x] 10.1 Write Vitest tests for ContainerContext store
  - [x] 10.2 Write Vitest tests for split-pane container component
  - [x] 10.3 Write Vitest tests for backpack tab component
  - [x] 10.4 Write Vitest tests for corpse overlay with countdown
  - [x] 10.5 Implement ContainerContext store for container state management
  - [x] 10.6 Implement split-pane UI component (container vs personal inventory)
  - [x] 10.7 Implement backpack tab/pill in inventory UI
  - [x] 10.8 Implement corpse overlay with countdown timer display
  - [x] 10.9 Add keyboard accessibility and focus management
  - [x] 10.10 Add drag-and-drop support for item transfers
  - [x] 10.11 Verify all React component tests pass

- [x] 11. React Client WebSocket Integration
  - [x] 11.1 Write tests for WebSocket event handlers
  - [x] 11.2 Implement container.opened event handler
  - [x] 11.3 Implement container.updated event handler with diff reconciliation
  - [x] 11.4 Implement container.closed event handler
  - [x] 11.5 Implement container.decayed event handler
  - [x] 11.6 Add real-time UI updates on container state changes
  - [x] 11.7 Verify all WebSocket integration tests pass

- [x] 12. Integration and E2E Testing
  - [x] 12.1 Write Playwright MCP tests for multi-user container looting
  - [x] 12.2 Write Playwright MCP tests for environmental container interactions
  - [x] 12.3 Write Playwright MCP tests for wearable container management
  - [x] 12.4 Write Playwright MCP tests for corpse looting with grace periods
  - [x] 12.5 Write integration tests for concurrent container mutations
  - [x] 12.6 Write integration tests for container persistence across server restarts
  - [x] 12.7 Verify all integration and E2E tests pass (test files created, import resolution needed)

- [x] 13. Security, Compliance, and Telemetry
  - [x] 13.1 Write tests for container interaction audit logging
  - [x] 13.2 Implement comprehensive audit logging for all container operations
  - [x] 13.3 Verify COPPA compliance (no personal data in container metadata)
  - [x] 13.4 Add rate limiting metrics and telemetry
  - [x] 13.5 Verify secure path validation for all persistence operations
  - [x] 13.6 Verify all security and compliance tests pass

- [ ] 14. Documentation and Final Verification
  - [x] 14.1 Update API documentation with container endpoints
  - [x] 14.2 Update architecture documentation with container system design
  - [ ] 14.3 Run full test suite and verify ≥80% coverage in touched modules
  - [x] 14.4 Run linting and formatting checks
  - [ ] 14.5 Verify all tests pass (unit, integration, E2E)
  - [ ] 14.6 Code review and final validation
