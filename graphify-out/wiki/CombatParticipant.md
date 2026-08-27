# CombatParticipant

> 173 nodes

## Key Concepts

- **AliasStorage** (244 connections) — `server/alias_storage.py`
- **test_alias_storage.py** (68 connections) — `server/tests/unit/test_alias_storage.py`
- **Path** (11 connections)
- **.get_player_aliases()** (10 connections) — `server/alias_storage.py`
- **.get_alias_file_path()** (9 connections) — `server/alias_storage.py`
- **._load_alias_data()** (9 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **._save_alias_data()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **alias_storage()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **Path** (6 connections)
- **test_alias_storage_init_with_env_var()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_io_error()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_delete_player_aliases_io_error()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **AliasPayload** (5 connections)
- **MonkeyPatch** (5 connections)
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias_count()** (4 connections) — `server/alias_storage.py`
- **.remove_alias()** (4 connections) — `server/alias_storage.py`
- **_as_alias_payload()** (4 connections) — `server/alias_storage.py`
- **sample_alias()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- *... and 148 more nodes in this community*

## Relationships

- [NATSMessageHandler](NATSMessageHandler.md) (28 shared connections)
- [test_look_room.py](test_look_room.py.md) (21 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (18 shared connections)
- [pytest.md](pytest.md.md) (17 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (12 shared connections)
- [test_dependency_analysis.py](test_dependency_analysis.py.md) (7 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (7 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (6 shared connections)
- [test_combat_integration_base.py](test_combat_integration_base.py.md) (5 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (4 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 394 (82%)
- INFERRED: 85 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*