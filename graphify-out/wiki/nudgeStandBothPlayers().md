# nudgeStandBothPlayers()

> 21 nodes

## Key Concepts

- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **._unwrap_string_inner_message_if_json()** (7 connections) — `server/realtime/message_validator.py`
- **.parse_and_validate()** (7 connections) — `server/realtime/message_validator.py`
- **._parse_outer_json_object()** (6 connections) — `server/realtime/message_validator.py`
- **.validate_size()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_schema()** (5 connections) — `server/realtime/message_validator.py`
- **._extract_csrf_token_string()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_csrf()** (5 connections) — `server/realtime/message_validator.py`
- **._validate_string_lengths()** (4 connections) — `server/realtime/message_validator.py`
- **._calculate_depth()** (3 connections) — `server/realtime/message_validator.py`
- **BaseModel** (2 connections)
- **Validate message size.          Args:             data: Raw message data as s** (1 connections) — `server/realtime/message_validator.py`
- **Validate JSON structure including depth limits.          Args:             me** (1 connections) — `server/realtime/message_validator.py`
- **Calculate the maximum nesting depth of a JSON structure.          Args:** (1 connections) — `server/realtime/message_validator.py`
- **Validate that strings in the JSON structure don't exceed length limits.** (1 connections) — `server/realtime/message_validator.py`
- **Validate message against Pydantic schema.          Args:             message:** (1 connections) — `server/realtime/message_validator.py`
- **Return the first string CSRF token from known keys, or None if absent.** (1 connections) — `server/realtime/message_validator.py`
- **Validate CSRF token in message.          Args:             message: Parsed JS** (1 connections) — `server/realtime/message_validator.py`
- **Parse raw payload to a dict; validate size and outer JSON structure.** (1 connections) — `server/realtime/message_validator.py`
- **If ``message["message"]`` is a JSON string, parse and validate inner object.** (1 connections) — `server/realtime/message_validator.py`
- **Parse and validate a complete WebSocket message.          This is the main ent** (1 connections) — `server/realtime/message_validator.py`

## Relationships

- [. init ()](_init_%28%29.md) (18 shared connections)

## Source Files

- `server/realtime/message_validator.py`

## Audit Trail

- EXTRACTED: 66 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*