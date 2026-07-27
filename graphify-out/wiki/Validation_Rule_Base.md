# Validation Rule Base

> 31 nodes · cohesion 0.07

## Key Concepts

- **ValidationRule** (10 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **String representation of the NPC definition.** (9 connections) — `server/models/npc.py`
- **ValidationError** (8 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **base_rule.py** (5 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.create_error()** (3 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.create_warning()** (3 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.validate()** (3 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **__init__.py** (3 connections) — `tools/room_toolkit/room_validator/rules/__init__.py`
- **.__repr__()** (2 connections) — `server/models/alias.py`
- **.__repr__()** (2 connections) — `server/models/npc.py`
- **.__repr__()** (2 connections) — `server/models/npc.py`
- **.__repr__()** (2 connections) — `server/models/profession.py`
- **.__str__()** (2 connections) — `server/models/room.py`
- **.__repr__()** (2 connections) — `server/models/skill.py`
- **.__repr__()** (2 connections) — `server/models/user.py`
- **.__init__()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.__str__()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **._filter_rooms_by_zone()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.get_rule_info()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.__init__()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **Base validation rule class.  This module defines the abstract base class for all** (1 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **Create a validation error for this rule.          Args:             room_id: Roo** (1 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **Represents a validation error with metadata.      As documented in the restricte** (1 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **Create a validation warning for this rule.          Args:             room_id: R** (1 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **Get information about this rule.          Returns:             Dictionary with r** (1 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- *... and 6 more nodes in this community*

## Relationships

- [[NPC Definition Schemas]] (2 shared connections)
- [[Game Mechanics Service]] (2 shared connections)
- [[Command Alias Model]] (1 shared connections)
- [[LRU Cache Manager]] (1 shared connections)
- [[Profession Model Tests]] (1 shared connections)
- [[Room Occupancy Class]] (1 shared connections)
- [[Game Service Bundle]] (1 shared connections)
- [[API Test Fixtures]] (1 shared connections)
- [[Standardized Error Responses]] (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/models/npc.py`
- `server/models/profession.py`
- `server/models/room.py`
- `server/models/skill.py`
- `server/models/user.py`
- `tools/room_toolkit/room_validator/rules/__init__.py`
- `tools/room_toolkit/room_validator/rules/base_rule.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
