# combat messaging services

> 8 nodes

## Key Concepts

- **test_combat_messaging_integration.py** (34 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_messaging_integration_init_no_connection_manager()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_resolve_connection_manager_from_container()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_mortally_wounded()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Unit tests for combat messaging integration.  Tests the CombatMessagingIntegrati** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test CombatMessagingIntegration initialization without connection manager.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test _resolve_connection_manager_from_container resolves manager.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test broadcast_player_mortally_wounded broadcasts message.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`

## Relationships

- [player persistence repository](player_persistence_repository.md) (13 shared connections)
- [npc idle movement](npc_idle_movement.md) (4 shared connections)
- [persistence player repository](persistence_player_repository.md) (4 shared connections)
- [idle npc movement](idle_npc_movement.md) (3 shared connections)
- [player repository persistence](player_repository_persistence.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [idle movement npc](idle_movement_npc.md) (1 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 44 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*