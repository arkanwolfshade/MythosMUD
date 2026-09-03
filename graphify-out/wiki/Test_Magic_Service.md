# Test Magic Service

> 119 nodes

## Key Concepts

- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **test_magic_service.py** (48 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **MagicService** (41 connections) — `server/game/magic/magic_service.py`
- **UUID** (26 connections)
- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **asyncio** (19 connections)
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **get_current_tick()** (14 connections) — `server/app/game_tick_counter.py`
- **MagicServiceCompletionMixin** (12 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (12 connections)
- **test_casting_state_manager.py** (12 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **Any** (11 connections)
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **game_tick_counter.py** (9 connections) — `server/app/game_tick_counter.py`
- **CastingState** (8 connections) — `server/game/magic/casting_state_manager.py`
- **StartCastingTarget** (8 connections) — `server/game/magic/casting_state_manager.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **UUID** (8 connections)
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **.start_casting()** (6 connections) — `server/game/magic/casting_state_manager.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- *... and 94 more nodes in this community*

## Relationships

- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (29 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (17 shared connections)
- [Test Spell](Test_Spell.md) (15 shared connections)
- [Magic Service](Magic_Service.md) (13 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (13 shared connections)
- [Test Magic Commands](Test_Magic_Commands.md) (9 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (6 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (5 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (4 shared connections)
- [Combat Events](Combat_Events.md) (3 shared connections)
- [Spell Learning Service](Spell_Learning_Service.md) (3 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 344 (86%)
- INFERRED: 57 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*