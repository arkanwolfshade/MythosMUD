# PlayerOccupantProcessor

> 20 nodes

## Key Concepts

- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **test_warded_indicator_in_player_occupant_processor()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **test_warded_indicator_not_shown_for_reconnections()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Any** (3 connections)
- **processor()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **Processes player occupants for rooms.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Initialize player occupant processor.          Args:             connection_mana** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Ensure a player is included in the player ID strings list if specified.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Convert player ID strings to UUIDs for batch loading.          Args:** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Create occupant information dictionary for a single player.          Args:** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Process players and convert to occupant information.          Args:** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Test that player occupant processor adds '(warded)' indicator.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Test that '(warded)' indicator is not shown for reconnections.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Create PlayerOccupantProcessor instance.** (1 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`

## Relationships

- [disconnect grace period](disconnect_grace_period.md) (7 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (4 shared connections)
- [login grace period](login_grace_period.md) (3 shared connections)
- [look room](look_room.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [test player occupant processor](test_player_occupant_processor.md) (2 shared connections)
- [npc occupant processor](npc_occupant_processor.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/player_occupant_processor.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`

## Audit Trail

- EXTRACTED: 75 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*