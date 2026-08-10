# Realtime Connection

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
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Exploration Command Factory](Exploration_Command_Factory.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*