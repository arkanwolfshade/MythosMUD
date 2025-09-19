# Spec Tasks

## Tasks

- [x] 1. **Create EventPublisher Service Infrastructure**
  - [x] 1.1 Write tests for EventPublisher service class
  - [x] 1.2 Create EventPublisher class in `server/realtime/event_publisher.py`
  - [x] 1.3 Implement NATS subject publishing methods (player_entered, player_left, game_tick)
  - [x] 1.4 Add error handling and logging for NATS publishing failures
  - [x] 1.5 Verify all tests pass

- [x] 2. **Extend NATSMessageHandler for Event Routing**
  - [x] 2.1 Write tests for NATSMessageHandler event subscription capabilities
  - [x] 2.2 Add event subscription methods to NATSMessageHandler class
  - [x] 2.3 Implement event routing logic for player_entered, player_left, game_tick
  - [x] 2.4 Add connection manager integration for event broadcasting
  - [x] 2.5 Verify all tests pass

- [x] 3. **Implement Game Tick System**
  - [x] 3.1 Write tests for game tick scheduler and event generation
  - [x] 3.2 Create GameTickService class in `server/services/game_tick_service.py`
  - [x] 3.3 Implement 10-second interval tick scheduler using asyncio
  - [x] 3.4 Add game tick event publishing to NATS global subject
  - [x] 3.5 Integrate GameTickService with application lifespan management
  - [x] 3.6 Verify all tests pass

- [x] 4. **Refactor ConnectionManager for NATS Integration**
  - [x] 4.1 Write tests for NATS-based event broadcasting in ConnectionManager
  - [x] 4.2 Replace direct broadcasting in `_handle_player_entered_room()` with NATS publication
  - [x] 4.3 Replace direct broadcasting in `_handle_player_left_room()` with NATS publication
  - [x] 4.4 Add EventPublisher dependency injection to ConnectionManager
  - [x] 4.5 Update event handling to use NATS message routing
  - [x] 4.6 Verify all tests pass

- [x] 5. **Integration Testing and Validation**
  - [x] 5.1 Write end-to-end integration tests for complete NATS event flow
  - [x] 5.2 Test player movement events (enter/leave room) through NATS
  - [x] 5.3 Test game tick events broadcasting to all connected players
  - [x] 5.4 Validate client receives events in correct format (no breaking changes)
  - [x] 5.5 Performance test with multiple concurrent players
  - [x] 5.6 Verify all tests pass and system meets performance requirements
