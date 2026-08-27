# test_enhanced_logging_config.py

> 18 nodes

## Key Concepts

- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (11 connections) — `server/schemas/players/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- **_stat_or_default()** (3 connections) — `server/api/character_creation.py`
- **_as_float()** (2 connections) — `server/api/character_creation.py`
- **_as_int()** (2 connections) — `server/api/character_creation.py`
- **Stats** (2 connections)
- **Convert Stats model to RolledStats schema.** (1 connections) — `server/api/character_creation.py`
- **Roll stats with no profession or class requirement. Plan 10.5 A1.** (1 connections) — `server/api/character_creation.py`
- **Roll once, apply profession stat_modifiers for preview. Plan 10.5 A1.** (1 connections) — `server/api/character_creation.py`
- **Roll stats using legacy class-based method.** (1 connections) — `server/api/character_creation.py`
- **Treat missing stats as the generator default (50).** (1 connections) — `server/api/character_creation.py`
- **Convert get_stat_summary dict to StatSummary model format. Args: stats: Stats…** (1 connections) — `server/api/character_creation.py`
- **Response model for rolling character stats.** (1 connections) — `server/schemas/players/character_creation.py`

## Relationships

- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (24 shared connections)
- [UpgradeImplementationPlan](UpgradeImplementationPlan.md) (4 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (2 shared connections)
- [maps.py](maps.py.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (1 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/schemas/players/character_creation.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*