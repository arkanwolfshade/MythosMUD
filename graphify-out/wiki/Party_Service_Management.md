# Party Service Management

> 73 nodes · cohesion 0.06

## Key Concepts

- **PartyService** (39 connections) — `server/game/party_service.py`
- **UUID** (20 connections) — `server/game/party_service.py`
- **PartyUpdated** (16 connections) — `server/events/event_types.py`
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **Any** (13 connections) — `server/game/party_service.py`
- **Party** (12 connections) — `server/game/party_service.py`
- **party_service.py** (11 connections) — `server/game/party_service.py`
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
- **test_party_flow.py** (9 connections) — `server/tests/integration/test_party_flow.py`
- **.accept_party_invite()** (8 connections) — `server/game/party_service.py`
- **.disband_party()** (8 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.kick_member()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.decline_party_invite()** (7 connections) — `server/game/party_service.py`
- **._expire_pending_invites()** (7 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (7 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **.__init__()** (6 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **PartyService** (6 connections) — `server/tests/integration/test_party_flow.py`
- *... and 48 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (13 shared connections)
- [[Room Occupant Events]] (7 shared connections)
- [[Game Service Bundle]] (7 shared connections)
- [[Game Party Service]] (5 shared connections)
- [[Combat Player Broadcasts]] (4 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[NPC Combat Events]] (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`

## Audit Trail

- EXTRACTED: 311 (88%)
- INFERRED: 44 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
