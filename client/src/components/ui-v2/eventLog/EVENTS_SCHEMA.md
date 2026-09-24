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

| event_type                                              | Description                 | data shape                                                                                       |
| ------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------ |
| `player_entered_game`                                   | Player entered game         | player identity / room id                                                                        |
| `player_entered`                                        | Player entered room         | player name, room                                                                                |
| `player_left_game`                                      | Player left game            | —                                                                                                |
| `player_left`                                           | Player left room            | —                                                                                                |
| `player_died` / `playerdied`                            | Player died                 | `{ current_dp?, death_location?, room_id? }`; sets `isDead: true`, `deathLocation`               |
| `player_respawned` / `playerrespawned`                  | Respawn                     | `{ player?, room?, message? }`; clears `isDead`/`deathLocation`/`isDelirious`/`deliriumLocation` |
| `player_delirium_respawned` / `playerdeliriumrespawned` | Delirium respawn            | same as `player_respawned` (same handler)                                                        |
| `player_dp_updated` / `playerdpupdated`                 | DP update                   | `{ new_dp, max_dp, posture?, posture_message?, player? }`                                        |
| `player_dp_decay`                                       | Mortally wounded bleed tick | `{ posture_message? }` (full bleed line deferred)                                                |
| `player_posture_change`                                 | Room posture observer       | `{ message, player_name, position, previous_position? }`                                         |
| `player_update`                                         | Full player update          | `{ stats?, posture_message?, in_combat? }`                                                       |

## Combat events

| event_type                  | Description      | data shape                         |
| --------------------------- | ---------------- | ---------------------------------- |
| `npc_attacked`              | NPC attacked     | combat target, damage              |
| `player_attacked`           | Player attacked  | combat target, damage              |
| `combat_started`            | Combat started   | participants                       |
| `combat_ended`              | Combat ended     | outcome                            |
| `npc_died` / `combat_death` | NPC/combat death | target, room                       |
| `combat_target_switch`      | NPC aggro switch | message, npc_name, new_target_name |

## Message events

| event_type         | Description    | data shape                 |
| ------------------ | -------------- | -------------------------- |
| `command_response` | Command result | text, channel              |
| `chat_message`     | Chat message   | text, channel, messageType |
| `room_message`     | Room message   | text, channel              |
| `system`           | System message | text, messageType          |

## System events

| event_type                           | Description                 | data shape                                                                                                                                      |
| ------------------------------------ | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `lucidity_change` / `luciditychange` | Lucidity update             | `{ current_lcd, max_lcd, delta, tier, liabilities?, reason?, source? }`; sets `lucidityStatus` and `player.stats.lucidity` (never `current_dp`) |
| `rescue_update`                      | Rescue/delirium             | `{ status, message?, current_lcd? }`; `status: 'delirium'` sets `isDelirious`/`deliriumLocation`                                                |
| `mythos_time_update`                 | Mythos clock (server push)  | `MythosTimePayload` shape; sets `mythosTime`, daypart/holiday flavor messages                                                                   |
| `game_tick`                          | Heartbeat/tick              | tick_number, mythos_clock?, mythos_datetime?                                                                                                    |
| `intentional_disconnect`             | Server-initiated disconnect | message?                                                                                                                                        |

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
