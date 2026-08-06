# persistence core infrastructure

> 209 nodes

## Key Concepts

- **PlayerService** (140 connections) — `server/game/player_service.py`
- **SpellEffects** (61 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (45 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_lifespan_startup.py** (39 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **PlayerSpellRepository** (38 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (37 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
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
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **_get_item_prototype_count()** (7 connections) — `server/app/lifespan_startup.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- *... and 184 more nodes in this community*

## Relationships

- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (46 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (26 shared connections)
- [player service game](player_service_game.md) (24 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (17 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (17 shared connections)
- [Player Stats](Player_Stats.md) (14 shared connections)
- [nats services service](nats_services_service.md) (13 shared connections)
- [aggro threat services](aggro_threat_services.md) (13 shared connections)
- [persistence container extended](persistence_container_extended.md) (13 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (12 shared connections)
- [player respawn event](player_respawn_event.md) (10 shared connections)
- [spell game magic](spell_game_magic.md) (10 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/app/lifespan_startup.py`
- `server/commands/magic_commands.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/game/player_service.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_registry.py`

## Audit Trail

- EXTRACTED: 797 (86%)
- INFERRED: 130 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*