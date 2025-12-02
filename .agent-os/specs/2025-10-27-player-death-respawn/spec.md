# Spec Requirements Document

> Spec: Player Death and Respawn System
> Created: 2025-10-27

## Overview

Implement a complete player death and respawn system that handles player mortality, a mortally wounded state, automatic HP decay, and resurrection mechanics with thematic narrative elements. This feature ensures players can experience meaningful consequences from combat while providing a smooth recovery flow that maintains immersion in the Lovecraftian atmosphere.

## User Stories

### Mortally Wounded Player

As a player in combat, I want to enter a mortally wounded state when my HP reaches 0, so that I have a chance to be rescued before dying completely.

**Workflow:**

1. Player is in combat with an NPC and takes damage that reduces HP to 0 or below (but above -10)
2. Player sees message: "<NPC name>'s attack causes you to collapse as darkness begins closing in on your vision"
3. Other players in the room see: "<Player name> collapses from <NPC name>'s attack and is on the verge of death!"
4. Player's UI changes to red theme with border effects applied to all panels
5. Player's command input is disabled (can only observe)
6. Player continues to see all room chat and combat messages
7. Player loses 1 HP per game tick (every 1 second)
8. NPC can continue attacking the mortally wounded player
9. HP decay and NPC damage stack (e.g., 0 HP → tick to -1 → NPC hits for 5 → -6 → tick to -7)
10. If player reaches -10 HP, they die

### Player Death and Resurrection

As a player who has died, I want to respawn at a safe location with full health, so that I can continue playing after defeat.

**Workflow:**

1. Player reaches -10 HP (either through HP decay or additional damage, capped at -10)
2. All players in the room see: "<Player name> exhales their last breath." The player sees a message: "You exhale your last breath."
3. Player is immediately shown a thematic death-resurrection interstitial screen
4. Player is moved to a "limbo" room (completely isolated from game)
5. Interstitial screen displays atmospheric Lovecraftian death/resurrection narrative
6. Player clicks "Rejoin the earthly plane" button (available immediately)
7. Player respawns in their saved respawn room (defaults to `earth_arkhamcity_sanitarium_room_foyer_001`)
8. Player respawns at full HP with UI restored to normal colors
9. Room sees message: "Patient <playername> opens their eyes and awakens from their coma." The player sees a message: "You open your eyes and awakens from your coma."
10. Death location is recorded for player reference

### Combat Continuity During Death

As an NPC in combat, I want to continue fighting remaining players when one dies, so that multi-player combat remains engaging.

**Workflow:**

1. NPC is in combat with multiple players
2. One player dies (reaches -10 HP)
3. NPC removes dead player from threat queue
4. If other players remain in threat queue: NPC continues combat with next target
5. If no players remain: NPC exits combat and returns to default behavior

## Spec Scope

1. **Mortally Wounded State** - Implement 0 to -10 HP range with incapacitation, UI changes, and 1 HP/tick decay
2. **Death Detection** - Trigger death at -10 HP with appropriate messaging and combat cleanup
3. **Interstitial Screen** - Create death/resurrection narrative screen with "Rejoin the earthly plane" button
4. **Respawn Mechanics** - Implement player respawn at designated location with full HP restoration
5. **Database Schema** - Add `respawn_room_id` field to players table for custom respawn locations
6. **HP Range Extension** - Support negative HP values from 0 to -10 with proper capping
7. **UI Updates** - Display negative HP, mortally wounded visual state, and HP decay messages
8. **Combat Integration** - Handle player death in combat, threat queue management, and combat continuation

## Out of Scope

- Player revival/healing mechanics (future feature)
- Death penalties (XP loss, item loss, respawn sickness, lucidity impact)
- Death counter statistics (future feature as part of broader player metrics)
- Environmental death sources (falling, traps, starvation) - combat only for now
- PVP death mechanics
- Inventory/equipment loss on death (inventory system not yet implemented)
- Custom respawn point selection UI (field added, but setting mechanism deferred)
- Respawn cooldown/timer
- Buffs/debuffs clearing on death (systems not yet implemented)

## Expected Deliverable

1. **Mortally Wounded Functionality**: Player can reach 0 HP, see red UI with border effects, lose 1 HP per tick, cannot take actions, and can observe combat/chat
2. **Death and Respawn Flow**: Player dies at -10 HP, sees interstitial screen, clicks button to respawn at sanitarium with full HP and normal UI
3. **Combat Continuity**: NPC continues fighting remaining players or exits combat when all players die
4. **Message Broadcasting**: All death-related messages display correctly to affected players and room occupants
5. **HP Persistence**: Negative HP values persist to database and display correctly in Player Information panel
6. **Tick Integration**: HP decay processes correctly with game ticks, with messages appearing in Game Info panel
