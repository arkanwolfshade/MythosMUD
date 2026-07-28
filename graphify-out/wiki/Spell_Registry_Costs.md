# Spell Registry Costs

> 18 nodes · cohesion 0.20

## Key Concepts

- **SpellLearningService** (30 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell()** (8 connections) — `server/game/magic/spell_learning_service.py`
- **UUID** (7 connections)
- **._validate_prerequisites()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (5 connections)
- **.__init__()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_book()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_npc()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_quest()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.increase_mastery_on_cast()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **Validate prerequisites for learning a spell.          Args:             player_i** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell from a spellbook item.          Args:             player_id: Playe** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Service for handling spell learning from various sources.      Manages spell acq** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell from an NPC teacher.          Args:             player_id: Player** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell as a quest reward.          Args:             player_id: Player ID** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Increase mastery level after casting a spell.          Args:             player_** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Initialize the spell learning service.          Args:             spell_registry** (1 connections) — `server/game/magic/spell_learning_service.py`
- **Learn a spell for a player.          Args:             player_id: Player ID** (1 connections) — `server/game/magic/spell_learning_service.py`

## Relationships

- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (8 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (3 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (3 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (3 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (2 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (1 shared connections)
- [Magic Game Service](Magic_Game_Service.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_learning_service.py`

## Audit Trail

- EXTRACTED: 75 (86%)
- INFERRED: 12 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*