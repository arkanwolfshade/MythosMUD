# server game mechanics gamemechanicsservice

> 41 nodes

## Key Concepts

- **GameMechanicsService** (27 connections) — `server/game/mechanics.py`
- **test_mechanics.py** (17 connections) — `server/tests/unit/game/test_mechanics.py`
- **_player()** (8 connections) — `server/tests/unit/game/test_mechanics.py`
- **asyncio** (8 connections)
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **.gain_occult_knowledge()** (4 connections) — `server/game/mechanics.py`
- **.__init__()** (4 connections) — `server/services/npc_combat_rewards.py`
- **test_apply_corruption_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_fear_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_lucidity_loss_player_not_found()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_lucidity_loss_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_damage_player_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_gain_experience_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_gain_occult_knowledge_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_heal_player_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **.apply_corruption()** (3 connections) — `server/game/mechanics.py`
- **.apply_fear()** (3 connections) — `server/game/mechanics.py`
- **.apply_lucidity_loss()** (3 connections) — `server/game/mechanics.py`
- **.damage_player()** (3 connections) — `server/game/mechanics.py`
- **.gain_experience()** (3 connections) — `server/game/mechanics.py`
- **.heal_player()** (3 connections) — `server/game/mechanics.py`
- **.__init__()** (3 connections) — `server/game/mechanics.py`
- **.calculate_xp_reward()** (3 connections) — `server/services/npc_combat_rewards.py`
- **service()** (3 connections) — `server/tests/unit/game/test_mechanics.py`
- **persistence()** (2 connections) — `server/tests/unit/game/test_mechanics.py`
- *... and 16 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (5 shared connections)
- [server persistence repositories experience repository](server_persistence_repositories_experience_repository.md) (2 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (2 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (1 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (1 shared connections)
- [server npc combat integration base](server_npc_combat_integration_base.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/npc/combat_integration_base.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/game/test_mechanics.py`

## Audit Trail

- EXTRACTED: 77 (88%)
- INFERRED: 11 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*