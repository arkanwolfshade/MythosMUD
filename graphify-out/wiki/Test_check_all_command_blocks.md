# Test check all command blocks

> 123 nodes

## Key Concepts

- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **CommunicationIntegrationProtocol** (10 connections) — `server/npc/npc_protocols.py`
- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **CombatIntegrationProtocol** (7 connections) — `server/npc/npc_protocols.py`
- **._handle_npc_death()** (6 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **._get_npc_instance()** (5 connections) — `server/services/target_resolution_service.py`
- **test_npc_combat_schedule.py** (5 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **.heal()** (4 connections) — `server/npc/npc_base.py`
- **.speak()** (4 connections) — `server/npc/npc_base.py`
- *... and 98 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (34 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (9 shared connections)
- [get current tick()](get_current_tick%28%29.md) (7 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [world](world.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [Any](Any.md) (3 shared connections)
- [PasswordHasher](PasswordHasher.md) (2 shared connections)
- [ensure database directory()](ensure_database_directory%28%29.md) (2 shared connections)
- [QuestCompleted](QuestCompleted.md) (1 shared connections)
- [default cors origins()](default_cors_origins%28%29.md) (1 shared connections)
- [.get explored rooms()](get_explored_rooms%28%29.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_protocols.py`
- `server/realtime/connection_manager.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 360 (91%)
- INFERRED: 35 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*