# Npc Services Combat

> 18 nodes

## Key Concepts

- **ItemFactory** (13 connections) — `server/game/items/item_factory.py`
- **._initialize_item_services()** (10 connections) — `server/container/bundles/game.py`
- **.create_instance()** (7 connections) — `server/game/items/item_factory.py`
- **initialize_components()** (5 connections) — `server/game/items/component_hooks.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **._build_instance_metadata()** (4 connections) — `server/game/items/item_factory.py`
- **.__init__()** (3 connections) — `server/game/items/item_factory.py`
- **._resolve_stack_slot()** (3 connections) — `server/game/items/item_factory.py`
- **Any** (3 connections)
- **Exception** (1 connections)
- **On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item regist** (1 connections) — `server/container/bundles/game.py`
- **Load item prototypes from PostgreSQL and create item factory.** (1 connections) — `server/container/bundles/game.py`
- **Any** (1 connections)
- **Prepare component state metadata for a new item instance.      This routine curr** (1 connections) — `server/game/items/component_hooks.py`
- **ItemInstance** (1 connections)
- **Factory responsible for instantiating runtime item instances.** (1 connections) — `server/game/items/item_factory.py`
- **Initialize the item factory with a prototype registry.          Args:** (1 connections) — `server/game/items/item_factory.py`
- **Create an item instance from a prototype.** (1 connections) — `server/game/items/item_factory.py`

## Relationships

- [NATS Retry Handler](NATS_Retry_Handler.md) (9 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (6 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/items/component_hooks.py`
- `server/game/items/item_factory.py`

## Audit Trail

- EXTRACTED: 56 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*