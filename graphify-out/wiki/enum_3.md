# enum

> 12 nodes

## Key Concepts

- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **Check if idle movement should be scheduled based on configuration and timing.…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Create a WANDER action message. Args: current_time: Current timestamp Returns:…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Queue a WANDER action via the thread manager. Args: wander_action: The wander…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Schedule a WANDER action for idle movement if interval has elapsed. This method…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Handle wandering action.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Perform wandering behavior using idle movement system.** (1 connections) — `server/npc/passive_mob_npc.py`

## Relationships

- [RoomDataCache](RoomDataCache.md) (6 shared connections)
- [fixtures/shared/__init__.py](fixtures-shared-__init__.py.md) (2 shared connections)
- [test_look_room.py](test_look_room.py.md) (1 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [login_user](login_user.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*