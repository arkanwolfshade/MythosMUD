# Services Combat Attack

> 13 nodes · cohesion 0.21

## Key Concepts

- **._apply_damage()** (8 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (6 connections) — `server/services/combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **CombatInstance** (4 connections) — `server/services/combat_attack_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **CombatParticipant** (3 connections) — `server/services/combat_attack_handler.py`
- **UUID** (2 connections) — `server/services/combat_attack_handler.py`
- **Apply damage to target and update combat state.          Args:             comba** (1 connections) — `server/services/combat_attack_handler.py`
- **Validate attack and retrieve combat participants.          Args:             att** (1 connections) — `server/services/combat_attack_handler.py`
- **Validate that attack is allowed.** (1 connections) — `server/services/combat_attack_handler.py`
- **Apply damage to target and check death states.          Delegates domain logic t** (1 connections) — `server/services/combat_attack_handler.py`
- **Check if room has no_death attribute (tutorial/safe zones).** (1 connections) — `server/services/combat_attack_handler.py`

## Relationships

- [[Combat Service Bundle]] (5 shared connections)
- [[Combat Taunt Tests]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Look Command Helpers]] (1 shared connections)
- [[Realtime WebSocket Auth]] (1 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
