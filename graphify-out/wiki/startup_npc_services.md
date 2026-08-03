# startup npc services

> 14 nodes

## Key Concepts

- **.learn_spell()** (8 connections) — `server/game/magic/spell_learning_service.py`
- **UUID** (7 connections)
- **._validate_prerequisites()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (5 connections)
- **.learn_spell_from_book()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_npc()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_quest()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.increase_mastery_on_cast()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell for a player.          Args:             player_id: Player ID** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Validate prerequisites for learning a spell.          Args:             player_i** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell from a spellbook item.          Args:             player_id: Playe** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell from an NPC teacher.          Args:             player_id: Player** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell as a quest reward.          Args:             player_id: Player ID** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Increase mastery level after casting a spell.          Args:             player_** (1 connections) — `server/game/magic/spell_learning_service.py`

## Relationships

- [game models player](game_models_player.md) (8 shared connections)

## Source Files

- `server/game/magic/spell_learning_service.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*