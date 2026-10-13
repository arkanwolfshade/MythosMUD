# Event Schema (Client Event Log)

Event types and their `data` shapes as received over the WebSocket. Used by the event-sourced projector to derive `GameState`.

## Room events

| event_type       | Description                                                  | data shape                                                                                                                   |
| ---------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `game_state`     | Initial state on connect                                     | `{ player, room, occupant_count?, lucidity_tier?, current_lcd?, login_grace_period_active?, login_grace_period_remaining? }` |
| `room_update`    | Room metadata and/or occupants                               | `{ room?, room_data?, occupants?, occupant_count? }` – room may be under `data.room` or top-level                            |
| `room_state`     | Authoritative single source for room (replace, do not merge) | `{ room: full room data, occupants?, occupant_count? }`; `room_id` on event                                                  |
| `room_occupants` | Authoritative occupant list                                  | `{ players?: string[], npcs?: NpcOccupant[], occupants?: string[], count? }`; `room_id` on event (see "NPC occupants")       |

## Player events

| event_type                                              | Description                 | data shape                                                                                                                                                                      |
| ------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `player_entered_game`                                   | Player entered game         | player identity / room id                                                                                                                                                       |
| `player_entered`                                        | Player entered room         | player name, room                                                                                                                                                               |
| `player_left_game`                                      | Player left game            | —                                                                                                                                                                               |
| `player_left`                                           | Player left room            | —                                                                                                                                                                               |
| `player_died` / `playerdied`                            | Player died                 | `{ current_dp?, death_location? }`; `death_location` is server-composed `Zone › Sub-zone › Room` (#910); sets `isDead: true`, `deathLocation` (null if absent, never `room_id`) |
| `player_respawned` / `playerrespawned`                  | Respawn                     | `{ player?, room?, message?, category }`; clears `isDead`/`deathLocation`/`isDelirious`/`deliriumLocation`                                                                      |
| `player_delirium_respawned` / `playerdeliriumrespawned` | Delirium respawn            | same as `player_respawned` (same handler)                                                                                                                                       |
| `player_dp_updated` / `playerdpupdated`                 | DP update                   | `{ new_dp, max_dp, posture?, posture_message?, player?, category? }`; `category` accompanies `posture_message`                                                                  |
| `player_dp_decay`                                       | Mortally wounded bleed tick | `{ posture_message?, category? }` (full bleed line deferred); `category` is `status.health`                                                                                     |
| `player_posture_change`                                 | Room posture observer       | `{ message, player_name, position, previous_position?, category }`                                                                                                              |
| `player_update`                                         | Full player update          | `{ stats?, posture_message?, category?, in_combat? }`; `category` accompanies `posture_message`                                                                                 |

## Combat events

| event_type                  | Description           | data shape                         |
| --------------------------- | --------------------- | ---------------------------------- |
| `npc_attacked`              | NPC attacked          | combat target, damage              |
| `player_attacked`           | Player attacked       | combat target, damage              |
| `combat_started`            | Combat started        | participants                       |
| `combat_ended`              | Combat ended          | outcome                            |
| `npc_died` / `combat_death` | NPC/combat death      | target, room                       |
| `combat_target_switch`      | NPC aggro switch      | message, npc_name, new_target_name |
| `combat_participant_joined` | Player joined a fight | message, player_name, npc_name     |
| `combat_taunt`              | Taunt resolved        | message                            |
| `combat_protect`            | Protect resolved      | message                            |

Each carries `category` (`combat.hit` / `combat.hurt` / `combat.status` / `combat.death`); `combat_attack` carries a
per-recipient `categories` map instead (see Message categories below).

## Message events

| event_type         | Description    | data shape                       |
| ------------------ | -------------- | -------------------------------- |
| `command_response` | Command result | `{ result, category, channel? }` |
| `chat_message`     | Chat message   | `{ message, channel, category }` |
| `room_message`     | Room message   | `{ message, category }`          |
| `system`           | System message | `{ message, category }`          |

Every event that puts text in the log also carries `data.category` (next section).

## Message categories

The server tags each line of player-visible text with a semantic `data.category` (`domain.kind`, for example
`chat.whisper` or `combat.hurt`). The client styles and routes the line from the category and never guesses meaning
from the text.

- **Source of truth:** `server/constants/message_category.py` (`MessageCategory`). `client/src/types/messageCategory.ts`
  mirrors it by hand; `server/tests/unit/constants/test_message_category.py` fails if the two drift.
- **Reserved namespaces** (no values yet): `lore.*`, `item.*`, `command.misfire`.
- **`npc.*` is a disposition tag, not a line's own category** (#1025): `npc.shopkeeper`, `npc.quest_giver`,
  `npc.passive_mob`, `npc.aggressive_mob`. Each is the `NPCDefinitionType` value word for word
  (`server/constants/npc_disposition.py`). See "NPC occupants" below.
- **Missing or unknown category:** the client reads every `data.category` through one validating helper
  (`readCategory` in `projectorMessageUtils.ts`). A missing or unknown value falls back to `command.output`, with one
  development-only warning per event type, so a server omission is visible rather than silently mis-styled.
- **Wire shape:** `data.category` is a string. `combat_attack` is the one exception: its recipients see different
  lines, so it carries `data.categories`, a map keyed exactly like `data.messages`
  (`attack_attacker` / `attack_defender` / `attack_other`), each value a category from that recipient's perspective.
- **`channel` is separate:** on `chat.*` events it names the conversation, not the meaning.
- **Where it is set:** only in shared builders and chokepoints, never per handler and never by hallucination code
  (ADR-024: a hallucinated line gets the category of the real thing it imitates by using the same builder). Command
  handlers put no `category` in successful results; `websocket_handler_commands.py` defaults it to
  `command.output`, and `build_event` does the same for any `command_response` that names none. Usage,
  permission, and system failures are the exception: they return `system.error` via `command_error`.
- **Posture self-lines** (`posture_message` on `player_update`, `player_dp_updated`, `player_dp_decay`) are tagged by
  `attach_posture_self_message` in `server/realtime/posture_notify.py`: `room.movement`, except the DP-decay collapse
  line, which is `status.health`.
- **Client-authored lines:** `client_message` carries its own `data.category` (`buildLocalMessageEvent` defaults it to
  `system.info`). Time and tick notices and `player_entered_game` / `player_left_game` get a fixed category per event
  type in `projectorHandlersMessages.ts` / `projectorHandlersState.ts`.
- **Invariant:** `server/tests/unit/realtime/test_message_category_invariants.py` drives every text emitter and checks
  the category, and cross-checks the list against the projector handlers above.

## NPC occupants

Wherever a payload lists a room's NPCs (`npcs` in `game_state.room`, `room_update`, `room_state`, `room_occupants`,
`player_respawned`) each entry is
`NpcOccupant = { name: string, disposition: 'shopkeeper' | 'quest_giver' | 'passive_mob' | 'aggressive_mob' }`.

- The flat `occupants` list stays `string[]` of names (players, then NPCs).
- **Server is authoritative.** `disposition` comes from the live NPC instance. A missing or unrecognised type is sent as
  `passive_mob` (with a server warning) so one bad definition row cannot empty a room's occupant list.
- **Phantom hostiles are always `aggressive_mob`** (ADR-024): every phantom, whatever its tier, carries the tag a real
  hostile does.
- **Client validation** is one function, `normalizeNpcOccupants` (`utils/npcOccupants.ts`): it keeps entries with a
  string `name`, falls back to `passive_mob` for an unknown `disposition`, and drops anything else (a bare string can
  only mean a bug now; it is not upgraded).
- **Styling:** the Occupants panel renders each NPC with the `npc.<disposition>` category classes, so colour, glyph and
  the "Text labels" word all come from the same CSS as message categories. Two NPCs with the same name stay separate
  rows.

## Segments (styled names inside a line)

A text event may carry `segments: { text: string, category?: string }[]` next to its `message` (#1025). The spans' `text`
values concatenate to exactly `message`; a span with no `category` takes the line's own. Today only NPC names are
styled, with `category: 'npc.<disposition>'`.

- **`message` is never replaced.** Search, history, `data-message-text` and screen readers all read it, so a client may
  drop `segments` and lose colour, never words.
- **Server builds them by construction** (`server/constants/message_segments.py`, `message_with_segments`), and
  `test_message_category_invariants.py` checks the join for every emitter that attaches `segments`.
- **Where the server sends them:** `room_message` (NPC enters, leaves or moves, and the default appear/leave lines;
  authored `behavior_config` text has no name placeholder and stays plain), `npc_died` / `combat_death` ("The X has been
  slain."), the combat status lines `combat_target_switch`, `combat_participant_joined` and `combat_taunt`, the
  `command_response` of `look` (the whole result text, with the "Also here: ..." names styled) and of the attack
  command ("You attack X!"), and `chat_message` lines
  from an NPC speaker (`speaker_disposition`) and system narration whose content names a phantom (the spans inside the
  content are framed by the channel prefix, e.g. the `[SYSTEM]` tag and the space after it).
- **Client-composed combat lines** (`npc_attacked`, `npc_took_damage`, `player_attacked`) are worded in the client, so the
  server sends the NPC's disposition instead: `npc_disposition` on the first two, `attacker_disposition` on
  `player_attacked` (present only when the attacker is an NPC). The client builds the spans from it.
- **Client validation** is `validateSegments` (`utils/messageSegments.ts`), reached through `buildChatMessage`: it drops
  all spans unless every span is well formed and the texts join to `message`; an unknown span category renders as plain
  text. HTML lines never carry segments.
- **Rendering:** `SegmentedText` gives an `npc.*` span the classes `seg seg-npc-<disposition>`: colour and weight only,
  with no glyph or Text-labels word (those stay on the line). Corruption decay (#804) runs on the whole line first; if it
  changes the line, the decayed plain text is shown and the segments are dropped.
- **Chat lines and dampening.** The speaker's name sits outside the content, so it stays styled when dampening rewrites
  the words; spans inside the content are kept only while the content is untouched, and otherwise dropped for that
  receiver. A hallucinated fake-NPC whisper carries no disposition (there is no real NPC to take one from).
- **Not segmented:** real NPC whispers do not exist yet (#1034). The phantom dissipation text is only logged (the
  server never sends it to a player), and protect lines name only players.

## System events

| event_type                           | Description                 | data shape                                                                                                                                                                                                                                                                                                    |
| ------------------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lucidity_change` / `luciditychange` | Lucidity update             | `{ current_lcd, max_lcd, delta, tier, liabilities?, reason?, source? }`; sets `lucidityStatus` and `player.stats.lucidity` (never `current_dp`)                                                                                                                                                               |
| `rescue_update`                      | Rescue/delirium             | `{ status, role?, message?, current_lcd?, rescuer_name?, target_name?, eta_seconds? }`; `status: 'delirium'` sets `isDelirious`/`deliriumLocation`; `channeling`/`success`/`failed`/`interrupted`/`rescued`/`sanitarium` set `rescueStatus` (`role` defaults to `target`; `eta_seconds` on `channeling` only) |
| `mythos_time_update`                 | Mythos clock (server push)  | `MythosTimePayload` shape; sets `mythosTime`, daypart/holiday flavor messages                                                                                                                                                                                                                                 |
| `game_tick`                          | Heartbeat/tick              | tick_number, mythos_clock?, mythos_datetime?                                                                                                                                                                                                                                                                  |
| `intentional_disconnect`             | Server-initiated disconnect | `{ message?, category }`                                                                                                                                                                                                                                                                                      |
| `shutdown_notification`              | Shutdown countdown mark     | `{ message, seconds_remaining, channel, category }`; `category` is `system.warning`; rendered like `system` (#1028)                                                                                                                                                                                           |
| `shutdown_cancelled`                 | Shutdown cancelled          | `{ message, channel, category }`; `category` is `system.info`; rendered like `system` (#1028)                                                                                                                                                                                                                 |
| `system_broadcast`                   | Admin broadcast             | `{ message, broadcaster, broadcaster_id, category }`; `category` is `system.info`; rendered like `system` (#1028)                                                                                                                                                                                             |

## Container / inventory events (#711)

See `server/services/container_websocket_events.py` and `server/services/inventory_websocket_events.py`.
Handled in `eventLog/projectorHandlersContainers.ts`.

| event_type          | Description                                                                  | data shape                                                                                                                                                                                                          |
| ------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `container.opened`  | Container opened. Personal copy carries `mutation_token`; room copy doesn't  | `{ container: ContainerSnapshot, owner_id?, mutation_token?, expires_at?, actor_id? }`; only the personal copy (has `mutation_token`) creates an `openContainers` entry -- see `.cursor/rules/server-authority.mdc` |
| `container.updated` | Full container snapshot after a transfer/loot-all                            | `{ container_id, container: ContainerSnapshot, actor_id }`; applied only if `container_id` is already in `openContainers` (stale `sequence_number` rejected)                                                        |
| `container.closed`  | Container session closed                                                     | `{ container_id }`; removes the `openContainers` entry if present                                                                                                                                                   |
| `container.created` | A new container appeared in the room (e.g. a corpse spawned)                 | `{ container: ContainerSnapshot }`; adds a `roomContainers` summary                                                                                                                                                 |
| `container.decayed` | A corpse container decayed and was cleaned up                                | `{ container_id, room_id }`; removes from both `openContainers` and `roomContainers`                                                                                                                                |
| `inventory_updated` | Player's inventory/equipped changed (pickup, drop, equip, unequip, get, put) | `{ inventory: InventoryStack[], equipped: Record<string, InventoryStack> }`; personal only                                                                                                                          |

Note: `container.updated` and `container.closed` share the same payload shape whether delivered
personally to the actor or broadcast to the room; the projector distinguishes them structurally by
only ever applying them to a `container_id` already present in `openContainers`, which -- because
container sessions are exclusive (server-side, #711) -- is only ever the actor's own entry.

## Local (client-only) events

Never sent by the server -- the `client_` prefix marks them as local. See
`eventLog/projectorMessageUtils.ts` (`buildLocalMessageEvent`/`buildLocalClearMessagesEvent`) and
`.cursor/rules/server-authority.mdc`.

| event_type                | Description                               | data shape            |
| ------------------------- | ----------------------------------------- | --------------------- |
| `client_message`          | Local UI message (error, connection lost) | `{ text, category? }` |
| `client_messages_cleared` | User clicked "Clear messages"             | `{}`                  |

## Common event envelope

All events have:

- `event_type: string`
- `timestamp: string` (ISO)
- `sequence_number: number`
- `player_id?: string`
- `room_id?: string`
- `data: Record<string, unknown>`
- `alias_chain?: Array<{ original, expanded, alias_name }>`
