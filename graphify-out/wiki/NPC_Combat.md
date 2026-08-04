# NPC Combat

> 725 nodes

## Key Concepts

- **get_logger()** (516 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (490 connections) — `server/structured_logging/enhanced_logging_config.py`
- **PlayerService** (140 connections) — `server/game/player_service.py`
- **NPCCombatIntegrationService** (90 connections) — `server/services/npc_combat_integration_service.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **threading.py** (48 connections) — `server/npc/threading.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **test_npc_combat_integration_service.py** (46 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **player_service.py** (45 connections) — `server/game/player_service.py`
- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **nats_exceptions.py** (36 connections) — `server/services/nats_exceptions.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- **SpellTargetingService** (32 connections) — `server/game/magic/spell_targeting.py`
- **NPCCombatLucidity** (30 connections) — `server/services/npc_combat_lucidity.py`
- **movement_service.py** (28 connections) — `server/game/movement_service.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **time_service.py** (26 connections) — `server/time/time_service.py`
- **game.py** (25 connections) — `server/api/game.py`
- **player_respawn.py** (25 connections) — `server/api/player_respawn.py`
- *... and 700 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (81 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (63 shared connections)
- [Loot Generation](Loot_Generation.md) (59 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (58 shared connections)
- [nats services service](nats_services_service.md) (44 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (38 shared connections)
- [Error Conversion](Error_Conversion.md) (35 shared connections)
- [target resolution service](target_resolution_service.md) (34 shared connections)
- [spell game magic](spell_game_magic.md) (34 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (32 shared connections)
- [Room Broadcast](Room_Broadcast.md) (30 shared connections)
- [Player Stats](Player_Stats.md) (30 shared connections)

## Source Files

- `server/api/base.py`
- `server/api/game.py`
- `server/api/player_respawn.py`
- `server/api/skills.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/container/bundles/combat.py`
- `server/dependencies.py`
- `server/game/chat_pose_manager.py`
- `server/game/chat_whisper_tracker.py`
- `server/game/level_service.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_materials.py`

## Audit Trail

- EXTRACTED: 4047 (94%)
- INFERRED: 275 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*