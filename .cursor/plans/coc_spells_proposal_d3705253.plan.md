---
name: CoC Spells Proposal
overview: Produce a list of proposed spells drawn from Call of Cthulhu / Grand Grimoire, mapped to MythosMUD's Spell model, with a balanced mix of mythos (lucidity/corruption) and clerical/elemental (MP-only) spells, and recommend how to add them to the game.
todos: []
isProject: false
---

# Proposed Spells from Call of Cthulhu for MythosMUD

## Source and constraints

- **Source**: Call of Cthulhu 7th Edition and _The Grand Grimoire of Cthulhu Mythos Magic_ (Chaosium). Your copies live under `C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium`; that path is not listable/readable from this environment (likely Proton Drive), so spell names and themes below are taken from publicly referenced CoC 7e and Grand Grimoire spell lists.
- **Model**: Every spell must conform to the existing [Spell](e:\projects\GitHub\MythosMUD\server\models\spell.py) Pydantic model and the `mythos_unit.spells` schema in [db/mythos_unit_ddl.sql](e:\projects\GitHub\MythosMUD\db\mythos_unit_ddl.sql) (spell_id, name, description, school, mp_cost, lucidity_cost, corruption_on_learn/cast, casting_time_seconds, target_type, range_type, effect_type, effect_data, materials).
- **Priority**: Balanced mix—some **mythos** (lucidity/corruption costs, school `mythos`), some **clerical** or **elemental** (MP-only, schools `clerical` / `elemental` / `other`).

---

## Proposed spell list (first batch)

Spells are grouped by intended school and cost type. Each row is a candidate for one DB row; exact numeric costs and effect_data should be tuned in implementation.

| Spell name (display) | spell_id (suggested) | School             | Effect type                    | Target        | Cost theme                      | Notes                                           |
| -------------------- | -------------------- | ------------------ | ------------------------------ | ------------- | ------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shrivelling          | shrivelling          | mythos             | damage                         | entity        | MP + lucidity + corruption      | Classic attack; single target                   |
| Fist of Yog-Sothoth  | fist_of_yog_sothoth  | mythos             | damage                         | entity/area   | MP + lucidity + corruption      | Area or single                                  |
| Breath of the Deep   | breath_of_the_deep   | mythos             | damage                         | entity/area   | MP + lucidity                   | Drowning/water theme                            |
| Death Spell          | death_spell          | mythos             | damage                         | entity        | High MP + lucidity + corruption | Lethal, high cost                               |
| Melt Flesh           | melt_flesh           | mythos             | damage                         | entity        | MP + lucidity + corruption      | Horrific damage                                 |
| Dominate             | dominate             | mythos             | status_effect                  | entity        | MP + lucidity                   | Control target                                  |
| Cloud Memory         | cloud_memory         | mythos             | status_effect                  | entity        | MP + lucidity                   | Remove aggro from mob for a period              |
| Implant Fear         | implant_fear         | mythos             | status_effect                  | entity        | MP + lucidity + corruption      | Cause target to /flee; flee not yet implemented |
| Mindblast            | mindblast            | mythos             | damage / lucidity_adjust       | entity        | MP + lucidity                   | Mental damage / SAN                             |
| Curse                | curse                | mythos             | status_effect or stat_modify   | entity        | MP + lucidity + corruption      | Generic curse                                   |
| Evil Eye             | evil_eye             | mythos             | status_effect                  | entity        | MP + lucidity                   | Curse/hex                                       |
| Steal Life           | steal_life           | mythos             | heal (self) + damage (target)  | entity        | MP + lucidity                   | Drain target, heal caster                       |
| Power Drain          | power_drain          | mythos             | stat_modify / damage           | entity        | MP + lucidity                   | Drain MP or stats                               |
| Cause Blindness      | cause_blindness      | mythos             | status_effect                  | entity        | MP + lucidity                   | Blind target                                    |
| Cure Blindness       | cure_blindness       | clerical           | status_effect                  | entity        | MP only                         | Remove blindness                                |
| Heal                 | heal                 | clerical           | heal                           | entity/self   | MP only                         | Restore HP                                      |
| Bind Wound           | bind_wound           | clerical           | heal                           | self/entity   | MP only                         | Minor heal                                      |
| Warding              | warding              | clerical/elemental | status_effect                  | self/area     | MP only                         | Protective ward                                 |
| Light                | light                | elemental          | create_object or status_effect | location/self | MP only                         | Create light                                    |
| Extinguish           | extinguish           | elemental          | status_effect                  | location      | MP only                         | Put out flames                                  |
| Resist Cold          | resist_cold          | elemental          | stat_modify / status_effect    | self          | MP only                         | Temp resistance                                 | **Effect type mapping**: Use existing [SpellEffectType](e:\projects\GitHub\MythosMUD\server\models\spell.py) values only: `heal`, `damage`, `status_effect`, `stat_modify`, `lucidity_adjust`, `corruption_adjust`, `teleport`, `create_object`. Spells that in CoC do “SAN loss” map to `lucidity_adjust` (or `damage` with flavor); “corruption” can use `corruption_adjust` or be encoded in spell costs only. |

**Range/target**: Use existing [SpellTargetType](e:\projects\GitHub\MythosMUD\server\models\spell.py) and [SpellRangeType](e:\projects\GitHub\MythosMUD\server\models\spell.py) (e.g. touch, same_room, entity, self, area). Multi-target CoC spells map to `entity` (single) or `area`/`all` where the engine supports it.

**Cloud Memory (game effect)**: In-game effect is to remove aggro from the target mob for a period of time (e.g. mob ceases to treat the caster—or optionally all players—as hostile for the duration). Use `effect_type: status_effect` with `effect_data` including a duration (e.g. `duration_seconds`) and a key such as `clear_aggro` or `suppress_aggro`. Implementing this will require combat/NPC logic to clear or ignore aggro for that entity for the given duration (the codebase has `threat_detected` and hostile behaviour in NPC/combat; spell execution will need to apply this status and have the combat or NPC layer respect it).

**Implant Fear (game effect)**: In-game effect is to cause the target to flee (equivalent to the target executing `/flee`). Use `effect_type: status_effect` with `effect_data` indicating forced flee (e.g. `force_flee: true`). **Note: `/flee` is not yet implemented.** Implementing Implant Fear will therefore require implementing the `/flee` command (or equivalent flee behaviour) first; spell execution then triggers that behaviour on the target entity (player or NPC).

---

## Gaps and extensions

- **Materials**: CoC often uses components; optional `materials` (list of item_id + consumed) can be filled later or left empty for the first batch.
- **New effect types**: If you later add summoning, binding, or “create creature,” that would require a new `SpellEffectType` and effect execution in [combat_turn_processor](e:\projects\GitHub\MythosMUD\server\services\combat_turn_processor.py) / magic service. This plan does not add new effect types.
- **Spell execution**: Current spell commands are partially broken (see [2025-12-14_session-001_spell-commands-failure.md](e:\projects\GitHub\MythosMUD\investigations\sessions\2025-12-14_session-001_spell-commands-failure.md)). Fixing `/cast` and related wiring is out of scope for this “list and add data” plan but should be done so new spells are usable.

---

## How to add spells to the game

- **Storage**: Spells are loaded at runtime from PostgreSQL by [SpellRegistry](e:\projects\GitHub\MythosMUD\server\game\magic\spell_registry.py) via [SpellRepository](e:\projects\GitHub\MythosMUD\server\persistence\repositories\spell_repository.py). There is no in-repo seed data for spells today.
- **Recommended approach**: Add spell rows to the database via one of:
  1. **SQL seed script** (e.g. `db/seed/spells.sql` or equivalent) that inserts into `mythos_unit.spells` with columns matching the DDL, run as part of DB setup or a one-off migration.
  2. **Idempotent migration** (e.g. Alembic or a versioned SQL migration) that INSERTs these spells only if they do not exist (e.g. by spell_id).
- **Data shape**: For each spell, supply at least: spell_id, name, description, school, mp_cost, lucidity_cost (0 for non-mythos), corruption_on_learn, corruption_on_cast, casting_time_seconds, target_type, range_type, effect_type, effect_data (JSON), materials (JSON array). effect_data should follow whatever the current magic/combat pipeline expects for that effect_type (e.g. damage amount, duration, stat key).

---

## Summary

- **Deliverable**: A concrete list of ~20 proposed spells (table above) with schools and effect types chosen for a balanced mythos vs clerical/elemental mix, all compatible with the current Spell model and DB schema.
- **Next steps**: (1) Confirm or trim the list from the table; (2) Assign exact costs and effect_data per spell; (3) Add spells via SQL seed or migration; (4) Fix spell command/execution pipeline so `/cast` and related commands work with the new spells.
