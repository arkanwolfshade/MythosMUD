# Server Services (29)

> 64 nodes

## Key Concepts

- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (14 connections) — `server/services/combat_service_events.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (10 connections) — `server/services/combat_service_attack.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (9 connections) — `server/services/combat_service_attack.py`
- **.handle_attack_events_and_xp()** (8 connections) — `server/services/combat_event_handler.py`
- **_check_involuntary_flee_with_session()** (8 connections) — `server/services/combat_flee_handler.py`
- **handle_combat_completion()** (8 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (8 connections) — `server/services/combat_service_attack.py`
- **publish_npc_damage_event()** (7 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (7 connections) — `server/services/combat_service_events.py`
- **check_involuntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **queue_combat_action()** (6 connections) — `server/services/combat_service_attack.py`
- **UUID** (6 connections)
- **.award_xp_to_player()** (5 connections) — `server/services/combat_event_handler.py`
- **_involuntary_flee_on_cooldown()** (5 connections) — `server/services/combat_flee_handler.py`
- **_effective_room_for_melee()** (5 connections) — `server/services/combat_service_attack.py`
- **broadcast_aggro_target_switches()** (5 connections) — `server/services/combat_service_events.py`
- *... and 39 more nodes in this community*

## Relationships

- [Server Services (9)](Server_Services_%289%29.md) (27 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (21 shared connections)
- [Server Models (2)](Server_Models_%282%29.md) (20 shared connections)
- [Server Services (17)](Server_Services_%2817%29.md) (19 shared connections)
- [Server Services (28)](Server_Services_%2828%29.md) (18 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (17 shared connections)
- [Server Commands](Server_Commands.md) (12 shared connections)
- [Server Services](Server_Services.md) (8 shared connections)
- [Server Services (68)](Server_Services_%2868%29.md) (7 shared connections)
- [Server Services (13)](Server_Services_%2813%29.md) (5 shared connections)
- [Server Services (4)](Server_Services_%284%29.md) (5 shared connections)
- [Server Game (7)](Server_Game_%287%29.md) (4 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/lucidity_command_disruption.py`

## Audit Trail

- EXTRACTED: 389 (97%)
- INFERRED: 14 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*