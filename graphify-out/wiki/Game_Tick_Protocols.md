# Game Tick Protocols

> 27 nodes

## Key Concepts

- **game_tick_protocols.py** (30 connections) — `server/app/game_tick_protocols.py`
- **Protocol** (9 connections)
- **UUID** (9 connections)
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
- **_TickCombatService** (5 connections) — `server/app/game_tick_protocols.py`
- **_TickMpRegen** (5 connections) — `server/app/game_tick_protocols.py`
- **AsyncSession** (5 connections)
- **_TickEventBus** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickMagicService** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickNpcLifecycle** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickRespawnService** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_combat_by_participant()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_dead_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_mortally_wounded_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.handle_player_death()** (3 connections) — `server/app/game_tick_protocols.py`
- **.process_mortally_wounded_tick()** (3 connections) — `server/app/game_tick_protocols.py`
- **.move_player_to_limbo()** (3 connections) — `server/app/game_tick_protocols.py`
- **.publish_player_dp_decay_event_to_nats()** (2 connections) — `server/app/game_tick_protocols.py`
- **.send_personal_message()** (2 connections) — `server/app/game_tick_protocols.py`
- **.process_tick_regeneration()** (2 connections) — `server/app/game_tick_protocols.py`
- **FastAPI** (2 connections)
- **Player** (2 connections)
- **.process_game_tick()** (1 connections) — `server/app/game_tick_protocols.py`
- **.publish()** (1 connections) — `server/app/game_tick_protocols.py`
- **.check_casting_progress()** (1 connections) — `server/app/game_tick_protocols.py`
- *... and 2 more nodes in this community*

## Relationships

- [Game Tick Death](Game_Tick_Death.md) (7 shared connections)
- [Game Tick Status Effects](Game_Tick_Status_Effects.md) (4 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (3 shared connections)
- [Test Game Tick Death](Test_Game_Tick_Death.md) (3 shared connections)
- [Test Combat Flee Handler](Test_Combat_Flee_Handler.md) (2 shared connections)
- [Combat Events](Combat_Events.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)
- [Async Persistence](Async_Persistence.md) (1 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (1 shared connections)
- [Service](Service.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*