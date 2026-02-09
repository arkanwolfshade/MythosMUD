# Effects System Reference Document

> "In the shadowed archives of Miskatonic University, we have compiled extensive research on
> the various implementations of status effects across different MUD architectures. This
> document serves as a comprehensive reference for understanding both established patterns
> and the current state of our own implementation."

## Overview

This document compiles research on MUD effects system implementations from various sources
(Ranvier, Evennia, CircleMUD, general MUD patterns) and analyzes the current MythosMUD
implementation to identify design patterns, conflicts, and implementation choices.

## Research Sources

### Ranvier MUD

**Architecture**: EffectList-based system with scriptable effects

**Key Features**:

- Effects are objects tied to characters via `EffectList`
- Each effect stored as a `.js` file in bundle's `effects/` folder
- Fully scriptable with access to all character events
- Effects receive all events that target characters plus special `updateTick` event
- Can modify incoming/outgoing damage
- Support for healing, damage-over-time, attribute modifications, damage shields,
  attribute penalties (silence, confusion), experience multipliers
- Effects can persist across login/logout
- Duration can be temporary or permanent
- Effects run code on activation, deactivation, and every game tick

**Implementation Pattern**: Event-driven with scriptable effect objects

### Evennia MUD

**Architecture**: Attribute-based system with callback handlers

**Key Features**:

- Uses Attributes system for persistent data storage
- Three ways to work with attributes:
  - `.db` shortcut for simple get/set
  - `.attributes` handler for organized, categorized attributes
  - `AttributeProperty` for class-level declarations
- Callback handler system (`obj.callbacks`) for event-driven implementation
- Event handler system with events (non-persistent) and callbacks (persistent)
- Custom event functions loaded from namespaces
- Event-driven architecture allows extensible callbacks responding to in-game events

**Implementation Pattern**: Event-driven with attribute storage and callback handlers

### CircleMUD

**Architecture**: Bitvector-based AFF flags system

**Key Features**:

- Uses bitvectors to track character conditions
- Standard implementation limited to single `long` integer (~31 flags)
- Extended implementations use multiple bitvector variables (`affected_by1`,
  `affected_by2`, etc.)
- Very fast flag checks using bitwise operations
- Requires tracking which flags belong to which bitvector
- Playerfile compatibility requires conversion utilities

**Implementation Pattern**: Bitvector flags with boolean state tracking

**Limitations**: Not suitable for dynamic effects or effects requiring metadata beyond
presence/absence

### General MUD Patterns

**Common Approaches**:

- Duration tracking: Absolute timestamps vs relative ticks vs remaining counters
- Stacking rules: No stacking (replace), stacking allowed, most potent wins,
  category-based stacking
- Persistence: JSONB columns, separate effects tables, bitvector flags
- Processing: Event-driven callbacks vs tick-based periodic processing

## Current MythosMUD Implementation

### Data Models

**StatusEffect** (`server/models/game.py`):

- Pydantic model with the following fields:
  - `effect_type: StatusEffectType` - Type of effect (enum)
  - `duration: int` - Duration in game ticks (0 = permanent)
  - `intensity: int` - Effect intensity from 1-10
  - `source: str | None` - Source of the effect (item, spell, etc.)
  - `applied_at: datetime` - When the effect was applied
- Method: `is_active(current_tick: int) -> bool` - Checks if effect is still active

**StatusEffectType** (`server/models/game.py`):

- Enum values: `STUNNED`, `POISONED`, `HALLUCINATING`, `PARANOID`, `TREMBLING`,
  `CORRUPTED`, `DELIRIOUS`, `BUFF`

**Player.status_effects** (`server/models/player.py`):

- Stored as JSON string (`Text()` column) containing list of effect dictionaries
- Methods:
  - `get_status_effects() -> list[dict[str, Any]]` - Parse JSON to list
  - `set_status_effects(status_effects: list[dict[str, Any]]) -> None` - Serialize
    list to JSON

**Note**: The Pydantic `Player` model (`server/models/game.py`) also has a
`status_effects: list[StatusEffect]` field for game logic, but the SQLAlchemy model
stores effects as JSON strings.

### Processing System

**Game Tick Processing** (`server/app/game_tick_processing.py`):

- `process_status_effects(app: FastAPI, tick_count: int)` - Processes effects for all
  online players every game tick
- `_process_player_status_effects()` - Processes effects for a single player
- `_process_all_status_effects()` - Iterates through all effects for a player
- `_process_single_effect()` - Processes individual effect, decrements `remaining` counter

**Effect Types Currently Supported**:

- `damage_over_time` - Processes via `_process_damage_over_time_effect()`
  - Checks login grace period (blocks negative effects)
  - Applies damage from effect's `damage` field
  - Uses `damage_type: "status_effect"`
- `heal_over_time` - Processes via `_process_heal_over_time_effect()`
  - Applies healing from effect's `healing` field

**Duration Tracking**:

- Uses both `duration` (initial duration) and `remaining` (current remaining ticks)
- `remaining` counter decrements each tick: `remaining = remaining - 1`
- Effect expires when `remaining <= 0`
- Effects with `duration: 0` are permanent (not currently handled in tick processing)

**Processing Flow**:

1. Every game tick, `process_status_effects()` is called
2. Iterates through all online players
3. For each player, retrieves status effects list
4. For each effect:
   - Decrements `remaining` counter
   - If effect type is `damage_over_time` or `heal_over_time`, applies effect
   - If `remaining > 0`, keeps effect; otherwise removes it
5. Updates player's status effects list if changes occurred

### Application Points

**Spell Effects** (`server/game/magic/spell_effects.py`):

- `_process_status_effect()` method applies status effects from spells
- Creates `StatusEffect` Pydantic model instance
- Converts to dict via `model_dump()` and appends to player's status effects list
- Checks login grace period (blocks negative effects during grace period)
- Applies mastery modifier to duration and intensity

**API Endpoints** (`server/api/player_effects.py`):

- Direct effect application endpoints:
  - `POST /{player_id}/lucidity-loss` - Apply lucidity loss
  - `POST /{player_id}/fear` - Apply fear
  - `POST /{player_id}/corruption` - Apply corruption
  - `POST /{player_id}/occult-knowledge` - Gain occult knowledge
  - `POST /{player_id}/heal` - Heal player
  - `POST /{player_id}/damage` - Damage player
- These endpoints call `PlayerService` methods rather than directly manipulating status
  effects

**Stat Modifications** (`server/game/magic/spell_effects.py`):

- `_process_stat_modify()` handles temporary stat modifications
- If duration > 0, creates a `StatusEffect` with `effect_type: BUFF` to track the
  modification
- Stat changes stored separately in player's stats dict
- Note: Current implementation doesn't automatically revert stat changes when effect
  expires

### Current Limitations and Observations

1. **No Stacking Logic**: Effects are simply appended to the list without checking for
   duplicates or handling stacking rules

2. **Mixed Duration Tracking**: Uses both `duration` and `remaining` fields, which can
   lead to inconsistencies

3. **Limited Effect Types**: Only `damage_over_time` and `heal_over_time` are processed
   in tick system; other effect types (STUNNED, POISONED, etc.) are stored but not
   actively processed

4. **No Stat Reversion**: Temporary stat modifications don't automatically revert when
   effects expire

5. **Storage Format**: Uses JSON string (Text column) instead of JSONB, limiting query
   capabilities

6. **Tick-Based Only**: All effects processed every tick, even if they don't need
   periodic updates

7. **No Effect Scripting**: Effects are data-only; no support for custom scripts or
   callbacks like Ranvier

8. **Intensity Usage Unclear**: Intensity field (1-10) is defined but usage in effect
   processing is not clear

### Implementation: First effect (ADR-009)

The effects system architecture is documented in **ADR-009: Effects System Architecture**
(see [docs/architecture/decisions/ADR-009-effects-system-architecture.md](architecture/decisions/ADR-009-effects-system-architecture.md)).
The first effect migrated to the new system is **game-entry warded** (login grace period):

- **Effect type:** `LOGIN_WARDED` (`StatusEffectType.LOGIN_WARDED`, value `"login_warded"`)
- **Category:** `entry_ward`
- **Storage:** Row in `player_effects` table with tick-based `duration` and `applied_at_tick`
- **Behavior:** When the player dismisses the MOTD, the API starts the grace period by adding
  a LOGIN_WARDED effect via `AsyncPersistenceLayer.add_player_effect()` and setting in-memory
  state on the connection manager. Game tick processing expires effects each tick; when
  LOGIN_WARDED expires, in-memory state is cleared and room occupants are updated.
- **Legacy:** The previous asyncio-based timer in `login_grace_period.py` is retained as a
  fallback when async_persistence/tick getters are not provided; once migration is verified,
  the task can be removed.

## Conflicting Implementation Approaches

### 1. Effect Stacking Rules

**Option A: No Stacking (Replace)**

- Same effect type replaces existing instance
- Most common in tabletop RPGs
- Simplest to implement
- Prevents overpowered stacking
- Example: Applying "Poisoned" when already poisoned replaces the old poison

**Option B: Stacking Allowed**

- Multiple instances of same effect can coexist
- Each instance tracked separately with its own duration
- More complex but allows cumulative effects
- Useful for effects like "damage over time" where multiple sources should stack
- Example: Multiple poison sources each dealing damage independently

**Option C: Most Potent Wins**

- Same effect type: keep the one with highest intensity/duration
- Common in competitive MUDs
- Prevents overpowered stacking while allowing upgrades
- Example: Stronger poison replaces weaker poison, but weaker poison doesn't replace
  stronger

**Option D: Category-Based Stacking**

- Effects grouped by category (buff/debuff/neutral)
- Same category replaces, different categories stack
- Most flexible but complex
- Example: Multiple buffs stack, but new buff replaces old buff; buffs and debuffs stack
  independently

**Current MythosMUD**: No explicit stacking logic found - effects are simply appended to
list, allowing unlimited stacking of same effect type

**Decision**: Most potent wins (Option C) with granular categories. Effects grouped by
granular categories (e.g. poison, stun, lucidity_protection, damage_reduction) rather
than broad "buff/debuff". Stacking rules apply per category: same category uses "most
potent wins", different categories stack independently. This allows fine-grained control
over which effects can coexist.

### 2. Duration Tracking Methods

**Option A: Absolute Timestamp**

- Store `expires_at: datetime` field
- Calculate remaining duration on read: `remaining = expires_at - now()`
- Handles server restarts gracefully (no tick counter needed)
- Works across time zones and server downtime
- Example: `expires_at: 2026-02-10 14:30:00`

**Option B: Relative Ticks**

- Store `duration: int` (total ticks) and `applied_at_tick: int`
- Calculate remaining: `remaining = duration - (current_tick - applied_at_tick)`
- Requires tick counter persistence across server restarts
- More efficient for tick-based games
- Example: `duration: 100, applied_at_tick: 5000` → at tick 5050, remaining = 50

**Option C: Remaining Counter**

- Store `remaining: int` that decrements each tick
- Simplest but requires periodic updates
- Doesn't handle server restarts well (loses progress)
- Current MythosMUD approach (mixed with duration)
- Example: `remaining: 50` → next tick → `remaining: 49`

**Option D: Hybrid Approach**

- Store both `expires_at` (for persistence) and `remaining` (for performance)
- Use `expires_at` for initial calculation, `remaining` for tick processing
- Reconcile on load/restart

**Current MythosMUD**: Uses both `duration` (initial) and `remaining` (current), but
`remaining` is decremented each tick without considering server restarts

**Decision**: Yes, durations survive server restarts. Use relative ticks: store
`duration` and `applied_at_tick`; persist the game tick counter; remaining =
duration - (current_tick - applied_at_tick).

### 3. Effect Storage Architecture

**Option A: JSONB Column (Recommended)**

- Single JSONB column storing array of effects
- Simple queries, atomic updates
- Good for flexible schemas
- Supports indexing on JSONB fields
- PostgreSQL native, efficient for read-heavy workloads
- Example: `status_effects JSONB DEFAULT '[]'::jsonb`

**Option B: JSON String (Current)**

- Single Text column storing JSON string
- Simple but limited querying capabilities
- No indexing support
- Requires parsing on every read
- Current MythosMUD approach
- Example: `status_effects TEXT DEFAULT '[]'`

**Option C: Separate Effects Table**

- Relational table with foreign key to players
- Better for queries, indexing, cascading deletes
- More normalized but more complex
- Requires joins for player data
- Example: `player_effects` table with `player_id`, `effect_type`, `duration`, etc.

**Option D: Bitvector Flags (CircleMUD style)**

- Boolean flags for predefined effects
- Very fast checks, limited to ~31-128 effects
- Not suitable for dynamic effects or effects requiring metadata
- Example: `affected_by BIGINT` with bit flags

**Current MythosMUD**: JSON string (Text column) - could migrate to JSONB for better
querying

**Decision**: Separate effects table (Option B). New table (e.g. `player_effects`) with
player_id, effect_type, category, duration, applied_at_tick, intensity, source, etc.
Better for queries, indexing, and cascading; use joins when loading player state.

### 4. Event-Driven vs Tick-Based Processing

**Option A: Event-Driven (Evennia/Ranvier)**

- Effects register callbacks for specific game events
- Effects react to specific triggers (combat, movement, spell casting, etc.)
- More efficient - only processes when relevant events occur
- Allows effects to modify event behavior
- Example: Poison effect registers callback for "on_take_damage" event

**Option B: Tick-Based (Current)**

- Process all effects every game tick
- Simpler logic, predictable timing
- May be less efficient for rare effects
- All effects processed uniformly
- Current MythosMUD approach
- Example: Every tick, check all effects and decrement counters

**Option C: Hybrid Approach**

- Tick-based for time-based effects (duration, DoT, HoT)
- Event-driven for reactive effects (on damage, on spell cast, etc.)
- Best of both worlds but more complex

**Current MythosMUD**: Tick-based processing in `process_status_effects()` - all effects
processed every tick

**Decision**: Tick-based only (Option B). Process all effects every game tick. Keep logic
simple and timing predictable; no event-driven callbacks for now.

### 5. Stat Modification Tracking

**Option A: Store in Effect Metadata**

- Effect contains stat changes in metadata field
- Revert on expiration by reading metadata
- Requires effect-specific logic for each stat
- Example: `effect.metadata = {"strength": +5, "dexterity": -2}`

**Option B: Separate Modification Registry**

- Track stat modifications separately from effects
- Effects reference modifications by ID
- Cleaner separation of concerns
- Easier to query "what modifies strength?"
- Example: `stat_modifications` table with `effect_id`, `stat_name`, `modifier`

**Option C: Calculate on Demand**

- Don't store modified stats, calculate from base stats + active effects
- Most accurate but requires calculation on every stat access
- Example: `current_strength = base_strength + sum(effect.strength_mod for effect in
active_effects)`

**Current MythosMUD**: Uses StatusEffect with BUFF type for temporary stat mods, but stat
changes stored separately in stats dict. No automatic reversion on expiration.

**Decision**: Calculate on demand (Option C). Don't store modified stats; compute from
base stats + active effects each time. If performance becomes an issue, migrate to
Option B (separate modification registry).

### 6. Effect Scripting and Extensibility

**Option A: Data-Only Effects (Current)**

- Effects are pure data structures
- Effect behavior hardcoded in processing logic
- Simple but not extensible
- Requires code changes for new effect types
- Current MythosMUD approach

**Option B: Scriptable Effects (Ranvier)**

- Effects can contain scripts/callbacks
- Effects register for events and execute custom code
- Highly extensible, allows modding
- More complex, requires sandboxing for security
- Example: Effect file contains JavaScript/Python code for custom behavior

**Option C: Effect Templates with Parameters**

- Predefined effect templates with configurable parameters
- Templates define behavior, parameters customize it
- Balance between extensibility and security
- Example: `damage_over_time` template with `damage_per_tick` parameter

**Current MythosMUD**: Data-only effects with hardcoded processing logic

**Decision**: Data-only (Option A). Effects are pure data; behavior is hardcoded in game
logic. New effect types require code changes. Keeps implementation simple and secure.

### 7. Intensity Scaling

**Current Implementation**: Intensity field (1-10) is defined in StatusEffect model but
usage in effect processing is unclear.

**Possible Approaches**:

- **Linear Scaling**: Intensity directly multiplies effect strength
  - Example: `damage = base_damage * intensity`
- **Exponential Scaling**: Intensity has exponential impact
  - Example: `damage = base_damage * (intensity ^ 1.5)`
- **Category-Based**: Different effects use intensity differently
  - Example: DoT uses linear, stat mods use step function
- **Duration Scaling**: Intensity affects duration instead of strength
  - Example: `duration = base_duration * intensity`

**Decision**: Effect-specific. Each effect type defines how it uses intensity (e.g. DoT
linear, stat mods step function, some ignore it). No single global formula.

## Design Questions for Clarification

The following questions need to be answered to guide the effects system implementation:

1. **Stacking Behavior**: Should identical effect types stack, replace, or use "most potent
   wins"? Should different effect types always stack?

2. **Duration Persistence**: Should durations survive server restarts? If yes, should we
   use absolute timestamps or persist the tick counter?

3. **Effect Categories**: Should we group effects (buffs/debuffs/neutral) with different
   stacking rules per category?

4. **Metadata Storage**: Should stat modifications be stored in effect metadata or tracked
   separately? How should temporary stat changes be reverted when effects expire?

5. **Event Integration**: Should effects register for specific game events (combat, movement,
   etc.) or continue processing every tick? Should we support both approaches?

6. **Storage Migration**: Should we migrate from Text JSON to JSONB for better querying and
   indexing? Or should we use a separate effects table?

7. **Effect Scripting**: Should effects support custom scripts/callbacks like Ranvier, or
   remain data-only with hardcoded processing logic?

8. **Intensity Scaling**: How should intensity (1-10) affect effect strength? Should it be
   linear, exponential, or effect-specific?

9. **Effect Expiration**: How should expired effects be cleaned up? Should we clean up
   immediately on expiration or batch cleanup periodically?

10. **Effect Visibility**: Should players see all active effects, or only certain types?
    Should effects have visibility levels (hidden, visible, detailed)?

## Design Decisions (Recorded)

Decisions made to guide implementation. Questions not yet decided are marked TBD.

1. **Stacking Behavior**: **Most potent wins (Option C).** Same effect type: keep the
   instance with highest intensity or longest duration; new applications replace only if
   they are more potent. Different effect types stack.

2. **Duration Persistence**: **Yes (tick counter).** Durations survive restarts. Store
   `duration` and `applied_at_tick`; persist game tick counter; remaining = duration -
   (current_tick - applied_at_tick).

3. **Effect Categories**: **Yes, granular categories.** Use specific categories (e.g.
   poison, stun, lucidity_protection, damage_reduction) rather than broad buff/debuff.
   Stacking rules apply per category: same category uses "most potent wins", different
   categories stack independently.

4. **Metadata Storage**: **Calculate on demand (Option C).** Compute stats from base +
   active effects on each access. If performance issues arise, migrate to Option B
   (separate modification registry).

5. **Event Integration**: **Tick-based only (Option B).** Process all effects every game
   tick; no event-driven callbacks.

6. **Storage Migration**: **Separate effects table (Option B).** New table (e.g.
   `player_effects`) with player_id, effect_type, category, duration, applied_at_tick,
   intensity, source, etc. Use joins when loading player state.

7. **Effect Scripting**: **Data-only (Option A).** Effects are pure data; behavior
   hardcoded in game logic. No custom scripts or callbacks.

8. **Intensity Scaling**: **Effect-specific.** Each effect type defines how it uses
   intensity (e.g. DoT linear, stat mods step function, some ignore it).

9. **Effect Expiration**: **Immediate cleanup.** Remove the effect as soon as it expires
   during the tick that processes it. Keeps the list accurate at all times.

10. **Effect Visibility**: **Visibility levels.** Each effect has a visibility level:
    hidden (not shown), visible (name and maybe duration), detailed (full info: source,
    intensity, etc.). Levels can be per effect type or per instance. Default: visible.

## Implementation Recommendations

Based on the research and current implementation analysis, here are recommended next
steps:

1. **Immediate**: Implement stacking logic (recommend "most potent wins" or
   category-based)

2. **Short-term**: Migrate from Text JSON to JSONB for better querying

3. **Short-term**: Add automatic stat modification reversion on effect expiration

4. **Medium-term**: Implement event-driven processing for reactive effects while keeping
   tick-based for time-based effects

5. **Medium-term**: Clarify and implement intensity scaling

6. **Long-term**: Consider effect scripting/extensibility if modding support is desired

## References

- Ranvier MUD Effects Documentation: <https://ranviermud.com/coding/effects/>
- Evennia Attributes Documentation: <https://evennia.com/docs/latest/Components/Attributes.html>
- CircleMUD AFF Flags: Various mailing list discussions (1995-1997)
- PostgreSQL JSONB Documentation:
  <https://www.postgresql.org/docs/16/datatype-json.html>
- Current MythosMUD Implementation:
  - `server/models/game.py` - StatusEffect model
  - `server/models/player.py` - Player model with status_effects storage
  - `server/app/game_tick_processing.py` - Tick-based effect processing
  - `server/game/magic/spell_effects.py` - Spell effect application

---

> "The knowledge contained herein represents years of research into the arcane arts of
> status effect implementation. May it guide our implementation decisions wisely."
>
> - Dr. Armitage, Miskatonic University Archives, 2026
