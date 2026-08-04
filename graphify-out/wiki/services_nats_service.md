# services nats service

> 130 nodes

## Key Concepts

- **NPCCombatIntegration** (103 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (46 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **combat_integration.py** (26 connections) — `server/npc/combat_integration.py`
- **test_combat_integration_base.py** (24 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **NPCAttacked** (16 connections) — `server/events/event_types.py`
- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **UUID** (7 connections)
- **.get_combat_stats()** (7 connections) — `server/npc/combat_integration.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_after_npc_damage()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_event()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_npc_attack_to_nats()** (5 connections) — `server/npc/combat_integration.py`
- **._get_int_stat()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_for_dp_update()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_and_stats_for_nats()** (4 connections) — `server/npc/combat_integration.py`
- **.handle_npc_death()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 105 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (16 shared connections)
- [Error Conversion](Error_Conversion.md) (15 shared connections)
- [npc combat base](npc_combat_base.md) (10 shared connections)
- [lucidity event services](lucidity_event_services.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [attack combat commands](attack_combat_commands.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [spell game magic](spell_game_magic.md) (3 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (3 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 485 (96%)
- INFERRED: 22 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*