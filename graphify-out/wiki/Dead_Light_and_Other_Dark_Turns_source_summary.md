# Dead Light and Other Dark Turns (source summary)

> 6 nodes · cohesion 0.33

## Key Concepts

- **.format()** (5 connections) — `server/structured_logging/player_guid_formatter.py`
- **_canonical_ip()** (3 connections) — `server/middleware/auth_rate_limit.py`
- **._convert_player_guids()** (3 connections) — `server/structured_logging/player_guid_formatter.py`
- **LogRecord** (1 connections)
- **Format a log record with enhanced player GUID display. Args: record: The log…** (1 connections) — `server/structured_logging/player_guid_formatter.py`
- **Convert player GUIDs in message to enhanced format. Args: message: The log…** (1 connections) — `server/structured_logging/player_guid_formatter.py`

## Relationships

- [PeriodicOrphanAuditor](PeriodicOrphanAuditor.md) (2 shared connections)
- [_PlayerCombatClearing](_PlayerCombatClearing.md) (1 shared connections)
- [Optimize Skill](Optimize_Skill.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/structured_logging/player_guid_formatter.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*