# Container API Endpoints

> 9 nodes

## Key Concepts

- **MythosValidationError** (8 connections)
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_create_command_object_re_raises_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_process_command_string_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_validated_command_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command handles ValidationError.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test _parse_command_string handles ValidationError.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test _create_command_object re-raises MythosValidationError without wrapping.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test process_command_string handles MythosMUD validation errors.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`

## Relationships

- [Spell Registry Costs](Spell_Registry_Costs.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [NPC Population Control](NPC_Population_Control.md) (2 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (1 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (1 shared connections)
- [Character Creation API](Character_Creation_API.md) (1 shared connections)
- [Cursor Agents Analyzer](Cursor_Agents_Analyzer.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 17 (63%)
- INFERRED: 10 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*