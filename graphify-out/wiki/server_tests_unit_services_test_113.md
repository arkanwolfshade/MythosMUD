# server tests unit services test

> 14 nodes

## Key Concepts

- **asyncio** (21 connections)
- **test_broadcast_combat_start()** (4 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_combat_attack_personal_message_error()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_combat_attack_with_attacker_id()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_death_personal_message_error()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_mortally_wounded_no_attacker()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_mortally_wounded_with_attacker()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_broadcast_player_respawn()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test broadcast_player_mortally_wounded with attacker name.** (2 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test broadcast_combat_attack handles personal message errors gracefully.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test broadcast_player_respawn broadcasts respawn message.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test broadcast_combat_attack sends personal message to attacker.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test broadcast_player_death handles personal message errors.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test broadcast_combat_start broadcasts combat start event.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (21 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*