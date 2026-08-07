# message handler factory

> 18 nodes

## Key Concepts

- **party_service.py** (16 connections) — `server/game/party_service.py`
- **PartyUpdated** (12 connections) — `server/events/event_types.py`
- **Party** (12 connections) — `server/game/party_service.py`
- **test_party_invite_join_leave_disband_state_and_events()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_leader_leaves_disbands()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **.get_party()** (3 connections) — `server/game/party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **.__post_init__()** (2 connections) — `server/game/party_service.py`
- **Event fired when party membership or leadership changes.      Emitted by PartySe** (1 connections) — `server/events/event_types.py`
- **Party service for MythosMUD.  In-memory ephemeral party state: parties exist onl** (1 connections) — `server/game/party_service.py`
- **In-memory party model.      Ephemeral: not persisted. party_id and member_ids ar** (1 connections) — `server/game/party_service.py`
- **Ensure leader is in member set.** (1 connections) — `server/game/party_service.py`
- **Return the party by id, or None.** (1 connections) — `server/game/party_service.py`
- **Two players: A creates party, adds B; B leaves; A disbands.     Verify in-memory** (1 connections) — `server/tests/integration/test_party_flow.py`
- **When leader leaves, party is disbanded and disbanded event is emitted.** (1 connections) — `server/tests/integration/test_party_flow.py`
- **Party __post_init__ ensures leader is in member_ids.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Party __post_init__ keeps existing members and adds leader.** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [party game service](party_game_service.md) (10 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (8 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [command service commands](command_service_commands.md) (1 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 63 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*