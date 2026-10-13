# Community 245

> 64 nodes

## Key Concepts

- **LucidityFluxService** (30 connections) — `server/services/passive_lucidity_flux/service.py`
- **player_lucidity** (19 connections) — `db/schema.sql`
- **LucidityUpdateResult** (17 connections) — `server/services/lucidity_helpers.py`
- **.process_tick()** (15 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context_async()** (12 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (11 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (10 connections)
- **FluxRoom** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **PlayerFluxCtx** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **_apply_grounding_adjustment()** (9 connections) — `server/commands/rescue_commands.py`
- **._lookup_base_flux_for_room()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **datetime** (8 connections)
- **._apply_player_flux_adjustment()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._build_room_cache()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **_as_float()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._companion_modifier()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._count_companion_tiers()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_for_context()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_world_override_flux()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._normalize_datetime_timezone()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 39 more nodes in this community*

## Relationships

- [Community 378](Community_378.md) (10 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (8 shared connections)
- [Community 207](Community_207.md) (7 shared connections)
- [Community 138](Community_138.md) (7 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (4 shared connections)
- [Community 115](Community_115.md) (3 shared connections)
- [Community 168](Community_168.md) (3 shared connections)
- [Community 156](Community_156.md) (2 shared connections)
- [Community 699](Community_699.md) (1 shared connections)
- [Community 222](Community_222.md) (1 shared connections)
- [Community 506](Community_506.md) (1 shared connections)
- [Community 166](Community_166.md) (1 shared connections)

## Source Files

- `db/schema.sql`
- `server/commands/rescue_commands.py`
- `server/services/lucidity_helpers.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 173 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*