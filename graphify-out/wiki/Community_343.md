# Community 343

> 49 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (23 connections) — `server/npc/combat_integration_base.py`
- **.state()** (19 connections) — `server/realtime/connection_state_machine.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
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
- **test_resolve_npc_combat_service_from_container()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **ABC** (2 connections)
- **UUID** (2 connections)
- *... and 24 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (9 shared connections)
- [Community 46](Community_46.md) (2 shared connections)
- [Community 48](Community_48.md) (2 shared connections)
- [Community 323](Community_323.md) (2 shared connections)
- [Community 65](Community_65.md) (1 shared connections)
- [Community 170](Community_170.md) (1 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (1 shared connections)
- [Community 511](Community_511.md) (1 shared connections)
- [Community 278](Community_278.md) (1 shared connections)
- [Community 1445](Community_1445.md) (1 shared connections)
- [Community 120](Community_120.md) (1 shared connections)
- [Community 783](Community_783.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/realtime/connection_state_machine.py`
- `server/tests/unit/npc/test_combat_integration_base.py`

## Audit Trail

- EXTRACTED: 83 (82%)
- INFERRED: 18 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*