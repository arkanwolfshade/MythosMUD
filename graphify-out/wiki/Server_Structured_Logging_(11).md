# Server Structured Logging (11)

> 13 nodes

## Key Concepts

- **datetime** (9 connections)
- **combat_audit.py** (6 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_start()** (3 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_attack()** (3 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_death()** (3 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_end()** (3 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_rate_limit()** (3 connections) — `server/structured_logging/combat_audit.py`
- **Combat-specific audit logging and monitoring.  This module provides specialized** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log the start of a combat encounter.          Args:             player_id: ID of** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat attack.          Args:             player_id: ID of the attacking p** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log the death of a combat target.          Args:             player_id: ID of th** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log the end of a combat encounter.          Args:             player_id: ID of t** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat rate limit event.          Args:             player_id: ID of the p** (1 connections) — `server/structured_logging/combat_audit.py`

## Relationships

- [Server Structured Logging (13)](Server_Structured_Logging_%2813%29.md) (6 shared connections)
- [Server Structured Logging (14)](Server_Structured_Logging_%2814%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Structured Logging (12)](Server_Structured_Logging_%2812%29.md) (1 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*