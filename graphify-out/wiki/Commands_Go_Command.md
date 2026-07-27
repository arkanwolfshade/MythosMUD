# Commands Go Command

> 13 nodes · cohesion 0.17

## Key Concepts

- **Any** (12 connections) — `server/commands/go_command.py`
- **_movement_service_for_go_command()** (6 connections) — `server/commands/go_command.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_movement_combat_and_event_bus_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **Resolve player_combat_service and event_bus from DI container or legacy app.stat** (1 connections) — `server/commands/go_command.py`
- **Use container.movement_service when wired; else build MovementService (tests / p** (1 connections) — `server/commands/go_command.py`
- **Return normalized direction string, or None if missing (after logging).** (1 connections) — `server/commands/go_command.py`
- **Resolve ConnectionManager from DI container or legacy app.state.** (1 connections) — `server/commands/go_command.py`
- **Prefer container.async_persistence; fall back to app.state.persistence (legacy).** (1 connections) — `server/commands/go_command.py`
- **Return the room id to use for movement; log if player record disagrees with room** (1 connections) — `server/commands/go_command.py`

## Relationships

- [[Commands Go Command]] (9 shared connections)
- [[Alias Expansion Logic]] (6 shared connections)
- [[Rest Command Flow]] (2 shared connections)
- [[Distributed Event Bus]] (1 shared connections)

## Source Files

- `server/commands/go_command.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
