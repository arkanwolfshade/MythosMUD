# casting game magic

> 22 nodes

## Key Concepts

- **npc_combat_grace.py** (14 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (11 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **test_npc_combat_grace.py** (9 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (3 connections)
- **._complete_player_attack_on_npc_after_grace()** (3 connections) — `server/services/npc_combat_integration_service.py`
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
- **Player attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle a player attacking an NPC using auto-progression combat system.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Unit tests for npc_combat_grace login grace checks.** (1 connections) — `server/tests/unit/services/test_npc_combat_grace.py`

## Relationships

- [player event realtime](player_event_realtime.md) (6 shared connections)
- [command utility models](command_utility_models.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [tools generate invite](tools_generate_invite.md) (1 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [tick game processing](tick_game_processing.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/services/npc_combat_grace.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 83 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*