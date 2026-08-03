# skill game service

> 14 nodes

## Key Concepts

- **PartyUpdated** (12 connections) — `server/events/event_types.py`
- **test_party_flow.py** (12 connections) — `server/tests/integration/test_party_flow.py`
- **party_events()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **party_service()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_invite_join_leave_disband_state_and_events()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_leader_leaves_disbands()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **event_bus()** (3 connections) — `server/tests/integration/test_party_flow.py`
- **Event fired when party membership or leadership changes.      Emitted by PartySe** (1 connections) — `server/events/event_types.py`
- **Integration tests for party (ephemeral grouping) feature.  Flow: Two players; le** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Real EventBus for integration.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Collect PartyUpdated events published during test.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **PartyService wired to real EventBus.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Two players: A creates party, adds B; B leaves; A disbands.     Verify in-memory** (1 connections) — `server/tests/integration/test_party_flow.py`
- **When leader leaves, party is disbanded and disbanded event is emitted.** (1 connections) — `server/tests/integration/test_party_flow.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (8 shared connections)
- [party game service](party_game_service.md) (8 shared connections)
- [command service commands](command_service_commands.md) (1 shared connections)
- [commands admin shutdown](commands_admin_shutdown.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/tests/integration/test_party_flow.py`

## Audit Trail

- EXTRACTED: 48 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*