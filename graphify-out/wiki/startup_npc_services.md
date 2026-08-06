# startup npc services

> 18 nodes

## Key Concepts

- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_is_player_in_combat_sync_true()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_cleanup_stale_combat_states()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_player_combat_state_post_init()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_player_combat_state_post_init_with_activity()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_player_xp_award_event_init()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **mock_npc_service()** (2 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Unit tests for player combat service.  Tests the PlayerCombatService class for m** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create mock persistence layer.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create mock event bus.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create mock NPC combat integration service (no _rewards so XP uses fallback path** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test is_player_in_combat_sync returns True when in combat.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test cleanup_stale_combat_states cleans up stale states.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test PlayerCombatState.__post_init__ sets last_activity.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test PlayerCombatState.__post_init__ preserves provided last_activity.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Test PlayerXPAwardEvent initialization.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`

## Relationships

- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (27 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [profession models rationale](profession_models_rationale.md) (2 shared connections)

## Source Files

- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*