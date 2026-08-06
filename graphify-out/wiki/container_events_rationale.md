# container events rationale

> 277 nodes

## Key Concepts

- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **ZoneConfiguration** (53 connections) — `server/npc/zone_configuration.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **should_spawn_npc()** (22 connections) — `server/npc/spawn_validator.py`
- **zone_config_loader.py** (22 connections) — `server/npc/zone_config_loader.py`
- **spawn_validator.py** (11 connections) — `server/npc/spawn_validator.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **._evaluate_spawn_requirements()** (9 connections) — `server/npc/spawning_service.py`
- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **ZoneSpecialRules** (7 connections) — `server/npc/zone_configuration.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **NPCSpawnRequest** (5 connections)
- **_ZoneConfigBucket** (5 connections) — `server/npc/zone_config_loader.py`
- *... and 252 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (47 shared connections)
- [room look commands](room_look_commands.md) (42 shared connections)
- [spell game magic](spell_game_magic.md) (18 shared connections)
- [lucidity event services](lucidity_event_services.md) (10 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [party service game](party_service_game.md) (3 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [auth rationale access](auth_rationale_access.md) (2 shared connections)
- [combat services rationale](combat_services_rationale.md) (2 shared connections)
- [profession models rationale](profession_models_rationale.md) (2 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_service.py`
- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_population_stats.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 866 (95%)
- INFERRED: 41 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*