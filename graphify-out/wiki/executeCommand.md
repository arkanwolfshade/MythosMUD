# executeCommand

> 65 nodes · cohesion 0.05

## Key Concepts

- **PassiveMobNPC** (61 connections) — `server/npc/passive_mob_npc.py`
- **test_npc_base.py** (26 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_passive_mob_npc.py** (19 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **.__init__()** (5 connections) — `server/npc/passive_mob_npc.py`
- **test_npc_base_execute_behavior_sets_in_combat_context()** (4 connections) — `server/tests/unit/npc/test_npc_base.py`
- **._handle_respond_to_greeting()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.respond_to_player()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._setup_passive_mob_behavior_rules()** (3 connections) — `server/npc/passive_mob_npc.py`
- **test_npc_base_execute_behavior()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_combat_stats()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_combat_stats_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_combat_stats_legacy_dp()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_is_alive_property()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_is_npc_in_combat_fails_closed_on_lookup_error()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_move_to_room_blocked_when_in_combat()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **passive_npc()** (3 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/passive_mob_npc.py`
- **._handle_flee()** (2 connections) — `server/npc/passive_mob_npc.py`
- **asyncio** (2 connections)
- **test_npc_base_ai_placeholders()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_from_dict()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_behavior_and_ai_config()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_handle_die_and_idle()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_heal_when_dead_returns_false()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_inventory_operations()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- *... and 40 more nodes in this community*

## Relationships

- [BaseEvent](BaseEvent.md) (8 shared connections)
- [dependencies](dependencies.md) (6 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/tests/unit/npc/test_npc_base.py`
- `server/tests/unit/npc/test_passive_mob_npc.py`

## Audit Trail

- EXTRACTED: 102 (82%)
- INFERRED: 22 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*