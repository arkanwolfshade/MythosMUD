# circuit breaker realtime

> 42 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
- **._handle_attribute_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_validation_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_unexpected_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **.handle_npc_attack()** (4 connections) — `server/npc/combat_integration_base.py`
- **._get_target_stats()** (4 connections) — `server/npc/combat_integration_base.py`
- **.calculate_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **UUID** (3 connections)
- **._apply_mental_effects()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_npc_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_player_dp_updated_after_npc_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_npc_attack_to_nats()** (3 connections) — `server/npc/combat_integration_base.py`
- **ABC** (2 connections)
- **ValidationError** (1 connections)
- **Exception** (1 connections)
- **Base implementation: damage, combat effects, and NPC attack orchestration.** (1 connections) — `server/npc/combat_integration_base.py`
- **Calculate damage based on attacker and target stats.          Args:** (1 connections) — `server/npc/combat_integration_base.py`
- *... and 17 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [tools generate invite](tools_generate_invite.md) (3 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (2 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [services nats service](services_nats_service.md) (1 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [room sync service](room_sync_service.md) (1 shared connections)
- [add used user](add_used_user.md) (1 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`

## Audit Trail

- EXTRACTED: 134 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*