# occupation slots 9()

> 6 nodes

## Key Concepts

- **.prune_stale_players()** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_stale_player_data()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Identify players whose last_seen timestamp exceeds the max age.          Args:** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove all data for a stale player.          Args:             pid: Player ID to** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove players whose presence is stale beyond the threshold.          Args:** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (5 shared connections)
- [Reset database state before each](Reset_database_state_before_each.md) (3 shared connections)
- [real time](real_time.md) (1 shared connections)
- [Test check grace period block](Test_check_grace_period_block.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 19 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*