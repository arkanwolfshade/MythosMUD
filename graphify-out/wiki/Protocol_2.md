# Protocol

> 12 nodes

## Key Concepts

- **Protocol** (7 connections)
- **UUID** (4 connections)
- **_ContainerPersistence** (3 connections) — `server/commands/look_container.py`
- **_LookPlayer** (3 connections) — `server/commands/look_container.py`
- **_LookRoom** (3 connections) — `server/commands/look_container.py`
- **_PrototypeRegistry** (3 connections) — `server/commands/look_container.py`
- **_WearableSvc** (3 connections) — `server/commands/look_container.py`
- **.get_container()** (3 connections) — `server/commands/look_container.py`
- **.get_wearable_containers_for_player()** (3 connections) — `server/commands/look_container.py`
- **_Prototype** (2 connections) — `server/commands/look_container.py`
- **.get_equipped_items()** (1 connections) — `server/commands/look_container.py`
- **.get()** (1 connections) — `server/commands/look_container.py`

## Relationships

- [test_look_container.py](test_look_container.py.md) (10 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (2 shared connections)

## Source Files

- `server/commands/look_container.py`

## Audit Trail

- EXTRACTED: 23 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*