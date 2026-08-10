# Playwright E2E Specs

> 11 nodes

## Key Concepts

- **npc_combat_grace.py** (13 connections) — `server/services/npc_combat_grace.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **UUID** (3 connections)
- **Return the runtime app instance attached during lifespan startup.      This prov** (1 connections) — `server/config/__init__.py`
- **Login grace-period checks for NPC combat integration (extracted to keep service** (1 connections) — `server/services/npc_combat_grace.py`
- **Resolve connection_manager from the public config app accessor.      Uses geta** (1 connections) — `server/services/npc_combat_grace.py`
- **True if the player should not attack (in login grace period). Fail-open on confi** (1 connections) — `server/services/npc_combat_grace.py`
- **True if NPC attack on this player should be blocked (player in login grace perio** (1 connections) — `server/services/npc_combat_grace.py`

## Relationships

- [Player Respawn Events](Player_Respawn_Events.md) (4 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (4 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/services/npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 46 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*