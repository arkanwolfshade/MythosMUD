# world models rationale

> 276 nodes

## Key Concepts

- **player.py** (85 connections) — `server/models/player.py`
- **__init__.py** (73 connections) — `server/models/__init__.py`
- **Base** (60 connections) — `server/models/base.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_world.py** (27 connections) — `server/tests/unit/models/test_world.py`
- **PlayerInventory** (25 connections) — `server/models/player.py`
- **LucidityAdjustmentLog** (23 connections) — `server/models/lucidity.py`
- **LucidityExposureState** (23 connections) — `server/models/lucidity.py`
- **PlayerSpell** (23 connections) — `server/models/player_spells.py`
- **base.py** (22 connections) — `server/models/base.py`
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **test_item.py** (19 connections) — `server/tests/unit/models/test_item.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
- **PlayerSkill** (17 connections) — `server/models/player_skill.py`
- **ItemPrototype** (14 connections) — `server/models/item.py`
- **test_calendar.py** (13 connections) — `server/tests/unit/models/test_calendar.py`
- **skill.py** (12 connections) — `server/models/skill.py`
- **ItemInstance** (11 connections) — `server/models/item.py`
- **player_spells.py** (11 connections) — `server/models/player_spells.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **EmoteAlias** (10 connections) — `server/models/emote.py`
- **player_skill.py** (10 connections) — `server/models/player_skill.py`
- *... and 251 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (60 shared connections)
- [combat models rationale](combat_models_rationale.md) (21 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (18 shared connections)
- [player preferences services](player_preferences_services.md) (15 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (10 shared connections)
- [command inventory factories](command_inventory_factories.md) (10 shared connections)
- [lucidity models rationale](lucidity_models_rationale.md) (9 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (9 shared connections)
- [game models player](game_models_player.md) (8 shared connections)
- [commands communication channels](commands_communication_channels.md) (6 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (5 shared connections)
- [grace period login](grace_period_login.md) (4 shared connections)

## Source Files

- `server/models/__init__.py`
- `server/models/base.py`
- `server/models/calendar.py`
- `server/models/dialogue.py`
- `server/models/emote.py`
- `server/models/item.py`
- `server/models/lucidity.py`
- `server/models/player.py`
- `server/models/player_effect.py`
- `server/models/player_skill.py`
- `server/models/player_spells.py`
- `server/models/skill.py`
- `server/models/skill_use_log.py`
- `server/models/spell_db.py`
- `server/models/world.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/tests/unit/models/test_calendar.py`
- `server/tests/unit/models/test_item.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 1063 (90%)
- INFERRED: 118 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*