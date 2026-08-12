# SpellLearningService

> 24 nodes

## Key Concepts

- **SpellLearningService** (37 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell()** (12 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (12 connections)
- **UUID** (10 connections)
- **._validate_prerequisites()** (9 connections) — `server/game/magic/spell_learning_service.py`
- **._load_spell_learn_context()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **._check_required_spell_prerequisites()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_book()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_npc()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_quest()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **._persist_spell_learning()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **._apply_mythos_corruption_on_learn()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._check_intelligence_requirement()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._check_power_requirement()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._spell_learn_success_response()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **.increase_mastery_on_cast()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **._resolve_spell()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell for a player.** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Validate prerequisites for learning a spell. Args: player_id: Player ID spell:…** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Service for handling spell learning from various sources. Manages spell…** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell from a spellbook item. Args: player_id: Player ID…** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell from an NPC teacher. Args: player_id: Player ID npc_id: ID of the…** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell as a quest reward. Args: player_id: Player ID quest_id: ID of the…** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Increase mastery level after casting a spell. Args: player_id: Player ID…** (1 connections) — `server/game/magic/spell_learning_service.py`

## Relationships

- [magic_service.py](magic_service.py.md) (15 shared connections)
- [Spell](Spell.md) (10 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (1 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_learning_service.py`

## Audit Trail

- EXTRACTED: 129 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*