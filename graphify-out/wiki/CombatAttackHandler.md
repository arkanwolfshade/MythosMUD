# CombatAttackHandler

> 52 nodes

## Key Concepts

- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **npc_combat_grace.py** (13 connections) — `server/services/npc_combat_grace.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (6 connections) — `server/services/npc_combat_grace.py`
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.__init__()** (3 connections) — `server/services/combat_attack_handler.py`
- **._validate_target_can_be_attacked()** (3 connections) — `server/services/combat_attack_handler.py`
- **.handle_npc_attack()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.award_xp_to_killer()** (3 connections) — `server/services/npc_combat_rewards.py`
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_rewards.py`
- **UUID** (3 connections)
- *... and 27 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (13 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (11 shared connections)
- [combat_service.py](combat_service.py.md) (8 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [test_damage_grace_period.py](test_damage_grace_period.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [CombatMessagingService](CombatMessagingService.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/npc_combat_grace.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 108 (88%)
- INFERRED: 15 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*