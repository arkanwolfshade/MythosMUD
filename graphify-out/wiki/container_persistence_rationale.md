# container persistence rationale

> 140 nodes

## Key Concepts

- **SpellEffects** (61 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (45 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **PlayerSpellRepository** (38 connections) — `server/persistence/repositories/player_spell_repository.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **SpellTargetingService** (32 connections) — `server/game/magic/spell_targeting.py`
- **MPRegenerationService** (20 connections) — `server/game/magic/mp_regeneration_service.py`
- **MagicServiceOptionalDeps** (17 connections) — `server/game/magic/magic_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (13 connections) — `server/app/lifespan_magic.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **FastAPI** (9 connections)
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (9 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **.__init__()** (6 connections) — `server/game/magic/spell_effects.py`
- **UUID** (5 connections)
- **Any** (5 connections)
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- *... and 115 more nodes in this community*

## Relationships

- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (48 shared connections)
- [nats services service](nats_services_service.md) (21 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (20 shared connections)
- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (9 shared connections)
- [lucidity active service](lucidity_active_service.md) (9 shared connections)
- [player respawn event](player_respawn_event.md) (8 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (8 shared connections)
- [room occupant manager](room_occupant_manager.md) (7 shared connections)
- [Player Stats](Player_Stats.md) (7 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (7 shared connections)
- [npc combat player](npc_combat_player.md) (6 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (6 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_targeting.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 524 (87%)
- INFERRED: 76 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*