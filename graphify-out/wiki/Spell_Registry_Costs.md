# Spell Registry Costs

> 117 nodes · cohesion 0.03

## Key Concepts

- **Spell** (98 connections) — `server/models/spell.py`
- **test_spell.py** (29 connections) — `server/tests/unit/models/test_spell.py`
- **StrEnum** (17 connections)
- **SpellMaterial** (16 connections) — `server/models/spell.py`
- **SpellTargetType** (15 connections) — `server/models/spell.py`
- **spell_targeting.py** (13 connections) — `server/game/magic/spell_targeting.py`
- **test_spell_targeting.py** (13 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **UUID** (12 connections) — `server/game/magic/spell_targeting.py`
- **SpellSchool** (10 connections) — `server/models/spell.py`
- **TargetMatch** (10 connections) — `server/game/magic/spell_targeting.py`
- **spell_registry.py** (9 connections) — `server/game/magic/spell_registry.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **spell.py** (9 connections) — `server/models/spell.py`
- **Spell** (8 connections) — `server/game/magic/spell_registry.py`
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **Spell** (7 connections) — `server/game/magic/spell_targeting.py`
- **._get_combat_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_area_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_entity_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_self_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **SpellRangeType** (6 connections) — `server/models/spell.py`
- **Any** (6 connections) — `server/game/magic/spell_targeting.py`
- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **UUID** (5 connections) — `server/game/magic/spell_costs.py`
- **SpellRepository** (5 connections) — `server/game/magic/spell_registry.py`
- *... and 92 more nodes in this community*

## Relationships

- [[Magic Service Bundle]] (47 shared connections)
- [[Spell Effect Protocols]] (23 shared connections)
- [[Game Magic Spell]] (19 shared connections)
- [[Combat Service Bundle]] (16 shared connections)
- [[Combat Command Handler]] (15 shared connections)
- [[NPC Admin API]] (7 shared connections)
- [[SQLAlchemy Model Base]] (6 shared connections)
- [[Combat Player Broadcasts]] (3 shared connections)
- [[Magic Game Healing]] (3 shared connections)
- [[Magic Lifespan Initialization]] (2 shared connections)
- [[Admin NPC Schemas]] (2 shared connections)
- [[Inventory Service Helpers]] (2 shared connections)

## Source Files

- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 382 (75%)
- INFERRED: 126 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
