# character creation validate

> 8 nodes

## Key Concepts

- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **Return connection manager from CombatService getter when exposed.** (1 connections) — `server/services/combat_death_handler.py`
- **Handle player death events including mortally wounded, death, and corpse creatio** (1 connections) — `server/services/combat_death_handler.py`
- **Create corpse container when player dies.** (1 connections) — `server/services/combat_death_handler.py`
- **Handle mortally wounded and death state changes for target.          Args:** (1 connections) — `server/services/combat_death_handler.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [command factories exploration](command_factories_exploration.md) (3 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [rate limiter services](rate_limiter_services.md) (1 shared connections)

## Source Files

- `server/services/combat_death_handler.py`

## Audit Trail

- EXTRACTED: 27 (87%)
- INFERRED: 4 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*