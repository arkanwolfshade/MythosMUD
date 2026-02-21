# Quest System Features: Common MUD Patterns

> Reference document of common quest system features observed across MUDs (Ranvier, Aardwolf,
> MUD Wiki, lysator design guide). Used to decide which features MythosMUD will include and how
> to implement them. Review each feature one-by-one for include/defer and scope.

## Purpose

This document lists common MUD quest features with short descriptions, sources, and implementation
notes. It supports a one-by-one design review: for each feature we decide whether to include it and
how (e.g. data-driven vs code, server vs client, persistence). No implementation is specified
here; decisions from the review will feed a later implementation plan.

---

## Feature 1: Quest goal types

**Description:** Reusable objective types that define what the player must do to advance a quest.
Common types: **Kill** (defeat specific NPCs or counts), **Gather/Collect (Fetch)** (acquire items,
often with a count), **Delivery** (take an item or message to a target), **Escort** (bring an NPC
or entity somewhere), **Combo** (hybrid: e.g. kill then gather). Each goal type has configuration
(e.g. item entity ref + count for Fetch, NPC ref for Kill).

**Where seen:** Ranvier (FetchGoal, KillGoal, etc.), MUD Wiki (Kill, Gather, Delivery, Escort,
Combo), Aardwolf (tasks under goals).

**Implementation note:** Goals are typically implemented as reusable classes or handlers (e.g.
FetchGoal with config `item`, `count`). Server-authoritative; progress is updated when relevant
events occur. Config can live in quest definitions (YAML) so builders add goals without coding.

---

## Feature 2: Quest reward types

**Description:** Reusable reward types granted when a quest is completed. Common types:
**Experience**, **currency**, **loot/items**, **access to areas** (flags or unlocks), **follow-up
quests** (unlock next in chain). Each reward type has configuration (e.g. amount for XP/currency,
item ref for loot).

**Where seen:** Ranvier (ExperienceReward, CurrencyReward, etc.), MUD Wiki (XP, gold, loot, area
access).

**Implementation note:** Rewards are applied server-side on quest completion. Reusable reward
handlers (e.g. static `reward(player, config)`) keep logic out of quest definitions. Config in
YAML (e.g. `type: ExperienceReward`, `config: { amount: 5 }`).

---

## Feature 3: Quest triggers

**Description:** The mechanism that starts a quest. Common triggers: **room entry** (player
enters a specific room), **NPC interaction** (e.g. talk to quest giver), **item acquisition**
(pick up a specific item), **prerequisite quest completion** (finishing one quest unlocks another).
A quest may support one or more trigger types.

**Where seen:** Ranvier (room scripts with `playerEnter`, NPC `quests` array, QuestFactory.canStart
/ create), MUD Wiki (talk to NPC, find item), Aardwolf (goals unlocked by actions).

**Implementation note:** Triggers are evaluated server-side when the relevant event occurs (enter
room, talk to NPC, get item, complete quest). Can be expressed in data (e.g. quest def lists
`trigger: npc_talk` and `trigger_entity_id`) or in small scripts. Room/NPC config references
quest IDs so builders can attach quests without code.

---

## Feature 4: Event-driven progression

**Description:** Quest progress updates in response to in-game events. Examples: **get** / **drop**
for fetch goals, **kill** or death events for kill goals, **give** to NPC for delivery. The server
emits or handles these events; active quests listen and update their internal state (e.g. count
collected, targets killed).

**Where seen:** Ranvier (FetchGoal listens to get/drop, goals subscribe to player events), general
MUD patterns (progress on action).

**Implementation note:** Server maintains active quest state per player. When a relevant command
or event occurs (get, drop, kill, give), a quest manager or goal handler checks active quests and
updates progress. Fully server-authoritative; client only displays state received from server.

---

## Feature 5: Declarative quest config (YAML)

**Description:** Quests are defined in data files (e.g. `quests.yml`) rather than hard-coded.
Typical fields: `id`, `title`, `description`, `goals[]` (each with `type` and `config`),
`rewards[]` (each with `type` and `config`), `requires` (prerequisite quest id), `repeatable`,
`autoComplete` (complete when goals met without explicit turn-in). Builders add or tune quests
without changing code.

**Where seen:** Ranvier (quests.yml, EntityReferences for goals/rewards), Aardwolf (Lua/config
for goals and tasks).

**Implementation note:** Load and validate YAML at startup or on demand; resolve entity refs to
internal IDs. Schema validation (e.g. Pydantic) ensures required fields and valid goal/reward
types. Stored in repo under a designated data path (e.g. `data/quests/`).

---

## Feature 6: Quest givers (questors)

**Description:** NPCs (or optionally rooms/objects) that offer one or more quests. Linkage from
NPC config to quest IDs: e.g. an NPC has a `quests` array listing which quests they offer. When
the player interacts (e.g. talk, "quests" command), the server checks which of those quests
the player can start or turn in.

**Where seen:** Ranvier (npcs.yml `quests` array with EntityReferences), MUD Wiki (NPCs as
quest givers).

**Implementation note:** NPC definition (or room script) holds a list of quest IDs. Server logic
determines offer/turn-in: e.g. "can start" if prerequisites met and not already active/completed
(unless repeatable). No client authority; server decides what is offered based on player state.

---

## Feature 7: Quest log / journal

**Description:** Player-facing way to view active quests, current objectives, progress text, and
optional hints. Implemented as a command (e.g. `quests`, `journal`, `tasklog`) and/or client UI
panel. Shows title, description, list of goals with progress (e.g. "Collect rust-covered sword
(1/1)"), and optionally hints that unlock as the player advances (Aardwolf-style).

**Where seen:** Ranvier (player events questStart, questProgress, questTurnInReady, questComplete
for UI), Aardwolf (tasklog command, hints per task), MUD Wiki (quest tracking).

**Implementation note:** Server stores active quest state and progress; an API or command returns
current quests and progress text. Client renders the list and updates when server sends state
(e.g. via WebSocket game_state or a dedicated quest log response). Hints, if supported, are
stored per player per quest/task and revealed by rules (e.g. after N steps).

---

## Feature 8: Quest chains / prerequisites

**Description:** A quest can require completion of another quest before it can be started (`requires`
or similar). Enables sequential storylines: complete "The Lost Tome" before "The Librarian's
Request" is offered. Prerequisite is checked when evaluating whether to offer or start a quest.

**Where seen:** Ranvier (quests.yml `requires`), MUD Wiki (quest chains for story advancement).

**Implementation note:** Quest definition includes optional `requires: [quest_id_1, ...]`. On
offer/start, server checks player's completed-quest set (or completion count for repeatables).
Simple dependency graph; no need for full DAG evaluation if we only support linear or small
chains initially.

---

## Feature 9: Repeatable quests

**Description:** A quest can be marked as repeatable so the player may accept and complete it
multiple times. Optionally: cooldown between completions, or a cap on completions. Completion
state for repeatables is typically "completed N times" or "last completed at T" rather than
a single "done" flag.

**Where seen:** Ranvier (quests.yml `repeatable: true`), MUD Wiki (repeatable quests).

**Implementation note:** Quest def has `repeatable: true/false`. Persistent player state stores
either completion count or last-completed timestamp. When offering, if repeatable, allow
re-accept after completion (subject to cooldown/cap if implemented). Rewards applied each
completion.

---

## Feature 10: Persistent quest state

**Description:** Per-player save/load of quest state across sessions: which quests are accepted,
in progress, or completed; per-goal progress (e.g. counts); for repeatables, completion count
or cooldown. Ensures progress is not lost on disconnect or logout.

**Where seen:** Ranvier (quest tracker state), Aardwolf (task progress and hints), general MUD
expectation (progress persists).

**Implementation note:** Store in database (e.g. PostgreSQL table or JSON column per player):
active_quests (quest_id, accepted_at, progress blob), completed_quests (quest_id, completed_at,
completion_count if repeatable). Load on login; save on progress change and completion.
Party/quest sync (e.g. for group objectives) is a separate, TBD design; this feature covers
single-player persistence only.

---

## Feature 11: Design principles (from lysator)

**Description:** Player-centric design principles for good quests: **clear hints** (no obscure
puzzles without guidance), **no un-warned death** (fair warning before lethal outcomes),
**winnable without meta-knowledge** (no requiring out-of-game knowledge), **meaningful rewards**
(advance the game or story, not just gold/XP grind). Avoid **syntax quests** (guessing exact
commands) and **boring grind** (repetitive, low-engagement tasks). Applies to how we design
quest content and tooling (e.g. hint system, reward variety).

**Where seen:** lysator.liu.se MUD quest design guide ("How to make good quests").

**Implementation note:** These are content and design guidelines rather than a single technical
feature. They inform quest authoring, quest log (hints), reward types, and difficulty tuning.
Can be captured in a "Quest design guidelines" section in docs or in builder-facing
documentation; optionally enforce some aspects in tooling (e.g. required hint fields for
certain goal types).

---

## Review order

Features are reviewed in the order above (1 through 11). For each feature:

- Decide: **include** (yes), **defer** (later), or **exclude** (no).
- If include: agree on **scope** and **how** (e.g. "goal types: start with Fetch and Kill only;
  config in YAML").

Decisions from this review will be recorded below and used in a follow-up implementation plan.

---

## Review decisions

| #   | Feature                         | Decision (include / defer / exclude) | Scope / how                                                                          |
| --- | ------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------ |
| 1   | Quest goal types                | include                              | Scope 1: complete activity (e.g. exit the tutorial room). Scope 2: kill N targets.   |
| 2   | Quest reward types              | include                              | Scope 1: XP. Scope 2: item. Scope 3: new spell in magic system.                      |
| 3   | Quest triggers                  | include                              | Scope: room + NPC + item.                                                            |
| 4   | Event-driven progression        | include                              | Only events for first two goal types: complete-activity + kill N.                    |
| 5   | Declarative quest config (YAML) | include                              | JSONB in a new database table for now.                                               |
| 6   | Quest givers (questors)         | include                              | NPCs or room data in the database.                                                   |
| 7   | Quest log / journal             | include                              | Command + API only at first.                                                         |
| 8   | Quest chains / prerequisites    | include                              | Linear chains only for now.                                                          |
| 9   | Repeatable quests               | defer                                |                                                                                      |
| 10  | Persistent quest state          | include                              | Quest instances table: FK to characters and quest definitions; holds instance state. |
| 11  | Design principles (lysator)     | include                              | Add to developer documents.                                                          |

---

## Client integration

- **Initial game state:** The WebSocket `game_state` event sent on connect includes a `quest_log`
  array (same shape as the GET quests API). The client can render the Journal from this payload.
- **Refresh:** The client may refresh the quest log via
  `GET /api/players/{player_id}/quests` (authenticated, `player_id` is the active character).
  Use when opening the Journal panel or after quest-related actions if the server does not push an
  updated game_state.

## Related documentation

- **Architecture:** [ADR-010: Quest Subsystem Architecture](architecture/decisions/ADR-010-quest-subsystem.md).
- **Quest design (lysator principles):** [QUEST_DESIGN_GUIDELINES.md](QUEST_DESIGN_GUIDELINES.md).
