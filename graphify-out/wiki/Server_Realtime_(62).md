# Server Realtime (62)

> 28 nodes

## Key Concepts

- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **test_warded_indicator_not_shown_for_reconnections()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Any** (3 connections)
- **test_filter_other_players_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_filter_other_players_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Player occupant processing utilities.  This module handles querying and processi** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Processes player occupants for rooms.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Initialize player occupant processor.          Args:             connection_mana** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Ensure a player is included in the player ID strings list if specified.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Convert player ID strings to UUIDs for batch loading.          Args:** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Create occupant information dictionary for a single player.          Args:** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Process players and convert to occupant information.          Args:** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Test that '(warded)' indicator is not shown for reconnections.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Unit tests for visual indicator (linkdead) display.  Tests that "(linkdead)" ind** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Test _filter_other_players() adds (linkdead) indicator for grace period players.** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- *... and 3 more nodes in this community*

## Relationships

- [Server Realtime (8)](Server_Realtime_%288%29.md) (9 shared connections)
- [Server Events](Server_Events.md) (4 shared connections)
- [Server Realtime (5)](Server_Realtime_%285%29.md) (4 shared connections)
- [Server Commands (17)](Server_Commands_%2817%29.md) (4 shared connections)
- [Server Commands (13)](Server_Commands_%2813%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Realtime (47)](Server_Realtime_%2847%29.md) (3 shared connections)
- [Server Realtime (20)](Server_Realtime_%2820%29.md) (2 shared connections)
- [Server Realtime (3)](Server_Realtime_%283%29.md) (1 shared connections)
- [Server Realtime (46)](Server_Realtime_%2846%29.md) (1 shared connections)

## Source Files

- `server/realtime/player_occupant_processor.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 111 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*