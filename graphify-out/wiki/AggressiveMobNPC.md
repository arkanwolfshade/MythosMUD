# AggressiveMobNPC

> 71 nodes

## Key Concepts

- **AggressiveMobNPC** (31 connections) — `server/npc/aggressive_mob_npc.py`
- **test_aggressive_mob_npc.py** (24 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **_make_aggro()** (13 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **._attack_target_impl()** (6 connections) — `server/npc/aggressive_mob_npc.py`
- **._compute_player_context()** (5 connections) — `server/npc/aggressive_mob_npc.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.attack_target()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._attack_via_combat_integration()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._enrich_behavior_context()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **.flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._get_attack_damage()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_attack_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.__init__()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._log_context_enriched()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._setup_aggressive_mob_behavior_rules()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration.py`
- **test_attack_via_create_task_with_running_loop()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_handles_no_current_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_sets_false_when_no_players_in_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- *... and 46 more nodes in this community*

## Relationships

- [NPCBase](NPCBase.md) (6 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [test_event_reaction_speech.py](test_event_reaction_speech.py.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/models/room.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 118 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*