# Command Alias Model

> 130 nodes

## Key Concepts

- **PartyService** (35 connections) — `server/game/party_service.py`
- **test_party_service.py** (35 connections) — `server/tests/unit/game/test_party_service.py`
- **UUID** (17 connections)
- **party_service.py** (16 connections) — `server/game/party_service.py`
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **PartyUpdated** (12 connections) — `server/events/event_types.py`
- **Party** (12 connections) — `server/game/party_service.py`
- **test_party_flow.py** (12 connections) — `server/tests/integration/test_party_flow.py`
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
- *... and 105 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (8 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (5 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (2 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (2 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Lucidity Database Models](Lucidity_Database_Models.md) (1 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (1 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 442 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*