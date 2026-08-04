# world models rationale

> 162 nodes

## Key Concepts

- **Base** (60 connections) — `server/models/base.py`
- **test_world.py** (27 connections) — `server/tests/unit/models/test_world.py`
- **base.py** (22 connections) — `server/models/base.py`
- **test_calendar.py** (13 connections) — `server/tests/unit/models/test_calendar.py`
- **test_emote.py** (13 connections) — `server/tests/unit/models/test_emote.py`
- **player_spells.py** (11 connections) — `server/models/player_spells.py`
- **test_metadata.py** (11 connections) — `server/tests/unit/test_metadata.py`
- **EmoteAlias** (10 connections) — `server/models/emote.py`
- **SpellDB** (10 connections) — `server/models/spell_db.py`
- **world.py** (10 connections) — `server/models/world.py`
- **RoomLink** (10 connections) — `server/models/world.py`
- **HolidayModel** (9 connections) — `server/models/calendar.py`
- **NPCScheduleModel** (9 connections) — `server/models/calendar.py`
- **Emote** (9 connections) — `server/models/emote.py`
- **player_effect.py** (9 connections) — `server/models/player_effect.py`
- **Zone** (9 connections) — `server/models/world.py`
- **Subzone** (9 connections) — `server/models/world.py`
- **RoomModel** (9 connections) — `server/models/world.py`
- **SkillUseLog** (8 connections) — `server/models/skill_use_log.py`
- **spell_db.py** (8 connections) — `server/models/spell_db.py`
- **ZoneConfigurationMapping** (8 connections) — `server/models/world.py`
- **calendar.py** (7 connections) — `server/models/calendar.py`
- **emote.py** (7 connections) — `server/models/emote.py`
- **dialogue.py** (6 connections) — `server/models/dialogue.py`
- **test_skill_use_log.py** (6 connections) — `server/tests/unit/models/test_skill_use_log.py`
- *... and 137 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (17 shared connections)
- [task registry app](task_registry_app.md) (17 shared connections)
- [Loot Generation](Loot_Generation.md) (8 shared connections)
- [combat models rationale](combat_models_rationale.md) (7 shared connections)
- [player requests schemas](player_requests_schemas.md) (6 shared connections)
- [player room realtime](player_room_realtime.md) (6 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (5 shared connections)
- [fixtures return shape](fixtures_return_shape.md) (3 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (2 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (1 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (1 shared connections)
- [profession models rationale](profession_models_rationale.md) (1 shared connections)

## Source Files

- `server/metadata.py`
- `server/models/base.py`
- `server/models/calendar.py`
- `server/models/dialogue.py`
- `server/models/emote.py`
- `server/models/player_effect.py`
- `server/models/player_spells.py`
- `server/models/skill_use_log.py`
- `server/models/spell_db.py`
- `server/models/world.py`
- `server/npc_metadata.py`
- `server/tests/unit/models/test_calendar.py`
- `server/tests/unit/models/test_emote.py`
- `server/tests/unit/models/test_skill_use_log.py`
- `server/tests/unit/models/test_spell_db.py`
- `server/tests/unit/models/test_world.py`
- `server/tests/unit/test_metadata.py`

## Audit Trail

- EXTRACTED: 497 (91%)
- INFERRED: 51 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*