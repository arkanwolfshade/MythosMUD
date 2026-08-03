# room persistence loader

> 28 nodes

## Key Concepts

- **GameMechanicsService** (27 connections) — `server/game/mechanics.py`
- **test_mechanics.py** (16 connections) — `server/tests/unit/game/test_mechanics.py`
- **_player()** (8 connections) — `server/tests/unit/game/test_mechanics.py`
- **.apply_fear()** (4 connections) — `server/game/mechanics.py`
- **.apply_corruption()** (4 connections) — `server/game/mechanics.py`
- **.heal_player()** (4 connections) — `server/game/mechanics.py`
- **.damage_player()** (4 connections) — `server/game/mechanics.py`
- **.gain_experience()** (4 connections) — `server/game/mechanics.py`
- **.__init__()** (3 connections) — `server/game/mechanics.py`
- **test_apply_lucidity_loss_success()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_lucidity_loss_player_not_found()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_fear_success()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_corruption_success()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_gain_occult_knowledge_success()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_heal_player_success()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_damage_player_success()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_gain_experience_success()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **service()** (2 connections) — `server/tests/unit/game/test_mechanics.py`
- **Any** (1 connections)
- **Service class for game mechanics operations.** (1 connections) — `server/game/mechanics.py`
- **Initialize the game mechanics service with a persistence layer.** (1 connections) — `server/game/mechanics.py`
- **Apply fear to a player.** (1 connections) — `server/game/mechanics.py`
- **Apply corruption to a player.** (1 connections) — `server/game/mechanics.py`
- **Heal a player's health.** (1 connections) — `server/game/mechanics.py`
- **Damage a player's health.** (1 connections) — `server/game/mechanics.py`
- *... and 3 more nodes in this community*

## Relationships

- [command inventory models](command_inventory_models.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [Database Config](Database_Config.md) (5 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (3 shared connections)
- [npc combat base](npc_combat_base.md) (2 shared connections)
- [Spell Validation](Spell_Validation.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/tests/unit/game/test_mechanics.py`

## Audit Trail

- EXTRACTED: 103 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*