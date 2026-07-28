# Server Game (3)

> 132 nodes

## Key Concepts

- **test_party_service.py** (35 connections) — `server/tests/unit/game/test_party_service.py`
- **PartyService** (32 connections) — `server/game/party_service.py`
- **UUID** (17 connections)
- **party_service.py** (16 connections) — `server/game/party_service.py`
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **Party** (12 connections) — `server/game/party_service.py`
- **test_party_flow.py** (12 connections) — `server/tests/integration/test_party_flow.py`
- **PartyUpdated** (12 connections) — `server/events/event_types.py`
- **Any** (10 connections)
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
- **.disband_party()** (8 connections) — `server/game/party_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/party_service.py`
- **.accept_party_invite()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **.kick_member()** (8 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **._expire_pending_invites()** (7 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (7 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **.decline_party_invite()** (7 connections) — `server/game/party_service.py`
- **.__init__()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- *... and 107 more nodes in this community*

## Relationships

- [Server Events](Server_Events.md) (13 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Realtime (48)](Server_Realtime_%2848%29.md) (2 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (2 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (1 shared connections)
- [Server Events (4)](Server_Events_%284%29.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 444 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*