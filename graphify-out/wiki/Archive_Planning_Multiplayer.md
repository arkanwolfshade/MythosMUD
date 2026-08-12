# Archive Planning Multiplayer

> 10 nodes

## Key Concepts

- **Party** (12 connections) — `server/game/party_service.py`
- **.get_party()** (3 connections) — `server/game/party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **.__post_init__()** (2 connections) — `server/game/party_service.py`
- **In-memory party model.      Ephemeral: not persisted. party_id and member_ids ar** (1 connections) — `server/game/party_service.py`
- **Ensure leader is in member set.** (1 connections) — `server/game/party_service.py`
- **Return the party by id, or None.** (1 connections) — `server/game/party_service.py`
- **Party __post_init__ ensures leader is in member_ids.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Party __post_init__ keeps existing members and adds leader.** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [Status Effect Model](Status_Effect_Model.md) (3 shared connections)
- [Command Alias Model](Command_Alias_Model.md) (3 shared connections)
- [Player State Command Factory](Player_State_Command_Factory.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 25 (89%)
- INFERRED: 3 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*