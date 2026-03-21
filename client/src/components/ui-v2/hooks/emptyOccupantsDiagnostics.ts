// Empty-occupants client diagnostic (occupants panel vs room state). Split out to keep hook CC low.

import type { SendMessageFn } from '../../../utils/clientErrorReporter';
import { OCCUPANTS_PANEL_EMPTY_PLAYERS, reportClientError } from '../../../utils/clientErrorReporter';
import type { Player, Room } from '../types';

/** True when room was set so recently that occupant lists may still be loading. */
function isWithinRoomOccupantsSettleGracePeriod(roomFirstSetAt: number | null, now: number): boolean {
  return roomFirstSetAt !== null && now - roomFirstSetAt < 2000;
}

/**
 * Connected, have a player and room id, and the room's player list is empty (diagnostic candidate).
 */
function tryGetRoomWithEmptyOccupantsList(
  isConnected: boolean,
  player: Player | null,
  room: Room | null
): { player: Player; room: Room & { id: string } } | null {
  if (!isConnected) {
    return null;
  }
  if (!player) {
    return null;
  }
  if (!room?.id) {
    return null;
  }
  if ((room.players ?? []).length > 0) {
    return null;
  }
  return { player, room };
}

/** When all checks pass, returns player + room for the diagnostic; otherwise null. */
function getEmptyOccupantsReportContextOrNull(
  isConnected: boolean,
  player: Player | null,
  room: Room | null,
  roomFirstSetAt: number | null,
  reportedRoomIds: Set<string>,
  now: number
): { player: Player; room: Room & { id: string } } | null {
  const base = tryGetRoomWithEmptyOccupantsList(isConnected, player, room);
  if (!base) {
    return null;
  }
  if (isWithinRoomOccupantsSettleGracePeriod(roomFirstSetAt, now)) {
    return null;
  }
  if (reportedRoomIds.has(base.room.id)) {
    return null;
  }
  return base;
}

export function runEmptyOccupantsReportIfNeeded(
  isConnected: boolean,
  player: Player | null,
  room: Room | null,
  roomFirstSetAt: number | null,
  reportedRoomIds: Set<string>,
  sendMessage: SendMessageFn
): void {
  const ctx = getEmptyOccupantsReportContextOrNull(
    isConnected,
    player,
    room,
    roomFirstSetAt,
    reportedRoomIds,
    Date.now()
  );
  if (!ctx) {
    return;
  }
  reportedRoomIds.add(ctx.room.id);
  reportClientError(
    sendMessage,
    OCCUPANTS_PANEL_EMPTY_PLAYERS,
    'Occupants panel players list is empty but current player exists',
    {
      player_name: ctx.player.name,
      room_id: ctx.room.id,
      room_name: ctx.room.name,
    }
  );
}
