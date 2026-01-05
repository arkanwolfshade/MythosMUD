# Phantom Hostile Implementation Requirements

**Status**: Partial Implementation (Foundation Complete)

**Last Updated**: 2026-01-02

**Related Documentation**: `docs/lucidity-system.md` (Section 5.1)

---

## Overview

Phantom hostiles are player-specific hallucinatory entities that appear during Fractured and Deranged lucidity tiers. These phantoms are visible only to the hallucinating player and can be engaged in combat, but dissipate immediately upon taking damage.

---

## Specification Requirements

### Frequency and Triggers

From `docs/lucidity-system.md` Section 5.1:

| Tier          | Hallucination Frequency   | Phantom Hostile Behavior                               |
| ------------- | ------------------------- | ------------------------------------------------------ |
| **Fractured** | 25% chance per 30 seconds | 15% chance of non-damaging combat                      |
| **Deranged**  | 45% chance per 20 seconds | Aggressive phantom mobs (attackable but vanish on hit) |

**Key Points**:

- Fractured: When a hallucination triggers, there's a **15% chance** it will be a phantom hostile
- Deranged: When a hallucination triggers, it will be an "aggressive phantom mob" (attackable, vanish on hit)
- Phantoms have **1 HP** (health bar = 1)
- On attack, phantoms **dissipate immediately** but consume commands, spell slots, and stamina
- Combat log marks them as `[Phantom]` **only after dismissal** (not before)

---

## Functional Requirements

### 1. Spawn Behavior

**FR-1.1: Tier-Based Spawn Probability**

- Fractured tier: 15% chance of phantom hostile when hallucination frequency check triggers
- Deranged tier: Always spawn phantom hostile when hallucination frequency check triggers
- Phantom spawns in the player's current room
- Only the hallucinating player can see the phantom

**FR-1.2: Phantom Properties**

- Health: 1 HP (max_dp = 1, current_dp = 1)
- Name: Randomly selected from a pool of phantom names (e.g., "Shambling Horror", "Writhing Shadow")
- Visibility: Player-specific (only visible to the hallucinating player)
- Persistence: Temporary (dissipate on hit)

**FR-1.3: Spawn Event**

- Server sends `phantom_hostile_spawn` hallucination event to the player
- Event includes metadata:
  - `phantom_id`: Unique identifier for this phantom
  - `phantom_name`: Name of the phantom
  - `room_id`: Room where phantom appears
  - `max_dp`: 1
  - `current_dp`: 1
  - `is_non_damaging`: Boolean (true for Fractured, false for Deranged)
  - `tier`: Current lucidity tier

### 2. Combat Integration

**FR-2.1: Combat Instance Creation**

- When player attacks a phantom, create a combat instance
- Phantom participant has:
  - `participant_type`: `CombatParticipantType.NPC`
  - `max_dp`: 1
  - `current_dp`: 1
  - `is_phantom`: true (custom flag for phantom identification)

**FR-2.2: Combat Mechanics**

- Fractured tier: Non-damaging combat (phantoms do not deal damage to player)
- Deranged tier: Phantoms can deal damage, but still vanish on hit
- Player attacks consume:
  - Commands (attack command used)
  - Spell slots (if casting spells)
  - Stamina (normal combat resource consumption)

**FR-2.3: Dissipation Logic**

- On taking damage (reaching 0 DP), phantom immediately dissipates
- No XP reward for defeating phantoms
- Combat ends immediately
- Phantom removed from active tracking

**FR-2.4: Combat Log Marking**

- Combat log messages for phantom attacks/damage/death should include `[Phantom]` tag
- Tag should appear **only after dismissal** (when phantom reaches 0 DP)
- Example: "The Shambling Horror [Phantom] dissipates into nothingness."

### 3. Player-Specific Visibility

**FR-3.1: Single-Player Visibility**

- Phantom entities are only visible to the hallucinating player
- Other players in the same room cannot see the phantom
- Phantom should not appear in room occupants list for other players
- Combat involving phantoms should not be visible to other players

**FR-3.2: Client-Side Rendering**

- Client receives `phantom_hostile_spawn` hallucination event
- Client renders phantom entity in the room (player-specific rendering)
- Phantom appears in player's room view but not in room occupants for others
- Phantom disappears when dissipated

### 4. Tracking and Cleanup

**FR-4.1: Active Phantom Tracking**

- Server tracks active phantoms per player
- Each phantom has unique ID: `phantom_{player_id}_{uuid}`
- Tracking allows cleanup on player disconnect or tier change

**FR-4.2: Cleanup Scenarios**

- Player tier changes (no longer Fractured/Deranged)
- Player disconnects
- Phantom dissipates (normal combat flow)
- Player leaves room (phantoms remain room-bound, could persist or despawn)

---

## Implementation Status

### ✅ Completed

1. **PhantomHostileService Foundation** (`server/services/phantom_hostile_service.py`)
   - Service structure created
   - Phantom name generation (8 phantom names)
   - Spawn probability logic (Fractured: 15%, Deranged: always)
   - Phantom data structure creation
   - Active phantom tracking (in-memory dictionary)

2. **Hallucination Event Integration** (`server/services/passive_lucidity_flux_service.py`)
   - Integrated into passive lucidity flux service
   - Calls `PhantomHostileService.should_spawn_phantom_hostile()` when hallucination triggers
   - Sends `phantom_hostile_spawn` hallucination events with metadata

3. **Frequency System Integration**
   - Phantom spawning integrated with tier-based hallucination frequency system
   - Respects cooldowns (Fractured: 30s, Deranged: 20s)

### ❌ Not Yet Implemented

1. **Combat Integration**
   - No combat instance creation for phantoms
   - No 1 HP phantom participant creation
   - No special dissipation logic in combat system
   - No `[Phantom]` tags in combat logs
   - No handling of non-damaging combat for Fractured tier

2. **Player-Specific Visibility System**
   - No player-specific NPC/entity system
   - Current NPC system is multi-player (all players see same NPCs)
   - Need architectural solution for player-specific entities

3. **Client-Side Rendering**
   - No client handling for `phantom_hostile_spawn` events
   - No phantom entity rendering in room view
   - No player-specific occupant display logic

4. **Attack Command Integration**
   - No integration with attack commands to detect phantom targets
   - No automatic combat instance creation when player attacks phantom

---

## Architectural Challenges

### Challenge 1: Player-Specific Entity System

**Problem**: The current NPC system is designed for multi-player visibility. All NPCs are visible to all players in a room. Phantom hostiles need to be visible only to the hallucinating player.

**Current Architecture**:

- NPCs stored in `NPCLifecycleManager.active_npcs` (global, multi-player)
- Room occupants include NPCs visible to all players
- Combat system uses NPC instances from lifecycle manager

**Potential Solutions**:

**Option A: Client-Side Only Rendering (Simplest)**

- Server sends hallucination events with phantom metadata
- Client renders phantom entities locally (not synced with server NPC system)
- Combat handled via special attack commands that create temporary combat instances
- **Pros**: Minimal server changes, no new entity system needed
- **Cons**: Combat integration requires special handling, harder to validate client state

**Option B: Server-Side Player-Specific Entity Tracking**

- Create new `PhantomEntityManager` that tracks phantoms per player
- Phantoms stored separately from NPC system
- Combat system checks both NPC system and phantom system for targets
- **Pros**: Server-side validation, cleaner architecture
- **Cons**: Requires new entity system, more complex

**Option C: Extended NPC System with Visibility Flags**

- Extend NPC system to support player-specific visibility
- Add `visible_to_players: set[str]` or `is_hallucination: bool` flags
- Filter NPCs in room occupant queries based on visibility
- **Pros**: Reuses existing NPC infrastructure
- **Cons**: Modifies core NPC system, potential performance impact

**Recommendation**: Start with Option A (client-side rendering) for MVP, migrate to Option B/C if needed for combat validation or multiplayer consistency.

### Challenge 2: Combat Integration with 1 HP Phantoms

**Problem**: Combat system needs to handle phantoms with special properties:

- 1 HP (always die on first hit)
- Immediate dissipation (no death animation/delay)
- No XP reward
- `[Phantom]` tag in combat logs
- Non-damaging combat for Fractured tier

**Current Architecture**:

- Combat participants use `CombatParticipant` dataclass
- NPC participants have `participant_type: CombatParticipantType.NPC`
- Death handling in `CombatDeathHandler.handle_npc_death()`
- Combat logs published via `CombatEventPublisher`

**Implementation Approach**:

1. **Add Phantom Flag to CombatParticipant**
   - Extend `CombatParticipant` with optional `is_phantom: bool = False`
   - Or use metadata dict for extensibility

2. **Phantom Detection in Combat**
   - When creating combat instance, check if target is a phantom (via `phantom_id` in metadata)
   - Mark combat participant as phantom
   - Set max_dp and current_dp to 1

3. **Special Death Handling**
   - Modify `CombatDeathHandler.handle_npc_death()` to check for phantom flag
   - Skip XP reward for phantoms
   - Send special dissipation message with `[Phantom]` tag
   - Immediately end combat

4. **Combat Log Tagging**
   - Modify `CombatEventPublisher` to add `[Phantom]` tag when publishing NPC death events for phantoms
   - Or modify combat message formatting to include tag

5. **Non-Damaging Combat (Fractured)**
   - Check `is_non_damaging` flag from phantom metadata
   - Skip damage application to player when phantom attacks
   - Still consume player resources (stamina, etc.)

### Challenge 3: Attack Command Integration

**Problem**: Players need to be able to attack phantoms. Current attack commands target NPCs by name or ID from the room's NPC list. Phantoms won't be in the standard NPC list.

**Current Architecture**:

- Attack commands use `CombatService` to initiate combat
- Target resolution via `NPCCombatDataProvider.get_npc_combat_data()`
- Targets must exist in `NPCLifecycleManager.active_npcs`

**Implementation Approach**:

1. **Phantom Target Resolution**
   - Extend attack command to check for phantom targets
   - Query `PhantomHostileService.get_active_phantoms()` for player
   - Match target name/ID against active phantoms
   - Create phantom combat data structure

2. **Combat Instance Creation**
   - When attacking phantom, create combat instance with phantom participant
   - Use `PhantomHostileService.create_phantom_hostile_data()` to get phantom properties
   - Set participant `is_phantom=True` and `max_dp=1`, `current_dp=1`

3. **Combat Flow**
   - Normal combat flow (turns, attacks, damage)
   - Special handling on phantom death (dissipation, no XP, `[Phantom]` tag)

---

## Design Decisions Needed

### Decision 1: Entity Storage and Visibility

**Question**: Where should phantom entities be stored and how should visibility be managed?

**Options**:

- A) Client-side only (hallucination events trigger client rendering)
- B) Server-side player-specific tracking (separate from NPC system)
- C) Extended NPC system with visibility flags

**Recommendation**: Start with A, document migration path to B/C if needed.

### Decision 2: Combat Instance Creation Timing

**Question**: When should combat instances be created for phantoms?

**Options**:

- A) On spawn (phantom appears in combat-ready state)
- B) On attack command (create combat instance when player attacks)
- C) Automatic (phantom attacks player, combat starts automatically)

**Recommendation**: B (on attack command) - matches current NPC combat flow, gives player agency.

### Decision 3: Fractured Tier Non-Damaging Combat

**Question**: How should "non-damaging combat" work for Fractured tier phantoms?

**Options**:

- A) Phantoms cannot deal damage to player (damage set to 0)
- B) Combat animations/effects but no actual HP loss
- C) Phantoms deal damage but it's immediately restored/healed

**Recommendation**: A (set damage to 0) - simplest implementation, clear to players.

### Decision 4: Room Persistence

**Question**: Should phantoms persist when player leaves room, or despawn?

**Options**:

- A) Phantoms despawn when player leaves room
- B) Phantoms persist in room (player can return to fight them)
- C) Phantoms persist but with timeout (e.g., 5 minutes)

**Recommendation**: A (despawn on room leave) - simpler, prevents phantom buildup, matches hallucination nature.

---

## Implementation Plan

### Phase 1: Foundation (✅ COMPLETED)

- [x] Create `PhantomHostileService`
- [x] Integrate with hallucination frequency system
- [x] Send phantom spawn events

### Phase 2: Combat Integration (PENDING)

- [ ] Add `is_phantom` flag to `CombatParticipant` (or metadata)
- [ ] Extend attack command to resolve phantom targets
- [ ] Create combat instances with 1 HP phantom participants
- [ ] Implement phantom dissipation logic (no XP, special message)
- [ ] Add `[Phantom]` tags to combat logs
- [ ] Handle non-damaging combat for Fractured tier

### Phase 3: Client-Side Rendering (PENDING)

- [ ] Handle `phantom_hostile_spawn` events in client
- [ ] Render phantom entities in room view (player-specific)
- [ ] Display phantoms in player's room occupants (filtered from others)
- [ ] Handle phantom disappearance on dissipation

### Phase 4: Cleanup and Edge Cases (PENDING)

- [ ] Cleanup phantoms on player disconnect
- [ ] Cleanup phantoms on tier change (no longer Fractured/Deranged)
- [ ] Handle room leave (despawn phantoms)
- [ ] Handle multiple phantoms (tracking, cleanup)

---

## Testing Considerations

### Unit Tests Needed

1. **PhantomHostileService**
   - Spawn probability calculation (Fractured: 15%, Deranged: always)
   - Phantom name generation
   - Active phantom tracking (add, remove, clear)
   - Phantom data structure creation

2. **Combat Integration**
   - Combat instance creation with phantom participants
   - Phantom dissipation on death (no XP, special message)
   - `[Phantom]` tag in combat logs
   - Non-damaging combat for Fractured tier

3. **Attack Command**
   - Phantom target resolution
   - Combat initiation with phantom targets

### Integration Tests Needed

1. **End-to-End Flow**
   - Hallucination frequency triggers → Phantom spawns → Player attacks → Phantom dissipates
   - Multiple phantoms tracking
   - Cleanup on tier change
   - Cleanup on disconnect

2. **Multi-Player Visibility**
   - Player A sees phantom, Player B in same room does not
   - Combat with phantom not visible to other players

---

## Related Files

### Server-Side

- `server/services/phantom_hostile_service.py` - Phantom spawning and tracking
- `server/services/hallucination_frequency_service.py` - Frequency checks
- `server/services/passive_lucidity_flux_service.py` - Integration point
- `server/services/lucidity_event_dispatcher.py` - Event sending
- `server/services/combat_service.py` - Combat system (needs modification)
- `server/services/combat_death_handler.py` - Death handling (needs modification)
- `server/services/combat_event_handler.py` - Event publishing (needs modification)
- `server/models/combat.py` - Combat models (may need extension)
- `server/commands/attack_command.py` or similar - Attack command (needs modification)

### Client-Side

- `client/src/utils/lucidityEventUtils.ts` - Hallucination event processing
- `client/src/components/ui-v2/eventHandlers/` - Event handler for `phantom_hostile_spawn`
- Room rendering components - Display phantom entities
- Combat UI components - Display phantom combat

---

## Notes

- Phantom hostiles are a **complex feature** requiring architectural decisions
- Current implementation provides foundation but needs combat integration and client rendering
- Consider starting with simplified version (client-side rendering only) and iterating
- Full implementation may require new entity system or extension of existing NPC system
- Combat integration is the most critical missing piece for core functionality

---

## References

- `docs/lucidity-system.md` - Section 5.1 (Hallucination & Phantom Event Tables)
- `server/services/phantom_hostile_service.py` - Current implementation
- `server/services/hallucination_frequency_service.py` - Frequency system
- `server/services/combat_service.py` - Combat system architecture
