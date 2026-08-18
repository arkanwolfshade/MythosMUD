# server events combat events

> 241 nodes

## Key Concepts

- **CombatService** (165 connections) — `server/services/combat_service.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **combat_event_publisher.py** (23 connections) — `server/services/combat_event_publisher.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **UUID** (20 connections)
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **finalize_attack_result()** (10 connections) — `server/services/combat_service_attack.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- *... and 216 more nodes in this community*

## Relationships

- [server events combat events combatendedevent](server_events_combat_events_combatendedevent.md) (40 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (37 shared connections)
- [server services aggro threat clear](server_services_aggro_threat_clear.md) (31 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (30 shared connections)
- [server services combat service npc](server_services_combat_service_npc.md) (26 shared connections)
- [server game mechanics](server_game_mechanics.md) (24 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (23 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (21 shared connections)
- [server models combat](server_models_combat.md) (20 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (19 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (15 shared connections)
- [server services combat initialization](server_services_combat_initialization.md) (14 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_persistence_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_combat_service_modules.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 686 (85%)
- INFERRED: 120 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*