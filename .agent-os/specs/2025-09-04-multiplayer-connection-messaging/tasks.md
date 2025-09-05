# Spec Tasks

## Tasks

- [ ] 1. **Investigate Server Event System**
  - [ ] 1.1 Write tests for WebSocket connection event firing
  - [ ] 1.2 Examine WebSocket connection handler for PlayerEnteredRoom event firing
  - [ ] 1.3 Examine WebSocket disconnection handler for PlayerLeftRoom event firing
  - [ ] 1.4 Verify EventBus integration and event publishing
  - [ ] 1.5 Add comprehensive logging to track event firing
  - [ ] 1.6 Verify all tests pass

- [ ] 2. **Repair Event Broadcasting System**
  - [ ] 2.1 Write tests for RealTimeEventHandler player event broadcasting
  - [ ] 2.2 Fix RealTimeEventHandler to properly handle PlayerEnteredRoom events
  - [ ] 2.3 Fix RealTimeEventHandler to properly handle PlayerLeftRoom events
  - [ ] 2.4 Implement proper event broadcasting to other players in same room
  - [ ] 2.5 Add error handling for event broadcasting failures
  - [ ] 2.6 Verify all tests pass

- [ ] 3. **Verify Complete Event Flow**
  - [ ] 3.1 Write integration tests for complete event flow
  - [ ] 3.2 Test WebSocket connection → event firing → broadcasting → client reception
  - [ ] 3.3 Verify event data structure matches client expectations
  - [ ] 3.4 Test multiple players entering/leaving simultaneously
  - [ ] 3.5 Verify all tests pass

- [ ] 4. **End-to-End Multiplayer Testing**
  - [ ] 4.1 Write browser-based tests for multiplayer connection messaging
  - [ ] 4.2 Test two players in same room - verify connection messages appear
  - [ ] 4.3 Test player disconnection - verify disconnection messages appear
  - [ ] 4.4 Test multiple players - verify all see each other's connection/disconnection
  - [ ] 4.5 Verify Room Info panel shows correct occupant counts
  - [ ] 4.6 Verify all tests pass
