# Messagebatcher Message Batcher

> 3 nodes · cohesion 0.67

## Key Concepts

- **ConnectionEvent** (4 connections) — `server/realtime/connection_state_machine.py`
- **Enum** (2 connections)
- **Events that trigger state transitions.      AI: Explicit events make the FSM det** (1 connections) — `server/realtime/connection_state_machine.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Chat Panel Separation](Chat_Panel_Separation.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*