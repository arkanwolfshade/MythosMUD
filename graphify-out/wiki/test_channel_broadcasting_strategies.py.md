# test_channel_broadcasting_strategies.py

> 13 nodes

## Key Concepts

- **.broadcast_combat_attack()** (7 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_target_switch()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_messages()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_combat_message()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Any** (3 connections)
- **Broadcast combat attack to room. Excludes attacker from broadcast; sends them a…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast one short room message when an NPC switches aggro target (ADR-016).** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Build perspective-specific attack messages.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Build combat_attack event payload.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Send personal combat message to attacker. Logs warning on failure.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Send personal combat message to attacker when attacker_id is present.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)

## Source Files

- `server/services/combat_messaging/combat_broadcasts.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*