# Player Death Service

> 31 nodes · cohesion 0.11

## Key Concepts

- **PlayerDiedEvent** (17 connections) — `server/events/event_types.py`
- **PlayerDPDecayEvent** (15 connections) — `server/events/event_types.py`
- **log_exception_once()** (14 connections) — `server/structured_logging/enhanced_logging_config.py`
- **player_death_service.py** (12 connections) — `server/services/player_death_service.py`
- **UUID** (9 connections) — `server/services/player_death_service.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **AsyncSession** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **Any** (6 connections) — `server/services/player_death_service.py`
- **Player** (6 connections) — `server/services/player_death_service.py`
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **._get_room_name_for_death()** (3 connections) — `server/services/player_death_service.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Event fired when a mortally wounded player loses DP due to decay.      This even** (1 connections) — `server/events/event_types.py`
- **Event fired when a player dies (DP <= -10).      This event is triggered when a** (1 connections) — `server/events/event_types.py`
- **Exception** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Player Death Service for managing player mortality and DP decay.  This service h** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player.          Decreases player** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead.          Args:             play** (1 connections) — `server/services/player_death_service.py`
- **Clear player combat state when they die.          BUGFIX #244: As documented in** (1 connections) — `server/services/player_death_service.py`
- **Get room name for death location display.          Args:             death_locat** (1 connections) — `server/services/player_death_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (12 shared connections)
- [[Player Domain Model]] (6 shared connections)
- [[Distributed Event Bus]] (4 shared connections)
- [[NPC Admin API]] (4 shared connections)
- [[Enhanced Logging Exceptions]] (3 shared connections)
- [[NPC Combat Events]] (2 shared connections)
- [[Event Bus Serialization]] (2 shared connections)
- [[Player Respawn Events]] (2 shared connections)
- [[Realtime Player Event]] (2 shared connections)
- [[Realtime Event Delegation]] (2 shared connections)
- [[Player Death Service Tests]] (2 shared connections)
- [[App Lifespan Management]] (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 125 (85%)
- INFERRED: 22 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
