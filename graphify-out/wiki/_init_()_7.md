# . init ()

> 267 nodes

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **get_combat_service()** (10 connections) — `server/dependencies.py`
- **get_player_service_for_testing()** (9 connections) — `server/dependencies.py`
- **get_connection_manager()** (9 connections) — `server/dependencies.py`
- **get_async_persistence()** (9 connections) — `server/dependencies.py`
- **get_player_respawn_service()** (9 connections) — `server/dependencies.py`
- **get_player_combat_service()** (9 connections) — `server/dependencies.py`
- **get_player_death_service()** (9 connections) — `server/dependencies.py`
- **get_magic_service()** (9 connections) — `server/dependencies.py`
- **get_spell_registry()** (9 connections) — `server/dependencies.py`
- **get_spell_targeting_service()** (9 connections) — `server/dependencies.py`
- **get_spell_effects()** (9 connections) — `server/dependencies.py`
- **get_spell_learning_service()** (9 connections) — `server/dependencies.py`
- **get_mp_regeneration_service()** (9 connections) — `server/dependencies.py`
- **get_npc_lifecycle_manager()** (9 connections) — `server/dependencies.py`
- **get_npc_spawning_service()** (9 connections) — `server/dependencies.py`
- **get_npc_population_controller()** (9 connections) — `server/dependencies.py`
- **get_catatonia_registry()** (9 connections) — `server/dependencies.py`
- *... and 242 more nodes in this community*

## Relationships

- [message handler factory](message_handler_factory.md) (52 shared connections)
- [ExitStack](ExitStack.md) (11 shared connections)
- [character creation](character_creation.md) (10 shared connections)
- [real time](real_time.md) (6 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (6 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (5 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [close db()](close_db%28%29.md) (4 shared connections)

## Source Files

- `server/database.py`
- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 922 (87%)
- INFERRED: 132 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*