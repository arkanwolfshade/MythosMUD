# Community 569

> 30 nodes

## Key Concepts

- **QuestRewardsMixin** (15 connections) — `server/game/quest/quest_rewards.py`
- **UUID** (11 connections)
- **._apply_item_reward()** (8 connections) — `server/game/quest/quest_rewards.py`
- **._apply_rewards()** (8 connections) — `server/game/quest/quest_rewards.py`
- **_config_value()** (7 connections) — `server/game/quest/quest_rewards.py`
- **PlayerStore** (6 connections) — `server/game/quest/quest_rewards.py`
- **._apply_respawn_room_reward()** (6 connections) — `server/game/quest/quest_rewards.py`
- **._apply_spell_reward()** (6 connections) — `server/game/quest/quest_rewards.py`
- **._apply_xp_reward()** (6 connections) — `server/game/quest/quest_rewards.py`
- **_inventory_has_slot()** (5 connections) — `server/game/quest/quest_rewards.py`
- **._turn_in_inventory_full_error()** (5 connections) — `server/game/quest/quest_rewards.py`
- **.get_player_by_id()** (4 connections) — `server/game/quest/quest_rewards.py`
- **.save_player()** (3 connections) — `server/game/quest/quest_rewards.py`
- **.learn_spell_from_quest()** (3 connections) — `server/game/quest/quest_rewards.py`
- **.grant_xp()** (3 connections) — `server/game/quest/quest_rewards.py`
- **.add_item_to_inventory()** (3 connections) — `server/npc/npc_base.py`
- **Player** (2 connections)
- **Apply a single item reward. Skips if inventory full (per plan).** (1 connections) — `server/game/quest/quest_rewards.py`
- **Point the player's respawn at config.room_id (leaving the tutorial ->…** (1 connections) — `server/game/quest/quest_rewards.py`
- **Apply XP, item, spell, and respawn_room rewards. Block item if inventory full…** (1 connections) — `server/game/quest/quest_rewards.py`
- **Return inventory-full error when an item reward needs a free slot.** (1 connections) — `server/game/quest/quest_rewards.py`
- **Grant experience to a player.** (1 connections) — `server/game/quest/quest_rewards.py`
- **Teach a spell granted by a quest.** (1 connections) — `server/game/quest/quest_rewards.py`
- **AsyncPersistenceLayer surface used by the respawn_room reward.** (1 connections) — `server/game/quest/quest_rewards.py`
- **First truthy config value among keys (reward config is untyped JSONB).** (1 connections) — `server/game/quest/quest_rewards.py`
- *... and 5 more nodes in this community*

## Relationships

- [Community 203](Community_203.md) (7 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (6 shared connections)
- [Character Creation & Professions](Character_Creation_&_Professions.md) (6 shared connections)
- [Community 630](Community_630.md) (5 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_rewards.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 62 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*