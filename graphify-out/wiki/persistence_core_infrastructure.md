# persistence core infrastructure

> 167 nodes

## Key Concepts

- **player_service.py** (45 connections) — `server/game/player_service.py`
- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **SpellRegistry** (37 connections) — `server/game/magic/spell_registry.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **spell.py** (28 connections) — `server/models/spell.py`
- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_materials.py** (22 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_magic_healing_events.py** (20 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_spell_costs.py** (19 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_spell_registry.py** (18 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **MagicServiceHealingMixin** (17 connections) — `server/game/magic/magic_healing_events.py`
- **_HealingService** (17 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **SpellSchool** (15 connections) — `server/models/spell.py`
- **SpellEffectType** (15 connections) — `server/models/spell.py`
- **SpellTargetType** (14 connections) — `server/models/spell.py`
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **SpellRangeType** (12 connections) — `server/models/spell.py`
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **_spell()** (11 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **UUID** (6 connections)
- *... and 142 more nodes in this community*

## Relationships

- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (44 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (20 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (15 shared connections)
- [player respawn event](player_respawn_event.md) (14 shared connections)
- [Player Stats](Player_Stats.md) (10 shared connections)
- [room occupant manager](room_occupant_manager.md) (10 shared connections)
- [player room realtime](player_room_realtime.md) (8 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (7 shared connections)
- [npc combat player](npc_combat_player.md) (7 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (6 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (6 shared connections)
- [spell game magic](spell_game_magic.md) (6 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/player_service.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/game/magic/test_spell_registry.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 722 (95%)
- INFERRED: 35 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*