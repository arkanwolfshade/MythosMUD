# Status Effect Model

> 18 nodes

## Key Concepts

- **PartyService** (35 connections) — `server/game/party_service.py`
- **party_service.py** (16 connections) — `server/game/party_service.py`
- **PartyUpdated** (12 connections) — `server/events/event_types.py`
- **test_party_flow.py** (12 connections) — `server/tests/integration/test_party_flow.py`
- **party_events()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **party_service()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_invite_join_leave_disband_state_and_events()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_leader_leaves_disbands()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **party_service()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **Event fired when party membership or leadership changes.      Emitted by PartySe** (1 connections) — `server/events/event_types.py`
- **Party service for MythosMUD.  In-memory ephemeral party state: parties exist onl** (1 connections) — `server/game/party_service.py`
- **In-memory party management: create, disband, add/remove/kick members, leader che** (1 connections) — `server/game/party_service.py`
- **Integration tests for party (ephemeral grouping) feature.  Flow: Two players; le** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Collect PartyUpdated events published during test.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **PartyService wired to real EventBus.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Two players: A creates party, adds B; B leaves; A disbands.     Verify in-memory** (1 connections) — `server/tests/integration/test_party_flow.py`
- **When leader leaves, party is disbanded and disbanded event is emitted.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **PartyService with no dependencies (in-memory only).** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [Player State Command Factory](Player_State_Command_Factory.md) (14 shared connections)
- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (9 shared connections)
- [Archive Planning Multiplayer](Archive_Planning_Multiplayer.md) (3 shared connections)
- [Command Alias Model](Command_Alias_Model.md) (3 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (3 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (2 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (2 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)
- [Lucidity Database Models](Lucidity_Database_Models.md) (1 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 97 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*