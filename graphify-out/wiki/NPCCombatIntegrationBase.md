# NPCCombatIntegrationBase

> 44 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_base.py** (23 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
- **._handle_attribute_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_unexpected_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_validation_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._apply_mental_effects()** (3 connections) — `server/npc/combat_integration_base.py`
- **.calculate_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_npc_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_target_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **.handle_npc_attack()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_npc_attack_to_nats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_player_dp_updated_after_npc_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **ABC** (2 connections)
- **UUID** (2 connections)
- **Exception** (1 connections)
- **ValidationError** (1 connections)
- **Base segment of NPC combat integration (damage, effects, attack orchestration).…** (1 connections) — `server/npc/combat_integration_base.py`
- *... and 19 more nodes in this community*

## Relationships

- [get_config](get_config.md) (5 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (3 shared connections)
- [combat_integration_protocols.py](combat_integration_protocols.py.md) (3 shared connections)
- [test_combat_integration_base.py](test_combat_integration_base.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`

## Audit Trail

- EXTRACTED: 93 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*