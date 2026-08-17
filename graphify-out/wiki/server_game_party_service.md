# server game party service

> 55 nodes

## Key Concepts

- **PartyService** (36 connections) — `server/game/party_service.py`
- **party_service.py** (17 connections) — `server/game/party_service.py`
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **Any** (10 connections)
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
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- *... and 30 more nodes in this community*

## Relationships

- [server events event types partyupdated](server_events_event_types_partyupdated.md) (8 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (3 shared connections)
- [playercombatservice](playercombatservice.md) (2 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (2 shared connections)
- [followtargetvalue](followtargetvalue.md) (2 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (1 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 140 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*