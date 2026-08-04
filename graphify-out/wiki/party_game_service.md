# party game service

> 48 nodes

## Key Concepts

- **PartyService** (36 connections) — `server/game/party_service.py`
- **UUID** (17 connections)
- **_str_id()** (16 connections) — `server/game/party_service.py`
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
- **._send_party_invite_to_target()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **.get_party()** (3 connections) — `server/game/party_service.py`
- *... and 23 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (14 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (1 shared connections)
- [room realtime subscription](room_realtime_subscription.md) (1 shared connections)
- [skill game service](skill_game_service.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 237 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*