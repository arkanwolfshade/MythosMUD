# NPC Combat Integration

> 197 nodes

## Key Concepts

- **NPCCombatIntegrationService** (94 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (47 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **asyncio** (25 connections)
- **test_npc_combat_integration_service_player_attacks.py** (22 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_npc_combat_integration_service_npc_aggro.py** (19 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **asyncio** (14 connections)
- **.__init__()** (13 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service_aggro_logging.py** (13 connections) — `server/tests/unit/services/test_npc_combat_integration_service_aggro_logging.py`
- **_RecordingLogger** (9 connections) — `server/tests/unit/services/test_npc_combat_integration_service_aggro_logging.py`
- **asyncio** (9 connections)
- **integration_service()** (8 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **_attack_raising()** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service_aggro_logging.py`
- **mock_async_persistence()** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_combat_service()** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_connection_manager()** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **_StubConfigRoot** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **.is_alive()** (5 connections) — `server/models/combat.py`
- **._complete_player_attack_on_npc_after_grace()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **test_already_dead_is_a_debug_skip_not_an_error()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service_aggro_logging.py`
- **test_already_in_combat_is_a_debug_skip_not_an_error()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service_aggro_logging.py`
- **test_unexpected_value_error_is_still_logged_as_error()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service_aggro_logging.py`
- **test_validate_combat_location_limbo_cross_room_uses_debug()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **fixture** (5 connections)
- **.handle_npc_attack_on_player()** (4 connections) — `server/services/npc_combat_integration_service.py`
- *... and 172 more nodes in this community*

## Relationships

- [Combat Attack Execution](Combat_Attack_Execution.md) (18 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (7 shared connections)
- [Community 251](Community_251.md) (7 shared connections)
- [Community 226](Community_226.md) (6 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (4 shared connections)
- [Community 126](Community_126.md) (3 shared connections)
- [Community 227](Community_227.md) (3 shared connections)
- [Community 82](Community_82.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 502](Community_502.md) (2 shared connections)
- [Community 369](Community_369.md) (2 shared connections)
- [Community 222](Community_222.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service_aggro_logging.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Audit Trail

- EXTRACTED: 312 (81%)
- INFERRED: 72 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*