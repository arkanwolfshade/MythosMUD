# test_party_flow.py

> 16 nodes

## Key Concepts

- **test_party_flow.py** (14 connections) — `server/tests/integration/test_party_flow.py`
- **PartyUpdated** (11 connections) — `server/events/event_types.py`
- **party_events()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **party_service()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_invite_join_leave_disband_state_and_events()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_leader_leaves_disbands()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **event_bus()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **asyncio** (3 connections)
- **fixture** (3 connections)
- **Event fired when party membership or leadership changes. Emitted by…** (1 connections) — `server/events/event_types.py`
- **Integration tests for party (ephemeral grouping) feature. Flow: Two players;…** (1 connections) — `server/tests/integration/test_party_flow.py`
- **When leader leaves, party is disbanded and disbanded event is emitted.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Real EventBus for integration.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Collect PartyUpdated events published during test.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **PartyService wired to real EventBus.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Two players: A creates party, adds B; B leaves; A disbands. Verify in-memory…** (1 connections) — `server/tests/integration/test_party_flow.py`

## Relationships

- [EventBus](EventBus.md) (5 shared connections)
- [PartyService](PartyService.md) (5 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/tests/integration/test_party_flow.py`

## Audit Trail

- EXTRACTED: 32 (80%)
- INFERRED: 8 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*