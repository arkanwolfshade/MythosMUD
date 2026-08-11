# Command Alias Model

> 54 nodes

## Key Concepts

- **test_party_service.py** (35 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_create_party_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_create_party_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_creates_pending()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_accept_party_invite_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_target_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_remove_member_leader_leaves_disbands()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_member_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_member_non_leader_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_self_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_id_without_caller()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_for_player_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_empty_when_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_includes_self()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_leader_false_when_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_leader_false_when_member()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_member_removed()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_leader_disbands_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_in_same_party_true_when_both_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- *... and 29 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (1 shared connections)
- [test_catatonia_registry.py](test_catatonia_registry.py.md) (1 shared connections)
- [Infrastructure Minimap Exploration](Infrastructure_Minimap_Exploration.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*