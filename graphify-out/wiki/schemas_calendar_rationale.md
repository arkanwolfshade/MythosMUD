# schemas calendar rationale

> 18 nodes

## Key Concepts

- **npc_combat_grace.py** (14 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (11 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **test_npc_combat_grace.py** (9 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **UUID** (3 connections)
- **test_player_attack_blocked_when_in_grace_period()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **test_player_attack_fail_open_without_connection_manager()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **test_player_attack_fail_open_on_invalid_uuid()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **test_npc_attack_blocked_when_target_in_grace_period()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **test_npc_attack_fail_open_without_app()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **Return the runtime app instance attached during lifespan startup.      This prov** (1 connections) — `server/config/__init__.py`
- **Login grace-period checks for NPC combat integration (extracted to keep service** (1 connections) — `server/services/npc_combat_grace.py`
- **Resolve connection_manager from the public config app accessor.      Uses geta** (1 connections) — `server/services/npc_combat_grace.py`
- **True if the player should not attack (in login grace period). Fail-open on confi** (1 connections) — `server/services/npc_combat_grace.py`
- **True if NPC attack on this player should be blocked (player in login grace perio** (1 connections) — `server/services/npc_combat_grace.py`
- **Unit tests for npc_combat_grace login grace checks.** (1 connections) — `server/tests/unit/services/test_npc_combat_grace.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (7 shared connections)
- [command utility models](command_utility_models.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/services/npc_combat_grace.py`
- `server/tests/unit/services/test_npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 74 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*