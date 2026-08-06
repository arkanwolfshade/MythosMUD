# npc combat player

> 35 nodes

## Key Concepts

- **SpellLearningService** (43 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_learning_service.py** (15 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.learn_spell()** (8 connections) — `server/game/magic/spell_learning_service.py`
- **UUID** (7 connections)
- **._validate_prerequisites()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (5 connections)
- **.learn_spell_from_book()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_npc()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_quest()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.increase_mastery_on_cast()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **.__init__()** (2 connections) — `server/commands/magic_commands.py`
- **learning_service()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_not_found()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_player_missing()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_already_known()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_success()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_validate_prerequisites_power_too_low()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_increase_mastery_on_cast()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_validate_prerequisites_intelligence_too_low()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_validate_prerequisites_missing_required_spells()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_from_npc()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_from_book_no_spell_id()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_from_book_with_spell()** (2 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [persistence core infrastructure](persistence_core_infrastructure.md) (7 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (6 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (5 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [player respawn event](player_respawn_event.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [room occupant manager](room_occupant_manager.md) (2 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (2 shared connections)
- [chat service game](chat_service_game.md) (1 shared connections)
- [subject nats manager](subject_nats_manager.md) (1 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/game/magic/spell_learning_service.py`
- `server/tests/unit/game/magic/test_spell_learning_service.py`

## Audit Trail

- EXTRACTED: 139 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*