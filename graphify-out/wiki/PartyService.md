# PartyService

> 25 nodes

## Key Concepts

- **PartyService** (35 connections) — `server/game/party_service.py`
- **party_service.py** (16 connections) — `server/game/party_service.py`
- **test_party_flow.py** (13 connections) — `server/tests/integration/test_party_flow.py`
- **PartyUpdated** (12 connections) — `server/events/event_types.py`
- **party_events()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **party_service()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_invite_join_leave_disband_state_and_events()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_leader_leaves_disbands()** (5 connections) — `server/tests/integration/test_party_flow.py`
- **._send_party_invite_to_target()** (4 connections) — `server/game/party_service.py`
- **event_bus()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **party_service()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **asyncio** (3 connections)
- **fixture** (3 connections)
- **fixture** (1 connections)
- **Event fired when party membership or leadership changes. Emitted by…** (1 connections) — `server/events/event_types.py`
- **Party service for MythosMUD. In-memory ephemeral party state: parties exist…** (1 connections) — `server/game/party_service.py`
- **Send party_invite event to the target player only.** (1 connections) — `server/game/party_service.py`
- **In-memory party management: create, disband, add/remove/kick members, leader…** (1 connections) — `server/game/party_service.py`
- **Integration tests for party (ephemeral grouping) feature. Flow: Two players;…** (1 connections) — `server/tests/integration/test_party_flow.py`
- **When leader leaves, party is disbanded and disbanded event is emitted.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Real EventBus for integration.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Collect PartyUpdated events published during test.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **PartyService wired to real EventBus.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Two players: A creates party, adds B; B leaves; A disbands. Verify in-memory…** (1 connections) — `server/tests/integration/test_party_flow.py`
- **PartyService with no dependencies (in-memory only).** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [_str_id](_str_id.md) (15 shared connections)
- [Any](Any.md) (8 shared connections)
- [EventBus](EventBus.md) (8 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [Party](Party.md) (3 shared connections)
- [test_party_service.py](test_party_service.py.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 84 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*