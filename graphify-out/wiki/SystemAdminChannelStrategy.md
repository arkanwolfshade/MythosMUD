# SystemAdminChannelStrategy

> 15 nodes · cohesion 0.25

## Key Concepts

- **test_look_room_segments.py** (17 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **_npc_section_parts()** (11 connections) — `server/commands/look_room.py`
- **test_a_phantom_is_tagged_exactly_like_a_real_hostile()** (6 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **test_room_look_carries_segments_that_join_to_the_whole_result()** (6 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **asyncio** (5 connections)
- **test_room_look_with_nobody_here_has_no_segments()** (5 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **_persistence()** (3 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **_phantom_patches()** (3 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **_room()** (3 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **test_section_parts_are_empty_without_npcs_or_a_room()** (3 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **test_section_parts_style_each_name_by_disposition()** (3 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **The "Also here: ..." line as parts, each NPC name styled by its disposition…** (1 connections) — `server/commands/look_room.py`
- **`look`'s "Also here: ..." line carries each NPC's name as a styled segment…** (1 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **Patch the viewer's phantom roster: one phantom named ``name``, or none.** (1 connections) — `server/tests/unit/commands/test_look_room_segments.py`
- **ADR-024: nothing in the line tells a hallucinated hostile from a real one.** (1 connections) — `server/tests/unit/commands/test_look_room_segments.py`

## Relationships

- [player_presence_tracker.py](player_presence_tracker.py.md) (7 shared connections)
- [look_container.py](look_container.py.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [security.ts](security.ts.md) (1 shared connections)
- [session](session.md) (1 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/tests/unit/commands/test_look_room_segments.py`

## Audit Trail

- EXTRACTED: 41 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*