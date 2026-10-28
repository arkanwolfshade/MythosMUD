# InventoryMutationGuard

> 61 nodes · cohesion 0.06

## Key Concepts

- **quest_rewards.py** (18 connections) — `server/game/quest/quest_rewards.py`
- **test_quest_rewards.py** (15 connections) — `server/tests/unit/game/test_quest_rewards.py`
- **QuestRewardsMixin** (13 connections) — `server/game/quest/quest_rewards.py`
- **UUID** (11 connections)
- **QuestRewardSchema** (10 connections) — `server/schemas/quest/quest.py`
- **_Host** (9 connections) — `server/tests/unit/game/test_quest_rewards.py`
- **._apply_item_reward()** (8 connections) — `server/game/quest/quest_rewards.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_rewards.py`
- **test_malformed_or_unservable_rewards_are_skipped()** (8 connections) — `server/tests/unit/game/test_quest_rewards.py`
- **_config_value()** (7 connections) — `server/game/quest/quest_rewards.py`
- **SpellLearner** (7 connections) — `server/game/quest/quest_rewards.py`
- **XpGranter** (7 connections) — `server/game/quest/quest_rewards.py`
- **_Inventory** (7 connections) — `server/tests/unit/game/test_quest_rewards.py`
- **test_rewards_grant_xp_spell_and_item()** (7 connections) — `server/tests/unit/game/test_quest_rewards.py`
- **PlayerStore** (6 connections) — `server/game/quest/quest_rewards.py`
- **._apply_respawn_room_reward()** (6 connections) — `server/game/quest/quest_rewards.py`
- **._apply_spell_reward()** (6 connections) — `server/game/quest/quest_rewards.py`
- **._apply_xp_reward()** (6 connections) — `server/game/quest/quest_rewards.py`
- **_inventory_has_slot()** (5 connections) — `server/game/quest/quest_rewards.py`
- **._turn_in_inventory_full_error()** (5 connections) — `server/game/quest/quest_rewards.py`
- **_definition()** (5 connections) — `server/tests/unit/game/test_quest_rewards.py`
- **_Levels** (5 connections) — `server/tests/unit/game/test_quest_rewards.py`
- **UUID** (5 connections)
- **_Spells** (5 connections) — `server/tests/unit/game/test_quest_rewards.py`
- **.get_player_by_id()** (4 connections) — `server/game/quest/quest_rewards.py`
- *... and 36 more nodes in this community*

## Relationships

- [item_catalog_repository.py](item_catalog_repository.py.md) (8 shared connections)
- [mcp.json](mcp.json.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [properties](properties.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_rewards.py`
- `server/npc/npc_base.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/game/test_quest_rewards.py`

## Audit Trail

- EXTRACTED: 129 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*