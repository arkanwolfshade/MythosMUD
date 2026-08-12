# Commands Inventory Display

> 13 nodes

## Key Concepts

- **_FleeCommandHandlerLike** (17 connections) — `server/commands/combat_flee.py`
- **.check_and_interrupt_rest()** (4 connections) — `server/commands/combat_flee.py`
- **.get_player_and_room()** (4 connections) — `server/commands/combat_flee.py`
- **.combat_service()** (3 connections) — `server/commands/combat_flee.py`
- **AppWithState** (3 connections)
- **.movement_service()** (2 connections) — `server/commands/combat_flee.py`
- **.player_position_service()** (2 connections) — `server/commands/combat_flee.py`
- **Handler surface for flee (avoids importing CombatCommandHandler; breaks import c** (1 connections) — `server/commands/combat_flee.py`
- **Combat service if wired.** (1 connections) — `server/commands/combat_flee.py`
- **Movement service if wired.** (1 connections) — `server/commands/combat_flee.py`
- **Player position service if wired (duck-typed; see _ensure_flee_standing).** (1 connections) — `server/commands/combat_flee.py`
- **Interrupt rest / block during grace; return message dict or None.** (1 connections) — `server/commands/combat_flee.py`
- **Load player and room or an error payload.** (1 connections) — `server/commands/combat_flee.py`

## Relationships

- [Investigations Sessions Session](Investigations_Sessions_Session.md) (9 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (2 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (2 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (1 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`

## Audit Trail

- EXTRACTED: 38 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*