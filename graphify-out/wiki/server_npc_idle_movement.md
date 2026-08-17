# server npc idle movement

> 36 nodes

## Key Concepts

- **IdleMovementHandler** (56 connections) — `server/npc/idle_movement.py`
- **idle_movement.py** (18 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.select_exit()** (6 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weights()** (5 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **_cfg_bool()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_distance_to_room()** (3 connections) — `server/npc/idle_movement.py`
- **._calculate_exit_weight()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **._select_weighted_exit()** (3 connections) — `server/npc/idle_movement.py`
- **_cfg_float()** (2 connections) — `server/npc/idle_movement.py`
- **_resolve_spawn_room()** (2 connections) — `server/npc/idle_movement.py`
- **NPC Idle Movement Handler for MythosMUD. This module provides idle movement…** (1 connections) — `server/npc/idle_movement.py`
- **Core gating for idle movement (interval handled by scheduler).** (1 connections) — `server/npc/idle_movement.py`
- **Determine if an NPC should attempt idle movement. Checks multiple conditions: -…** (1 connections) — `server/npc/idle_movement.py`
- *... and 11 more nodes in this community*

## Relationships

- [server tests unit npc test](server_tests_unit_npc_test.md) (32 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server npc init](server_npc_init.md) (3 shared connections)
- [server npc idle movement idlemovementhandler](server_npc_idle_movement_idlemovementhandler.md) (3 shared connections)
- [server npc passive mob npc](server_npc_passive_mob_npc.md) (2 shared connections)
- [server models game rationale 108](server_models_game_rationale_108.md) (2 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (1 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (1 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`

## Audit Trail

- EXTRACTED: 78 (70%)
- INFERRED: 33 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*