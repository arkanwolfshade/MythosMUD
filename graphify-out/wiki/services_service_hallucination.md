# services service hallucination

> 23 nodes

## Key Concepts

- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
- **_format_core_attributes()** (10 connections) — `server/commands/look_npc.py`
- **_format_other_stats()** (10 connections) — `server/commands/look_npc.py`
- **_format_single_npc_result()** (10 connections) — `server/commands/look_npc.py`
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_format_lifecycle_info_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **NPC look functionality for MythosMUD.  This module handles looking at NPCs, incl** (1 connections) — `server/commands/look_npc.py`
- **Find NPCs matching the target name.** (1 connections) — `server/commands/look_npc.py`
- **Format core attributes section.** (1 connections) — `server/commands/look_npc.py`
- **Format other stats section (excluding core attributes).** (1 connections) — `server/commands/look_npc.py`
- **Format lifecycle information section.** (1 connections) — `server/commands/look_npc.py`
- **Format NPC stats for admin display.** (1 connections) — `server/commands/look_npc.py`
- **Format result for a single matching NPC.** (1 connections) — `server/commands/look_npc.py`
- **Format result for multiple matching NPCs.** (1 connections) — `server/commands/look_npc.py`
- **Try to find and display an NPC in implicit lookup.** (1 connections) — `server/commands/look_npc.py`
- **Test formatting lifecycle information.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test finding matching NPCs successfully.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`

## Relationships

- [npc look commands](npc_look_commands.md) (26 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (12 shared connections)
- [connection realtime statistics](connection_realtime_statistics.md) (3 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (3 shared connections)
- [cache caching lru](cache_caching_lru.md) (3 shared connections)
- [message filtering helpers](message_filtering_helpers.md) (3 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (3 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (3 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (3 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 137 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*