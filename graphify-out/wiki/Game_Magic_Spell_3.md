# Game Magic Spell

> 20 nodes · cohesion 0.14

## Key Concepts

- **spell_learning_service.py** (13 connections) — `server/game/magic/spell_learning_service.py`
- **UUID** (11 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (9 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell()** (8 connections) — `server/game/magic/spell_learning_service.py`
- **._validate_prerequisites()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_book()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_npc()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_quest()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **Spell** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.increase_mastery_on_cast()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **Spell learning service for handling spell acquisition.  This module provides ser** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Validate prerequisites for learning a spell.          Args:             player_i** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell from a spellbook item.          Args:             player_id: Playe** (1 connections) — `server/game/magic/spell_learning_service.py`
- **# TODO: Integrate with item system to get spellbook data  # pylint: disable=fixm** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell from an NPC teacher.          Args:             player_id: Player** (1 connections) — `server/game/magic/spell_learning_service.py`
- **# TODO: Integrate with NPC system to validate teacher status  # pylint: disable=** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell as a quest reward.          Args:             player_id: Player ID** (1 connections) — `server/game/magic/spell_learning_service.py`
- **# TODO: Integrate with quest system to validate quest completion  # pylint: disa** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Increase mastery level after casting a spell.          Args:             player_** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell for a player.          Args:             player_id: Player ID** (1 connections) — `server/game/magic/spell_learning_service.py`

## Relationships

- [[Magic Service Bundle]] (15 shared connections)
- [[Combat Command Handler]] (4 shared connections)
- [[Spell Registry Costs]] (4 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Magic Lifespan Initialization]] (1 shared connections)

## Source Files

- `server/game/magic/spell_learning_service.py`

## Audit Trail

- EXTRACTED: 68 (85%)
- INFERRED: 12 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
