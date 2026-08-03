# nats services service

> 25 nodes

## Key Concepts

- **test_combat_death_handler.py** (30 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **handler()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **combat()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **player_target()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **npc_target()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **combat_service()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_resolve_connection_manager_from_service()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_resolve_connection_manager_missing_getter()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_handle_player_death_events_success()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_handle_player_death_events_broadcast_error()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_create_corpse_skips_without_persistence()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_create_corpse_success()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_create_corpse_service_error()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_log_room_subscribers()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_log_room_subscribers_error()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_resolve_original_npc_id_no_integration()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_resolve_original_npc_id_with_mapping()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_resolve_original_npc_id_missing_mapping()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_publish_npc_death_event_success()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_publish_npc_death_event_error()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_handle_npc_death()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_handle_target_state_mortally_wounded()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_handle_target_state_player_death()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_handle_target_state_mortally_wounded_error()** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **Unit tests for CombatDeathHandler.** (1 connections) — `server/tests/unit/services/test_combat_death_handler.py`

## Relationships

- [Item Instances](Item_Instances.md) (3 shared connections)
- [combat commands handler](combat_commands_handler.md) (2 shared connections)
- [command factories exploration](command_factories_exploration.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_death_handler.py`

## Audit Trail

- EXTRACTED: 57 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*