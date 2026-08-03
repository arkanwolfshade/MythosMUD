# npc combat services

> 15 nodes

## Key Concepts

- **npc_combat_grace.py** (13 connections) — `server/services/npc_combat_grace.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (3 connections)
- **._complete_player_attack_on_npc_after_grace()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **Return the runtime app instance attached during lifespan startup.      This prov** (1 connections) — `server/config/__init__.py`
- **Login grace-period checks for NPC combat integration (extracted to keep service** (1 connections) — `server/services/npc_combat_grace.py`
- **Resolve connection_manager from the public config app accessor.      Uses geta** (1 connections) — `server/services/npc_combat_grace.py`
- **True if the player should not attack (in login grace period). Fail-open on confi** (1 connections) — `server/services/npc_combat_grace.py`
- **True if NPC attack on this player should be blocked (player in login grace perio** (1 connections) — `server/services/npc_combat_grace.py`
- **Player attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle a player attacking an NPC using auto-progression combat system.** (1 connections) — `server/services/npc_combat_integration_service.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [grace period login](grace_period_login.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [config models rationale](config_models_rationale.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/services/npc_combat_grace.py`
- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 55 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*