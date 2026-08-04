# regeneration service magic

> 16 nodes

## Key Concepts

- **MPRegenerationService** (20 connections) — `server/game/magic/mp_regeneration_service.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **UUID** (5 connections)
- **Any** (5 connections)
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.__init__()** (3 connections) — `server/game/magic/mp_regeneration_service.py`
- **Service for managing MP regeneration.      Handles passive regeneration over tim** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Initialize the MP regeneration service.          Args:             player_servic** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Process MP regeneration for a player on a game tick.          Args:** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Get MP regeneration multiplier based on player state.          Args:** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from resting (accelerated regeneration).          Args:             p** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from meditation (highly accelerated regeneration).          Args:** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from consuming an item.          Args:             player_id: Player** (1 connections) — `server/game/magic/mp_regeneration_service.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [config rationale reset](config_rationale_reset.md) (1 shared connections)
- [add fastapi users](add_fastapi_users.md) (1 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)
- [tick services game](tick_services_game.md) (1 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`

## Audit Trail

- EXTRACTED: 59 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*