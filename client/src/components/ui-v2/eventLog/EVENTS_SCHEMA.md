# Event Schema (Client Event Log)

Event types and their `data` shapes as received over the WebSocket. Used by the event-sourced projector to derive `GameState`.

## Room events

| event_type       | Description                                                  | data shape                                                                                          |
| ---------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| `game_state`     | Initial state on connect                                     | `{ player, room, occupants?: string[], login_grace_period_active?, login_grace_period_remaining? }` |
| `room_update`    | Room metadata and/or occupants                               | `{ room?, room_data?, occupants?, occupant_count? }` – room may be under `data.room` or top-level   |
| `room_state`     | Authoritative single source for room (replace, do not merge) | `{ room: full room data, occupants?, occupant_count? }`; `room_id` on event                         |
| `room_occupants` | Authoritative occupant list                                  | `{ players?: string[], npcs?: string[], occupants?: string[], count? }`; `room_id` on event         |

## Player events

| event_type                                              | Description         | data shape                |
| ------------------------------------------------------- | ------------------- | ------------------------- |
| `player_entered_game`                                   | Player entered game | player identity / room id |
| `player_entered`                                        | Player entered room | player name, room         |
| `player_left_game`                                      | Player left game    | —                         |
| `player_left`                                           | Player left room    | —                         |
| `player_died` / `playerdied`                            | Player died         | death details             |
| `player_respawned` / `playerrespawned`                  | Respawn             | —                         |
| `player_delirium_respawned` / `playerdeliriumrespawned` | Delirium respawn    | —                         |
| `player_dp_updated` / `playerdpupdated`                 | DP update           | stats                     |
| `player_update`                                         | Full player update  | player object             |

## Combat events

| event_type                  | Description      | data shape            |
| --------------------------- | ---------------- | --------------------- |
| `npc_attacked`              | NPC attacked     | combat target, damage |
| `player_attacked`           | Player attacked  | combat target, damage |
| `combat_started`            | Combat started   | participants          |
| `combat_ended`              | Combat ended     | outcome               |
| `npc_died` / `combat_death` | NPC/combat death | target, room          |

## Message events

| event_type         | Description    | data shape                 |
| ------------------ | -------------- | -------------------------- |
| `command_response` | Command result | text, channel              |
| `chat_message`     | Chat message   | text, channel, messageType |
| `room_message`     | Room message   | text, channel              |
| `system`           | System message | text, messageType          |

## System events

| event_type                           | Description                 | data shape                                   |
| ------------------------------------ | --------------------------- | -------------------------------------------- |
| `lucidity_change` / `luciditychange` | Lucidity update             | current_dp, max_dp, etc.                     |
| `rescue_update`                      | Rescue/delirium             | status, message                              |
| `mythos_time_update`                 | Mythos clock                | mythos_clock, mythos_datetime, daypart, etc. |
| `game_tick`                          | Heartbeat/tick              | tick_number, mythos_clock?, mythos_datetime? |
| `intentional_disconnect`             | Server-initiated disconnect | message?                                     |

## Common event envelope

All events have:

- `event_type: string`
- `timestamp: string` (ISO)
- `sequence_number: number`
- `player_id?: string`
- `room_id?: string`
- `data: Record<string, unknown>`
- `alias_chain?: Array<{ original, expanded, alias_name }>`
