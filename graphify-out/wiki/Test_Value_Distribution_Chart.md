# Test Value Distribution Chart

> 15 nodes

## Key Concepts

- **_AppWithState** (10 connections) — `server/realtime/websocket_initial_state.py`
- **persistence()** (7 connections) — `server/tests/unit/game/test_mechanics.py`
- **._get_persistence_from_app()** (6 connections) — `server/commands/combat_handler.py`
- **.check_and_interrupt_rest()** (5 connections) — `server/commands/combat_handler.py`
- **.get_player_and_room()** (5 connections) — `server/commands/combat_handler.py`
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_taunt.py`
- **.get_player_and_room()** (3 connections) — `server/commands/combat_taunt.py`
- **fixture** (2 connections)
- **Check if player is resting or in login grace period, interrupt rest if needed.…** (1 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Resolve persistence from app (container preferred, then app.state). Returns…** (1 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails.** (1 connections) — `server/commands/combat_handler.py`
- **Load player and room from the request context, or return an error dict.** (1 connections) — `server/commands/combat_taunt.py`
- **Return a blocking error dict (e.g. rest), or None if the player may act.** (1 connections) — `server/commands/combat_taunt.py`
- **Minimal FastAPI/Starlette app shape for reading ``state``.** (1 connections) — `server/realtime/websocket_initial_state.py`

## Relationships

- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (3 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (3 shared connections)
- [field_validator](field_validator.md) (2 shared connections)
- [playerHandlers.ts](playerHandlers.ts.md) (2 shared connections)
- [EldritchIcon.tsx](EldritchIcon.tsx.md) (2 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (1 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/game/test_mechanics.py`

## Audit Trail

- EXTRACTED: 26 (81%)
- INFERRED: 6 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*