# schemas calendar rationale

> 28 nodes

## Key Concepts

- **test_look_npc_helpers.py** (34 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **_should_include_npc()** (14 connections) — `server/commands/look_npc.py`
- **test_should_include_npc_alive_with_name()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_should_include_npc_dead()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_should_include_npc_no_name()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_core_attributes()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info_no_lifecycle_state()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_should_include_npc()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_should_include_npc_no_name()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_should_include_npc_not_alive()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Check if an NPC should be included in the results (has name and is alive).** (1 connections) — `server/commands/look_npc.py`
- **Test should_include_npc for alive NPC with name.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test should_include_npc for dead NPC.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test should_include_npc for NPC without name.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Unit tests for look_npc helper functions.  Tests the helper functions in look_np** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _format_core_attributes() formats core attributes.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _format_core_attributes() returns empty list when no core attributes.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _format_other_stats() formats non-core stats.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _format_other_stats() returns empty list when no other stats.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _format_lifecycle_info() formats lifecycle information.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _format_lifecycle_info() returns empty list when no lifecycle_state.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- *... and 3 more nodes in this community*

## Relationships

- [services service hallucination](services_service_hallucination.md) (12 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (6 shared connections)
- [message filtering helpers](message_filtering_helpers.md) (5 shared connections)
- [npc look commands](npc_look_commands.md) (4 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (4 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (4 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (2 shared connections)
- [cache caching lru](cache_caching_lru.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 98 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*