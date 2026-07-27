# Magic Lifespan Initialization

> 28 nodes · cohesion 0.15

## Key Concepts

- **lifespan_magic.py** (33 connections) — `server/app/lifespan_magic.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (10 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (7 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (7 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (7 connections) — `server/app/lifespan_magic.py`
- **ApplicationContainer** (7 connections) — `server/app/lifespan_magic.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (5 connections) — `server/app/lifespan_magic.py`
- **_validate_magic_prerequisites()** (5 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (3 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (3 connections) — `server/app/lifespan_magic.py`
- **SpellRepositoryClass** (3 connections) — `server/app/lifespan_magic.py`
- **MagicService** (2 connections) — `server/app/lifespan_magic.py`
- **Magic system initialization for application startup.  Extracted from lifespan_st** (1 connections) — `server/app/lifespan_magic.py`
- **Initialize MagicService and attach to app.state.** (1 connections) — `server/app/lifespan_magic.py`
- **Set magic_service reference in combat_service if available.** (1 connections) — `server/app/lifespan_magic.py`
- **Initialize magic system services and wire them to app.state.      DEPRECATED: Th** (1 connections) — `server/app/lifespan_magic.py`
- **Ensure required container services exist before magic initialization.** (1 connections) — `server/app/lifespan_magic.py`
- **Create spell-related repositories.** (1 connections) — `server/app/lifespan_magic.py`
- **Initialize SpellRegistry, load spells, and attach to app.state.** (1 connections) — `server/app/lifespan_magic.py`
- **Initialize SpellTargetingService and attach to app.state.** (1 connections) — `server/app/lifespan_magic.py`
- *... and 3 more nodes in this community*

## Relationships

- [[Magic Service Bundle]] (14 shared connections)
- [[NPC Admin API]] (4 shared connections)
- [[MP Regeneration Service]] (3 shared connections)
- [[Spell Effect Protocols]] (3 shared connections)
- [[Combat Command Handler]] (3 shared connections)
- [[Spell Registry Costs]] (2 shared connections)
- [[Database Manager Tests]] (2 shared connections)
- [[Lifespan Startup Hooks]] (2 shared connections)
- [[Application DI Bundles]] (1 shared connections)
- [[Game Magic Spell]] (1 shared connections)

## Source Files

- `server/app/lifespan_magic.py`

## Audit Trail

- EXTRACTED: 144 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
