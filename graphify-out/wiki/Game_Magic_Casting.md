# Game Magic Casting

> 20 nodes · cohesion 0.12

## Key Concepts

- **UUID** (8 connections) — `server/game/magic/casting_state_manager.py`
- **CastingState** (6 connections) — `server/game/magic/casting_state_manager.py`
- **casting_state_manager.py** (5 connections) — `server/game/magic/casting_state_manager.py`
- **.start_casting()** (5 connections) — `server/game/magic/casting_state_manager.py`
- **.complete_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.get_casting_state()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.interrupt_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.get_all_casting_players()** (3 connections) — `server/game/magic/casting_state_manager.py`
- **.is_casting()** (3 connections) — `server/game/magic/casting_state_manager.py`
- **.update_casting_progress()** (3 connections) — `server/game/magic/casting_state_manager.py`
- **Check if a player is currently casting.          Args:             player_id: Pl** (2 connections) — `server/game/magic/casting_state_manager.py`
- **Casting state manager for tracking active spell castings.  This module manages t** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Get the casting state for a player.          Args:             player_id: Player** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Complete and remove a casting state.          Args:             player_id: Playe** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Interrupt and remove a casting state.          Args:             player_id: Play** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Update casting progress for a player.          Args:             player_id: Play** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Represents an active spell casting state.** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Get all players currently casting.          Returns:             list[uuid.UUID]** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Start a new casting state.          Args:             player_id: ID of the playe** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Any** (1 connections) — `server/game/magic/casting_state_manager.py`

## Relationships

- [[Magic Service Bundle]] (8 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Realtime Player Event]] (1 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
