# Community 443

> 40 nodes

## Key Concepts

- **test_bank_service.py** (23 connections) — `server/tests/unit/services/test_bank_service.py`
- **get_or_create_bank_box()** (18 connections) — `server/services/bank_service.py`
- **FakeBankPersistence** (14 connections) — `server/tests/unit/services/test_bank_service.py`
- **forward_to_bank_box()** (13 connections) — `server/services/bank_service.py`
- **is_bank_room()** (8 connections) — `server/services/bank_service.py`
- **asyncio** (7 connections)
- **test_a_create_failure_with_no_box_to_fall_back_on_is_raised()** (6 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_forward_over_fills_a_full_box_rather_than_evicting()** (6 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_forward_creates_the_box_when_the_player_has_none()** (5 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_losing_a_create_race_uses_the_winners_box()** (5 connections) — `server/tests/unit/services/test_bank_service.py`
- **UUID** (5 connections)
- **.create_container()** (4 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_each_player_gets_their_own_box()** (4 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_first_use_creates_a_bank_box_owned_by_the_player()** (4 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_is_bank_room_only_for_a_literal_true_flag()** (4 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_second_use_returns_the_same_box_instead_of_creating_another()** (4 connections) — `server/tests/unit/services/test_bank_service.py`
- **.create_container()** (3 connections) — `server/services/bank_service.py`
- **.get_bank_container()** (3 connections) — `server/services/bank_service.py`
- **.update_container()** (3 connections) — `server/services/bank_service.py`
- **_box()** (3 connections) — `server/tests/unit/services/test_bank_service.py`
- **_stack()** (3 connections) — `server/tests/unit/services/test_bank_service.py`
- **UUID** (3 connections)
- **.get_bank_container()** (2 connections) — `server/tests/unit/services/test_bank_service.py`
- **.update_container()** (2 connections) — `server/tests/unit/services/test_bank_service.py`
- **test_is_bank_room_is_false_for_no_room()** (2 connections) — `server/tests/unit/services/test_bank_service.py`
- *... and 15 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (19 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (5 shared connections)
- [Community 1173](Community_1173.md) (5 shared connections)
- [Community 414](Community_414.md) (2 shared connections)
- [Community 155](Community_155.md) (1 shared connections)

## Source Files

- `server/services/bank_service.py`
- `server/tests/unit/services/test_bank_service.py`

## Audit Trail

- EXTRACTED: 98 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*