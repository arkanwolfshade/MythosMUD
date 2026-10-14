# test_aggression.py

> 16 nodes

## Key Concepts

- **test_aggression.py** (15 connections) — `server/tests/unit/schemas/test_aggression.py`
- **parse_aggression_level()** (8 connections) — `server/schemas/combat/aggression.py`
- **aggression.py** (8 connections) — `server/schemas/combat/aggression.py`
- **parametrize** (5 connections)
- **test_admin_model_normalises_to_an_int()** (4 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_catalog_names_land_on_the_ends_of_the_threat_scale()** (4 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_parse_aggression_level()** (4 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_admin_model_still_rejects_bad_levels()** (3 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_combat_schema_accepts_both_spellings()** (3 connections) — `server/tests/unit/schemas/test_aggression.py`
- **test_combat_schema_rejects_everything_else()** (3 connections) — `server/tests/unit/schemas/test_aggression.py`
- **NPC ``behavior_config["aggression_level"]``: one contract, two spellings…** (1 connections) — `server/schemas/combat/aggression.py`
- **Resolve a stored ``aggression_level`` to an int 0-10, or None when unset or…** (1 connections) — `server/schemas/combat/aggression.py`
- **#999: NPC aggression_level is one contract (int 0-10, or the catalog names…** (1 connections) — `server/tests/unit/schemas/test_aggression.py`
- **Names map to the ends of the 0-10 scale, numbers are clamped, anything…** (1 connections) — `server/tests/unit/schemas/test_aggression.py`
- **aggressive is full threat (same as unset); passive is the damped end.** (1 connections) — `server/tests/unit/schemas/test_aggression.py`
- **A catalog NPC (string level) loads through the admin model and is reported as…** (1 connections) — `server/tests/unit/schemas/test_aggression.py`

## Relationships

- [SecureBaseModel](SecureBaseModel.md) (5 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (4 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/schemas/combat/aggression.py`
- `server/tests/unit/schemas/test_aggression.py`

## Audit Trail

- EXTRACTED: 39 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*