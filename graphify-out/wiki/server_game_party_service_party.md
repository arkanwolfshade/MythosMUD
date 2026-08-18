# server game party service party

> 10 nodes

## Key Concepts

- **Party** (9 connections) — `server/game/party_service.py`
- **.get_party()** (3 connections) — `server/game/party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **.__post_init__()** (2 connections) — `server/game/party_service.py`
- **In-memory party model. Ephemeral: not persisted. party_id and member_ids are…** (1 connections) — `server/game/party_service.py`
- **Return the party by id, or None.** (1 connections) — `server/game/party_service.py`
- **Ensure leader is in member set.** (1 connections) — `server/game/party_service.py`
- **Party __post_init__ ensures leader is in member_ids.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Party __post_init__ keeps existing members and adds leader.** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [server game party service partyservice](server_game_party_service_partyservice.md) (3 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*