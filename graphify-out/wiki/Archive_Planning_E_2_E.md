# Archive Planning E 2 E

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

- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (5 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (4 shared connections)
- [Command Parser](Command_Parser.md) (2 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (1 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/services/npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 46 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*