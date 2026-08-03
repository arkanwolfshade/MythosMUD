# NPC Services Bootstrap

> 30 nodes

## Key Concepts

- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **.initialize()** (8 connections) — `server/container/bundles/combat.py`
- **PlayerLifecycleServices** (8 connections) — `server/services/combat_service_types.py`
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
- **Initialize combat services.** (1 connections) — `server/container/bundles/combat.py`
- **Small types shared by CombatService wiring.** (1 connections) — `server/services/combat_service_types.py`
- **Player death and respawn services for CombatService injection.** (1 connections) — `server/services/combat_service_types.py`
- **Service for managing player death, mortally wounded state, and DP decay.      Th** (1 connections) — `server/services/player_death_service.py`
- **Initialize the player death service.          Args:             event_bus: Optio** (1 connections) — `server/services/player_death_service.py`
- **Get all players currently in the mortally wounded state.          A player is co** (1 connections) — `server/services/player_death_service.py`
- **Get all players who are dead (DP <= -10).          Args:             session: As** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player.          Decreases player** (1 connections) — `server/services/player_death_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [Async Query Helpers](Async_Query_Helpers.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [Item Instances](Item_Instances.md) (5 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (4 shared connections)
- [System Metrics](System_Metrics.md) (4 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [player death service](player_death_service.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (1 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`

## Audit Trail

- EXTRACTED: 115 (87%)
- INFERRED: 17 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*