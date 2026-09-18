# Community 888

> 17 nodes

## Key Concepts

- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_movement_service_for_go_command()** (6 connections) — `server/commands/go_command.py`
- **_cancel_rest_if_moving()** (5 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (5 connections) — `server/commands/go_command.py`
- **_movement_combat_and_event_bus_from_go_app()** (5 connections) — `server/commands/go_command.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **Resolve player_combat_service and event_bus from DI container or legacy…** (1 connections) — `server/commands/go_command.py`
- **Use container.movement_service when wired; else build MovementService (tests /…** (1 connections) — `server/commands/go_command.py`
- **Return normalized direction string, or None if missing (after logging).** (1 connections) — `server/commands/go_command.py`
- **Resolve ConnectionManager from DI container or legacy app.state.** (1 connections) — `server/commands/go_command.py`
- **Cancel rest if active; return interrupt note so movement can continue in the…** (1 connections) — `server/commands/go_command.py`
- **Prefer container.async_persistence; fall back to app.state.persistence (legacy).** (1 connections) — `server/commands/go_command.py`
- **Return the room id to use for movement; log if player record disagrees with…** (1 connections) — `server/commands/go_command.py`
- **Setup and validate go command prerequisites.** (1 connections) — `server/commands/go_command.py`

## Relationships

- [Community 313](Community_313.md) (13 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (8 shared connections)
- [Community 467](Community_467.md) (1 shared connections)
- [Community 1420](Community_1420.md) (1 shared connections)
- [Community 260](Community_260.md) (1 shared connections)
- [Community 442](Community_442.md) (1 shared connections)
- [Community 1081](Community_1081.md) (1 shared connections)

## Source Files

- `server/commands/go_command.py`

## Audit Trail

- EXTRACTED: 43 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*