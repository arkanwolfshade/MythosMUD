# Realtime Conftest Mocks

> 12 nodes

## Key Concepts

- **party_service.py** (16 connections) — `server/game/party_service.py`
- **Party** (12 connections) — `server/game/party_service.py`
- **.get_party()** (3 connections) — `server/game/party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **.__post_init__()** (2 connections) — `server/game/party_service.py`
- **Party service for MythosMUD.  In-memory ephemeral party state: parties exist onl** (1 connections) — `server/game/party_service.py`
- **In-memory party model.      Ephemeral: not persisted. party_id and member_ids ar** (1 connections) — `server/game/party_service.py`
- **Ensure leader is in member set.** (1 connections) — `server/game/party_service.py`
- **Return the party by id, or None.** (1 connections) — `server/game/party_service.py`
- **Party __post_init__ ensures leader is in member_ids.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Party __post_init__ keeps existing members and adds leader.** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (6 shared connections)
- [Command Alias Model](Command_Alias_Model.md) (4 shared connections)
- [Combat DP Persistence Tests](Combat_DP_Persistence_Tests.md) (3 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 42 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*