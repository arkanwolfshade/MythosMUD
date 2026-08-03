# combat services messaging

> 11 nodes

## Key Concepts

- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **envelope_assertions.py** (6 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_follow_request_event_envelope_shape()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_party_invite_event_envelope_shape()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **test_broadcast_combat_start()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **follow_request producer emits a build_event-shaped envelope.** (1 connections) — `server/tests/unit/game/test_follow_service.py`
- **party_invite producer emits a build_event-shaped envelope.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Any** (1 connections)
- **Shared contract assertions for realtime event envelopes produced via build_event** (1 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **Assert a fan-out producer event matches the build_event envelope shape.** (1 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **Test broadcast_combat_start broadcasts combat start event.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`

## Relationships

- [party service game](party_service_game.md) (3 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (3 shared connections)
- [command parser rationale](command_parser_rationale.md) (3 shared connections)
- [combat messaging services](combat_messaging_services.md) (3 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)
- [party game service](party_game_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/game/test_party_service.py`
- `server/tests/unit/realtime/envelope_assertions.py`
- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*