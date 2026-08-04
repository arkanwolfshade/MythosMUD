# room persistence loader

> 32 nodes

## Key Concepts

- **GameMechanicsService** (27 connections) — `server/game/mechanics.py`
- **test_mechanics.py** (16 connections) — `server/tests/unit/game/test_mechanics.py`
- **mechanics.py** (13 connections) — `server/game/mechanics.py`
- **npc_combat_rewards.py** (10 connections) — `server/services/npc_combat_rewards.py`
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
- **Game mechanics service for MythosMUD server.  This module handles all game mecha** (1 connections) — `server/game/mechanics.py`
- **Service class for game mechanics operations.** (1 connections) — `server/game/mechanics.py`
- **Initialize the game mechanics service with a persistence layer.** (1 connections) — `server/game/mechanics.py`
- **Apply fear to a player.** (1 connections) — `server/game/mechanics.py`
- *... and 7 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (10 shared connections)
- [Loot Generation](Loot_Generation.md) (9 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [npc rewards combat](npc_rewards_combat.md) (1 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/game/test_mechanics.py`

## Audit Trail

- EXTRACTED: 128 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*