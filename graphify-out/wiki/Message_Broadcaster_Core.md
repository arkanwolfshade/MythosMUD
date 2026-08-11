# Message Broadcaster Core

> 20 nodes

## Key Concepts

- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_attack_handler.py`
- **UUID** (3 connections)
- **._validate_target_can_be_attacked()** (3 connections) — `server/services/combat_attack_handler.py`
- **attack_handler()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **Any** (1 connections)
- **Handles combat attack processing and damage application.** (1 connections) — `server/services/combat_attack_handler.py`
- **Initialize the attack handler.          Args:             combat_service: Refere** (1 connections) — `server/services/combat_attack_handler.py`
- **Validate that attack is allowed.** (1 connections) — `server/services/combat_attack_handler.py`
- **Apply damage to target and check death states.          Delegates domain logic t** (1 connections) — `server/services/combat_attack_handler.py`
- **Check if room has no_death attribute (tutorial/safe zones).** (1 connections) — `server/services/combat_attack_handler.py`
- **Apply damage to target and update combat state.          Args:             comba** (1 connections) — `server/services/combat_attack_handler.py`
- **Validate attack and retrieve combat participants.          Args:             att** (1 connections) — `server/services/combat_attack_handler.py`
- **Create CombatAttackHandler instance.** (1 connections) — `server/tests/unit/services/test_combat_attack_handler.py`

## Relationships

- [Combat Death Handling](Combat_Death_Handling.md) (5 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (5 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (4 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (2 shared connections)
- [Health Check Models](Health_Check_Models.md) (1 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (1 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (1 shared connections)
- [Command Parser](Command_Parser.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`
- `server/tests/unit/services/test_combat_attack_handler.py`

## Audit Trail

- EXTRACTED: 73 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*