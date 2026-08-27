# ChatMessage

> 63 nodes

## Key Concepts

- **.connection_manager()** (26 connections) — `server/services/combat_messaging/base.py`
- **.get_instance()** (25 connections) — `server/container/main.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **test_npc_combat_grace.py** (9 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **_CombatServiceDeps** (8 connections) — `server/services/combat_death_handler.py`
- **._create_corpse_on_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **check_attacker_grace_period()** (7 connections) — `server/services/combat_service_start.py`
- **._log_room_subscribers_before_npc_death()** (6 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (6 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (5 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **_NPCCombatIntegrationLike** (4 connections) — `server/services/combat_death_handler.py`
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (4 connections) — `server/services/combat_death_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **Protocol** (3 connections)
- **.get_npc_combat_integration_service()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_player_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- *... and 38 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (11 shared connections)
- [MythosMUDError](MythosMUDError.md) (9 shared connections)
- [NATSService](NATSService.md) (8 shared connections)
- [command_service.py](command_service.py.md) (6 shared connections)
- [User](User.md) (6 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (5 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (4 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (3 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service_start.py`
- `server/services/npc_combat_grace.py`
- `server/tests/unit/services/test_npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 129 (84%)
- INFERRED: 25 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*