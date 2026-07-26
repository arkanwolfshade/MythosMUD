# CastingStateManager

> 26 nodes · cohesion 0.11

## Key Concepts

- **CastingStateManager** (18 connections) — `server/game/magic/casting_state_manager.py`
- **casting_state_manager.py** (8 connections) — `server/game/magic/casting_state_manager.py`
- **UUID** (8 connections)
- **CastingState** (6 connections) — `server/game/magic/casting_state_manager.py`
- **.start_casting()** (5 connections) — `server/game/magic/casting_state_manager.py`
- **.complete_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.get_casting_state()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.interrupt_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.get_all_casting_players()** (3 connections) — `server/game/magic/casting_state_manager.py`
- **.is_casting()** (3 connections) — `server/game/magic/casting_state_manager.py`
- **.update_casting_progress()** (3 connections) — `server/game/magic/casting_state_manager.py`
- **.clear_all()** (2 connections) — `server/game/magic/casting_state_manager.py`
- **.__init__()** (2 connections) — `server/game/magic/casting_state_manager.py`
- **Any** (1 connections)
- **Casting state manager for tracking active spell castings.  This module manages t** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Check if a player is currently casting.          Args:             player_id: Pl** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Get the casting state for a player.          Args:             player_id: Player** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Complete and remove a casting state.          Args:             player_id: Playe** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Interrupt and remove a casting state.          Args:             player_id: Play** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Update casting progress for a player.          Args:             player_id: Play** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Represents an active spell casting state.** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Get all players currently casting.          Returns:             list[uuid.UUID]** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Clear all casting states (for testing/reset).** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Manages casting state for all active spell castings.      Tracks which players a** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Initialize the casting state manager.** (1 connections) — `server/game/magic/casting_state_manager.py`
- *... and 1 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (6 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [MagicServiceCompletionMixin](MagicServiceCompletionMixin.md) (1 shared connections)
- [SpellRegistry](SpellRegistry.md) (1 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`

## Audit Trail

- EXTRACTED: 79 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*