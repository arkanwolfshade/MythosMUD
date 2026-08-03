# combat messaging services

> 73 nodes

## Key Concepts

- **test_combat_messaging_integration.py** (34 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **envelope_assertions.py** (6 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_follow_request_event_envelope_shape()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_party_invite_event_envelope_shape()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **messaging_integration()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_messaging_integration_init_no_connection_manager()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_combat_start()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_messaging_integration_init()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_connection_manager_property_lazy_load()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_resolve_connection_manager_from_container()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_resolve_connection_manager_from_container_no_manager()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_resolve_connection_manager_from_container_error()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_combat_attack()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_combat_attack_personal_message_error()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_combat_death()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_combat_ended()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_combat_end()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_combat_error()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_mortally_wounded()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_died()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_mortally_wounded_with_attacker()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_mortally_wounded_no_attacker()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_respawn()** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- *... and 48 more nodes in this community*

## Relationships

- [party service game](party_service_game.md) (3 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (3 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (2 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)
- [party game service](party_game_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/game/test_party_service.py`
- `server/tests/unit/realtime/envelope_assertions.py`
- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 159 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*