# Event Schema (Client Event Log)

Event types and their `data` shapes as received over the WebSocket. Used by the event-sourced projector to derive `GameState`.

## Room events

| event_type       | Description                                                  | data shape                                                                                                                   |
| ---------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `game_state`     | Initial state on connect                                     | `{ player, room, occupant_count?, lucidity_tier?, current_lcd?, login_grace_period_active?, login_grace_period_remaining? }` |
| `room_update`    | Room metadata and/or occupants                               | `{ room?, room_data?, occupants?, occupant_count? }` – room may be under `data.room` or top-level                            |
| `room_state`     | Authoritative single source for room (replace, do not merge) | `{ room: full room data, occupants?, occupant_count? }`; `room_id` on event                                                  |
| `room_occupants` | Authoritative occupant list                                  | `{ players?: string[], npcs?: string[], occupants?: string[], count? }`; `room_id` on event                                  |

## Player events

| event_type                                              | Description                 | data shape                                                                                                                                                                      |
| ------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `player_entered_game`                                   | Player entered game         | player identity / room id                                                                                                                                                       |
| `player_entered`                                        | Player entered room         | player name, room                                                                                                                                                               |
| `player_left_game`                                      | Player left game            | —                                                                                                                                                                               |
| `player_left`                                           | Player left room            | —                                                                                                                                                                               |
| `player_died` / `playerdied`                            | Player died                 | `{ current_dp?, death_location? }`; `death_location` is server-composed `Zone › Sub-zone › Room` (#910); sets `isDead: true`, `deathLocation` (null if absent, never `room_id`) |
| `player_respawned` / `playerrespawned`                  | Respawn                     | `{ player?, room?, message? }`; clears `isDead`/`deathLocation`/`isDelirious`/`deliriumLocation`                                                                                |
| `player_delirium_respawned` / `playerdeliriumrespawned` | Delirium respawn            | same as `player_respawned` (same handler)                                                                                                                                       |
| `player_dp_updated` / `playerdpupdated`                 | DP update                   | `{ new_dp, max_dp, posture?, posture_message?, player? }`                                                                                                                       |
| `player_dp_decay`                                       | Mortally wounded bleed tick | `{ posture_message? }` (full bleed line deferred)                                                                                                                               |
| `player_posture_change`                                 | Room posture observer       | `{ message, player_name, position, previous_position? }`                                                                                                                        |
| `player_update`                                         | Full player update          | `{ stats?, posture_message?, in_combat? }`                                                                                                                                      |

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

## Message events

| event_type         | Description    | data shape                 |
| ------------------ | -------------- | -------------------------- |
| `command_response` | Command result | text, channel              |
| `chat_message`     | Chat message   | text, channel, messageType |
| `room_message`     | Room message   | text, channel              |
| `system`           | System message | text, messageType          |

## System events

| event_type                           | Description                 | data shape                                                                                                                                                                                                                                                                                                    |
| ------------------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lucidity_change` / `luciditychange` | Lucidity update             | `{ current_lcd, max_lcd, delta, tier, liabilities?, reason?, source? }`; sets `lucidityStatus` and `player.stats.lucidity` (never `current_dp`)                                                                                                                                                               |
| `rescue_update`                      | Rescue/delirium             | `{ status, role?, message?, current_lcd?, rescuer_name?, target_name?, eta_seconds? }`; `status: 'delirium'` sets `isDelirious`/`deliriumLocation`; `channeling`/`success`/`failed`/`interrupted`/`rescued`/`sanitarium` set `rescueStatus` (`role` defaults to `target`; `eta_seconds` on `channeling` only) |
| `mythos_time_update`                 | Mythos clock (server push)  | `MythosTimePayload` shape; sets `mythosTime`, daypart/holiday flavor messages                                                                                                                                                                                                                                 |
| `game_tick`                          | Heartbeat/tick              | tick_number, mythos_clock?, mythos_datetime?                                                                                                                                                                                                                                                                  |
| `intentional_disconnect`             | Server-initiated disconnect | message?                                                                                                                                                                                                                                                                                                      |

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

| event_type                | Description                               | data shape               |
| ------------------------- | ----------------------------------------- | ------------------------ |
| `client_message`          | Local UI message (error, connection lost) | `{ text, messageType? }` |
| `client_messages_cleared` | User clicked "Clear messages"             | `{}`                     |

## Common event envelope

All events have:

- `event_type: string`
- `timestamp: string` (ISO)
- `sequence_number: number`
- `player_id?: string`
- `room_id?: string`
- `data: Record<string, unknown>`
- `alias_chain?: Array<{ original, expanded, alias_name }>`
