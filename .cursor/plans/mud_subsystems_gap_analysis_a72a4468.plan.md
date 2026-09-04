---
name: MUD Subsystems Gap Analysis
overview: Analysis of MythosMUD against typical MUD subsystems and open GitHub issues, identifying which major subsystems are implemented versus missing or only partially present.
todos: []
isProject: false
---

# MythosMUD Subsystems Gap Analysis

## Implemented Subsystems (Confirmed in Codebase)

- **Combat**: Full round-based combat, flee, death, respawn, NPC combat, XP rewards on kill, lucidity/catatonia ([docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md](docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md), [server/services/npc_combat_rewards.py](server/services/npc_combat_rewards.py))
- **Magic**: Spells, MP, targeting, effects, learning, mastery ([server/game/magic/](server/game/magic/))
- **Items & Inventory**: Containers, equipment, wearable containers, item prototypes, inventory service ([docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md](docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md))
- **Weapons**: Weapon handling in combat and equipment
- **Grouping**: Ephemeral party system (formation, leadership, shared context) per [docs/PLANNING_ephemeral_grouping.md](docs/PLANNING_ephemeral_grouping.md) and [docs/PARTY_SYSTEM_REFERENCE.md](docs/PARTY_SYSTEM_REFERENCE.md)
- **Movement & World**: Rooms, exploration, movement service, coordinate system
- **Professions & Level/XP**: Character creation with profession, `experience_points` and `level` on Player, `ExperienceRepository`, `gain_experience` (combat rewards), level-from-XP formula ([server/models/player.py](server/models/player.py), [server/persistence/repositories/experience_repository.py](server/persistence/repositories/experience_repository.py))
- **NPCs**: Lifecycle, spawning, types including **shopkeeper** (buy/sell) and **quest_giver** (type exists; no quest logic) ([server/npc/shopkeeper_npc.py](server/npc/shopkeeper_npc.py), [server/models/npc.py](server/models/npc.py))
- **Chat**: Room say, whisper, NATS-backed ([docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md](docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md))
- **Temporal**: In-game time, holidays, schedule

---

## Major Subsystems Not Implemented (or Stub-Only)

### 1. Quest System

- **Status**: Not implemented. README lists "Quest System - Dynamic quest generation and tracking" under **Planned Features** ([README.md](README.md)).
- **What exists**: NPC type `quest_giver` in schema and spawning; no quest definitions, objectives, progress tracking, or reward pipeline. Parser help text says "Learn a spell by name (temporary command until quests/vendors are implemented)" ([server/utils/command_parser.py](server/utils/command_parser.py)).
- **Typical MUD features**: Quest definitions, objectives (kill/fetch/talk), progress state per player, completion rewards (XP, items, gold), journal/quest log.

### 2. Crafting System

- **Status**: Not implemented. README lists "Crafting System - Item crafting and modification" under **Planned Features** ([README.md](README.md)).
- **What exists**: No crafting modules or services (no `*craft`* files in server). `COMPLEX_COMMANDS` in lucidity disruption includes "craft" as a placeholder ([server/services/lucidity_command_disruption.py](server/services/lucidity_command_disruption.py)).
- **Typical MUD features**: Recipes, ingredients, combine/forge commands, skill-based success, output items.

### 3. Economy / Currency / Player Trading

- **Status**: Partially present. "currency" exists in item constants ([server/game/items/constants.py](server/game/items/constants.py)); Shopkeeper NPCs have buy/sell with shop inventory. No player-to-player trading, no centralized economy (e.g. auction house, market), no gold/currency persistence model clearly exposed.
- **Gap**: Full economy (currency flow, player-to-player trade, pricing, inflation control) is not a first-class subsystem.

### 4. Skills (Beyond Profession)

- **Status**: Profession is the only “class-like” choice at creation. No separate skill system (e.g. skill points, skill trees, non-spell skills that level with use or XP).
- **Note**: Magic has “mastery” and learning; that is spell-specific, not a generic skill subsystem.

### 5. Friends List / Social Graph

- **Status**: Not implemented. Tracked in open issue [#147](https://github.com/arkanwolfshade/MythosMUD/issues/147) (Add friends list and friend communication features).

### 6. Moderation Tooling

- **Status**: Partially or not implemented. Open issues: [#139](https://github.com/arkanwolfshade/MythosMUD/issues/139) (Progressive warning system), [#140](https://github.com/arkanwolfshade/MythosMUD/issues/140) (AI-powered auto-moderation), [#141](https://github.com/arkanwolfshade/MythosMUD/issues/141) (Enhanced moderator interface).

---

## Summary Table (High Level)


| Subsystem                  | Implemented | Notes                                                |
| -------------------------- | ----------- | ---------------------------------------------------- |
| Combat                     | Yes         | Rounds, flee, death, respawn, NPC combat, XP on kill |
| Magic                      | Yes         | Spells, MP, learning, mastery                        |
| Items/Inventory            | Yes         | Containers, equipment, prototypes                    |
| Grouping (Party)           | Yes         | Ephemeral parties, shared context                    |
| Movement/World             | Yes         | Rooms, exploration                                   |
| Level/XP                   | Yes         | experience_points, level, gain from combat           |
| Professions                | Yes         | Character creation, profession_id                    |
| NPCs (incl. shop)          | Yes         | Shopkeeper buy/sell; quest_giver type only           |
| Chat                       | Yes         | Say, whisper, channels                               |
| Quest system               | No          | Planned; only quest_giver NPC type                   |
| Crafting                   | No          | Planned                                              |
| Economy/Trading            | Partial     | Shopkeeper only; no P2P trade                        |
| Skills (beyond profession) | No          | No skill trees / skill points                        |
| Friends list               | No          | Issue #147                                           |
| Moderation tools           | Partial/No  | Issues #139–#141                                     |


---

## References

- Bounded contexts: [docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md](docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md)
- Open issues: [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues)
- Planned features: [README.md](README.md) (lines 111–122), [PLANNING.md](PLANNING.md)
- Party/grouping: [docs/PARTY_SYSTEM_REFERENCE.md](docs/PARTY_SYSTEM_REFERENCE.md), [docs/PLANNING_ephemeral_grouping.md](docs/PLANNING_ephemeral_grouping.md)
