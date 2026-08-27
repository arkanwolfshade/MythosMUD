# test_room_occupant_manager.py

> 30 nodes

## Key Concepts

- **game_tick_protocols.py** (28 connections) — `server/app/game_tick_protocols.py`
- **Protocol** (9 connections)
- **UUID** (9 connections)
- **_online_player_ids()** (8 connections) — `server/app/game_tick_protocols.py`
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
- **_TickCombatService** (5 connections) — `server/app/game_tick_protocols.py`
- **_TickConnectionManager** (5 connections) — `server/app/game_tick_protocols.py`
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
- **Player** (2 connections)
- **.process_game_tick()** (1 connections) — `server/app/game_tick_protocols.py`
- **.publish()** (1 connections) — `server/app/game_tick_protocols.py`
- *... and 5 more nodes in this community*

## Relationships

- [RoomInfoPanel.tsx](RoomInfoPanel.tsx.md) (11 shared connections)
- [FakeHallucinationService](FakeHallucinationService.md) (8 shared connections)
- [User](User.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*