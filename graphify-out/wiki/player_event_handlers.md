# player event handlers

> 22 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **Any** (6 connections)
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **.set_legacy_environment_variables()** (2 connections) — `server/config/models/app.py`
- **BaseSettings** (1 connections)
- **Composite application configuration.      This is the main configuration class t** (1 connections) — `server/config/models/app.py`
- **Initialize configuration and set environment variables for legacy compatibility.** (1 connections) — `server/config/models/app.py`
- **Set environment variables for legacy code that reads them directly.** (1 connections) — `server/config/models/app.py`
- **Return first set CORS origins env var to reduce CCN in _sanitize.** (1 connections) — `server/config/models/app.py`
- **Normalize environment variables so nested configs can parse them reliably.** (1 connections) — `server/config/models/app.py`
- **Convert to legacy dict format for backward compatibility.          This allows g** (1 connections) — `server/config/models/app.py`
- **Build legacy dict entries for game config.** (1 connections) — `server/config/models/app.py`
- **Build legacy nats nested dict.** (1 connections) — `server/config/models/app.py`
- **Build legacy chat nested dict.** (1 connections) — `server/config/models/app.py`
- **Build legacy cors nested dict.** (1 connections) — `server/config/models/app.py`

## Relationships

- [lucidity npc combat](lucidity_npc_combat.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [config models cors](config_models_cors.md) (2 shared connections)
- [invite models rationale](invite_models_rationale.md) (2 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)
- [config models rationale](config_models_rationale.md) (2 shared connections)
- [persistence container parse](persistence_container_parse.md) (1 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (1 shared connections)

## Source Files

- `server/config/models/app.py`

## Audit Trail

- EXTRACTED: 78 (88%)
- INFERRED: 11 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*