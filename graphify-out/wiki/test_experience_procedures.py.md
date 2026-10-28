# test_experience_procedures.py

> 28 nodes · cohesion 0.09

## Key Concepts

- **party_service.py** (18 connections) — `server/game/party_service.py`
- **test_party_flow.py** (13 connections) — `server/tests/integration/test_party_flow.py`
- **PartyUpdated** (11 connections) — `server/events/event_types.py`
- **Party** (9 connections) — `server/game/party_service.py`
- **party_events()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **party_service()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_invite_join_leave_disband_state_and_events()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_leader_leaves_disbands()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **event_bus()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **.get_party()** (3 connections) — `server/game/party_service.py`
- **asyncio** (3 connections)
- **fixture** (3 connections)
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **.__post_init__()** (2 connections) — `server/game/party_service.py`
- **Event fired when party membership or leadership changes. Emitted by…** (1 connections) — `server/events/event_types.py`
- **Party service for MythosMUD. In-memory ephemeral party state: parties exist…** (1 connections) — `server/game/party_service.py`
- **In-memory party model. Ephemeral: not persisted. party_id and member_ids are…** (1 connections) — `server/game/party_service.py`
- **Return the party by id, or None.** (1 connections) — `server/game/party_service.py`
- **Ensure leader is in member set.** (1 connections) — `server/game/party_service.py`
- **Integration tests for party (ephemeral grouping) feature. Flow: Two players;…** (1 connections) — `server/tests/integration/test_party_flow.py`
- **When leader leaves, party is disbanded and disbanded event is emitted.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Real EventBus for integration.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Collect PartyUpdated events published during test.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **PartyService wired to real EventBus.** (1 connections) — `server/tests/integration/test_party_flow.py`
- *... and 3 more nodes in this community*

## Relationships

- [test_wearable_container_service.py](test_wearable_container_service.py.md) (12 shared connections)
- [get_username_from_user](get_username_from_user.md) (6 shared connections)
- [LogAggregator](LogAggregator.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [test_passive_lucidity_flux_service.py](test_passive_lucidity_flux_service.py.md) (1 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [.publish_with_pool](publish_with_pool.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 62 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*