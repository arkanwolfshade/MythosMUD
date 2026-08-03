# magic healing game

> 90 nodes

## Key Concepts

- **PlayerService** (140 connections) — `server/game/player_service.py`
- **MagicServiceHealingMixin** (15 connections) — `server/game/magic/magic_healing_events.py`
- **magic_healing_events.py** (14 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (11 connections)
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **PlayerRespawnWrapper** (8 connections) — `server/game/player_respawn_wrapper.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **TestGetPlayerService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **UUID** (6 connections)
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **.__init__()** (6 connections) — `server/game/magic/spell_effects.py`
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (5 connections)
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **TestGetPlayerServiceForTesting** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **._effect_result_has_healing()** (4 connections) — `server/game/magic/magic_healing_events.py`
- **.resolve_player_name()** (4 connections) — `server/game/player_search_service.py`
- **.apply_lucidity_loss()** (4 connections) — `server/game/player_service.py`
- **.apply_fear()** (4 connections) — `server/game/player_service.py`
- **.apply_corruption()** (4 connections) — `server/game/player_service.py`
- **.gain_occult_knowledge()** (4 connections) — `server/game/player_service.py`
- **.heal_player()** (4 connections) — `server/game/player_service.py`
- *... and 65 more nodes in this community*

## Relationships

- [NPC Definitions Admin](NPC_Definitions_Admin.md) (43 shared connections)
- [Player Stats](Player_Stats.md) (27 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (18 shared connections)
- [command inventory factories](command_inventory_factories.md) (16 shared connections)
- [spell models rationale](spell_models_rationale.md) (13 shared connections)
- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [Item Instances](Item_Instances.md) (4 shared connections)
- [character creation validate](character_creation_validate.md) (4 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (4 shared connections)
- [respawn player handlers](respawn_player_handlers.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 337 (82%)
- INFERRED: 74 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*