# lifespan_startup.py

> 97 nodes · cohesion 0.04

## Key Concepts

- **get_help_content()** (40 connections) — `server/help/help_content.py`
- **help_content.py** (38 connections) — `server/help/help_content.py`
- **test_help_docs.py** (29 connections) — `server/tests/unit/help/test_help_docs.py`
- **load_help_docs()** (22 connections) — `server/help/help_content.py`
- **test_bank_wiring.py** (19 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- **get_manual()** (15 connections) — `server/help/help_content.py`
- **CommandDoc** (12 connections) — `server/help/help_content.py`
- **HelpDocs** (12 connections) — `server/help/help_content.py`
- **_e()** (9 connections) — `server/help/help_content.py`
- **_format_command()** (9 connections) — `server/help/help_content.py`
- **GuideDoc** (9 connections) — `server/help/help_content.py`
- **_AllowlistChecker** (8 connections) — `server/tests/unit/help/test_help_docs.py`
- **_format_index()** (7 connections) — `server/help/help_content.py`
- **TypedDict** (7 connections)
- **_all_topics()** (6 connections) — `server/tests/unit/help/test_help_docs.py`
- **test_hidden_admin_commands_are_not_offered_as_suggestions_or_see_also()** (6 connections) — `server/tests/unit/help/test_help_docs.py`
- **test_websocket_handler_help.py** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **_format_guide()** (5 connections) — `server/help/help_content.py`
- **_see_also_html()** (5 connections) — `server/help/help_content.py`
- **_subhead()** (5 connections) — `server/help/help_content.py`
- **server/help/__init__.py** (5 connections) — `server/help/__init__.py`
- **test_see_also_only_points_at_documented_topics()** (5 connections) — `server/tests/unit/help/test_help_docs.py`
- **test_the_docs_do_not_describe_diagonal_movement()** (5 connections) — `server/tests/unit/help/test_help_docs.py`
- **_argument_html()** (4 connections) — `server/help/help_content.py`
- **_complete_command()** (4 connections) — `server/help/help_content.py`
- *... and 72 more nodes in this community*

## Relationships

- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (6 shared connections)
- [CommandFactory](CommandFactory.md) (6 shared connections)
- [command_parser.py](command_parser.py.md) (4 shared connections)
- [NATSService](NATSService.md) (4 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (3 shared connections)
- [QuestService](QuestService.md) (3 shared connections)
- [RoomBasedChannelStrategy](RoomBasedChannelStrategy.md) (3 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (3 shared connections)
- [deprecated_patterns.py](deprecated_patterns.py.md) (3 shared connections)
- [Communities (10 total, 2 thin omitted)](Communities_10_total,_2_thin_omitted.md) (1 shared connections)
- [event_handler.py](event_handler.py.md) (1 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (1 shared connections)

## Source Files

- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/api/test_help_api.py`
- `server/tests/unit/commands/test_bank_wiring.py`
- `server/tests/unit/help/test_help_docs.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 231 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*