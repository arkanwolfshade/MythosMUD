# PartyService

> 44 nodes

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
- **._notify_player_removed_from_party()** (6 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **._send_party_invite_to_target()** (4 connections) — `server/game/party_service.py`
- **Create a new party with the given player as leader. Returns dict with success…** (1 connections) — `server/game/party_service.py`
- **Disband a party. If by_player_id is given, only the leader may disband. If…** (1 connections) — `server/game/party_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [party_service.py](party_service.py.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [Party](Party.md) (3 shared connections)
- [.__init__](__init__.md) (2 shared connections)
- [party_service](party_service.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_party_service.py](test_party_service.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 121 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*