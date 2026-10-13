# Community 574

> 30 nodes

## Key Concepts

- **PlayerOccupantProcessor** (20 connections) — `server/realtime/player_occupant_processor.py`
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **._create_player_occupant_info()** (6 connections) — `server/realtime/player_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **test_filter_other_players_adds_linkdead_indicator()** (4 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_filter_other_players_no_linkdead_when_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_format_player_look_display_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_format_player_look_display_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Any** (3 connections)
- **asyncio** (2 connections)
- **PlayerNameExtractor** (1 connections)
- **Process players and convert to occupant information. Args: room_id: The room ID…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Processes player occupants for rooms.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Initialize player occupant processor. Args: connection_manager:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Ensure a player is included in the player ID strings list if specified. Args:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Convert player ID strings to UUIDs for batch loading. Args: player_id_strings:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Create occupant information dictionary for a single player. Args:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Unit tests for visual indicator (linkdead) display. Tests that "(linkdead)"…** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Test PlayerOccupantProcessor adds (linkdead) indicator for grace period players.** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- *... and 5 more nodes in this community*

## Relationships

- [Community 46](Community_46.md) (5 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Community 87](Community_87.md) (4 shared connections)
- [Community 124](Community_124.md) (4 shared connections)
- [Community 367](Community_367.md) (2 shared connections)
- [Community 356](Community_356.md) (2 shared connections)
- [Community 103](Community_103.md) (1 shared connections)
- [Community 139](Community_139.md) (1 shared connections)

## Source Files

- `server/realtime/player_occupant_processor.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 57 (90%)
- INFERRED: 6 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*