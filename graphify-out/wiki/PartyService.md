# PartyService

> 79 nodes

## Key Concepts

- **PartyService** (42 connections) — `server/game/party_service.py`
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **party_service.py** (16 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **test_party_flow.py** (13 connections) — `server/tests/integration/test_party_flow.py`
- **PartyUpdated** (11 connections) — `server/events/event_types.py`
- **Any** (11 connections)
- **Party** (9 connections) — `server/game/party_service.py`
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
- *... and 54 more nodes in this community*

## Relationships

- [test_party_service.py](test_party_service.py.md) (9 shared connections)
- [EventBus](EventBus.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [send_game_event](send_game_event.md) (2 shared connections)
- [._bind_event_type](_bind_event_type.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`

## Audit Trail

- EXTRACTED: 183 (93%)
- INFERRED: 13 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*