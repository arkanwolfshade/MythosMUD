# test_check_codacy_yaml.py

> 7 nodes · cohesion 0.33

## Key Concepts

- **test_get_dead_players_debug_only_when_found()** (7 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_debug_only_when_found()** (7 connections) — `server/tests/unit/services/test_player_death_service.py`
- **_session_with_players()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **parametrize** (2 connections)
- **Async session whose select(Player) returns the given players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **#912: runs every tick; an empty result must not emit a debug line.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **#912: runs every game-second; an empty result must not emit a debug line.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`

## Relationships

- [MythosMUD Dependency Upgrade Strategy - Implementation Summary](MythosMUD_Dependency_Upgrade_Strategy_-_Implementation_Summary.md) (5 shared connections)
- [Test Suite Analyzer Subagent](Test_Suite_Analyzer_Subagent.md) (2 shared connections)
- [test_lifecycle_respawn.py](test_lifecycle_respawn.py.md) (2 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 14 (88%)
- INFERRED: 2 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*