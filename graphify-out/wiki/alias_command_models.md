# alias command models

> 33 nodes

## Key Concepts

- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **.get_mortally_wounded_players()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **._get_room_name_for_death()** (4 connections) — `server/services/player_death_service.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **player_death_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Small types shared by CombatService wiring.** (1 connections) — `server/services/combat_service_types.py`
- **Service for managing player death, mortally wounded state, and DP decay.      Th** (1 connections) — `server/services/player_death_service.py`
- **Initialize the player death service.          Args:             event_bus: Optio** (1 connections) — `server/services/player_death_service.py`
- **Get all players currently in the mortally wounded state.          A player is co** (1 connections) — `server/services/player_death_service.py`
- **Get all players who are dead (DP <= -10).          Args:             session: As** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player.          Decreases player** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead.          Args:             play** (1 connections) — `server/services/player_death_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [item models rationale](item_models_rationale.md) (8 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [combat models rationale](combat_models_rationale.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [command base models](command_base_models.md) (3 shared connections)
- [player death service](player_death_service.md) (3 shared connections)
- [container schemas containers](container_schemas_containers.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 127 (91%)
- INFERRED: 12 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*