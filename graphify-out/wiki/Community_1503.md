# Community 1503

> 5 nodes

## Key Concepts

- **RoomDropStore** (5 connections) — `server/services/instance_flush_service.py`
- **.pop_room_drops_with_prefix()** (2 connections) — `server/services/instance_flush_service.py`
- **Protocol** (1 connections)
- **Where floor drops live (RoomSubscriptionManager).** (1 connections) — `server/services/instance_flush_service.py`
- **Remove and return the drops of every room whose id starts with prefix.** (1 connections) — `server/services/instance_flush_service.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)

## Source Files

- `server/services/instance_flush_service.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*