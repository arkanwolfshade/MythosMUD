# server events event types partyupdated

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

- [server game party service](server_game_party_service.md) (8 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (4 shared connections)
- [server events event bus](server_events_event_bus.md) (3 shared connections)
- [moduletype](moduletype.md) (1 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/tests/integration/test_party_flow.py`

## Audit Trail

- EXTRACTED: 30 (75%)
- INFERRED: 10 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*