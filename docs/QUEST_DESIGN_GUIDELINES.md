# Quest Design Guidelines

> Player-centric principles for authoring MythosMUD quests. Informed by common MUD practice and
> the lysator.liu.se quest design guide ("How to make good quests"). Use these when creating or
> reviewing quest content and when extending the quest system.

## Purpose

These guidelines help authors and reviewers design quests that are fair, discoverable, and
rewarding. They are content and design principles, not enforced by code; tooling or review
checklists may reference them.

---

## Core Principles (Lysator-Inspired)

### 1. Clear hints

- Avoid obscure puzzles with no in-world guidance. Provide enough information (description,
  NPC dialogue, or environmental clues) so a player can reason toward the solution.
- If a quest requires a specific action or target, make that target identifiable (e.g. named
  NPC, clear room or object description).

### 2. No un-warned death

- Do not use quest outcomes that kill or permanently harm the character without fair warning
  (e.g. narrative or mechanical telegraph). Lethal content should be optional or clearly
  signposted.

### 3. Winnable without meta-knowledge

- Quests should be completable using only information available in the game (or clearly
  documented in-game). Avoid requiring out-of-game knowledge (e.g. real-world trivia or
  undocumented command syntax).

### 4. Meaningful rewards

- Rewards should advance the player’s experience or the story (XP, items, spells, or
  narrative payoff). Avoid pure grind (repetitive tasks with no meaningful progression or
  payoff).

### 5. Avoid syntax quests

- Do not design quests that depend on guessing exact command phrasing. Prefer triggers and
  goals that align with natural player actions (entering a room, talking to an NPC, using
  an item, defeating a foe).

### 6. Avoid boring grind

- Minimize repetitive, low-engagement tasks. Prefer variety in objectives and pacing;
  if repetition is used (e.g. “kill N”), keep N reasonable and mix with other goal types
  where possible.

---

## Practical Guidelines for MythosMUD

### Triggers and offers

- **Room triggers**: Use when the story is tied to a place (e.g. “leave the tutorial” when
  entering the tutorial bedroom). Ensure the room id in `quest_offers` and in the definition
  trigger match.
- **NPC triggers**: Use for quest givers; link the quest in `quest_offers` (offer_entity_type
  `npc`, offer_entity_id the NPC definition id). Player must be able to encounter that NPC.
- **Item triggers**: Use when picking up a specific item should start the quest; wire to
  item acquisition events.

### Goals

- **complete_activity**: Use for one-off actions (e.g. exit a room, use an object). Set
  `target` to a stable identifier (e.g. `exit_<room_id>` for “exit this room”).
- **kill_n**: Use for “defeat N of X” (e.g. NPC definition id). Set `target` or config
  `npc_id` and `count` as appropriate. Avoid very high counts unless part of a deliberate
  design.

### Prerequisites

- Use `requires_all` for linear chains (must complete A before B). Use `requires_any` for
  “one of these” gates. Keep chains short and understandable.

### Rewards

- **XP**: Use for steady progression; amounts should feel meaningful relative to level.
- **Item**: Ensure the item exists and inventory has capacity (or document that full
  inventory may skip the reward).
- **Spell**: Use for quest lines that teach magic; spell must exist in the spell system.

### Descriptions and titles

- **Title**: Short, in-world name (e.g. “Leave the tutorial”).
- **Description**: One or two sentences explaining what the player is asked to do and why
  (if relevant). Avoid spoilers for puzzles; do give enough context to start.

---

## References

- [QUEST_SYSTEM_FEATURES.md](QUEST_SYSTEM_FEATURES.md) — Feature list and review decisions.
- [ADR-010: Quest Subsystem Architecture](architecture/decisions/ADR-010-quest-subsystem.md) —
  Technical architecture for the quest system.
- lysator.liu.se MUD quest design guide (external) — “How to make good quests.”
