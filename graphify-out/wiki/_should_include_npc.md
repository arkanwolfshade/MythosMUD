# _should_include_npc

> 22 nodes

## Key Concepts

- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **test_create_pickup_command_empty_search_term()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_with_extra_tokens()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_quantity_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_quantity_only()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **._parse_index_or_search_term()** (4 connections) — `server/utils/command_factories_inventory.py`
- **._parse_quantity_from_args()** (4 connections) — `server/utils/command_factories_inventory.py`
- **Test create_pickup_command() creates PickupCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when quantity is zero.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when index is zero.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when index is negative.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when index has extra tokens.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when search term is empty.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() handles single number as index.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Parse quantity from args if present. Args: args: Original args list…** (1 connections) — `server/utils/command_factories_inventory.py`
- **Parse index or search term from selector tokens. Args: args: Original args list…** (1 connections) — `server/utils/command_factories_inventory.py`
- **Create pickup command supporting numeric indices or fuzzy names.** (1 connections) — `server/utils/command_factories_inventory.py`

## Relationships

- [test_connection_error_methods.py](test_connection_error_methods.py.md) (20 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (9 shared connections)
- [TestVerificationSqlUsersPlayers](TestVerificationSqlUsersPlayers.md) (4 shared connections)
- [maps/__init__.py](maps-__init__.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 41 (75%)
- INFERRED: 14 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*