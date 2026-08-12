# Api Player Respawn

> 10 nodes

## Key Concepts

- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_PlayerPositionServiceLike** (8 connections) — `server/commands/combat_flee.py`
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
- **Protocol** (3 connections)
- **.change_position()** (3 connections) — `server/commands/combat_flee.py`
- **Protocol** (1 connections)
- **Shared Starlette/FastAPI-shaped protocols for combat command modules.  Keeps ``A** (1 connections) — `server/commands/combat_app_protocols.py`
- **Application object with a ``state`` namespace (dynamic attributes).** (1 connections) — `server/commands/combat_app_protocols.py`
- **Surface used when forcing standing before flee.** (1 connections) — `server/commands/combat_flee.py`
- **Set position; flee ignores the return value.** (1 connections) — `server/commands/combat_flee.py`

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (7 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (5 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Commands Inventory Display](Commands_Inventory_Display.md) (2 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (2 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (1 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (1 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (1 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_flee.py`

## Audit Trail

- EXTRACTED: 28 (67%)
- INFERRED: 14 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*