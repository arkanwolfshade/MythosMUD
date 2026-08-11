# Calendar NPC Schedule

> 6 nodes

## Key Concepts

- **connection_state_machine.py** (10 connections) — `server/realtime/connection_state_machine.py`
- **ConnectionEvent** (4 connections) — `server/realtime/connection_state_machine.py`
- **Enum** (2 connections)
- **StateMachine** (2 connections)
- **Connection state machine for NATS messaging.  Implements a robust state machine** (1 connections) — `server/realtime/connection_state_machine.py`
- **Events that trigger state transitions.      AI: Explicit events make the FSM det** (1 connections) — `server/realtime/connection_state_machine.py`

## Relationships

- [Room Subscription Helpers](Room_Subscription_Helpers.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (2 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*