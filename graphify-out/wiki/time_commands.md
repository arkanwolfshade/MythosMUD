# time commands

> 21 nodes

## Key Concepts

- **Any** (7 connections)
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_start()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_death()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_end()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_error()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_target_switch()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_messages()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Build perspective-specific attack messages.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Build combat_attack event payload.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Send personal combat message to attacker. Logs warning on failure.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Send personal combat message to attacker when attacker_id is present.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast combat start message to all players in the room.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast combat attack to room. Excludes attacker from broadcast; sends them a** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast NPC death message to all players in the room.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast combat end message to all players in the room.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast combat error message to a specific player.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast one short room message when an NPC switches aggro target (ADR-016).** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`

## Relationships

- [. init ()](_init_%28%29.md) (10 shared connections)
- [circuit breaker](circuit_breaker.md) (7 shared connections)

## Source Files

- `server/services/combat_messaging/combat_broadcasts.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*