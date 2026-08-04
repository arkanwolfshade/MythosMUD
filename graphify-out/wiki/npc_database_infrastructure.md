# npc database infrastructure

> 167 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **UUID** (20 connections)
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (12 connections) — `server/services/combat_service_npc.py`
- **UUID** (11 connections)
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (11 connections) — `server/services/combat_service_npc.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc_via_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (10 connections) — `server/services/combat_service_npc.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (8 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_string_id_mapping()** (8 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **PlayerLifecycleServices** (8 connections) — `server/services/combat_service_types.py`
- **test_combat_service_npc_in_combat.py** (8 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **.get_uuid_for_string_id()** (7 connections) — `server/services/combat_service_npc.py`
- *... and 142 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (38 shared connections)
- [command factories exploration](command_factories_exploration.md) (33 shared connections)
- [Item Instances](Item_Instances.md) (19 shared connections)
- [retry nats handler](retry_nats_handler.md) (18 shared connections)
- [NPC Combat](NPC_Combat.md) (15 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (13 shared connections)
- [services combat sync](services_combat_sync.md) (12 shared connections)
- [player death service](player_death_service.md) (9 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (8 shared connections)
- [movement monitor game](movement_monitor_game.md) (8 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (6 shared connections)
- [combat flee commands](combat_flee_commands.md) (5 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/commands/combat_taunt.py`
- `server/container/bundles/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 699 (91%)
- INFERRED: 66 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*