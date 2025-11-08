-- NPC Sample Data for Testing and Development
-- This script populates the NPC database with sample data covering all NPC types
-- and various scenarios for testing the NPC subsystem
-- Clear existing data (for clean testing)
DELETE FROM npc_relationships;
DELETE FROM npc_spawn_rules;
DELETE FROM npc_definitions;
-- Sample NPC Definitions
-- Each NPC type is represented with Mythos-appropriate characters
-- SHOPKEEPER NPCs
INSERT INTO npc_definitions (
        name,
        description,
        npc_type,
        sub_zone_id,
        room_id,
        required_npc,
        max_population,
        spawn_probability,
        base_stats,
        behavior_config,
        ai_integration_stub
    )
VALUES (
        'Ezekiel Whateley',
        'A gaunt, elderly shopkeeper with eyes that seem to see beyond the veil of normal reality. His shop contains artifacts of questionable origin, and he speaks in riddles that hint at forbidden knowledge.',
        'shopkeeper',
        'merchant',
        'earth_arkhamcity_merchant_room_peabody_ave_001',
        1,
        1,
        1.0,
        '{"health": 100, "sanity": 50, "intelligence": 18, "charisma": 12, "strength": 8, "dexterity": 10}',
        '{"shop_type": "occult_artifacts", "buy_multiplier": 0.5, "sell_multiplier": 1.5, "greeting": "Welcome, seeker of knowledge...", "farewell": "May the stars guide your path."}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_shopkeeper"}'
    ),
    (
        'Madame Lavinia',
        'A mysterious fortune teller who operates a small shop selling herbs, crystals, and other mystical items. Her predictions are eerily accurate, though they often speak of dark futures.',
        'shopkeeper',
        'downtown',
        'earth_arkhamcity_downtown_room_derby_st_001',
        0,
        1,
        0.8,
        '{"health": 80, "sanity": 40, "intelligence": 16, "charisma": 15, "strength": 6, "dexterity": 12}',
        '{"shop_type": "mystical_supplies", "buy_multiplier": 0.6, "sell_multiplier": 1.3, "greeting": "The cards have foretold your arrival...", "farewell": "Beware the shadows that follow."}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_shopkeeper"}'
    );
-- QUEST GIVER NPCs
INSERT INTO npc_definitions (
        name,
        description,
        npc_type,
        sub_zone_id,
        room_id,
        required_npc,
        max_population,
        spawn_probability,
        base_stats,
        behavior_config,
        ai_integration_stub
    )
VALUES (
        'Professor Henry Armitage',
        'The head librarian of Miskatonic University, a learned scholar who has encountered more than his share of the supernatural. He often has research tasks for those brave enough to investigate the unknown.',
        'quest_giver',
        'campus',
        'earth_arkhamcity_campus_room_boundary_st_001',
        1,
        1,
        1.0,
        '{"health": 90, "sanity": 60, "intelligence": 20, "charisma": 14, "strength": 9, "dexterity": 11}',
        '{"quest_types": ["research", "investigation", "artifact_recovery"], "greeting": "Ah, another seeker of knowledge. I may have work for you.", "farewell": "Remember, some knowledge comes with a price."}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_quest_giver"}'
    ),
    (
        'Dr. Francis Morgan',
        'A physician at the Arkham Sanitarium who has seen too much. He occasionally needs help with patients who exhibit... unusual symptoms.',
        'quest_giver',
        'sanitarium',
        'earth_arkhamcity_sanitarium_room_foyer_entrance_001',
        1,
        1,
        1.0,
        '{"health": 85, "sanity": 45, "intelligence": 17, "charisma": 13, "strength": 10, "dexterity": 12}',
        '{"quest_types": ["medical_research", "patient_observation", "supply_delivery"], "greeting": "I need someone with a strong constitution...", "farewell": "Be careful out there. The world is not as it seems."}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_quest_giver"}'
    );
-- PASSIVE MOB NPCs
INSERT INTO npc_definitions (
        name,
        description,
        npc_type,
        sub_zone_id,
        room_id,
        required_npc,
        max_population,
        spawn_probability,
        base_stats,
        behavior_config,
        ai_integration_stub
    )
VALUES (
        'Wandering Scholar',
        'A lost academic who roams the streets of Arkham, muttering to himself about ancient texts and forgotten languages. He is harmless but may provide cryptic clues to those who listen.',
        'passive_mob',
        'downtown',
        'earth_arkhamcity_downtown_room_derby_st_002',
        0,
        2,
        0.6,
        '{"health": 60, "sanity": 30, "intelligence": 15, "charisma": 8, "strength": 7, "dexterity": 9}',
        '{"wander_radius": 3, "wander_frequency": 300, "response_to_attack": "flee", "greeting": "The stars... they whisper secrets...", "farewell": "The truth lies in the spaces between words."}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_wanderer"}'
    ),
    (
        'Sanitarium Patient',
        'A former patient of the sanitarium who now wanders the grounds, seemingly lost in their own world. They are docile but may react unpredictably to sudden movements.',
        'passive_mob',
        'sanitarium',
        'earth_arkhamcity_sanitarium_room_foyer_001',
        0,
        3,
        0.7,
        '{"health": 50, "sanity": 20, "intelligence": 10, "charisma": 6, "strength": 8, "dexterity": 11}',
        '{"wander_radius": 2, "wander_frequency": 180, "response_to_attack": "cower", "greeting": "They... they told me I was cured...", "farewell": "The walls... they still whisper to me..."}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_wanderer"}'
    ),
    (
        'Street Vendor',
        'A local merchant who sets up a small stall in the northside district, selling various goods to passersby. They are friendly but cautious of strangers.',
        'passive_mob',
        'northside',
        'earth_arkhamcity_northside_room_high_ln_001',
        0,
        1,
        0.5,
        '{"health": 70, "sanity": 55, "intelligence": 12, "charisma": 14, "strength": 10, "dexterity": 13}',
        '{"wander_radius": 1, "wander_frequency": 600, "response_to_attack": "call_for_help", "greeting": "Good day! Care to browse my wares?", "farewell": "Come back anytime, friend."}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_wanderer"}'
    );
-- AGGRESSIVE MOB NPCs
INSERT INTO npc_definitions (
        name,
        description,
        npc_type,
        sub_zone_id,
        room_id,
        required_npc,
        max_population,
        spawn_probability,
        base_stats,
        behavior_config,
        ai_integration_stub
    )
VALUES (
        'Cultist of the Yellow Sign',
        'A deranged follower of Hastur who lurks in the shadows of Arkham, seeking to spread madness and corruption. They are extremely dangerous and will attack anyone who gets too close.',
        'aggressive_mob',
        'downtown',
        'earth_arkhamcity_downtown_room_derby_st_003',
        0,
        2,
        0.3,
        '{"health": 120, "sanity": 10, "intelligence": 14, "charisma": 8, "strength": 15, "dexterity": 12}',
        '{"hunt_radius": 5, "attack_damage": 25, "territorial": true, "hunt_frequency": 120, "greeting": "Ia! Ia! Hastur fhtagn!", "farewell": "The King in Yellow comes!"}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_hunter"}'
    ),
    (
        'Deep One Hybrid',
        'A half-human, half-amphibious creature that has emerged from the waters near Innsmouth. They are territorial and will attack any surface-dwellers they encounter.',
        'aggressive_mob',
        'waterfront',
        'earth_innsmouth_waterfront_room_waterfront_001',
        0,
        1,
        0.4,
        '{"health": 150, "sanity": 5, "intelligence": 11, "charisma": 4, "strength": 18, "dexterity": 14}',
        '{"hunt_radius": 4, "attack_damage": 30, "territorial": true, "hunt_frequency": 90, "greeting": "Ph''nglui mglw''nafh Cthulhu R''lyeh wgah''nagl fhtagn", "farewell": "The Deep Ones rise!"}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_hunter"}'
    ),
    (
        'Nightgaunt',
        'A shadowy, bat-like creature that hunts in the darkness. They are fast, silent, and deadly, preferring to attack from above or behind.',
        'aggressive_mob',
        'northside',
        'earth_arkhamcity_northside_room_high_ln_002',
        0,
        1,
        0.2,
        '{"health": 80, "sanity": 0, "intelligence": 13, "charisma": 3, "strength": 12, "dexterity": 20}',
        '{"hunt_radius": 6, "attack_damage": 20, "territorial": false, "hunt_frequency": 60, "greeting": "*silent screech*", "farewell": "*fades into shadows*"}',
        '{"ai_enabled": false, "ai_model": null, "fallback_behavior": "deterministic_hunter"}'
    );
-- Sample NPC Spawn Rules
-- These define when and where NPCs should spawn based on various conditions
INSERT INTO npc_spawn_rules (
        npc_definition_id,
        sub_zone_id,
        min_players,
        max_players,
        spawn_conditions
    )
VALUES -- Shopkeeper spawn rules
    (
        1,
        'merchant',
        0,
        999,
        '{"time_of_day": "any", "weather": "any", "special_events": []}'
    ),
    (
        2,
        'downtown',
        1,
        999,
        '{"time_of_day": "evening", "weather": "any", "special_events": ["full_moon"]}'
    ),
    -- Quest giver spawn rules
    (
        3,
        'campus',
        0,
        999,
        '{"time_of_day": "day", "weather": "any", "special_events": []}'
    ),
    (
        4,
        'sanitarium',
        0,
        999,
        '{"time_of_day": "any", "weather": "any", "special_events": []}'
    ),
    -- Passive mob spawn rules
    (
        5,
        'downtown',
        0,
        999,
        '{"time_of_day": "any", "weather": "any", "special_events": []}'
    ),
    (
        6,
        'sanitarium',
        0,
        999,
        '{"time_of_day": "night", "weather": "any", "special_events": []}'
    ),
    (
        7,
        'northside',
        0,
        999,
        '{"time_of_day": "day", "weather": "clear", "special_events": []}'
    ),
    -- Aggressive mob spawn rules
    (
        8,
        'downtown',
        0,
        999,
        '{"time_of_day": "night", "weather": "fog", "special_events": ["full_moon"]}'
    ),
    (
        9,
        'waterfront',
        0,
        999,
        '{"time_of_day": "any", "weather": "storm", "special_events": []}'
    ),
    (
        10,
        'northside',
        0,
        999,
        '{"time_of_day": "night", "weather": "any", "special_events": []}'
    );
-- Sample NPC Relationships
-- These define how NPCs interact with each other
INSERT INTO npc_relationships (
        npc_id_1,
        npc_id_2,
        relationship_type,
        relationship_strength
    )
VALUES -- Professor Armitage and Dr. Morgan are allies (both academics/medical professionals)
    (3, 4, 'ally', 0.8),
    -- The Wandering Scholar and Street Vendor are neutral (both downtown NPCs)
    (5, 7, 'neutral', 0.5),
    -- Cultist and Nightgaunt are allies (both serve dark forces)
    (8, 10, 'ally', 0.7),
    -- Deep One Hybrid and Cultist are enemies (different factions)
    (9, 8, 'enemy', 0.9),
    -- Sanitarium Patient and Dr. Morgan have a follower relationship
    (6, 4, 'follower', 0.6),
    -- Ezekiel Whateley and Madame Lavinia are neutral (both shopkeepers, different specialties)
    (1, 2, 'neutral', 0.4);
-- Verify the data was inserted correctly
SELECT 'NPC Definitions' as table_name,
    COUNT(*) as count
FROM npc_definitions
UNION ALL
SELECT 'NPC Spawn Rules' as table_name,
    COUNT(*) as count
FROM npc_spawn_rules
UNION ALL
SELECT 'NPC Relationships' as table_name,
    COUNT(*) as count
FROM npc_relationships;
