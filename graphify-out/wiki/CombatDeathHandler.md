# CombatDeathHandler

> 67 nodes

## Key Concepts

- **CombatDeathHandler** (22 connections) — `server/services/combat_death_handler.py`
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **_CombatServiceDeps** (8 connections) — `server/services/combat_death_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (6 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (6 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (6 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (5 connections) — `server/services/combat_death_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (4 connections) — `server/services/combat_death_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_attack_handler.py`
- **._validate_target_can_be_attacked()** (3 connections) — `server/services/combat_attack_handler.py`
- *... and 42 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (12 shared connections)
- [CombatParticipant](CombatParticipant.md) (12 shared connections)
- [models/combat.py](models-combat.py.md) (11 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (5 shared connections)
- [SpellEffects](SpellEffects.md) (4 shared connections)
- [combat_service.py](combat_service.py.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (2 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`

## Audit Trail

- EXTRACTED: 138 (85%)
- INFERRED: 24 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*