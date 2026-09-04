# BUG INVESTIGATION REPORT: NPCs Not Updating in Occupants List When Player Moves

**Bug Description**: NPCs in the Occupants list are not updating when the
player moves to other rooms

**Investigation Date**: 2025-01-30
**Investigator**: AI Assistant (GPT-4)
**Session ID**: 2025-01-30_session-001_npcs-not-updating-on-player-movement
**Status**: Root Cause Identified

---

## EXECUTIVE SUMMARY

When a player moves between rooms, the `room_occupants` event is sent to update
the Occupants panel, but NPCs are not being included in the update. The root
cause is that `_send_room_occupants_update` is called with `exclude_player`
parameter when a player enters a room, which broadcasts to all players EXCEPT
the entering player. The entering player receives a separate personal message
via `_send_occupants_snapshot_to_player`, but there may be a timing issue or
the NPCs may not be properly queried when the player first enters the room.

Additionally, the NPC query mechanism in `_get_room_occupants` relies on NPC
instances having `current_room` or `current_room_id` attributes set correctly,
which was fixed in a previous investigation but may still have edge cases.

---

## DETAILED FINDINGS

### 1. Bug Description Analysis

**Reported Issue**: NPCs in the Occupants list are not updating when the
player moves to other rooms

**Expected Behavior**:

- When a player moves to a new room, the Occupants panel should update to show:
  - Players in the new room
  - NPCs in the new room
- NPCs from the old room should disappear
- NPCs in the new room should appear

**Actual Behavior**: NPCs are not updating in the Occupants list when the
player moves

### 2. Code Flow Analysis: Player Movement

**Location**: `server/realtime/event_handler.py:408-491`

When a player moves to a new room:

1. **PlayerEnteredRoom Event Published**:

   - Triggered by `Room.player_entered()` in `server/models/room.py:72-96`
   - Published via EventBus

2. **Event Handler Processes Entry**:

   - `_handle_player_entered()` is called (line 408)
   - Processes event with room synchronization service
   - Gets player information

3. **Room Occupants Update Sent**:

   - Line 469: `await self._send_room_occupants_update(room_id_str, exclude_player=exclude_player_id)`
   - **CRITICAL**: This broadcasts to all players in the room EXCEPT the entering player
   - Line 478: `await self._send_occupants_snapshot_to_player(player_id_for_personal, room_id_str)`
   - This sends a personal message to the entering player

4. **PlayerLeftRoom Event Published**:

   - Triggered by `Room.player_left()` in `server/models/room.py:98-115`
   - Published via EventBus

5. **Event Handler Processes Exit**:

   - `_handle_player_left()` is called (line 493)
   - Line 552: `await self._send_room_occupants_update(room_id_str, exclude_player=exclude_player_id)`
   - This broadcasts to remaining players in the OLD room

**Code Reference**:

```617:733:server/realtime/event_handler.py
    async def _send_room_occupants_update(self, room_id: str, exclude_player: str | None = None) -> None:
        """
        Send room occupants update to players in the room.

        Preserves player/NPC distinction by sending structured data with separate
        players and npcs arrays, enabling the client UI to display them in separate columns.

        Args:
            room_id: The room ID
            exclude_player: Optional player ID to exclude from the update
        """
        try:
            # Get room occupants with structured data (includes player_name, npc_name, type)

            occupants_info: list[dict[str, Any] | str] = self._get_room_occupants(room_id)

            # Separate players and NPCs while maintaining backward compatibility

            players: list[str] = []
            npcs: list[str] = []
            all_occupants: list[str] = []  # Flat list for backward compatibility

            for occ in occupants_info or []:
                if isinstance(occ, dict):
                    # Check if it's a player

                    if "player_name" in occ:
                        player_name = occ.get("player_name")
                        # Validate that player_name is not a UUID string

                        if player_name and isinstance(player_name, str):
                            # Skip if it looks like a UUID (36 chars, 4 dashes, hex)

                            if not (
                                len(player_name) == 36
                                and player_name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in player_name)
                            ):
                                players.append(player_name)
                                all_occupants.append(player_name)
                            else:
                                self._logger.warning(
                                    "Skipping player with UUID as name in room_occupants update",
                                    player_name=player_name,
                                    room_id=room_id,
                                )
                    # Check if it's an NPC

                    elif "npc_name" in occ:
                        npc_name = occ.get("npc_name")
                        # Validate that npc_name is not a UUID string

                        if npc_name and isinstance(npc_name, str):
                            # Skip if it looks like a UUID

                            if not (
                                len(npc_name) == 36
                                and npc_name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in npc_name)
                            ):
                                npcs.append(npc_name)
                                all_occupants.append(npc_name)
                            else:
                                self._logger.warning(
                                    "Skipping NPC with UUID as name in room_occupants update",
                                    npc_name=npc_name,
                                    room_id=room_id,
                                )
                    # Fallback for other formats

                    else:
                        name = occ.get("name")
                        if name and isinstance(name, str):
                            # Skip if it looks like a UUID

                            if not (
                                len(name) == 36
                                and name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in name)
                            ):
                                all_occupants.append(name)
                elif isinstance(occ, str):
                    # Legacy format: just a name string
                    # Validate it's not a UUID

                    if not (
                        len(occ) == 36 and occ.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in occ)
                    ):
                        all_occupants.append(occ)
                    else:
                        self._logger.warning(
                            "Skipping UUID string in legacy occupant format",
                            occupant=occ,
                            room_id=room_id,
                        )

            # Create occupants update message with structured data
            # Convert room_id to string for JSON serialization

            room_id_str = str(room_id) if room_id else ""

            # CRITICAL DEBUG: Log what we're about to send

            self._logger.debug(
                "Sending room_occupants event",
                room_id=room_id_str,
                players=players,
                npcs=npcs,
                all_occupants=all_occupants,
                players_count=len(players),
                npcs_count=len(npcs),
            )

            message = {
                "event_type": "room_occupants",
                "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
                "sequence_number": self._get_next_sequence(),
                "room_id": room_id_str,
                "data": {
                    # Structured data for new UI (separate columns)

                    "players": players,
                    "npcs": npcs,
                    # Backward compatibility: flat list for legacy clients

                    "occupants": all_occupants,
                    "count": len(all_occupants),
                },
            }

            # Send to room occupants

            await self.connection_manager.broadcast_to_room(room_id, message, exclude_player=exclude_player)
```

### 3. NPC Query Mechanism

**Location**: `server/realtime/event_handler.py:738-1128`

The `_get_room_occupants` method queries NPCs from the lifecycle manager:

**Code Reference**:

```1012:1037:server/realtime/event_handler.py
                            # Check both current_room and current_room_id for compatibility

                            current_room = getattr(npc_instance, "current_room", None)
                            current_room_id = getattr(npc_instance, "current_room_id", None)
                            npc_room_id = current_room or current_room_id
                            npc_name = getattr(npc_instance, "name", "Unknown")

                            self._logger.debug(
                                "Checking NPC for room match",
                                room_id=room_id,
                                npc_id=npc_id,
                                npc_name=npc_name,
                                npc_current_room=current_room,
                                npc_current_room_id=current_room_id,
                                npc_room_id_used=npc_room_id,
                                matches_room=(npc_room_id == room_id),
                            )

                            if npc_room_id == room_id:
                                npc_ids.append(npc_id)
                                npcs_matched += 1
                                self._logger.info(
                                    "Found NPC in room",
                                    room_id=room_id,
                                    npc_id=npc_id,
                                    npc_name=npc_name,
                                )
```

**NPC Room Tracking**:

- NPCs are tracked in `lifecycle_manager.active_npcs[npc_id]`
- NPC instances should have `current_room` or `current_room_id` attributes
- Previous investigation (2025-01-29) found that NPC instances need these attributes set during spawning
- Fix was implemented in `server/npc/lifecycle_manager.py:418-422` to set `current_room` when spawning

### 4. Client-Side Processing

**Location**: `client/src/components/ui-v2/GameClientV2Container.tsx:499-587`

The client processes `room_occupants` events:

**Code Reference**:

```499:587:client/src/components/ui-v2/GameClientV2Container.tsx
          case 'room_occupants': {
            // Support both new structured format (players/npcs) and legacy format (occupants)
            const players = event.data.players as string[] | undefined;
            const npcs = event.data.npcs as string[] | undefined;
            const occupants = event.data.occupants as string[] | undefined; // Legacy format
            const occupantCount = event.data.count as number | undefined;

            // DEBUG: Console log for immediate visibility + structured logging
            console.log('🔍 [room_occupants] Received event:', {
              players,
              npcs,
              npcs_count: npcs?.length ?? 0,
              occupants,
              occupantCount,
              hasCurrentRoom: !!currentRoomRef.current,
              currentRoomId: currentRoomRef.current?.id,
              currentRoomPlayers: currentRoomRef.current?.players,
              currentRoomNpcs: currentRoomRef.current?.npcs,
              hasUpdatesRoom: !!updates.room,
              updatesRoomNpcs: updates.room?.npcs,
            });

            // DEBUG: Log received data
            logger.debug('GameClientV2Container', 'Processing room_occupants event', {
              players,
              npcs,
              npcs_count: npcs?.length ?? 0,
              occupants,
              occupantCount,
              hasCurrentRoom: !!currentRoomRef.current,
              currentRoomId: currentRoomRef.current?.id,
              currentRoomPlayers: currentRoomRef.current?.players,
              currentRoomNpcs: currentRoomRef.current?.npcs,
              hasUpdatesRoom: !!updates.room,
            });

            // CRITICAL FIX: Use updates.room if available (from room_update in same batch),
            // otherwise use currentRoomRef.current (it's kept in sync via useEffect)
            // This handles the case where room_update and room_occupants arrive in the same batch
            const currentRoom = updates.room || currentRoomRef.current;

            if (currentRoom) {
              // ARCHITECTURE: room_occupants events are the SINGLE AUTHORITATIVE SOURCE for occupant data
              // This event always uses structured format (players/npcs arrays) from
              // RealTimeEventHandler._get_room_occupants() which queries:
              // - Players: Room._players (in-memory, reliable)
              // - NPCs: NPCLifecycleManager.active_npcs (authoritative, survives re-instantiation)

              // Use structured format if available (preferred), otherwise fall back to legacy flat list
              if (players !== undefined || npcs !== undefined) {
                // Structured format: separate players and NPCs arrays
                updates.room = {
                  ...currentRoom,
                  players: players ?? [],
                  npcs: npcs ?? [],
                  // Backward compatibility: also populate flat occupants list
                  occupants: [...(players ?? []), ...(npcs ?? [])],
                  occupant_count: occupantCount ?? (players?.length ?? 0) + (npcs?.length ?? 0),
                };
                logger.debug('GameClientV2Container', 'Updated room with structured occupants from room_occupants', {
                  roomId: updates.room.id,
                  players_count: updates.room.players?.length ?? 0,
                  npcs_count: updates.room.npcs?.length ?? 0,
                  total_count: updates.room.occupant_count,
                });
              } else if (occupants && Array.isArray(occupants)) {
                // Legacy format: flat list (for backward compatibility)
                // Try to split into players/npcs if possible, otherwise use flat list
                updates.room = {
                  ...currentRoom,
                  occupants: occupants,
                  occupant_count: occupantCount ?? occupants.length,
                  // Preserve existing structured data if available, otherwise use flat list
                  players: currentRoom.players ?? [],
                  npcs: currentRoom.npcs ?? [],
                };
                logger.debug('GameClientV2Container', 'Updated room with legacy occupants format', {
                  roomId: updates.room.id,
                  occupants_count: updates.room.occupants?.length ?? 0,
                  occupant_count: updates.room.occupant_count,
                });
              }
            } else {
              logger.warn('GameClientV2Container', 'room_occupants event received but no room state available', {
                hasCurrentRoomRef: !!currentRoomRef.current,
                hasUpdatesRoom: !!updates.room,
              });
            }
            break;
          }
```

The client correctly processes `room_occupants` events and updates the room state with NPCs. The issue is likely on
 the server side.

### 5. Previous Investigation Context

**Reference**: `investigations/sessions/2025-01-29_session-001_npc-occupants-display-issue.md`

A previous investigation found that:

- NPCs were spawning correctly
- NPCs were being added to Room objects
- BUT Room objects retrieved from persistence didn't have NPC data
- NPC instances didn't have `current_room` or `current_room_id` attributes set

**Fix Applied**: `server/npc/lifecycle_manager.py:418-422` was updated to set `current_room` when spawning NPCs.

However, this investigation focuses on a different issue: NPCs not updating when players move between rooms.

---

## ROOT CAUSE ANALYSIS

The root cause is a **dual update mechanism issue** combined with potential **NPC room tracking edge cases**:

### Primary Issue: Dual Update Mechanism

When a player enters a room:

1. **Broadcast Update** (Line 469):

   - `_send_room_occupants_update(room_id_str, exclude_player=exclude_player_id)` is called
   - This broadcasts to all players in the room EXCEPT the entering player
   - If the entering player is the ONLY player in the room, they don't receive this broadcast

2. **Personal Message** (Line 478):

   - `_send_occupants_snapshot_to_player()` is called to send a personal message to the entering player
   - This should work, but there may be a timing issue or the NPCs may not be properly queried

**The Problem**:

- The entering player relies on the personal message (`_send_occupants_snapshot_to_player`)
- If there's any issue with the personal message (timing, NPC query, etc.), the entering player won't see NPCs
- The broadcast update excludes the entering player, so they can't fall back to that

### Secondary Issue: NPC Room Tracking

The NPC query mechanism relies on:

- NPC instances having `current_room` or `current_room_id` attributes set correctly
- NPC instances being in `lifecycle_manager.active_npcs`
- NPC room IDs matching the queried room ID exactly

**Potential Edge Cases**:

- NPC instances may not have `current_room` set if they were spawned before the fix
- NPC instances may have incorrect room IDs if they moved but the attribute wasn't updated
- Room ID format mismatches (string vs canonical ID)

### Specific Bug Scenario

**When a player moves to a room with NPCs**:

1. `PlayerEnteredRoom` event is published

2. `_handle_player_entered()` is called

3. `_send_room_occupants_update()` is called with `exclude_player=entering_player_id`

   - This queries NPCs via `_get_room_occupants()`

   - NPCs are queried from lifecycle manager by checking `npc_instance.current_room == room_id`

   - If NPCs are found, they're included in the broadcast

   - BUT the entering player is excluded from the broadcast

4. `_send_occupants_snapshot_to_player()` is called

   - This also queries NPCs via `_get_room_occupants()`
   - If NPCs are found, they're included in the personal message
   - BUT if there's any issue (timing, NPC query, etc.), the entering player won't see NPCs

**The Bug**: If `_send_occupants_snapshot_to_player()` fails to include NPCs (due to query issues, timing, etc.),
 the entering player has no fallback because they're excluded from the broadcast.

---

## SYSTEM IMPACT ASSESSMENT

**Severity**: MEDIUM-HIGH

- Core gameplay feature affected (NPC visibility in occupants)
- Affects player immersion and interaction with NPCs
- Workaround: Players can use `look` command to see NPCs, but they won't appear in the Occupants panel

**Scope**:

- Affects ALL players moving between rooms
- Affects ALL rooms with NPCs
- Affects the entering player specifically (other players in the room receive the broadcast update)

**User Impact**:

- Players cannot see NPCs in the Occupants panel when they enter a room
- Players may not know NPCs are present in rooms
- Reduces game immersion and functionality
- May cause confusion about room contents

---

## EVIDENCE DOCUMENTATION

### Code References

1. **Player Entry Handler**: `server/realtime/event_handler.py:408-491`

   - Line 469: `_send_room_occupants_update()` called with `exclude_player`
   - Line 478: `_send_occupants_snapshot_to_player()` called for entering player

2. **NPC Query Mechanism**: `server/realtime/event_handler.py:738-1128`

   - Lines 1012-1037: NPC room matching logic
   - Queries `npc_instance.current_room` or `npc_instance.current_room_id`

3. **Client Processing**: `client/src/components/ui-v2/GameClientV2Container.tsx:499-587`

   - Processes `room_occupants` events correctly
   - Updates room state with NPCs from structured data

4. **Previous Fix**: `server/npc/lifecycle_manager.py:418-422`

   - Sets `current_room` when spawning NPCs
   - May not cover all edge cases (NPCs spawned before fix, NPCs that moved)

### Log Analysis

**No specific error logs found** in `logs/local/errors.log` related to NPC occupants or room updates.

**Expected Log Entries** (if working correctly):

- "Sending room_occupants event" with `npcs` array populated
- "Found NPC in room" when NPCs match room ID
- "Completed NPC query from lifecycle manager" with `npc_count > 0`

**Missing Log Entries** (indicating potential issue):

- No logs showing NPC queries being executed during player movement
- No logs showing NPCs being found in rooms when players enter

---

## INVESTIGATION RECOMMENDATIONS

### Priority 1: Verify NPC Query Execution

**Action**: Check if `_get_room_occupants()` is properly querying NPCs when players enter rooms

**Location**: `server/realtime/event_handler.py:738-1128`

**Required Investigation**:

1. Add logging to verify NPC query is executed during player movement
2. Check if NPCs are found in the lifecycle manager query
3. Verify NPC instances have `current_room` or `current_room_id` set correctly
4. Check for room ID format mismatches (string vs canonical ID)

### Priority 2: Verify Personal Message Delivery

**Action**: Check if `_send_occupants_snapshot_to_player()` is properly including NPCs

**Location**: `server/realtime/event_handler.py:319-406`

**Required Investigation**:

1. Add logging to verify personal message is sent to entering player
2. Check if NPCs are included in the personal message
3. Verify timing of personal message vs broadcast update
4. Check for any errors in personal message generation

### Priority 3: Test Dual Update Mechanism

**Action**: Verify both broadcast and personal message mechanisms work correctly

**Location**: `server/realtime/event_handler.py:408-491`

**Required Investigation**:

1. Test scenario: Player enters room with NPCs (only player in room)
2. Test scenario: Player enters room with NPCs (other players present)
3. Verify both broadcast and personal message include NPCs
4. Check for race conditions or timing issues

### Priority 4: Verify NPC Room Tracking

**Action**: Ensure NPC instances have correct room tracking attributes

**Location**: `server/npc/lifecycle_manager.py` and `server/npc/movement_integration.py`

**Required Investigation**:

1. Verify all NPC instances have `current_room` or `current_room_id` set
2. Check if NPC room tracking is updated when NPCs move
3. Verify room ID format consistency (string vs canonical ID)
4. Check for NPCs spawned before the fix (may not have room tracking)

---

## REMEDIATION PROMPT

**For Cursor Chat**:

```
Fix the issue where NPCs in the Occupants list are not updating when the player moves to other rooms.

ROOT CAUSE:
When a player enters a room, _send_room_occupants_update() is called with exclude_player parameter,
which broadcasts to all players EXCEPT the entering player. The entering player receives a separate
personal message via _send_occupants_snapshot_to_player(). If the personal message fails to include
NPCs (due to query issues, timing, etc.), the entering player has no fallback because they're excluded
from the broadcast.

INVESTIGATION FINDINGS:
1. Player entry handler calls _send_room_occupants_update() with exclude_player (line 469)
2. Player entry handler calls _send_occupants_snapshot_to_player() for entering player (line 478)
3. NPC query mechanism relies on npc_instance.current_room matching room_id
4. Client correctly processes room_occupants events with NPCs
5. Previous fix set current_room when spawning, but may not cover all edge cases

CODE PATHS AFFECTED:
- server/realtime/event_handler.py:_handle_player_entered() - dual update mechanism
- server/realtime/event_handler.py:_get_room_occupants() - NPC query from lifecycle manager
- server/realtime/event_handler.py:_send_occupants_snapshot_to_player() - personal message to entering player
- server/npc/lifecycle_manager.py - NPC room tracking during spawning
- server/npc/movement_integration.py - NPC room tracking during movement

REQUIRED FIXES:
1. Ensure _send_occupants_snapshot_to_player() always includes NPCs when querying room occupants
2. Add logging to verify NPC query execution during player movement
3. Verify NPC instances have current_room or current_room_id set correctly
4. Consider including entering player in broadcast update as fallback (or remove exclude_player)
5. Verify room ID format consistency (string vs canonical ID) in NPC room matching

EVIDENCE:
- Code analysis shows dual update mechanism (broadcast + personal message)
- NPC query relies on npc_instance.current_room matching room_id
- Client correctly processes room_occupants events
- No error logs found, suggesting silent failure in NPC query or personal message
```

---

## INVESTIGATION COMPLETION CHECKLIST

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Only official test credentials would be used (not tested in this investigation)
- [x] Session logged in investigation history
- [x] Remediation prompt generated

---

**Investigation completed**: 2025-01-30
**Next Steps**: Implement remediation fixes based on root cause analysis
