# PartyUpdated

> 16 nodes

## Key Concepts

- **party_service.py** (16 connections) — `server/game/party_service.py`
- **PartyUpdated** (12 connections) — `server/events/event_types.py`
- **test_party_flow.py** (12 connections) — `server/tests/integration/test_party_flow.py`
- **party_events()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **party_service()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_invite_join_leave_disband_state_and_events()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_leader_leaves_disbands()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **event_bus()** (3 connections) — `server/tests/integration/test_party_flow.py`
- **Event fired when party membership or leadership changes.      Emitted by PartySe** (1 connections) — `server/events/event_types.py`
- **Party service for MythosMUD.  In-memory ephemeral party state: parties exist onl** (1 connections) — `server/game/party_service.py`
- **Integration tests for party (ephemeral grouping) feature.  Flow: Two players; le** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Real EventBus for integration.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Collect PartyUpdated events published during test.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **PartyService wired to real EventBus.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Two players: A creates party, adds B; B leaves; A disbands.     Verify in-memory** (1 connections) — `server/tests/integration/test_party_flow.py`
- **When leader leaves, party is disbanded and disbanded event is emitted.** (1 connections) — `server/tests/integration/test_party_flow.py`

## Relationships

- [PartyService](PartyService.md) (8 shared connections)
- [Any](Any.md) (6 shared connections)
- [.initialize()](initialize%28%29.md) (5 shared connections)
- [Party](Party.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [. post init ()](_post_init_%28%29.md) (1 shared connections)
- [.create party()](create_party%28%29.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [test party service](test_party_service.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`

## Audit Trail

- EXTRACTED: 65 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*