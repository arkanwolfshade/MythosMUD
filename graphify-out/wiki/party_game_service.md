# party game service

> 48 nodes

## Key Concepts

- **PartyService** (36 connections) — `server/game/party_service.py`
- **UUID** (17 connections)
- **party_service.py** (16 connections) — `server/game/party_service.py`
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
- *... and 23 more nodes in this community*

## Relationships

- [skill game service](skill_game_service.md) (8 shared connections)
- [combat services messaging](combat_services_messaging.md) (5 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [commands admin shutdown](commands_admin_shutdown.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (3 shared connections)
- [holiday service services](holiday_service_services.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 250 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*