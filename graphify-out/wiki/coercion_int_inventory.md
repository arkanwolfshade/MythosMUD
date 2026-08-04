# coercion int inventory

> 248 nodes

## Key Concepts

- **PlayerService** (140 connections) — `server/game/player_service.py`
- **SpellEffects** (61 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (45 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **TargetType** (39 connections) — `server/schemas/shared/target_resolution.py`
- **PlayerSpellRepository** (38 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (37 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **spell.py** (28 connections) — `server/models/spell.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **test_spell_costs.py** (19 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_spell_registry.py** (18 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **MagicServiceOptionalDeps** (17 connections) — `server/game/magic/magic_service.py`
- **SpellCostsService** (16 connections) — `server/game/magic/spell_costs.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_create_registry_and_targeting()** (15 connections) — `server/container/bundles/magic.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **SpellSchool** (15 connections) — `server/models/spell.py`
- **SpellEffectType** (15 connections) — `server/models/spell.py`
- *... and 223 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (93 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (42 shared connections)
- [Loot Generation](Loot_Generation.md) (41 shared connections)
- [Database Config](Database_Config.md) (26 shared connections)
- [Player Stats](Player_Stats.md) (24 shared connections)
- [player respawn event](player_respawn_event.md) (23 shared connections)
- [retry nats handler](retry_nats_handler.md) (20 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (18 shared connections)
- [admin auth service](admin_auth_service.md) (14 shared connections)
- [nats services service](nats_services_service.md) (14 shared connections)
- [security sessionManager SessionManager](security_sessionManager_SessionManager.md) (14 shared connections)
- [target resolution service](target_resolution_service.md) (13 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/game/player_service.py`
- `server/models/spell.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/game/magic/test_spell_costs.py`

## Audit Trail

- EXTRACTED: 1215 (90%)
- INFERRED: 142 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*