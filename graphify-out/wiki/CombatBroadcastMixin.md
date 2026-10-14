# CombatBroadcastMixin

> 33 nodes

## Key Concepts

- **CombatBroadcastMixin** (20 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._broadcast_combat_event()** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_attack()** (7 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **_npc_part()** (7 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **HasConnectionManager** (6 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_combat_target_switch()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_joined_combat()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **_line_fields()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_taunt_result()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_protect_result()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_categories()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_messages()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **NpcDisposition** (3 connections)
- **Any** (2 connections)
- **MessageCategory** (1 connections)
- **Base for mixins that require connection_manager. Satisfies mypy attr-defined…** (1 connections) — `server/services/combat_messaging/base.py`
- **Send personal combat message to attacker when attacker_id is present.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast combat attack to room. Excludes attacker from broadcast; sends them a…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **An NPC's name as a line part: styled when its disposition is known, plain text…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Build one combat event tagged with its message category and send it to the…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast one short room message when an NPC switches aggro target (ADR-016).** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast one room line when a player joins a fight already under way (#833).…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- *... and 8 more nodes in this community*

## Relationships

- [NpcDisposition](NpcDisposition.md) (10 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [MessageCategory](MessageCategory.md) (2 shared connections)
- [.connection_manager](connection_manager.md) (2 shared connections)
- [log_room_broadcast_result](log_room_broadcast_result.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`

## Audit Trail

- EXTRACTED: 65 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*