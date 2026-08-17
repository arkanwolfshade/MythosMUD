# test_target_resolution_service.py

> 20 nodes

## Key Concepts

- **test_target_resolution_service.py** (41 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_add_disambiguation_suffixes()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_disambiguation_suffix_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_single_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_clean_target_name_empty()** (2 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_clean_target_name_extracts_suffix()** (2 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_normalize_name_for_matching()** (2 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_validate_player_and_room_blank_room_id()** (2 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_validate_player_and_room_player_not_found()** (2 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_validate_room_exists_sync_get_room_by_id()** (2 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Unit tests for target resolution service. Tests the TargetResolutionService…** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Disambiguation suffix is parsed from target name.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Whitespace-only target names are empty.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Missing player returns error result.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Blank room id is treated as not in a room.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Punctuation is stripped for fuzzy name matching.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Sync get_room_by_id validates room presence.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Duplicate names receive numeric suffixes.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Single match returns success.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Suffix selects one match from duplicates.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`

## Relationships

- [TargetResolutionService](TargetResolutionService.md) (10 shared connections)
- [asyncio](asyncio.md) (9 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [target_service](target_service.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (1 shared connections)
- [test_search_npcs_in_room_empty_list](test_search_npcs_in_room_empty_list.md) (1 shared connections)
- [test_resolve_target_no_persistence_methods](test_resolve_target_no_persistence_methods.md) (1 shared connections)
- [test_resolve_target_no_room](test_resolve_target_no_room.md) (1 shared connections)
- [test_resolve_target_empty_target_name](test_resolve_target_empty_target_name.md) (1 shared connections)
- [test_resolve_target_whitespace_target_name](test_resolve_target_whitespace_target_name.md) (1 shared connections)
- [test_resolve_target_uses_get_player_fallback](test_resolve_target_uses_get_player_fallback.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 50 (85%)
- INFERRED: 9 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*