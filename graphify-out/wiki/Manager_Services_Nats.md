# Manager Services Nats

> 9 nodes

## Key Concepts

- **_run_command_service_for_validated()** (6 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (6 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (6 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **_parse_command_line_or_client_error()** (3 connections) — `server/command_handler/processing.py`
- **Validate the raw command string via CommandProcessor.      Returns:         (** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- **Parse the command line; on success run CommandService (see ``_parse_command_line** (1 connections) — `server/command_handler/processing.py`
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Async Audit Cursor](Async_Audit_Cursor.md) (1 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`

## Audit Trail

- EXTRACTED: 28 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*