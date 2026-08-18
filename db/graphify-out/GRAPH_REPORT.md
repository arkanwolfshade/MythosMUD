# Graph Report - db  (2026-08-18)

## Corpus Check
- 35 files · ~52,211 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 544 nodes · 653 edges · 42 communities (37 shown, 5 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.9)
- Token cost: 7,977 input · 1,962 output

## Community Hubs (Navigation)
- Dev Schema Procedures
- NPC Schedule Schema
- Holiday Calendar Schema
- E2E Schema Tables
- Unit Schema Tables
- Room JSON Schema
- Emote JSON Schema
- Room Exit Schema
- Container Procedures
- Dev Player Tables
- Holidays Schema Root
- NPC Schedules Root
- NPC Definition Procedures
- Schema Generation Pipeline
- Dev Item Containers
- Dev Rooms And Zones
- Dev NPC Tables
- Item Instance Procedures
- Dev Users And Invites
- Dev Quest Tables
- Dev Emote Tables
- Procedures README
- Zone Catalog

## God Nodes (most connected - your core abstractions)
1. `mythos_dev.players` - 15 edges
2. `mythos_e2e.players` - 15 edges
3. `mythos_unit.players` - 15 edges
4. `string` - 11 edges
5. `null` - 11 edges
6. `required` - 9 edges
7. `required` - 9 edges
8. `required` - 8 edges
9. `mythos_dev.item_instances` - 7 edges
10. `mythos_dev.container_contents` - 5 edges

## Surprising Connections (you probably didn't know these)
- `mythos_dev.players` --references--> `mythos_dev.users`  [EXTRACTED]
  mythos_dev_ddl.sql →   _Bridges community 25 → community 9_
- `mythos_dev.containers` --references--> `mythos_dev.players`  [EXTRACTED]
  mythos_dev_ddl.sql → mythos_dev_ddl.sql  _Bridges community 17 → community 9_
- `mythos_dev.player_exploration` --references--> `mythos_dev.players`  [EXTRACTED]
  mythos_dev_ddl.sql → mythos_dev_ddl.sql  _Bridges community 20 → community 9_
- `mythos_dev.quest_instances` --references--> `mythos_dev.players`  [EXTRACTED]
  mythos_dev_ddl.sql → mythos_dev_ddl.sql  _Bridges community 9 → community 26_

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Database Initialization Execution Order** — db_roles_roles, db_databases_databases, db_mythos_dev_ddl, data_db_mythos_dev_dml [EXTRACTED 1.00]
- **Authoritative Environment Files** — db_mythos_dev_ddl, db_mythos_unit_ddl, db_mythos_e2e_ddl, data_db_mythos_dev_dml, data_db_mythos_unit_dml, data_db_mythos_e2e_dml [EXTRACTED 1.00]

## Communities (42 total, 5 thin omitted)

### Community 0 - "Dev Schema Procedures"
Cohesion: 0.02
Nodes (5): mythos_dev.aliases, mythos_dev.calendar_holidays, mythos_dev.calendar_npc_schedules, mythos_dev.id_map_users, mythos_dev.professions

### Community 1 - "NPC Schedule Schema"
Cohesion: 0.05
Nodes (48): applies_to, category, days, effects, end_hour, start_hour, items, minItems (+40 more)

### Community 2 - "Holiday Calendar Schema"
Cohesion: 0.04
Nodes (46): autumn, bonus_tags, day, duration_hours, month, season, spring, summer (+38 more)

### Community 3 - "E2E Schema Tables"
Cohesion: 0.09
Nodes (42): mythos_e2e.aliases, mythos_e2e.calendar_holidays, mythos_e2e.calendar_npc_schedules, mythos_e2e.container_contents, mythos_e2e.containers, mythos_e2e.dialogue_definitions, mythos_e2e.emote_aliases, mythos_e2e.emotes (+34 more)

### Community 4 - "Unit Schema Tables"
Cohesion: 0.09
Nodes (42): mythos_unit.aliases, mythos_unit.calendar_holidays, mythos_unit.calendar_npc_schedules, mythos_unit.container_contents, mythos_unit.containers, mythos_unit.dialogue_definitions, mythos_unit.emote_aliases, mythos_unit.emotes (+34 more)

### Community 5 - "Room JSON Schema"
Cohesion: 0.05
Nodes (37): description, exits, plane, sub_zone, zone, additionalProperties, additionalProperties, type (+29 more)

### Community 6 - "Emote JSON Schema"
Cohesion: 0.06
Nodes (31): aliases, emotes, other_message, self_message, additionalProperties, additionalProperties, properties, required (+23 more)

### Community 7 - "Room Exit Schema"
Cohesion: 0.13
Nodes (27): null, string, type, type, type, additionalProperties, properties, type (+19 more)

### Community 8 - "Container Procedures"
Cohesion: 0.13
Nodes (5): container_contents, item_prototypes, schema_name.add_item_to_container(), schema_name.get_container_contents_json(), item_instances

### Community 9 - "Dev Player Tables"
Cohesion: 0.17
Nodes (13): mythos_dev.lucidity_adjustment_log, mythos_dev.lucidity_cooldowns, mythos_dev.lucidity_exposure_state, mythos_dev.player_channel_preferences, mythos_dev.player_effects, mythos_dev.player_inventories, mythos_dev.player_lucidity, mythos_dev.player_skills (+5 more)

### Community 11 - "Holidays Schema Root"
Cohesion: 0.17
Nodes (11): holidays, additionalProperties, minItems, type, $id, properties, holidays, required (+3 more)

### Community 12 - "NPC Schedules Root"
Cohesion: 0.17
Nodes (11): schedules, additionalProperties, $id, properties, schedules, required, minItems, type (+3 more)

### Community 13 - "NPC Definition Procedures"
Cohesion: 0.18
Nodes (3): npc_definitions, npc_spawn_rules, schema_name.get_npc_system_statistics()

### Community 17 - "Dev Item Containers"
Cohesion: 0.36
Nodes (8): mythos_dev.add_item_to_container(), mythos_dev.container_contents, mythos_dev.containers, mythos_dev.get_container_contents_json(), mythos_dev.item_component_states, mythos_dev.item_instance_exists(), mythos_dev.item_instances, mythos_dev.item_prototypes

### Community 20 - "Dev Rooms And Zones"
Cohesion: 0.40
Nodes (6): mythos_dev.player_exploration, mythos_dev.room_links, mythos_dev.rooms, mythos_dev.zone_configurations, mythos_dev.zones, mythos_dev.subzones

### Community 23 - "Dev NPC Tables"
Cohesion: 0.50
Nodes (5): mythos_dev.dialogue_definitions, mythos_dev.get_npc_system_statistics(), mythos_dev.npc_definitions, mythos_dev.npc_relationships, mythos_dev.npc_spawn_rules

### Community 25 - "Dev Users And Invites"
Cohesion: 0.50
Nodes (4): mythos_dev.id_map_players, mythos_dev.invites, mythos_dev.muting_rules, mythos_dev.users

### Community 26 - "Dev Quest Tables"
Cohesion: 0.67
Nodes (3): mythos_dev.quest_definitions, mythos_dev.quest_instances, mythos_dev.quest_offers

## Knowledge Gaps
- **145 isolated node(s):** `mythos_dev.aliases`, `mythos_dev.calendar_holidays`, `mythos_dev.calendar_npc_schedules`, `mythos_dev.id_map_users`, `mythos_dev.professions` (+140 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `properties` connect `Room JSON Schema` to `Room Exit Schema`?**
  _High betweenness centrality (0.011) - this node is a cross-community bridge._
- **What connects `mythos_dev.aliases`, `mythos_dev.calendar_holidays`, `mythos_dev.calendar_npc_schedules` to the rest of the system?**
  _145 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Dev Schema Procedures` be split into smaller, more focused modules?**
  _Cohesion score 0.023529411764705882 - nodes in this community are weakly interconnected._
- **Should `NPC Schedule Schema` be split into smaller, more focused modules?**
  _Cohesion score 0.04609929078014184 - nodes in this community are weakly interconnected._
- **Should `Holiday Calendar Schema` be split into smaller, more focused modules?**
  _Cohesion score 0.044444444444444446 - nodes in this community are weakly interconnected._
- **Should `E2E Schema Tables` be split into smaller, more focused modules?**
  _Cohesion score 0.08527131782945736 - nodes in this community are weakly interconnected._
- **Should `Unit Schema Tables` be split into smaller, more focused modules?**
  _Cohesion score 0.08748615725359911 - nodes in this community are weakly interconnected._