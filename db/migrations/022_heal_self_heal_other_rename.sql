-- Description: Rename clerical_basic_heal -> heal_self, clerical_minor_heal -> heal_other.
-- heal_self: self-target heal (/cast heal, /cast heal self, /cast heal me).
-- heal_other: entity-target heal (/cast heal other <target>, /cast heal <target>).
-- Idempotent: only migrates if old spell_id rows exist; skips if already migrated.

-- Migrate clerical_basic_heal -> heal_self (insert new, update refs, delete old)
INSERT INTO spells (
    spell_id, name, description, school, mp_cost, lucidity_cost,
    corruption_on_learn, corruption_on_cast, casting_time_seconds,
    target_type, range_type, effect_type, effect_data, materials
)
SELECT
    'heal_self',
    'Heal Self',
    description,
    school,
    mp_cost,
    lucidity_cost,
    corruption_on_learn,
    corruption_on_cast,
    casting_time_seconds,
    target_type,
    range_type,
    effect_type,
    effect_data,
    materials
FROM spells
WHERE spell_id = 'clerical_basic_heal'
  AND NOT EXISTS (SELECT 1 FROM spells WHERE spell_id = 'heal_self');

UPDATE player_spells SET spell_id = 'heal_self' WHERE spell_id = 'clerical_basic_heal';
DELETE FROM spells WHERE spell_id = 'clerical_basic_heal';

-- Migrate clerical_minor_heal -> heal_other (entity target, Heal Other)
INSERT INTO spells (
    spell_id, name, description, school, mp_cost, lucidity_cost,
    corruption_on_learn, corruption_on_cast, casting_time_seconds,
    target_type, range_type, effect_type, effect_data, materials
)
SELECT
    'heal_other',
    'Heal Other',
    'Restore health to another willing creature in the same room (player or non-hostile NPC).',
    school,
    GREATEST(mp_cost, 8),
    lucidity_cost,
    corruption_on_learn,
    corruption_on_cast,
    casting_time_seconds,
    'entity',
    'same_room',
    effect_type,
    COALESCE(effect_data, '{}'::jsonb) || '{"heal_amount": 10}'::jsonb,
    materials
FROM spells
WHERE spell_id = 'clerical_minor_heal'
  AND NOT EXISTS (SELECT 1 FROM spells WHERE spell_id = 'heal_other');

UPDATE player_spells SET spell_id = 'heal_other' WHERE spell_id = 'clerical_minor_heal';
DELETE FROM spells WHERE spell_id = 'clerical_minor_heal';
