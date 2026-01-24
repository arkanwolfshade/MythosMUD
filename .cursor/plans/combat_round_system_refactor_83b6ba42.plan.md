---
name: Combat Round System Refactor
overview: Refactor combat system from turn-based to round-based where 1 combat round = 100 server ticks (10 seconds), all combatants act each round in initiative order, and actions can be queued for execution in subsequent rounds.
todos:
  - id: combat-model-update
    content: "Update CombatInstance model: change turn_interval_ticks to 100, keep next_turn_tick, add queued_actions and round_actions fields"
    status: completed
  - id: combat-processor-refactor
    content: "Refactor CombatTurnProcessor: change semantics to round-based (all participants act each round in initiative order), keep method names"
    status: completed
  - id: action-queue-service
    content: "Create CombatActionQueue service: manage queued actions for participants, support action queuing and retrieval"
    status: completed
  - id: combat-service-integration
    content: "Update CombatService: add action queuing methods, update combat processing to use round-based system"
    status: completed
  - id: command-queuing
    content: "Update command handlers: queue combat commands (/attack, /heal) instead of immediate execution"
    status: completed
  - id: spell-queuing
    content: "Update magic service: queue spell casting actions for next round execution"
    status: completed
  - id: game-tick-integration
    content: "Update game_tick_processing: call round-based combat processing instead of turn-based"
    status: completed
  - id: config-updates
    content: "Update configuration: change combat_tick_interval default from 6 to 10 seconds (keep name, change semantics)"
    status: completed
  - id: test-updates
    content: "Update all combat tests: adapt to round-based system, test action queuing, initiative ordering"
    status: completed
  - id: documentation
    content: "Update combat system documentation: reflect round-based mechanics, action queuing, initiative system"
    status: completed
isProject: false
---

# Combat Round System Refactor Plan

## Overview

Refactor the combat system from a sequential turn-based system to a round-based system where:

- **1 combat round = 100 server ticks = 10 realtime seconds**
- **All combatants act in each round** - every participant acts every round
- **Within each round, combatants act sequentially in initiative order** (highest dexterity first)
- **Actions can be queued** (e.g., `/heal` command queued in round 1, executes in round 2)

## Current System Analysis

### Current Architecture

- **Turn-based**: Participants act sequentially (`current_turn` index cycles through `turn_order`)
- **Turn interval**: `turn_interval_ticks = 6` (each turn = 6 ticks)
- **Round completion**: Round increments when `current_turn` wraps around
- **Auto-progression**: `CombatTurnProcessor` advances turns every `turn_interval_ticks`
- **Action execution**: Immediate (no queuing system)

### Key Files

- `server/models/combat.py` - CombatInstance model with turn-based fields
- `server/services/combat_turn_processor.py` - Processes individual turns sequentially
- `server/services/combat_initialization.py` - Creates combat instances
- `server/services/combat_service.py` - Core combat logic
- `server/app/game_tick_processing.py` - Calls combat tick processing

## Required Changes

**IMPORTANT: We are NOT renaming any fields or methods.** We keep all "turn" terminology and only change values and semantics.

### 1. Update CombatInstance Model (`server/models/combat.py`)

**Changes:**

- Change `turn_interval_ticks` value from `6` to `100` (keep name, change value - now represents round interval)
- Keep `next_turn_tick` name (now represents when next round starts)
- Keep `combat_round` field (already exists) - tracks current round number for multi-turn actions
- Repurpose or remove `current_turn` - no longer needed to track "whose turn" (all act each round), but may be repurposed for other timing needs
- Add `queued_actions: dict[UUID, list[CombatAction]]` - Actions queued per participant
- Add `round_actions: dict[UUID, CombatAction]` - Actions for current round
- Modify `advance_turn()` to process all participants in initiative order and increment `combat_round` (keep name, change semantics)

**Updated fields:**

```python
turn_interval_ticks: int = 100  # 100 ticks = 10 seconds (round interval)
next_turn_tick: int = 0  # When next round starts
combat_round: int = 0  # Current round number (already exists - tracks round for multi-turn actions)
# current_turn: int = 0  # May be repurposed or removed (no longer tracks "whose turn")
queued_actions: dict[UUID, list[CombatAction]] = field(default_factory=dict)
round_actions: dict[UUID, CombatAction] = field(default_factory=dict)
```

### 2. Refactor CombatTurnProcessor (`server/services/combat_turn_processor.py`)

**Changes:**

- Keep `process_game_tick()` method name (semantics change to round-based)
- Change turn-based logic to round-based logic (keep method names, change behavior)
- Process ALL participants EVERY round (not alternating)
- Within each round, execute actions sequentially in initiative order (highest dexterity first)
- Execute queued actions before default actions
- Handle action queuing for commands like `/heal`

**Updated method structure:**

```python
async def process_game_tick(self, current_tick: int, active_combats: dict, auto_progression_enabled: bool) -> None:
    """Process combat round - all participants act in initiative order each round."""
    for combat in active_combats.values():
        if current_tick >= combat.next_turn_tick:
            await self._execute_round(combat, current_tick)

async def _execute_round(self, combat: CombatInstance, current_tick: int) -> None:
    """Execute all actions for a round - all participants act sequentially in initiative order."""
    # 1. Load queued actions into round_actions (actions queued for this round)
    # 2. Generate default actions for participants without queued actions
    # 3. Sort participants by dexterity (highest first) for initiative order
    # 4. Execute actions sequentially in initiative order (all participants act this round)
    # 5. Track round number via combat.combat_round for multi-turn action timing
    # 6. Advance to next round via advance_turn() (increments combat_round)
```

### 3. Add Action Queuing System

**New file:** `server/services/combat_action_queue.py`

**Purpose:** Manage queued combat actions (spells, special abilities, etc.)

**Key methods:**

- `queue_action(combat_id, participant_id, action)` - Queue action for next round
- `get_queued_actions(combat_id, participant_id)` - Get actions for participant
- `clear_queued_actions(combat_id, participant_id)` - Clear after execution

**Integration points:**

- Command handlers (e.g., `/heal`) queue actions instead of executing immediately
- Combat service checks for queued actions before generating default actions

### 4. Update Combat Initialization (`server/services/combat_initialization.py`)

**Changes:**

- Set `turn_interval_ticks = 100` (changed from 6 to represent round interval)
- Set `next_turn_tick = current_tick + 100` (when next round starts)
- Initialize `queued_actions` and `round_actions` dictionaries

### 5. Update Combat Service (`server/services/combat_service.py`)

**Changes:**

- Keep `turn_interval_seconds` but change default to `10` (represents round interval)
- Add method to queue actions: `queue_combat_action(combat_id, participant_id, action)`
- Update combat processing to use round-based system
- Modify `process_attack()` to support immediate execution vs queued execution

### 6. Integrate Command Queuing

**Files to modify:**

- `server/commands/combat.py` - Queue `/attack` commands instead of immediate execution
- `server/game/magic/magic_service.py` - Queue spell casting actions
- `server/services/player_combat_service.py` - Support action queuing

**Logic:**

- When player issues command during combat, queue it for next round
- Commands execute in initiative order within the round
- If no command queued, use default action (basic attack)

### 7. Update Game Tick Processing (`server/app/game_tick_processing.py`)

**Changes:**

- Keep `process_combat_tick()` calling `process_game_tick()` (semantics change to round-based)
- Ensure combat processing happens every tick (not just on round boundaries)

### 8. Update Configuration (`server/config/models.py`)

**Changes:**

- Keep `combat_tick_interval` name (semantics change - now represents round interval)
- Change default value from `6` to `10` seconds (100 ticks)

## Implementation Steps

### Phase 1: Model Changes

1. Update `CombatInstance` dataclass: change `turn_interval_ticks` to 100, add queuing fields
2. Keep `combat_round` field for tracking round number (needed for multi-turn actions)
3. Evaluate `current_turn` field - repurpose or remove based on multi-turn action needs
4. Add `CombatAction` queuing support with round tracking
5. Update `advance_turn()` method to increment `combat_round` (semantics change, name stays)
6. Add action queuing methods that track which round actions execute

### Phase 2: Processor Refactor

1. Refactor `CombatTurnProcessor` to round-based logic
2. Implement initiative-based action ordering
3. Add queued action execution logic
4. Update default action generation

### Phase 3: Action Queue System

1. Create `CombatActionQueue` service
2. Integrate with combat service
3. Add queuing methods for commands/spells

### Phase 4: Command Integration

1. Update combat command handler to queue actions
2. Update magic service to queue spell actions
3. Add action validation and execution

### Phase 5: Testing & Validation

1. Update unit tests for round-based system
2. Test action queuing and execution
3. Test initiative ordering
4. Test round timing (100 ticks = 10 seconds)

## Example Flow (After Changes)

**Combat between Player AP (DEX 90) and NPC NP (DEX 50):**

**Round 1 (tick 0-99):**

- Tick 0: Combat starts, `next_turn_tick = 100`
- Tick 0-99: Players can queue actions during the round
- Tick 0: AP queues `/heal` command for Round 2
- Tick 0: **Round 1 actions execute sequentially in initiative order:**
  - AP attacks NP (DEX 90, goes first)
  - NP attacks AP (DEX 50, goes second)
- Tick 100: Round 1 completes, Round 2 begins

**Round 2 (tick 100-199):**

- Tick 100: **Round 2 actions execute sequentially in initiative order:**
  - AP's `/heal` spell executes (DEX 90, goes first - queued from Round 1)
  - NP attacks AP (DEX 50, goes second - default action)
- Tick 200: Round 2 completes, Round 3 begins

**Key Point:** Both AP and NP act in EVERY round. Within each round, they act sequentially based on initiative (dexterity), with AP (DEX 90) always acting before NP (DEX 50).

## Testing Considerations

1. **Round Timing**: Verify rounds advance exactly every 100 ticks
2. **Round Tracking**: Verify `combat_round` increments correctly for multi-turn actions
3. **Initiative Order**: Verify actions execute in dexterity order
4. **Action Queuing**: Verify queued actions execute in correct round
5. **Multi-Turn Actions**: Test actions that take multiple rounds to complete (tracking via `combat_round`)
6. **Multi-Round Effects**: Test effects that last multiple rounds (tracking via `combat_round`)
7. **Default Actions**: Verify default attacks when no action queued
8. **Multiple Participants**: Test with 3+ participants
9. **Spell Casting**: Test queued spell execution and multi-round casting
10. **Combat End**: Verify combat ends correctly with round-based system

## Migration Notes

- Existing combat instances will need to be migrated or allowed to complete
- `turn_interval_ticks` config value changes from 6 to 100 (backward compatibility: old value will be incorrect but won't break)
- Update all combat-related tests
- Update documentation and specs to clarify that "turn" terminology now refers to rounds where all participants act
