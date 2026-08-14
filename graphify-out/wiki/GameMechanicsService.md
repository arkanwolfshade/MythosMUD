# GameMechanicsService

> 32 nodes

## Key Concepts

- **GameMechanicsService** (27 connections) — `server/game/mechanics.py`
- **test_mechanics.py** (16 connections) — `server/tests/unit/game/test_mechanics.py`
- **_player()** (8 connections) — `server/tests/unit/game/test_mechanics.py`
- **asyncio** (8 connections)
- **test_apply_corruption_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_fear_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_lucidity_loss_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_damage_player_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_gain_experience_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_gain_occult_knowledge_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_heal_player_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **.apply_corruption()** (3 connections) — `server/game/mechanics.py`
- **.apply_fear()** (3 connections) — `server/game/mechanics.py`
- **.apply_lucidity_loss()** (3 connections) — `server/game/mechanics.py`
- **.damage_player()** (3 connections) — `server/game/mechanics.py`
- **.gain_experience()** (3 connections) — `server/game/mechanics.py`
- **.heal_player()** (3 connections) — `server/game/mechanics.py`
- **.__init__()** (3 connections) — `server/game/mechanics.py`
- **service()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_lucidity_loss_player_not_found()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **persistence()** (2 connections) — `server/tests/unit/game/test_mechanics.py`
- **fixture** (2 connections)
- **Any** (1 connections)
- **Heal a player's health.** (1 connections) — `server/game/mechanics.py`
- **Damage a player's health.** (1 connections) — `server/game/mechanics.py`
- *... and 7 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (1 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [NPCCombatRewards](NPCCombatRewards.md) (1 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/tests/unit/game/test_mechanics.py`

## Audit Trail

- EXTRACTED: 72 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*