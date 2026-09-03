# Party Service

> 47 nodes

## Key Concepts

- **PartyService** (36 connections) — `server/game/party_service.py`
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **Any** (10 connections)
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
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
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **.__init__()** (6 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (6 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **._send_party_invite_to_target()** (4 connections) — `server/game/party_service.py`
- **ConnectionManager** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [Test Party Flow](Test_Party_Flow.md) (9 shared connections)
- [Test Party Service](Test_Party_Service.md) (6 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (2 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (1 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Test Envelope](Test_Envelope.md) (1 shared connections)
- [Connection Manager Api](Connection_Manager_Api.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 121 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*