# room realtime rationale

> 24 nodes

## Key Concepts

- **npc_combat_grace.py** (13 connections) — `server/services/npc_combat_grace.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **.handle_npc_attack_on_player()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (3 connections)
- **._complete_player_attack_on_npc_after_grace()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_original_string_id()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (3 connections)
- **Return the runtime app instance attached during lifespan startup.      This prov** (1 connections) — `server/config/__init__.py`
- **Login grace-period checks for NPC combat integration (extracted to keep service** (1 connections) — `server/services/npc_combat_grace.py`
- **Resolve connection_manager from the public config app accessor.      Uses geta** (1 connections) — `server/services/npc_combat_grace.py`
- **True if the player should not attack (in login grace period). Fail-open on confi** (1 connections) — `server/services/npc_combat_grace.py`
- **True if NPC attack on this player should be blocked (player in login grace perio** (1 connections) — `server/services/npc_combat_grace.py`
- **Player attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **NPC attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle a player attacking an NPC using auto-progression combat system.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Aggressive-mob entrypoint; matches NPCCombatIntegration.handle_npc_attack for in** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle an NPC attacking a player (aggro) using the same combat codepath as playe** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Get the original string ID from a UUID.** (1 connections) — `server/services/npc_combat_integration_service.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [command utility models](command_utility_models.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)
- [command models admin](command_models_admin.md) (1 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/services/npc_combat_grace.py`
- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 77 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*