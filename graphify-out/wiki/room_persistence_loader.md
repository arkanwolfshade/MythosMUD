# room persistence loader

> 34 nodes

## Key Concepts

- **GameMechanicsService** (27 connections) — `server/game/mechanics.py`
- **test_mechanics.py** (16 connections) — `server/tests/unit/game/test_mechanics.py`
- **_player()** (8 connections) — `server/tests/unit/game/test_mechanics.py`
- **.gain_occult_knowledge()** (6 connections) — `server/game/mechanics.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/mechanics.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
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
- **Apply lucidity loss to a player.** (1 connections) — `server/game/mechanics.py`
- *... and 9 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (2 shared connections)
- [npc combat base](npc_combat_base.md) (2 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/npc/combat_integration_base.py`
- `server/tests/unit/game/test_mechanics.py`

## Audit Trail

- EXTRACTED: 120 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*