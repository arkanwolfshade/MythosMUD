# npc behavior engine

> 10 nodes

## Key Concepts

- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **Perform wandering behavior using idle movement system.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Check if idle movement should be scheduled based on configuration and timing.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Create a WANDER action message.          Args:             current_time: Curr** (1 connections) — `server/npc/passive_mob_npc.py`
- **Schedule a WANDER action for idle movement if interval has elapsed.          T** (1 connections) — `server/npc/passive_mob_npc.py`
- **Handle wandering action.** (1 connections) — `server/npc/passive_mob_npc.py`

## Relationships

- [command input commands](command_input_commands.md) (5 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (2 shared connections)
- [realtime player connection](realtime_player_connection.md) (1 shared connections)
- [idle movement npc](idle_movement_npc.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*