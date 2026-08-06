# services npc startup

> 10 nodes

## Key Concepts

- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **PlayerLifecycleServices** (8 connections) — `server/services/combat_service_types.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **set_combat_service()** (6 connections) — `server/services/combat_service_state.py`
- **test_initialize_nats_and_combat_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **Initialize NATS-dependent services including combat service.      DEPRECATED: Th** (1 connections) — `server/app/lifespan_startup.py`
- **Create CombatService with NATS and register it. Assumes NATS is connected.** (1 connections) — `server/container/bundles/combat.py`
- **Set the global combat service instance.** (1 connections) — `server/services/combat_service_state.py`
- **Player death and respawn services for CombatService injection.** (1 connections) — `server/services/combat_service_types.py`
- **Test initialize_nats_and_combat_services() initializes NATS and combat.** (1 connections) — `server/tests/unit/app/test_lifespan_startup.py`

## Relationships

- [npc database infrastructure](npc_database_infrastructure.md) (4 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (2 shared connections)
- [subject admin controller](subject_admin_controller.md) (2 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (1 shared connections)
- [spell game magic](spell_game_magic.md) (1 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/combat.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 27 (71%)
- INFERRED: 11 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*