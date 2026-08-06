# dead letter queue

> 15 nodes

## Key Concepts

- **MagicBundle** (22 connections) — `server/container/bundles/magic.py`
- **_create_registry_and_targeting()** (15 connections) — `server/container/bundles/magic.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
- **_validate_magic_prerequisites()** (6 connections) — `server/container/bundles/magic.py`
- **.initialize()** (6 connections) — `server/container/bundles/magic.py`
- **test_magic_bundle_create_registry_and_targeting()** (3 connections) — `server/tests/unit/container/test_container_bundles.py`
- **test_magic_create_learning_mp_regen_and_magic()** (3 connections) — `server/tests/unit/container/test_container_bundles.py`
- **Any** (2 connections)
- **test_magic_validate_prerequisites()** (2 connections) — `server/tests/unit/container/test_container_bundles.py`
- **test_magic_bundle_initialize_unit_test()** (2 connections) — `server/tests/unit/container/test_container_bundles.py`
- **Raise if prerequisites for magic services are missing.** (1 connections) — `server/container/bundles/magic.py`
- **Create spell registry, targeting, and effects services. Return (spell_registry,** (1 connections) — `server/container/bundles/magic.py`
- **Create spell learning, MP regen, and magic services; link magic to combat.** (1 connections) — `server/container/bundles/magic.py`
- **Magic system services.** (1 connections) — `server/container/bundles/magic.py`
- **Initialize magic services.** (1 connections) — `server/container/bundles/magic.py`

## Relationships

- [nats services service](nats_services_service.md) (11 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (9 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (9 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (2 shared connections)
- [player respawn event](player_respawn_event.md) (2 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (2 shared connections)

## Source Files

- `server/container/bundles/magic.py`
- `server/tests/unit/container/test_container_bundles.py`

## Audit Trail

- EXTRACTED: 66 (86%)
- INFERRED: 11 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*