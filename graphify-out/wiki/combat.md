# combat

> 223 nodes

## Key Concepts

- **NPCCombatIntegrationService** (89 connections) — `server/services/npc_combat_integration_service.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **test_npc_combat_integration_service.py** (44 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack_on_player()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **_StubConfigRoot** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **integration_service()** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **player_combat_service()** (6 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
- *... and 198 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (28 shared connections)
- [. init ()](_init_%28%29.md) (17 shared connections)
- [CombatService](CombatService.md) (12 shared connections)
- [Any](Any.md) (11 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (7 shared connections)
- [Player](Player.md) (5 shared connections)
- [look container](look_container.md) (4 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (3 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (3 shared connections)
- [Test despawn npc handles NPC](Test_despawn_npc_handles_NPC.md) (3 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/models/combat.py`
- `server/realtime/connection_manager.py`
- `server/services/combat_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 715 (94%)
- INFERRED: 47 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*