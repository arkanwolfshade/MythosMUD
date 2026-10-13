# Community 635

> 27 nodes

## Key Concepts

- **CombatBroadcastMixin** (17 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._broadcast_combat_event()** (8 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_target_switch()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_joined_combat()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_protect_result()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_taunt_result()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_categories()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_messages()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Any** (2 connections)
- **HasConnectionManager** (1 connections)
- **MessageCategory** (1 connections)
- **Send personal combat message to attacker when attacker_id is present.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast combat attack to room. Excludes attacker from broadcast; sends them a…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Mixin for combat-related broadcast methods. Requires connection_manager on self.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Build one combat event tagged with its message category and send it to the…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast one short room message when an NPC switches aggro target (ADR-016).** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast one room line when a player joins a fight already under way (#833).…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Build perspective-specific attack messages.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast the one room line for a resolved taunt: success, failure or fumble…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast one room line for a protect: its cast result, or one hit the cover…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Category of each perspective line in ``messages``, from that recipient's point…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- *... and 2 more nodes in this community*

## Relationships

- [Community 41](Community_41.md) (6 shared connections)
- [Community 98](Community_98.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/combat_broadcasts.py`

## Audit Trail

- EXTRACTED: 42 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*