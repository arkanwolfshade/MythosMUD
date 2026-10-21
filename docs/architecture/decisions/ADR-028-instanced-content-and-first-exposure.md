# ADR-028: Instanced Content Mechanics and the First Exposure Tutorial

**Version 1.0.0** · MythosMUD · 2026-10-16

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Proposed
**Date:** 2026-10-16
**Builds on:** ADR-009 (instanced rooms), ADR-024 (server-authoritative perceived reality)
**Supersedes:** the one-room Patient Bedroom tutorial described in ADR-009

## 2. Context

**[NOTE]**
The current tutorial is a single instanced room that teaches nothing about the three systems every character will
meet: DP loss, corruption, and lucidity. The design brief (vault: "first exposure to the Mythos"; "all new players
start with corruption 1") calls for a multi-room tutorial that ends in lucidity collapse and a Sanitarium respawn.

Exploration found that `InstanceManager` already clones N template rooms and remaps exits, but the surrounding
systems assume a single room and a shared world:

- NPCs, containers and floor items are never created inside instances, and instance teardown does not remove them.
- `no_death` caps damage at 0 DP, which leaves the player mortally wounded and bleeding out to death.
- Delirium, sanitarium and death respawns never clear `tutorial_instance_id` or flush the instance.
- Reconnect always resets to the first room, and the start room is whichever room the cache returns first.
- Nothing can gate an exit on an item, run an action from a dialogue node, or drain lucidity over time.

## 3. Decision

**[SPEC]**
Tutorial needs are met by **generic, data-driven mechanics** that later instanced content can reuse. There are no
tutorial-only special cases in Python.

| Mechanic | Data surface | Purpose |
| --- | --- | --- |
| `instance_start` room attribute | room attributes | Explicit start room; replaces cache-order `get_first_room_id`. |
| `instance_npcs` room attribute | room attributes | NPCs owned by the instance; spawned on create, despawned on flush, never respawned. |
| Instance containers and items | furniture / item seeds | Template-room containers and floor items are cloned into instances and destroyed on flush. |
| `instance_bound` item flag | item prototype | Stacks dropped in an instance are destroyed on flush, never forwarded to the bank. |
| `exit_requirements` room attribute | room attributes | `{dir: {item?, quest_activity?, refusal}}`; every named condition must hold. `item` is a prototype held anywhere on the player; `quest_activity` is a `complete_activity` target done in any of the player's quests (`cmd_look`, or `dialogue_complete_<npc>` fired by a dialogue node's `quest_activity` action). Enforced in `MovementService` (flee and follow too), message in `go`; malformed data, or no quest reader wired, leaves the exit open. |
| Dialogue node `actions` | dialogue tree JSON | Run scripted actions (heal, corruption floor, quest, effect, narrate, debrief). |
| Container `on_put` | furniture metadata | Run scripted actions when a matching item is put in a container. |
| `lucidity_drain_over_time` effect | status-effect dict | Per-second escalating drain, tier narration, scripted hallucination beats, self-removes at -10. |
| `disengage_at_target_dp_ratio` | NPC `behavior_config` | A hostile NPC ends combat and despawns when its target falls to a DP ratio. |
| `cmd_<name>` quest goals | quest goal config | Quest progress from commands (`look`, `talk`, `read`, `map`) for in-instance players. |

One scripted-action runner (`server/game/scripted_actions.py`) serves dialogue actions and `on_put`.

World-wide engine fixes that ship with it:

1. `no_death` floors damage at 1 DP, not 0.
2. Fights started by an aggressive NPC apply first-encounter lucidity shock.
3. All delirium and sanitarium respawns land in a new second-floor Sanitarium **Recovery Ward** wing. Death
   respawns are unchanged.
4. Dr. Morgan performs the debrief through dialogue, resolving #872. The bare `debrief` command stays unregistered.

The tutorial itself (**First Exposure**, 12 template rooms, template id changes from `tutorial_sanitarium`) is
content on top of these mechanics:

- Acts: Dusk (Independence Square), Burying Ground (hostile ghoul, friendly ghoul, jade amulet), Below (gated
  stair, ghoul warrens, coffin vault).
- Ending: `put amulet in coffin` starts the Hound's Scent. Lucidity falls to -10 in about 90 seconds, delirium
  fires, and the player wakes in the Recovery Ward at lucidity 70, full DP, corruption at least 1, without the amulet.
- The tutorial has no external exits; the delirium ending is the only way out.
- Corruption is raised to at least 1 by the healer ghoul and is never added twice. Replay, restart and skip are idempotent.
- Ending, skip and restart all call one function, `apply_first_exposure_end_state()`.
- Skip at character creation is allowed only when another character on the account completed the new tutorial, and
  the server verifies it.

## 4. Alternatives Considered

**[NOTE]**

- **Hardcoded tutorial script/event handler**: Rejected. Fastest, but gives later instanced content nothing and
  special-cases one NPC and room in Python.
- **Bedroom kept as epilogue or framing device**: Rejected. It fakes the respawn, or opens on a non-mundane room.
- **Ambient room corruption flux to reach corruption 1**: Rejected. The gain is invisible and timing-dependent.
- **Room-by-room scripted lucidity shocks**: Rejected. They stall if the player stops and cannot guarantee landing
  past -10 without skipping catatonia.
- **Hound of Tindalos, Nyarlathotep avatar, Shub-Niggurath as the entity**: Rejected. Lovecraft's "The Hound"
  (1924, public domain) ties directly to ghouls; Dark Young are Chaosium's and not allowlisted; Mordiggian is
  Clark Ashton Smith's and not allowlisted.
- **Checkpoint resume after disconnect**: Rejected. Every checkpoint needs a state-reconstruction path.

## 5. Consequences

**[SPEC]**

- **Positive**: instanced dungeons and group content get gated exits, owned NPCs, containers, dialogue actions and
  drain effects with no new code; #872 is resolved game-wide; the `no_death` bleed-out hole is closed everywhere.
- **Negative**: aggressive NPCs now cost lucidity on first contact (world balance change); delirium and sanitarium
  respawn location changes for all players; ADR-009's "exit via Main Foyer" is superseded for the tutorial.
- **Neutral**: no corruption backfill; only characters created after release start at corruption 1. A character
  mid-old-tutorial at deploy moves into the new tutorial on reconnect.

## 6. Open Items

**[?]**

- Second-floor map placement (no `map_z`; offset 2D coordinates assumed).
- Whether `rescue_update(delirium)` is re-sent on connect when lucidity is at or below -10 (page refresh during
  the interstitial); verify in `websocket_initial_state.py`.

## 7. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-10-16 | Initial proposal |
