# NPCCombatIntegrationBase

> 53 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **_resolve_npc_combat_service_raw()** (5 connections) — `server/npc/combat_integration_base.py`
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
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **ABC** (2 connections)
- *... and 28 more nodes in this community*

## Relationships

- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (6 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [.initialize()](initialize%28%29.md) (5 shared connections)
- [.state()](state%28%29.md) (3 shared connections)
- [login grace period](login_grace_period.md) (2 shared connections)
- [.handle()](handle%28%29.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 160 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*