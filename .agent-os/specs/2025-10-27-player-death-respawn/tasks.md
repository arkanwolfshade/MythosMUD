# Spec Tasks

## Tasks

[x] 1. Database Schema and Player Model Updates

- [x] 1.1 Write tests for `respawn_room_id` field in Player model
- [x] 1.2 Add `respawn_room_id` column to players table schema
- [x] 1.3 Create and run migration script for local and test databases
- [x] 1.4 Update `Player` model in `server/models/player.py` to include `respawn_room_id` field
- [x] 1.5 Add methods: `get_health_state()`, `is_mortally_wounded()`, `is_dead()` to Player model
- [x] 1.6 Verify all tests pass

- [x] 2. Player Death Service Implementation
  - [x] 2.1 Write tests for `PlayerDeathService` (HP decay, mortally wounded detection, death detection)
  - [x] 2.2 Create `server/services/player_death_service.py` with `PlayerDeathService` class
  - [x] 2.3 Implement `get_mortally_wounded_players()` method
  - [x] 2.4 Implement `process_mortally_wounded_tick(player_id)` method (1 HP decay, cap at -10)
  - [x] 2.5 Implement `handle_player_death(player_id, death_location, killer_info)` method
  - [x] 2.6 Add service initialization in `server/app/lifespan.py`
  - [x] 2.7 Verify all tests pass

- [x] 3. Player Respawn Service Implementation
  - [x] 3.1 Write tests for `PlayerRespawnService` (limbo movement, respawn, room validation)
  - [x] 3.2 Create `server/services/player_respawn_service.py` with `PlayerRespawnService` class
  - [x] 3.3 Create limbo room JSON: `data/local/rooms/limbo/limbo_room.json`
  - [x] 3.4 Implement `move_player_to_limbo(player_id, death_location)` method
  - [x] 3.5 Implement `get_respawn_room(player_id)` method with default fallback
  - [x] 3.6 Implement `respawn_player(player_id)` method (restore HP, move to respawn room, publish events)
  - [x] 3.7 Add service initialization in `server/app/lifespan.py`
  - [x] 3.8 Verify all tests pass

- [x] 4. Event Types and Message Broadcasting
  - [x] 4.1 Write tests for new event types
  - [x] 4.2 Add `PlayerMortallyWoundedEvent` to `server/events/event_types.py`
  - [x] 4.3 Add `PlayerDiedEvent` to `server/events/event_types.py`
  - [x] 4.4 Add `PlayerRespawnedEvent` to `server/events/event_types.py`
  - [x] 4.5 Add `PlayerHPDecayEvent` to `server/events/event_types.py`
  - [x] 4.6 Update `server/services/combat_messaging_integration.py` with mortally wounded/death/respawn broadcast methods
  - [x] 4.7 Update NATS message handler to subscribe to new event subjects
  - [x] 4.8 Verify all tests pass

- [x] 5. Combat Service Integration
  - [x] 5.1 Write tests for HP capping at -10 and death state detection in combat
  - [x] 5.2 Update `CombatService._apply_damage()` to cap player HP at -10
  - [x] 5.3 Update `CombatService.process_attack()` to detect mortally wounded state (HP = 0)
  - [x] 5.4 Update `CombatService.process_attack()` to detect death state (HP = -10)
  - [x] 5.5 Implement threat queue removal for dead players
  - [x] 5.6 Implement combat continuation logic (end if no players, continue if others remain)
  - [x] 5.7 Publish appropriate events (mortally wounded, death) when states are detected
  - [x] 5.8 Verify all tests pass

- [x] 6. Game Tick Integration
  - [x] 6.1 Write tests for HP decay processing in game tick loop
  - [x] 6.2 Update `server/app/lifespan.py` game_tick_loop to call PlayerDeathService
  - [x] 6.3 Implement HP decay for all mortally wounded players each tick
  - [x] 6.4 Broadcast HP decay messages via NATS for each affected player
  - [x] 6.5 Verify decay stops at -10 HP
  - [x] 6.6 Verify all tests pass

- [x] 7. API Endpoint for Respawn
  - [x] 7.1 Write tests for `/api/player/respawn` endpoint
  - [x] 7.2 Create respawn endpoint in appropriate router file
  - [x] 7.3 Implement request validation (player must be dead)
  - [x] 7.4 Call `PlayerRespawnService.respawn_player()`
  - [x] 7.5 Return respawn room data and updated player state
  - [x] 7.6 Implement rate limiting (1 request per 5 seconds)
  - [x] 7.7 Verify all tests pass

- [x] 8. Frontend - Mortally Wounded UI State
  - [x] 8.1 Write tests/storybook for mortally wounded UI states
  - [x] 8.2 Add `isMortallyWounded` state to `GameTerminalWithPanels.tsx`
  - [x] 8.3 Create CSS classes for `.mortally-wounded` and `.border-effect`
  - [x] 8.4 Listen for `player_mortally_wounded` event to trigger red UI mode
  - [x] 8.5 Disable command input field when mortally wounded
  - [x] 8.6 Apply red theme and border effects to all panels
  - [x] 8.7 Listen for `player_hp_decay` events to display decay messages
  - [x] 8.8 Ensure negative HP displays correctly in Player Information panel
  - [x] 8.9 Verify UI updates work correctly

- [x] 9. Frontend - Death Interstitial Screen
  - [x] 9.1 Write tests/storybook for DeathInterstitial component
  - [x] 9.2 Create `client/src/components/DeathInterstitial.tsx` component
  - [x] 9.3 Implement full-screen modal with thematic death narrative
  - [x] 9.4 Display death location information
  - [x] 9.5 Add "Rejoin the earthly plane" button
  - [x] 9.6 Implement respawn API call on button click
  - [x] 9.7 Listen for `player_died` event to show interstitial
  - [x] 9.8 Listen for `player_respawned` event to close interstitial and reset UI
  - [x] 9.9 Verify interstitial appears and functions correctly

- [x] 10. Integration Testing and Bug Fixes
  - [x] 10.1 Run full test suite and fix any integration issues
  - [x] 10.2 Test with Playwright MCP for real browser verification
  - [x] 10.3 Verify all messaging displays correctly
  - [x] 10.4 Verify UI state transitions work smoothly

- [x] 11. Best practices validation
  - [x] 11.1 Enhanced logger is used throughout the new code
  - [x] 11.2 No use of f-strings or print statements for logging
  - [x] 11.3 Apply all relevant *.mdc files from .cursor/rules directory
  - [x] 11.4 Linting passes
  - [x] 11.5 Unit and integration tests pass
  - [x] 11.6 Pre-commit hooks pass
