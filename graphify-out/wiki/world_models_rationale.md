# world models rationale

> 280 nodes

## Key Concepts

- **player.py** (85 connections) — `server/models/player.py`
- **__init__.py** (73 connections) — `server/models/__init__.py`
- **Base** (60 connections) — `server/models/base.py`
- **PlayerChannelPreferences** (30 connections) — `server/models/player.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **test_world.py** (27 connections) — `server/tests/unit/models/test_world.py`
- **PlayerInventory** (25 connections) — `server/models/player.py`
- **LucidityAdjustmentLog** (23 connections) — `server/models/lucidity.py`
- **PlayerSpell** (23 connections) — `server/models/player_spells.py`
- **base.py** (22 connections) — `server/models/base.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **test_item.py** (19 connections) — `server/tests/unit/models/test_item.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
- **__init__.py** (18 connections) — `server/tests/fixtures/integration/__init__.py`
- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
- **PlayerSkill** (17 connections) — `server/models/player_skill.py`
- **ItemPrototype** (14 connections) — `server/models/item.py`
- **test_calendar.py** (13 connections) — `server/tests/unit/models/test_calendar.py`
- **test_emote.py** (13 connections) — `server/tests/unit/models/test_emote.py`
- **skill.py** (12 connections) — `server/models/skill.py`
- **ItemInstance** (11 connections) — `server/models/item.py`
- **player_spells.py** (11 connections) — `server/models/player_spells.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_metadata.py** (11 connections) — `server/tests/unit/test_metadata.py`
- *... and 255 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (34 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (23 shared connections)
- [auth users rationale](auth_users_rationale.md) (15 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (12 shared connections)
- [player preferences services](player_preferences_services.md) (11 shared connections)
- [fixtures return shape](fixtures_return_shape.md) (11 shared connections)
- [Database Config](Database_Config.md) (10 shared connections)
- [NATS Messaging](NATS_Messaging.md) (10 shared connections)
- [player model models](player_model_models.md) (10 shared connections)
- [npc populate databases](npc_populate_databases.md) (9 shared connections)
- [player room persistence](player_room_persistence.md) (9 shared connections)
- [effect player repository](effect_player_repository.md) (9 shared connections)

## Source Files

- `server/metadata.py`
- `server/models/__init__.py`
- `server/models/base.py`
- `server/models/calendar.py`
- `server/models/dialogue.py`
- `server/models/emote.py`
- `server/models/game.py`
- `server/models/item.py`
- `server/models/lucidity.py`
- `server/models/player.py`
- `server/models/player_effect.py`
- `server/models/player_skill.py`
- `server/models/player_spells.py`
- `server/models/profession.py`
- `server/models/skill.py`
- `server/models/skill_use_log.py`
- `server/models/spell_db.py`
- `server/models/world.py`
- `server/npc_metadata.py`
- `server/persistence/repositories/player_repository_mappers.py`

## Audit Trail

- EXTRACTED: 1069 (89%)
- INFERRED: 138 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*