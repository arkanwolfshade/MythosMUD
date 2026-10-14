# .__init__

> 7 nodes

## Key Concepts

- **RoomDropStore** (5 connections) — `server/services/instance_flush_service.py`
- **.__init__()** (5 connections) — `server/services/instance_flush_service.py`
- **.pop_room_drops_with_prefix()** (2 connections) — `server/services/instance_flush_service.py`
- **Protocol** (1 connections)
- **Where floor drops live (RoomSubscriptionManager).** (1 connections) — `server/services/instance_flush_service.py`
- **Remove and return the drops of every room whose id starts with prefix.** (1 connections) — `server/services/instance_flush_service.py`
- **Wire the instance store, the floor-drop store, and bank box persistence.** (1 connections) — `server/services/instance_flush_service.py`

## Relationships

- [get_logger](get_logger.md) (1 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (1 shared connections)
- [ContainerCreateParams](ContainerCreateParams.md) (1 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (1 shared connections)

## Source Files

- `server/services/instance_flush_service.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*