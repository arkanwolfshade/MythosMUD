# packages/README.md

> 29 nodes · cohesion 0.07

## Key Concepts

- **players** (27 connections) — `db/schema.sql`
- **experience.sql** (3 connections) — `db/procedures/experience.sql`
- **player_skills** (3 connections) — `db/schema.sql`
- **player_spells** (3 connections) — `db/schema.sql`
- **quest_definitions** (3 connections) — `db/schema.sql`
- **quest_instances** (3 connections) — `db/schema.sql`
- **skill_use_log** (3 connections) — `db/schema.sql`
- **skills** (3 connections) — `db/schema.sql`
- **20260928120000_player_aliases_and_mutes.sql** (2 connections) — `db/migrations/20260928120000_player_aliases_and_mutes.sql`
- **player_aliases** (2 connections) — `db/migrations/20260928120000_player_aliases_and_mutes.sql`
- **player_mutes** (2 connections) — `db/migrations/20260928120000_player_aliases_and_mutes.sql`
- **schema_name.award_player_xp()** (2 connections) — `db/procedures/experience.sql`
- **corruption_adjustment_log** (2 connections) — `db/schema.sql`
- **corruption_cooldowns** (2 connections) — `db/schema.sql`
- **lucidity_adjustment_log** (2 connections) — `db/schema.sql`
- **lucidity_cooldowns** (2 connections) — `db/schema.sql`
- **lucidity_exposure_state** (2 connections) — `db/schema.sql`
- **player_aliases** (2 connections) — `db/schema.sql`
- **player_channel_preferences** (2 connections) — `db/schema.sql`
- **player_effects** (2 connections) — `db/schema.sql`
- **player_inventories** (2 connections) — `db/schema.sql`
- **player_is_deleted()** (2 connections) — `db/schema.sql`
- **player_lucidity** (2 connections) — `db/schema.sql`
- **player_mutes** (2 connections) — `db/schema.sql`
- **quest_offers** (2 connections) — `db/schema.sql`
- *... and 4 more nodes in this community*

## Relationships

- [test_connection_delegates.py](test_connection_delegates.py.md) (22 shared connections)
- [📋 Test Coverage Breakdown](📋_Test_Coverage_Breakdown.md) (2 shared connections)
- [Motion Design](Motion_Design.md) (1 shared connections)
- [test_ascii_map_exits.py](test_ascii_map_exits.py.md) (1 shared connections)
- [_make_mock_row](_make_mock_row.md) (1 shared connections)
- [rooms](rooms.md) (1 shared connections)

## Source Files

- `db/migrations/20260928120000_player_aliases_and_mutes.sql`
- `db/procedures/experience.sql`
- `db/schema.sql`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*