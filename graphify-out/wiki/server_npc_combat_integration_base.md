# server npc combat integration base

> 45 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
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
- **test_resolve_npc_combat_service_from_container()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **ABC** (2 connections)
- **UUID** (2 connections)
- **Exception** (1 connections)
- **ValidationError** (1 connections)
- *... and 20 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (3 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (3 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (2 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)
- [server game mechanics gamemechanicsservice](server_game_mechanics_gamemechanicsservice.md) (1 shared connections)
- [server events combat events](server_events_combat_events.md) (1 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)
- [server container main get container](server_container_main_get_container.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`

## Audit Trail

- EXTRACTED: 77 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*