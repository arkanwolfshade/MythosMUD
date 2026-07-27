# Combat Command Handler

> 404 nodes · cohesion 0.01

## Key Concepts

- **PlayerService** (164 connections) — `server/game/player_service.py`
- **NPCCombatIntegrationService** (106 connections) — `server/services/npc_combat_integration_service.py`
- **TargetMatch** (86 connections) — `server/schemas/shared/target_resolution.py`
- **TargetResolutionService** (74 connections) — `server/services/target_resolution_service.py`
- **CombatCommandHandler** (48 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (45 connections) — `server/schemas/shared/target_resolution.py`
- **AppWithState** (40 connections) — `server/commands/combat_app_protocols.py`
- **CombatValidator** (38 connections) — `server/validators/combat_validator.py`
- **test_combat_handler.py** (34 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **CombatCommandHandlerExtras** (29 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (28 connections) — `server/commands/combat_handler.py`
- **TargetType** (28 connections) — `server/schemas/shared/target_resolution.py`
- **combat_taunt.py** (24 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (23 connections) — `server/commands/combat_taunt.py`
- **target_resolution_service.py** (23 connections) — `server/services/target_resolution_service.py`
- **test_follow_commands.py** (22 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_handler_with_persistence()** (21 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **UUID** (19 connections) — `server/game/player_service.py`
- **handle_follow_command()** (17 connections) — `server/commands/follow_commands.py`
- **Any** (17 connections) — `server/commands/combat_handler.py`
- **_NpcWithLife** (16 connections) — `server/commands/combat_handler.py`
- **AliasStorage** (16 connections) — `server/commands/combat_handler.py`
- **AppWithState** (16 connections) — `server/commands/combat_handler.py`
- **Any** (16 connections) — `server/game/player_service.py`
- **PlayerRead** (16 connections) — `server/game/player_service.py`
- *... and 379 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (58 shared connections)
- [[Alias Expansion Logic]] (44 shared connections)
- [[Magic Service Bundle]] (27 shared connections)
- [[NPC Services Bundle]] (26 shared connections)
- [[NPC Combat Lifecycle]] (25 shared connections)
- [[Player Creation Service]] (19 shared connections)
- [[Dependency Injection Tests]] (19 shared connections)
- [[NPC Admin API]] (18 shared connections)
- [[Combat Taunt Tests]] (18 shared connections)
- [[Distributed Event Bus]] (16 shared connections)
- [[Spell Effects Tests]] (16 shared connections)
- [[Async Persistence Layer]] (15 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/commands/combat_taunt.py`
- `server/commands/follow_commands.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/player_service.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_follow_commands.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 1572 (73%)
- INFERRED: 587 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
