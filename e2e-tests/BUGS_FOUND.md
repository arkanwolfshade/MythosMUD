# Bugs Found During Multiplayer E2E Testing

## Bug #1: Mute Command Server Error

**Scenario**: scenario-04-muting-system-emotes.md
**Status**: FIXED
**Severity**: HIGH
**Date Found**: 2026-01-16
**Date Fixed**: 2026-01-16

### Description

The `mute` command fails with a server-side error: `'State' object has no attribute 'user_manager'`

### Fix Applied

Services (`user_manager` and `player_service`) are now set on `app.state` during initialization in
`initialize_container_and_legacy_services()` and also ensured in `websocket_handler.py` when processing commands. This
ensures command handlers can access these services via `app.state.user_manager` and `app.state.player_service`.

### Error Message

```
Error processing CommandType.MUTE command: 'State' object has no attribute 'user_manager'
```

### Steps to Reproduce

1. Log in as ArkanWolfshade (AW)
2. Log in as Ithaqua in a separate tab
3. Both players are in the same room (Main Foyer)
4. AW attempts to mute Ithaqua: `mute Ithaqua`
5. Server error occurs

### Expected Behavior

AW should successfully mute Ithaqua and receive confirmation: "You have muted Ithaqua permanently."

### Actual Behavior

Server error occurs, mute command fails, no confirmation message is displayed.

### Impact

Scenario 4 cannot be completed

- Mute functionality is completely broken
- Users cannot mute other players

### Notes

Error occurs on the server side, not in the client

- The `State` object appears to be missing the `user_manager` attribute
- This is a backend implementation issue

---

## Bug #2: Chat Messages Not Displayed to Sender

**Scenario**: scenario-05-chat-messages.md
**Status**: FIXED
**Severity**: MEDIUM
**Date Found**: 2026-01-16
**Date Fixed**: 2026-01-16

### Description

When Ithaqua sends a chat message, AW does not see it in the chat panel. However, Ithaqua can see AW's messages.

### Root Cause

Player ID format mismatch between `room_subscriptions` (uses string IDs) and `online_players` dict (uses UUID objects as
keys). When filtering target players for message broadcasting, `get_player_room_from_online_players` was looking up
player IDs as strings, but the dict keys are UUID objects, causing lookups to fail and players to be filtered out
incorrectly.

### Fix Applied

Modified `get_player_room_from_online_players` in `server/realtime/message_filtering.py` to normalize player ID strings
to UUID objects before looking them up in the `online_players` dict. This ensures that player IDs from
`room_subscriptions` (strings) can be correctly found in `online_players` (UUID keys).

### Steps to Reproduce

1. Log in as ArkanWolfshade (AW) in tab 0

2. Log in as Ithaqua in tab 1

3. Both players are in the same room (Main Foyer)

4. AW sends: `say Hello Ithaqua`

   ✅ AW sees: "You say: Hello Ithaqua"

   ✅ Ithaqua sees: "ArkanWolfshade says: Hello Ithaqua"

5. Ithaqua sends: `say Greetings ArkanWolfshade`

   ✅ Ithaqua sees: "You say: Greetings ArkanWolfshade"

   ❌ AW does NOT see: "Ithaqua says: Greetings ArkanWolfshade"

### Expected Behavior

AW should see Ithaqua's reply message: "Ithaqua says: Greetings ArkanWolfshade"

### Actual Behavior

AW's chat panel only shows their own message. Ithaqua's reply is not displayed to AW.

### Impact

One-way communication issue

- AW cannot see messages from Ithaqua
- Bidirectional chat verification fails in Scenario 5

### Notes

Messages are being sent successfully (Ithaqua sees their own confirmation)

- Messages are being received by Ithaqua (Ithaqua saw AW's message)
- The issue appears to be with message display/filtering on AW's side
- Could be a client-side filtering issue or a server-side message routing problem
- Ithaqua's chat panel correctly shows both messages

### Potential Causes

1. Client-side message filtering (self-message filtering may be too aggressive)
2. Server-side message routing issue (messages not being broadcast to all players in room)
3. Channel/panel configuration issue (messages going to wrong panel)

---

## Bug #3: Teleport Command Server Error

**Scenario**: scenario-06-admin-teleportation.md
**Status**: FIXED
**Severity**: HIGH
**Date Found**: 2026-01-16
**Date Fixed**: 2026-01-16

### Description

The `teleport` command fails with a server-side error: `'State' object has no attribute 'player_service'`

### Fix Applied

Same fix as Bug #1 - services are now set on `app.state` during initialization and when processing WebSocket commands.
The `player_service` is now available to teleport command handlers.

### Error Message

```
Error processing teleport command: 'State' object has no attribute 'player_service'
```

### Steps to Reproduce

1. Log in as ArkanWolfshade (AW)
2. Log in as Ithaqua in a separate tab
3. Both players are in the same room (Main Foyer)
4. AW attempts to teleport Ithaqua: `teleport Ithaqua east`
5. Server error occurs

### Expected Behavior

AW should successfully teleport Ithaqua to the east room and receive confirmation: "You teleport Ithaqua to the east"

### Actual Behavior

Server error occurs, teleport command fails, no confirmation message is displayed.

### Impact

Scenario 6 cannot be completed

- Admin teleportation functionality is completely broken
- Admin users cannot teleport other players

### Notes

Error occurs on the server side, not in the client

- The `State` object appears to be missing the `player_service` attribute
- This is a backend implementation issue, similar to Bug #1
- Pattern suggests a systemic issue with the `State` object missing required service attributes

---

## Test Execution Summary

**Scenarios Completed**: 3/11

✅ Scenario 1: Basic Connection

✅ Scenario 2: Clean Game State

✅ Scenario 3: Movement Between Rooms

**Scenarios Blocked/Partial**: 3/11

❌ Scenario 4: Muting System (BLOCKED - Bug #1)

- ⚠️ Scenario 5: Chat Messages (PARTIAL - Bug #2)
- ❌ Scenario 6: Admin Teleportation (BLOCKED - Bug #3)

**Scenarios Completed (Additional)**: 2/11

✅ Scenario 7: Who Command (mostly working - who command functions correctly)

- ⚠️ Scenario 8: Local Channel Basic (PARTIAL - same issue as Bug #2: AW doesn't see Ithaqua's local messages)

**Scenarios Remaining**: 3/11

- Scenario 9: Local Channel Isolation (pending - likely affected by Bug #2)
- Scenario 10: Local Channel Movement (pending - likely affected by Bug #2)
- Scenario 11: Local Channel Errors (pending - may work independently)

### Additional Note

Bug #2 (chat messages not displayed to AW) also affects local channel messages. AW cannot see Ithaqua's local channel
messages, confirming this is a systemic one-way communication issue affecting both `say` and `local` channels. This
suggests a player-specific filtering or routing issue on AW's side.

### Pattern Analysis

**Bugs #1 & #3**: Both involve missing service attributes on the `State` object (`user_manager`, `player_service`). This
indicates a systemic backend initialization issue where command handlers are not receiving properly initialized State
objects.

**Bug #2**: Affects message display for AW specifically. Ithaqua can see all messages (both say and local) from AW,
  but AW cannot see messages from Ithaqua. This suggests a player-specific issue, possibly related to:

- Client-side message filtering (self-message filtering too aggressive)
- Server-side message routing (messages not being sent to AW's connection)
- Player ID or connection state issue specific to AW's session
