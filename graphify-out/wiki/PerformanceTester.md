# PerformanceTester

> 34 nodes · cohesion 0.09

## Key Concepts

- **test_combat_status_segments.py** (23 connections) — `server/tests/unit/services/test_combat_status_segments.py`
- **CombatBroadcastMixin** (20 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._broadcast_combat_event()** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **_Broadcaster** (9 connections) — `server/tests/unit/services/test_combat_status_segments.py`
- **.broadcast_combat_attack()** (7 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **asyncio** (5 connections)
- **.broadcast_taunt_result()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **test_aggro_switches_look_up_each_npcs_disposition()** (4 connections) — `server/tests/unit/services/test_combat_status_segments.py`
- **test_join_styles_the_foe_not_the_joiner()** (4 connections) — `server/tests/unit/services/test_combat_status_segments.py`
- **test_target_switch_styles_the_npc_when_its_disposition_is_known()** (4 connections) — `server/tests/unit/services/test_combat_status_segments.py`
- **.broadcast_protect_result()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_categories()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_messages()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **test_target_switch_without_a_disposition_stays_plain()** (3 connections) — `server/tests/unit/services/test_combat_status_segments.py`
- **test_taunt_accepts_a_plain_line_or_parts()** (3 connections) — `server/tests/unit/services/test_combat_status_segments.py`
- **Any** (2 connections)
- **MessageCategory** (1 connections)
- **Send personal combat message to attacker when attacker_id is present.** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast combat attack to room. Excludes attacker from broadcast; sends them a…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Build one combat event tagged with its message category and send it to the…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast the one room line for a resolved taunt: success, failure or fumble…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Broadcast one room line for a protect: its cast result, or one hit the cover…** (1 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- *... and 9 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (20 shared connections)
- [Reporter](Reporter.md) (5 shared connections)
- [.publish_with_pool](publish_with_pool.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (2 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/combat_broadcasts.py`
- `server/tests/unit/services/test_combat_status_segments.py`

## Audit Trail

- EXTRACTED: 80 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*