# TerminalButtonProps

> 489 nodes

## Key Concepts

- **EventBus** (135 connections) — `server/events/event_bus.py`
- **NPCDefinition** (119 connections) — `server/models/npc.py`
- **event_types.py** (79 connections) — `server/events/event_types.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **PlayerLeftRoom** (53 connections) — `server/events/event_types.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **NPCSpawningService** (50 connections) — `server/npc/spawning_service.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **npc.py** (37 connections) — `server/models/npc.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **event_bus.py** (31 connections) — `server/events/event_bus.py`
- **event_reaction_system.py** (29 connections) — `server/npc/event_reaction_system.py`
- **combat_integration.py** (25 connections) — `server/npc/combat_integration.py`
- **spawning_instance_factory.py** (24 connections) — `server/npc/spawning_instance_factory.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **test_npc_combat_integration_class.py** (23 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **spawning_request_execution.py** (19 connections) — `server/npc/spawning_request_execution.py`
- *... and 464 more nodes in this community*

## Relationships

- [parse jsonb column()](parse_jsonb_column%28%29.md) (82 shared connections)
- [get current tick()](get_current_tick%28%29.md) (54 shared connections)
- [combat initialization](combat_initialization.md) (49 shared connections)
- [world](world.md) (44 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (40 shared connections)
- [. repr ()](_repr_%28%29.md) (37 shared connections)
- [Test check all command blocks](Test_check_all_command_blocks.md) (34 shared connections)
- [Any](Any.md) (33 shared connections)
- [. init ()](_init_%28%29.md) (28 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (23 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (22 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (21 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`

## Audit Trail

- EXTRACTED: 2301 (91%)
- INFERRED: 240 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*