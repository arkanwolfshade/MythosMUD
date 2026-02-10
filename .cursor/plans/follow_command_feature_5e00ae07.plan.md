---
name: Follow Command Feature
overview: Implement the /follow, /unfollow, and /following commands with player-to-player (acceptance required, client prompt), player-to-NPC and NPC-to-player (automatic). In-memory follow state; follower moves when target moves; auto-unfollow on failed move; mute/block auto-decline. No persistence across reboots.
todos:
  - id: from-room-id-event
    content: Add from_room_id to Room.player_entered() and pass it in PlayerEnteredRoom; have MovementService pass from_room.id in _execute_room_transfer
    status: completed
  - id: connection-manager-send-to-player
    content: Add or confirm ConnectionManager method to send a WebSocket event to a single player by player_id (for follow_request)
    status: completed
  - id: follow-service
    content: Create FollowService (server/game/follow_service.py) with in-memory state, request_follow/accept/decline/unfollow, get_followers/get_following/get_following_display, mute check, 60s pending-request expiry with requestor notification, and EventBus subscription for PlayerEnteredRoom/NPCEnteredRoom to propagate movement and auto-unfollow on failure
    status: completed
  - id: wire-follow-service
    content: Register FollowService in app container; inject EventBus, MovementService, UserManager, ConnectionManager; subscribe to disconnect to clear follow state and pending requests
    status: completed
  - id: command-parser-follow
    content: Add follow, unfollow, following to CommandType and command factories (command_parser.py, command_factories.py) so command_data has correct command_type and args
    status: completed
  - id: follow-commands-handlers
    content: Create server/commands/follow_commands.py with handle_follow_command, handle_unfollow_command, handle_following_command (same-room resolve, no self-follow, call FollowService)
    status: completed
  - id: command-service-register
    content: Register follow, unfollow, following handlers in command_service.py command_handlers dict
    status: completed
  - id: follow-response-handler
    content: Add FollowResponseMessageHandler and handle_follow_response_message; register follow_response in message_handler_factory.py
    status: completed
  - id: client-follow-request-ui
    content: "Client: handle follow_request event in event pipeline; add modal/banner with Accept/Decline that sends follow_response WebSocket message"
    status: completed
  - id: unit-tests-follow-service
    content: Unit tests for FollowService (mute auto-decline, accept/decline, unfollow, movement propagation, auto-unfollow on move failure)
    status: completed
  - id: unit-tests-follow-commands
    content: Unit tests for follow commands (follow self rejected, follow player/NPC same room, unfollow, following output)
    status: completed
  - id: integration-tests-follow
    content: "Integration test: A requests follow B, B accepts, B moves then A moves; B moves through restricted exit and A is auto-unfollowed"
    status: completed
  - id: follow-display-title-panel
    content: "Display who/what the player is following in the game UI title panel (header); server sends following in game_state and follow_state event"
    status: completed
  - id: follow-auto-stand
    content: "When follower is sitting or prone and target moves: try to auto-stand then move; if cannot stand, unfollow and notify"
    status: completed
isProject: false
---

# Follow / Unfollow / Following Feature Plan

## Requirements summary

- **Follow**: Player can follow a player (same room) or an NPC (same room). Cannot follow self.
- **Player following player**: Target must accept via client prompt "[Accept] [Decline]". If target has muted/blocked the requestor, request is auto-declined (no prompt).
- **Player following NPC / NPC following player**: Automatic (no acceptance).
- **Movement**: When the followed entity moves, each follower attempts the same move (same `from_room_id` -> `to_room_id`). If the move fails (e.g. restricted exit), the follower is auto-unfollowed.
- **Unfollow**: `/unfollow` clears the current follow target.
- **Following**: `/following` shows who you are following and who is following you.
- **State**: In-memory only; does not persist across server reboots.

---

## Architecture

```mermaid
sequenceDiagram
  participant ClientA as Client A (requestor)
  participant Server as Server
  participant FollowSvc as FollowService
  participant UserMgr as UserManager
  participant ClientB as Client B (target)
  participant MovSvc as MovementService

  ClientA->>Server: command "follow Bob"
  Server->>FollowSvc: request_follow(A_id, B_id)
  FollowSvc->>UserMgr: is_player_muted_async(B_id, A_id)
  alt Muted
    FollowSvc-->>ClientA: "They are not accepting follow requests."
  else Not muted
    FollowSvc->>FollowSvc: Store pending request
    FollowSvc->>ClientB: send event "follow_request" (request_id, requestor_name)
    ClientB->>ClientB: Show prompt "X wants to follow you. [Accept] [Decline]"
    ClientB->>Server: follow_response { request_id, accept: true }
    Server->>FollowSvc: accept_follow(B_id, request_id)
    FollowSvc->>FollowSvc: Add A -> B to follow map
    FollowSvc-->>ClientA: "You are now following Bob."
    FollowSvc-->>ClientB: "Alice is now following you."
  end

  Note over ClientB,MovSvc: When B moves (go north)
  MovSvc->>MovSvc: move_player(B, from_room, to_room)
  MovSvc->>Room: to_room.player_entered(B, from_room_id=from_room.id)
  Room->>Room: Publish PlayerEnteredRoom(player_id=B, room_id=to_room, from_room_id=from_room)
  FollowSvc->>FollowSvc: On PlayerEnteredRoom: get_followers(B) -> [A]
  FollowSvc->>MovSvc: move_player(A, from_room, to_room)
  alt Success
    MovSvc-->>FollowSvc: True
  else Failure
    MovSvc-->>FollowSvc: False
    FollowSvc->>FollowSvc: unfollow(A); notify A "You lost your target."
  end
```

---

## 1. Server: FollowService (in-memory)

- **New module**: e.g. `server/game/follow_service.py` (or `server/services/follow_service.py`).
- **State** (all in-memory, no DB):
  - `_follow_target: dict[player_id_str, tuple[target_id_str, target_type: "player"|"npc"]]` — who each player is following.
  - `_pending_requests: dict[request_id_str, { requestor_id, requestor_name, target_id, created_at }]` — pending player-to-player follow requests.
  - **Request TTL**: Pending requests expire after 60s; on expiry remove the request and send the requestor a message ("Your follow request has expired."). On disconnect, cancel pending requests where target or requestor disconnected.
- **API**:
  - `request_follow(requestor_id, target_identifier)` — target_identifier is name or id. Resolve to player or NPC in same room. If player: check mute (UserManager); if muted, return error; else create pending request, send `follow_request` event to target’s connection. If NPC: add follow immediately.
  - `accept_follow(target_id, request_id)`, `decline_follow(target_id, request_id)` — complete or cancel pending request; notify both sides.
  - `unfollow(follower_id)` — remove follower’s target; clear pending if any for that follower.
  - `get_followers(target_id)` — return list of follower ids (for movement propagation).
  - `get_following(follower_id)` — return (target_id, target_type) or None.
  - `get_following_display(follower_id)` — for `/following`: who I follow; and `get_followers(my_id)` for who follows me (names resolved for display).
- **Movement propagation**: Subscribe to `PlayerEnteredRoom` and `NPCEnteredRoom`. For each event, get followers of `player_id` / `npc_id`. For each follower (must be a player), call `movement_service.move_player(follower_id, from_room_id, to_room_id)`. If move returns False, call `unfollow(follower_id)` and send the follower a message (e.g. "You lost your target and are no longer following.").
- **Dependency injection**: FollowService needs: EventBus (subscribe), MovementService (move followers), UserManager (mute check), a way to send a WebSocket event to a single player (e.g. ConnectionManager method to send to one player by id). Register FollowService in the app container and inject these dependencies.

---

## 2. PlayerEnteredRoom: include from_room_id

- **Event**: `PlayerEnteredRoom` already has `from_room_id: str | None = None` in [server/events/event_types.py](server/events/event_types.py).
- **Room**: In [server/models/room.py](server/models/room.py), extend `player_entered(self, player_id, force_event=False, from_room_id=None)` and pass `from_room_id` into `PlayerEnteredRoom(player_id=..., room_id=self.id, from_room_id=from_room_id)`.
- **MovementService**: In [server/game/movement_service.py](server/game/movement_service.py), in `_execute_room_transfer`, call `to_room.player_entered(resolved_player_id, force_event=True, from_room_id=from_room.id)` so the event carries the source room for follow propagation.

---

## 3. Commands: follow, unfollow, following

- **Command registration**: In [server/commands/command_service.py](server/commands/command_service.py), add handlers to `command_handlers`: `"follow": handle_follow_command`, `"unfollow": handle_unfollow_command`, `"following": handle_following_command`.
- **Parser / factories**: Ensure the command parser and command factories recognize `follow`, `unfollow`, `following` (e.g. add `CommandType` values and factory methods in [server/utils/command_parser.py](server/utils/command_parser.py) and [server/utils/command_factories.py](server/utils/command_factories.py)) so that `command_data` includes the right `command_type` and args (e.g. target name for `follow`).
- **Handlers** (new file or in a dedicated commands module, e.g. `server/commands/follow_commands.py`):
  - **follow**: Parse target (name or id). Same-room check; cannot follow self. If target is player: call `FollowService.request_follow(current_player_id, target_identifier)` (result message or error). If target is NPC: resolve NPC in room, call a method that adds follow immediately and returns message.
  - **unfollow**: Call `FollowService.unfollow(current_player_id)`; return "You are no longer following anyone." or "You weren't following anyone."
  - **following**: Call `FollowService.get_following_display(current_player_id)` and return formatted lines (who you follow; who follows you).

---

## 4. Mute check for player follow requests

- In `FollowService.request_follow`, when target is a player: before creating a pending request, call `user_manager.is_player_muted_async(target_id, requestor_id)`. If True, do not create a request and do not send a prompt; return a single message to the requestor (e.g. "They are not accepting follow requests."). **Mute is sufficient for "not accepting follow requests"**; no separate block concept for now.

---

## 5. WebSocket: follow_request event and follow_response message

- **Sending follow_request to target**: When a pending follow request is created, the server must send an event to the target player only. Use the existing ConnectionManager (or equivalent) to send a JSON event to one connection by `player_id` (e.g. `send_to_player(player_id, build_event("follow_request", { "request_id": ..., "requestor_name": ..., "requestor_id": ... }))`). If no such API exists, add it.
- **Client**: On receiving an event with `event_type === "follow_request"` and payload `request_id`, `requestor_name` (and optionally `requestor_id`), show a small modal or inline prompt: "&lt;requestor_name&gt; wants to follow you." with [Accept] and [Decline] buttons.
- **Client → Server**: On Accept or Decline, send a WebSocket message: `{ type: "follow_response", data: { request_id: "<id>", accept: true | false } }`.
- **Server**: Register a handler for message type `follow_response` in [server/realtime/message_handler_factory.py](server/realtime/message_handler_factory.py) (e.g. `FollowResponseMessageHandler`). In the handler, call `FollowService.accept_follow(player_id, data["request_id"])` or `decline_follow(player_id, data["request_id"])`, and send appropriate feedback to the current player and, for accept, to the requestor (either via the same connection or by sending a targeted event to the requestor).

---

## 6. Client prompt and event handling

- **Event handling**: In the client’s event pipeline (e.g. [client/src/components/ui-v2/eventLog/projector.ts](client/src/components/ui-v2/eventLog/projector.ts) or a dedicated handler), handle `follow_request` events: store or pass the request (request_id, requestor_name) into a small UI component that shows the prompt.
- **UI**: A modal or banner with the message and Accept/Decline buttons. On click, send the `follow_response` WebSocket message as above. Optionally dismiss the prompt on send or when a subsequent event confirms the outcome.
- **State**: Prefer minimal state (e.g. one pending follow request per client); if a second request arrives before the first is answered, either replace or queue per product preference (replace is simpler).

---

## 7. NPC movement and NPC follow targets

- **NPCEnteredRoom**: Already has `from_room_id` in [server/events/event_types.py](server/events/event_types.py). FollowService subscribes to `NPCEnteredRoom`; for each follower of `event.npc_id`, call `movement_service.move_player(follower_id, event.from_room_id, event.room_id)`; on failure, unfollow and notify.
- **Resolving NPC for follow**: When the user types `follow &lt;name&gt;`, resolve to a player in the same room first; if none, resolve to an NPC in the same room (using existing room/lifecycle or NPC listing). If NPC, add follow in FollowService (in-memory map: follower_id -> (npc_id, "npc")) and return success message.

---

## 8. Cleanup and edge cases

- **Disconnect**: On player disconnect, remove them from follow state (they are no longer following anyone; remove them from anyone’s follower list). Cancel any pending request where they are requestor or target.
- **Request timeout**: Pending follow requests expire after **60 seconds**. When a request expires, remove it and **notify the requestor** (e.g. "Your follow request has expired."). Implement via periodic cleanup or TTL check when processing.
- **Single follow target**: One follow target per player (standard); one pending request per target (or per requestor) to avoid duplicate prompts.

---

## 9. Files to add or touch (summary)

| Area                                                                     | Action                                                                                                       |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `server/game/follow_service.py` (or `server/services/follow_service.py`) | New: FollowService with in-memory state, EventBus subscription, MovementService and UserManager integration. |
| `server/commands/follow_commands.py`                                     | New: `handle_follow_command`, `handle_unfollow_command`, `handle_following_command`.                         |
| `server/commands/command_service.py`                                     | Register follow, unfollow, following handlers.                                                               |
| `server/utils/command_parser.py` / `command_factories.py`                | Add follow, unfollow, following command types and parsing.                                                   |
| `server/models/room.py`                                                  | Add `from_room_id` to `player_entered()`.                                                                    |
| `server/game/movement_service.py`                                        | Pass `from_room_id` into `player_entered()`.                                                                 |
| `server/realtime/message_handler_factory.py`                             | Register `follow_response` handler.                                                                          |
| `server/realtime/message_handlers.py` (or new)                           | Implement follow_response handling (accept/decline).                                                         |
| ConnectionManager (or equivalent)                                        | Ensure or add ability to send an event to a single player by id (for follow_request).                        |
| App container / lifespan                                                 | Wire FollowService (EventBus, MovementService, UserManager, connection manager).                             |
| Client: event handling                                                   | Handle `follow_request` and show prompt.                                                                     |
| Client: UI component                                                     | Modal or banner with Accept/Decline; send `follow_response`.                                                 |
| Client: WebSocket send                                                   | Send `follow_response` message when user clicks Accept/Decline.                                              |

---

## 10. Testing (high level)

- Unit: FollowService (request_follow with mute, accept/decline, unfollow, get_followers/get_following, movement propagation and auto-unfollow on move failure).
- Unit: Follow commands (follow self rejected, follow same-room player/NPC, unfollow, following output).
- Integration: Player A requests follow player B; B receives event; B accepts → A follows B; B moves → A moves; B logs out → A fails and is unfollowed.
- Optional: Client E2E for follow_request prompt and follow_response send.

---

## Decisions (confirmed)

- **Request timeout**: Pending follow requests expire after **60 seconds**. The requestor is **notified** when their request expires (e.g. "Your follow request has expired.").
- **Mute vs block**: **Mute is sufficient** for "not accepting follow requests"; no separate block concept for this feature.

---

## Additional requirements (recorded)

### 1. Display following in game UI title panel

- **Requirement**: Since players can only follow one target at a time, display who/what they are following in the game UI title panel (header).
- **Implementation**: Server includes `following` in `game_state` (and/or sends a `follow_state` event when follow is established or cleared). Client stores `followingTarget?: { target_name: string; target_type: "player" | "npc" } | null` and HeaderBar shows e.g. "Following: &lt;name&gt;" when set.

### 2. Auto-stand when following and target moves

- **Requirement**: If the follower is sitting or prone and their target moves, the system should try to automatically stand the follower and then move. If the follower is unable to stand, they should stop following the target.
- **Implementation**: In FollowService movement propagation (`_on_player_entered_room`, `_on_npc_entered_room`), before calling `movement_service.move_player(follower_id, ...)`: load follower's player, read `stats.position`; if not standing (sitting or lying), call position service to change to standing; if stand fails, unfollow and notify the follower; otherwise proceed with move. FollowService needs `async_persistence` and `PlayerPositionService` (or equivalent) injected.
