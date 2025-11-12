INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.head.clockwork_crown', 'Clockwork Aether Crown', 'a crown of interlocking brass sigils', 'This delicate coronet hums with aetheric resonance siphoned from Wilmarth''s tower array.', 'equipment', 1.2, 2400, 80, '["MAGICAL"]', '["HEAD"]', '{"max_stack": 1}', '{"faction": ["miskatonic"]}', '["component.sanity_guard"]', '{"lore": "Recovered from Dr. Wilmarth''s attic in 1927"}', '["equipment","head","artifact"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.head.veilwoven_hood', 'Veilwoven Hood', 'a hood of translucent night silk', 'A veil spun from Leng spider silk that refracts hostile gazes and muffles whispered horrors.', 'equipment', 0.6, 720, 50, '["MAGICAL","GLOW"]', '["HEAD"]', '{"max_stack": 1}', '{"profession": ["occultist","archivist"]}', '["component.light_emitter"]', '{"lore": "Issued to the 1908 Miskatonic Deep Archive expedition"}', '["equipment","head","occult"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.torso.starsteel_breastplate', 'Starsteel Breastplate', 'a breastplate etched with non-euclidean constellations', 'Forged from meteoric ore mined near Dunwich, it resonates softly when eldritch entities draw near.', 'equipment', 6.3, 1950, 120, '["MAGICAL","NO_SALE"]', '["TORSO"]', '{"max_stack": 1}', '{"faction": ["silver_twilight"]}', '["component.durability"]', '{"lore": "Rewarded to Silver Twilight conclave guardians"}', '["equipment","torso","defense"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.torso.reinforced_trenchcoat', 'Reinforced Trenchcoat', 'a storm-grey trenchcoat lined with armored plates', 'Investigator-issue coat threaded with Kevlar runes for protection during prolonged stakeouts.', 'equipment', 4.8, 880, 90, '[]', '["TORSO"]', '{"max_stack": 1}', '{"profession": ["detective"]}', '["component.durability"]', '{"lore": "Standard Mythos Control field kit, 1935 revision"}', '["equipment","torso","investigator"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.legs.moonlight_tassets', 'Moonlight Tassets', 'segment plates shimmering with lunar sheen', 'Segmented leg guards bathed in Arkham moonlight to resist claws from beyond.', 'equipment', 3.4, 1120, 100, '["MAGICAL"]', '["LEGS"]', '{"max_stack": 1}', '{}', '["component.durability"]', '{"lore": "Blessed on the Sanitarium parapets during a blood moon"}', '["equipment","legs","defense"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.legs.shadowstep_breeches', 'Shadowstep Breeches', 'charcoal breeches lined with whisperthread', 'Favored by clandestine archivists; these breeches dampen footfalls and blur the wearer''s outline.', 'equipment', 1.7, 930, 70, '["MAGICAL"]', '["LEGS"]', '{"max_stack": 1}', '{"profession": ["archivist","rogue"]}', '["component.sanity_guard"]', '{"lore": "Tailored in Innsmouth prior to the 1928 raid"}', '["equipment","legs","stealth"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.main_hand.eldritch_tonfa', 'Eldritch Tonfa', 'a hardened oak tonfa veined with glowing sigils', 'Strikes trace sigils in the air, disrupting unstable geometries during close-quarter engagements.', 'equipment', 2.4, 1350, 65, '["MAGICAL"]', '["MAIN_HAND"]', '{"max_stack": 1}', '{}', '["component.charge"]', '{"lore": "Crafted by Dr. Armitage''s personal wardens"}', '["equipment","main_hand","melee"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.main_hand.sunken_revolver', 'Sunken Revolver', 'a revolver encrusted with barnacle inlays', 'Recovered from the Deep Ones'' reliquary, it fires rounds humming with abyssal harmonics.', 'equipment', 1.9, 1680, 55, '["MAGICAL"]', '["MAIN_HAND"]', '{"max_stack": 1}', '{"faction": ["coastal_watch"]}', '["component.charge","component.cooldown"]', '{"lore": "Weaponized by Innsmouth resistance fighters"}', '["equipment","main_hand","ranged"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.off_hand.sigil_lantern', 'Sigil Lantern', 'a brass lantern etched with protective glyphs', 'Projects a barrier of pale light that erodes the courage of encroaching horrors.', 'equipment', 1.6, 780, 60, '["MAGICAL","GLOW"]', '["OFF_HAND"]', '{"max_stack": 1}', '{}', '["component.light_emitter"]', '{"lore": "Standard issue for Sanitarium orderlies on night rounds"}', '["equipment","off_hand","utility"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.off_hand.mirror_ward_tome', 'Mirror Ward Tome', 'a tome bound with mirrored obsidian', 'Reflects lesser glamours and absorbs stray ritual backlash into its mirrored cover.', 'equipment', 2.1, 910, 45, '["MAGICAL"]', '["OFF_HAND"]', '{"max_stack": 1}', '{"profession": ["occultist"]}', '["component.sanity_guard"]', '{"lore": "Annotated by Wilmarth during the Dunwich incident"}', '["equipment","off_hand","tome"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.feet.eldersalt_boots', 'Eldersalt Boots', 'boots dusted with crystalline elder salt', 'Crunching steps trace radiant wards, preventing pursuit by incorporeal entities.', 'equipment', 2.3, 990, 70, '["MAGICAL"]', '["FEET"]', '{"max_stack": 1}', '{}', '["component.light_emitter"]', '{"lore": "Prepared by the Arkham Salt Guild for field operatives"}', '["equipment","feet","defense"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.feet.silent_combat_boots', 'Silent Combat Boots', 'lacquered boots with nullfoam soles', 'Nullfoam soles dampen vibrations, making even hurried strides inaudible to mundane senses.', 'equipment', 1.9, 640, 55, '[]', '["FEET"]', '{"max_stack": 1}', '{"profession": ["scout","detective"]}', '["component.cooldown"]', '{"lore": "Issued during Mythos Control''s 1933 urban sweep"}', '["equipment","feet","stealth"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.hands.blackstone_gauntlets', 'Blackstone Gauntlets', 'gauntlets carved from polished blackstone', 'Their weight anchors the wearer in Euclidean space, resisting spatial distortion.', 'equipment', 3.0, 1220, 90, '["MAGICAL","NO_DROP"]', '["HANDS"]', '{"max_stack": 1}', '{}', '["component.durability"]', '{"lore": "Chiseled from the Standing Stones outside Kingsport"}', '["equipment","hands","defense"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.hands.fine_lockbreak_gloves', 'Fine Lockbreak Gloves', 'supple gloves studded with aether picks', 'Aether-tuned picks extrude from the fingertips, easing clandestine operations on sealed wards.', 'equipment', 0.9, 540, 40, '[]', '["HANDS"]', '{"max_stack": 1}', '{"profession": ["rogue","scout"]}', '["component.cooldown"]', '{"lore": "Smuggled from the Leng black markets"}', '["equipment","hands","utility"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.accessory.phosphor_charm', 'Phosphor Charm', 'a charm vial filled with radiant phosphor', 'When crushed, the charm floods the air with phosphor light, exposing invisible adversaries.', 'equipment', 0.2, 480, NULL, '["MAGICAL","CONSUMABLE"]', '["ACCESSORY"]', '{"max_stack": 3}', '{}', '["component.charge"]', '{"lore": "Synthesized in the Sanitarium chemical labs"}', '["equipment","accessory","consumable"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.accessory.whisperquartz_brooch', 'Whisperquartz Brooch', 'a brooch crowned with whispering quartz', 'Resonant quartz harmonizes stray telepathic echoes, shielding the wearer from maddening whispers.', 'equipment', 0.3, 820, NULL, '["MAGICAL"]', '["ACCESSORY"]', '{"max_stack": 1}', '{"profession": ["psyker"]}', '["component.sanity_guard"]', '{"lore": "Calibrated using fragments from Plateau of Leng monoliths"}', '["equipment","accessory","sanity"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.ring.aetheric_focus_ring', 'Aetheric Focus Ring', 'a sterling ring engraved with focusing runes', 'Concentrates personal energies, accelerating ritual charge accumulation.', 'equipment', 0.1, 960, NULL, '["MAGICAL"]', '["RING"]', '{"max_stack": 1}', '{}', '["component.charge"]', '{"lore": "Crafted by Miskatonic jewelers for sanctioned mages"}', '["equipment","ring","focus"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.ring.bound_ward_band', 'Bound Ward Band', 'a tarnished silver band set with ward sigils', 'This band binds minor wards directly to the wearer, providing subtle protective currents.', 'equipment', 0.1, 540, NULL, '[]', '["RING"]', '{"max_stack": 1}', '{"profession": ["guardian"]}', '["component.sanity_guard"]', '{"lore": "Recovered from the 1880 Arkham chapel sanctum"}', '["equipment","ring","defense"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.amulet.starlit_focus_amulet', 'Starlit Focus Amulet', 'an amulet housing a captured starlit mote', 'A mote captured during a rare planetary alignment fuels the wearer''s invocations.', 'equipment', 0.2, 1100, NULL, '["MAGICAL"]', '["AMULET"]', '{"max_stack": 1}', '{}', '["component.charge"]', '{"lore": "Blessed under Professor Armitage''s supervision"}', '["equipment","amulet","focus"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.amulet.deepwatch_pendant', 'Deepwatch Pendant', 'a pendant carved from abyssal coral', 'Its pulse synchronizes with the ocean tides, warning of impending aquatic incursions.', 'equipment', 0.3, 760, NULL, '["MAGICAL"]', '["AMULET"]', '{"max_stack": 1}', '{"faction": ["coastal_watch"]}', '["component.cooldown"]', '{"lore": "Gifted to Coastal Watch sentinels on their commissioning"}', '["equipment","amulet","utility"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.belt.hierophant_sash', 'Hierophant Sash', 'a sash woven with golden hierophant thread', 'Maintains ritual focus, stabilizing the wearer''s attunement during extended channeling.', 'equipment', 0.4, 680, NULL, '["MAGICAL"]', '["BELT"]', '{"max_stack": 1}', '{"profession": ["occultist","ritualist"]}', '["component.attunement"]', '{"lore": "Used in the 1912 Arkham anti-summoning conclave"}', '["equipment","belt","ritual"]');

INSERT OR REPLACE INTO item_prototypes (
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags
) VALUES
('equipment.belt.field_operator_bandolier', 'Field Operator Bandolier', 'a rugged bandolier fitted with rune-stamped pockets', 'Keeps eldritch reagents insulated and suppresses unstable reactions during field deployment.', 'equipment', 0.7, 420, NULL, '[]', '["BELT"]', '{"max_stack": 1}', '{"profession": ["investigator","scout"]}', '["component.cooldown"]', '{"lore": "Mandatory for Mythos Control responders assigned to sanitarium duty"}', '["equipment","belt","utility"]');
