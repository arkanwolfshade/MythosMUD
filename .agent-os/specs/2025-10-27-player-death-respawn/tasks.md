# Spec Tasks

## Tasks

- [x] 1. Database Schema and Player Model Updates
  - [x] 1.1 Write tests for `respawn_room_id` field in Player model
  - [x] 1.2 Add `respawn_room_id` column to players table schema
  - [x] 1.3 Create and run migration script for local and test databases
  - [x] 1.4 Update `Player` model in `server/models/player.py` to include `respawn_room_id` field
  - [x] 1.5 Add methods: `get_health_state()`, `is_mortally_wounded()`, `is_dead()` to Player model
  - [x] 1.6 Verify all tests pass

- [ ] 2. Player Death Service Implementation
  - [ ] 2.1 Write tests for `PlayerDeathService` (HP decay, mortally wounded detection, death detection)
  - [ ] 2.2 Create `server/services/player_death_service.py` with `PlayerDeathService` class
  - [ ] 2.3 Implement `get_mortally_wounded_players()` method
  - [ ] 2.4 Implement `process_mortally_wounded_tick(player_id)` method (1 HP decay, cap at -10)
  - [ ] 2.5 Implement `handle_player_death(player_id, death_location, killer_info)` method
  - [ ] 2.6 Add service initialization in `server/app/lifespan.py`
  - [ ] 2.7 Verify all tests pass

- [ ] 3. Player Respawn Service Implementation
  - [ ] 3.1 Write tests for `PlayerRespawnService` (limbo movement, respawn, room validation)
  - [ ] 3.2 Create `server/services/player_respawn_service.py` with `PlayerRespawnService` class
  - [ ] 3.3 Create limbo room JSON: `data/local/rooms/limbo/limbo_room.json`
  - [ ] 3.4 Implement `move_player_to_limbo(player_id, death_location)` method
  - [ ] 3.5 Implement `get_respawn_room(player_id)` method with default fallback
  - [ ] 3.6 Implement `respawn_player(player_id)` method (restore HP, move to respawn room, publish events)
  - [ ] 3.7 Add service initialization in `server/app/lifespan.py`
  - [ ] 3.8 Verify all tests pass

- [ ] 4. Event Types and Message Broadcasting
  - [ ] 4.1 Write tests for new event types
  - [ ] 4.2 Add `PlayerMortallyWoundedEvent` to `server/events/event_types.py`
  - [ ] 4.3 Add `PlayerDiedEvent` to `server/events/event_types.py`
  - [ ] 4.4 Add `PlayerRespawnedEvent` to `server/events/event_types.py`
  - [ ] 4.5 Add `PlayerHPDecayEvent` to `server/events/event_types.py`
  - [ ] 4.6 Update `server/services/combat_messaging_integration.py` with mortally wounded/death/respawn broadcast methods
  - [ ] 4.7 Update NATS message handler to subscribe to new event subjects
  - [ ] 4.8 Verify all tests pass

- [ ] 5. Combat Service Integration
  - [ ] 5.1 Write tests for HP capping at -10 and death state detection in combat
  - [ ] 5.2 Update `CombatService._apply_damage()` to cap player HP at -10
  - [ ] 5.3 Update `CombatService.process_attack()` to detect mortally wounded state (HP = 0)
  - [ ] 5.4 Update `CombatService.process_attack()` to detect death state (HP = -10)
  - [ ] 5.5 Implement threat queue removal for dead players
  - [ ] 5.6 Implement combat continuation logic (end if no players, continue if others remain)
  - [ ] 5.7 Publish appropriate events (mortally wounded, death) when states are detected
  - [ ] 5.8 Verify all tests pass

- [ ] 6. Game Tick Integration
  - [ ] 6.1 Write tests for HP decay processing in game tick loop
  - [ ] 6.2 Update `server/app/lifespan.py` game_tick_loop to call PlayerDeathService
  - [ ] 6.3 Implement HP decay for all mortally wounded players each tick
  - [ ] 6.4 Broadcast HP decay messages via NATS for each affected player
  - [ ] 6.5 Verify decay stops at -10 HP
  - [ ] 6.6 Verify all tests pass

- [ ] 7. API Endpoint for Respawn
  - [ ] 7.1 Write tests for `/api/player/respawn` endpoint
  - [ ] 7.2 Create respawn endpoint in appropriate router file
  - [ ] 7.3 Implement request validation (player must be dead)
  - [ ] 7.4 Call `PlayerRespawnService.respawn_player()`
  - [ ] 7.5 Return respawn room data and updated player state
  - [ ] 7.6 Implement rate limiting (1 request per 5 seconds)
  - [ ] 7.7 Verify all tests pass

- [ ] 8. Frontend - Mortally Wounded UI State
  - [ ] 8.1 Write tests/storybook for mortally wounded UI states
  - [ ] 8.2 Add `isMortallyWounded` state to `GameTerminalWithPanels.tsx`
  - [ ] 8.3 Create CSS classes for `.mortally-wounded` and `.border-effect`
  - [ ] 8.4 Listen for `player_mortally_wounded` event to trigger red UI mode
  - [ ] 8.5 Disable command input field when mortally wounded
  - [ ] 8.6 Apply red theme and border effects to all panels
  - [ ] 8.7 Listen for `player_hp_decay` events to display decay messages
  - [ ] 8.8 Ensure negative HP displays correctly in Player Information panel
  - [ ] 8.9 Verify UI updates work correctly

- [ ] 9. Frontend - Death Interstitial Screen
  - [ ] 9.1 Write tests/storybook for DeathInterstitial component
  - [ ] 9.2 Create `client/src/components/DeathInterstitial.tsx` component
  - [ ] 9.3 Implement full-screen modal with thematic death narrative
  - [ ] 9.4 Display death location information
  - [ ] 9.5 Add "Rejoin the earthly plane" button
  - [ ] 9.6 Implement respawn API call on button click
  - [ ] 9.7 Listen for `player_died` event to show interstitial
  - [ ] 9.8 Listen for `player_respawned` event to close interstitial and reset UI
  - [ ] 9.9 Verify interstitial appears and functions correctly

- [ ] 10. Integration Testing and Bug Fixes
  - [ ] 10.1 Write E2E tests for complete death → respawn flow
  - [ ] 10.2 Write E2E tests for mortally wounded → HP decay → death
  - [ ] 10.3 Write E2E tests for multi-player combat with one player death
  - [ ] 10.4 Write E2E tests for NPC behavior after all players die
  - [ ] 10.5 Run full test suite and fix any integration issues
  - [ ] 10.6 Test with Playwright MCP for real browser verification
  - [ ] 10.7 Verify all messaging displays correctly
  - [ ] 10.8 Verify UI state transitions work smoothly
