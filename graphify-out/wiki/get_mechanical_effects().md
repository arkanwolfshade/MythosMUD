# .get mechanical effects()

> 16 nodes

## Key Concepts

- **PartyService** (36 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **test_party_invite_event_envelope_shape()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **.get_party()** (3 connections) — `server/game/party_service.py`
- **party_service()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **In-memory party management: create, disband, add/remove/kick members, leader che** (1 connections) — `server/game/party_service.py`
- **Return the party the player is in, or None.** (1 connections) — `server/game/party_service.py`
- **Return the party by id, or None.** (1 connections) — `server/game/party_service.py`
- **Return True if the player is the leader of their current party.** (1 connections) — `server/game/party_service.py`
- **Return list of party member IDs for the given player (including themselves).** (1 connections) — `server/game/party_service.py`
- **Return True if both players are in the same party. For combat/validator hook:** (1 connections) — `server/game/party_service.py`
- **PartyService with no dependencies (in-memory only).** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **party_invite producer emits a build_event-shaped envelope.** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [test command factories player state](test_command_factories_player_state.md) (16 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (9 shared connections)
- [.calculate backoff()](calculate_backoff%28%29.md) (7 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [test party service](test_party_service.md) (3 shared connections)
- [Player](Player.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 72 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*