# Spec Tasks

## Tasks

- [x] 1. **Create EventPublisher Service Infrastructure**
  - [x] 1.1 Write tests for EventPublisher service class
  - [x] 1.2 Create EventPublisher class in `server/realtime/event_publisher.py`
  - [x] 1.3 Implement NATS subject publishing methods (player_entered, player_left, game_tick)
  - [x] 1.4 Add error handling and logging for NATS publishing failures
  - [x] 1.5 Verify all tests pass

- [ ] 2. **Extend NATSMessageHandler for Event Routing**
  - [ ] 2.1 Write tests for NATSMessageHandler event subscription capabilities
  - [ ] 2.2 Add event subscription methods to NATSMessageHandler class
  - [ ] 2.3 Implement event routing logic for player_entered, player_left, game_tick
  - [ ] 2.4 Add connection manager integration for event broadcasting
  - [ ] 2.5 Verify all tests pass

- [ ] 3. **Implement Game Tick System**
  - [ ] 3.1 Write tests for game tick scheduler and event generation
  - [ ] 3.2 Create GameTickService class in `server/services/game_tick_service.py`
  - [ ] 3.3 Implement 10-second interval tick scheduler using asyncio
  - [ ] 3.4 Add game tick event publishing to NATS global subject
  - [ ] 3.5 Integrate GameTickService with application lifespan management
  - [ ] 3.6 Verify all tests pass

- [ ] 4. **Refactor ConnectionManager for NATS Integration**
  - [ ] 4.1 Write tests for NATS-based event broadcasting in ConnectionManager
  - [ ] 4.2 Replace direct broadcasting in `_handle_player_entered_room()` with NATS publication
  - [ ] 4.3 Replace direct broadcasting in `_handle_player_left_room()` with NATS publication
  - [ ] 4.4 Add EventPublisher dependency injection to ConnectionManager
  - [ ] 4.5 Update event handling to use NATS message routing
  - [ ] 4.6 Verify all tests pass

- [ ] 5. **Integration Testing and Validation**
  - [ ] 5.1 Write end-to-end integration tests for complete NATS event flow
  - [ ] 5.2 Test player movement events (enter/leave room) through NATS
  - [ ] 5.3 Test game tick events broadcasting to all connected players
  - [ ] 5.4 Validate client receives events in correct format (no breaking changes)
  - [ ] 5.5 Performance test with multiple concurrent players
  - [ ] 5.6 Verify all tests pass and system meets performance requirements
