# server services passive lucidity flux

> 9 nodes

## Key Concepts

- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **datetime** (8 connections)
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._normalize_datetime_timezone()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._parse_last_active()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **Parse last_active from various formats.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Normalize datetime to timezone-aware UTC.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Check if player is active based on last_active and created_at.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Filter players to only those active in the last 5 minutes.** (1 connections) — `server/services/passive_lucidity_flux/service.py`

## Relationships

- [server services passive lucidity flux](server_services_passive_lucidity_flux.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*