# MythosMUD Database Placement

> 15 nodes · cohesion 0.22

## Key Concepts

- **test_player_aliases_and_mutes_db.py** (14 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **_Players** (12 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **asyncio** (5 connections)
- **test_global_mute_survives_restart_without_muter_online()** (5 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **test_mute_repository_upsert_replaces_and_filters_expired()** (5 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **test_alias_crud_round_trip()** (4 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **test_alias_rejected_for_unknown_player_and_over_limit()** (4 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **test_aliases_are_per_player_and_deleted_by_id()** (4 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **async_sessionmaker** (1 connections)
- **AsyncSession** (1 connections)
- **fixture** (1 connections)
- **MonkeyPatch** (1 connections)
- **Integration tests for DB-backed player aliases (#680) and mutes (#681). Drives…** (1 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **Regression: global mutes used to live in the muter's JSON file and vanished…** (1 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **Two fresh players; storage classes are pointed at the integration session…** (1 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`

## Relationships

- [command_parser.py](command_parser.py.md) (5 shared connections)
- [test_aggression.py](test_aggression.py.md) (5 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [CombatBroadcastMixin](CombatBroadcastMixin.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_player_aliases_and_mutes_db.py`

## Audit Trail

- EXTRACTED: 30 (81%)
- INFERRED: 7 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*