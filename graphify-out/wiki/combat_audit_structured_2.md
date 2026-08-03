# combat audit structured

> 11 nodes

## Key Concepts

- **datetime** (9 connections)
- **.log_combat_start()** (3 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_attack()** (3 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_death()** (3 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_end()** (3 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_rate_limit()** (3 connections) — `server/structured_logging/combat_audit.py`
- **Log the start of a combat encounter.          Args:             player_id: ID of** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat attack.          Args:             player_id: ID of the attacking p** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log the death of a combat target.          Args:             player_id: ID of th** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log the end of a combat encounter.          Args:             player_id: ID of t** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat rate limit event.          Args:             player_id: ID of the p** (1 connections) — `server/structured_logging/combat_audit.py`

## Relationships

- [combat audit structured](combat_audit_structured.md) (8 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*