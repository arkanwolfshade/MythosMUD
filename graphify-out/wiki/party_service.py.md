# party_service.py

> 18 nodes

## Key Concepts

- **party_service.py** (17 connections) — `server/game/party_service.py`
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
- **Party service for MythosMUD. In-memory ephemeral party state: parties exist…** (1 connections) — `server/game/party_service.py`
- **Integration tests for party (ephemeral grouping) feature. Flow: Two players;…** (1 connections) — `server/tests/integration/test_party_flow.py`
- **When leader leaves, party is disbanded and disbanded event is emitted.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Real EventBus for integration.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Collect PartyUpdated events published during test.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **PartyService wired to real EventBus.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Two players: A creates party, adds B; B leaves; A disbands. Verify in-memory…** (1 connections) — `server/tests/integration/test_party_flow.py`

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [PartyService](PartyService.md) (9 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [test_party_service.py](test_party_service.py.md) (1 shared connections)
- [Party](Party.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`

## Audit Trail

- EXTRACTED: 45 (82%)
- INFERRED: 10 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*