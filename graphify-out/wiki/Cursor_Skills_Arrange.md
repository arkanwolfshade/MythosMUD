# Cursor Skills Arrange

> 11 nodes

## Key Concepts

- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **Calculate weight for an exit based on distance from spawn.          Args:** (1 connections) — `server/npc/idle_movement.py`
- **Calculate weights for all exits.          Args:             valid_exits: Dict** (1 connections) — `server/npc/idle_movement.py`
- **Select exit based on weighted probabilities.          Args:             exit_** (1 connections) — `server/npc/idle_movement.py`
- **Select an exit using weighted random selection favoring exits closer to spawn ro** (1 connections) — `server/npc/idle_movement.py`
- **Calculate approximate distance between two rooms.          This is a simplifie** (1 connections) — `server/npc/idle_movement.py`

## Relationships

- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (5 shared connections)
- [Dual Connection Monitoring Guide](Dual_Connection_Monitoring_Guide.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*