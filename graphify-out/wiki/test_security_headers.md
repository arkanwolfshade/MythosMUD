# test security headers

> 117 nodes

## Key Concepts

- **factory.py** (37 connections) — `server/app/factory.py`
- **test_security_headers.py** (20 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **create_app()** (16 connections) — `server/app/factory.py`
- **main.py** (15 connections) — `server/main.py`
- **SecurityHeadersMiddleware** (13 connections) — `server/middleware/security_headers.py`
- **ComprehensiveLoggingMiddleware** (10 connections) — `server/middleware/comprehensive_logging.py`
- **.__call__()** (8 connections) — `server/middleware/comprehensive_logging.py`
- **.dispatch()** (7 connections) — `server/middleware/comprehensive_logging.py`
- **CORSConfigDict** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **UserRead** (6 connections) — `server/auth/endpoints.py`
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **comprehensive_logging.py** (6 connections) — `server/middleware/comprehensive_logging.py`
- **security_headers.py** (6 connections) — `server/middleware/security_headers.py`
- **MutableHeaders** (6 connections)
- **middleware()** (6 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **._log_request_start()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_success_with_status()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_error()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (4 connections) — `server/app/factory.py`
- *... and 92 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (11 shared connections)
- [Connection Manager](Connection_Manager.md) (7 shared connections)
- [metrics](metrics.md) (5 shared connections)
- [.shutdown()](shutdown%28%29.md) (4 shared connections)
- [process dead players()](process_dead_players%28%29.md) (3 shared connections)
- [Response](Response.md) (3 shared connections)
- [equipment helpers](equipment_helpers.md) (2 shared connections)
- [APIRouter](APIRouter.md) (1 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [fetch container items()](fetch_container_items%28%29.md) (1 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (1 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/main.py`
- `server/middleware/comprehensive_logging.py`
- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 340 (93%)
- INFERRED: 24 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*