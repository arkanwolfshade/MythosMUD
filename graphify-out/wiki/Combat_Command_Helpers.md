# Combat Command Helpers

> 38 nodes · cohesion 0.10

## Key Concepts

- **combat_loader.py** (19 connections) — `server/commands/combat_loader.py`
- **combat.py** (14 connections) — `server/commands/combat.py`
- **get_combat_command_handler()** (14 connections) — `server/commands/combat_loader.py`
- **AliasStorage** (14 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (9 connections) — `server/commands/combat_loader.py`
- **_app_from_request()** (8 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (7 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (7 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (7 connections) — `server/commands/combat_loader.py`
- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- **handle_flee_command()** (6 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (6 connections) — `server/commands/combat_loader.py`
- **test_combat_helpers.py** (5 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **combat_helpers.py** (4 connections) — `server/commands/combat_helpers.py`
- **test_format_combat_status_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_format_combat_status_not_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target_not_found()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **Any** (2 connections) — `server/commands/combat_helpers.py`
- **Shared helpers and exceptions for combat commands.  Extracted from combat.py to** (1 connections) — `server/commands/combat_helpers.py`
- **Produce a human-readable combat status string.      This helper is retained for** (1 connections) — `server/commands/combat_helpers.py`
- **Resolve a combat target by name.      The current implementation is intentionall** (1 connections) — `server/commands/combat_helpers.py`
- **Combat command handler singleton and public async command entry points.  Extract** (1 connections) — `server/commands/combat_loader.py`
- **Handle kick command (alias for attack).** (1 connections) — `server/commands/combat_loader.py`
- *... and 13 more nodes in this community*

## Relationships

- [[Combat Command Handler]] (9 shared connections)
- [[Alias Expansion Logic]] (4 shared connections)
- [[Combat Service Bundle]] (4 shared connections)
- [[Combat Flee Command]] (2 shared connections)
- [[Async Persistence Layer]] (2 shared connections)
- [[Distributed Event Bus]] (2 shared connections)
- [[Room Occupant Events]] (2 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)
- [[Flee Command Tests]] (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_helpers.py`

## Audit Trail

- EXTRACTED: 146 (89%)
- INFERRED: 18 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
