# server tests unit services test

> 9 nodes

## Key Concepts

- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **fixture** (4 connections)
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **mock_npc_service()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create mock persistence layer.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create mock event bus.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create mock NPC combat integration service (no _rewards so XP uses fallback…** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create PlayerCombatService instance.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`

## Relationships

- [server game magic spell targeting](server_game_magic_spell_targeting.md) (5 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (1 shared connections)
- [server commands combat](server_commands_combat.md) (1 shared connections)
- [server commands exploration commands](server_commands_exploration_commands.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 13 (81%)
- INFERRED: 3 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*