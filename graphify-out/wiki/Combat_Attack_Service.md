# Combat Attack Service

> 531 nodes

## Key Concepts

- **ApplicationContainer** (151 connections) — `server/container/main.py`
- **Spell** (93 connections) — `server/models/spell.py`
- **player_service.py** (44 connections) — `server/game/player_service.py`
- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **SpellLearningService** (38 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_effects.py** (38 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **PlayerSpellRepository** (37 connections) — `server/persistence/repositories/player_spell_repository.py`
- **lifespan_magic.py** (35 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **main.py** (33 connections) — `server/container/main.py`
- **MagicService** (30 connections) — `server/game/magic/magic_service.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **SpellTargetingService** (29 connections) — `server/game/magic/spell_targeting.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **SpellEffectsDeps** (25 connections) — `server/game/magic/spell_effects.py`
- **CombatBundle** (24 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (24 connections) — `server/container/bundles/realtime.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **MPRegenerationService** (20 connections) — `server/game/magic/mp_regeneration_service.py`
- **spell_targeting.py** (20 connections) — `server/game/magic/spell_targeting.py`
- **player_spell_repository.py** (20 connections) — `server/persistence/repositories/player_spell_repository.py`
- *... and 506 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (92 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (74 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (44 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (24 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (22 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (21 shared connections)
- [Security Headers Middleware](Security_Headers_Middleware.md) (20 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (18 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (15 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (15 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (13 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (12 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`

## Audit Trail

- EXTRACTED: 2343 (92%)
- INFERRED: 217 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*