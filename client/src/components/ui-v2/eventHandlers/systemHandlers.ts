// System-related event handlers (time, ticks, lucidity, rescue)
// As documented in "System Event Processing" - Dr. Armitage, 1928

import type { MythosTimePayload } from '../../../types/mythosTime';
import { logger } from '../../../utils/logger';
import { buildLucidityStatus } from '../../../utils/lucidityEventUtils';
import { DAYPART_MESSAGES, buildMythosTimeState, formatMythosTime12Hour } from '../../../utils/mythosTime';
import { sanitizeChatMessageForState } from '../utils/messageUtils';
import type { EventHandler } from './types';

export const handleLucidityChange: EventHandler = (event, context) => {
  // Use player's max_lucidity as fallback if event doesn't provide correct max_lcd
  const playerMaxLucidity = context.currentPlayerRef.current?.stats?.max_lucidity;
  const { status: updatedStatus } = buildLucidityStatus(
    context.lucidityStatusRef.current,
    event.data,
    event.timestamp,
    playerMaxLucidity
  );
  context.setLucidityStatus(updatedStatus);
  if (context.currentPlayerRef.current) {
    return {
      player: {
        ...context.currentPlayerRef.current,
        stats: {
          ...context.currentPlayerRef.current.stats,
          current_dp: context.currentPlayerRef.current.stats?.current_dp ?? 0,
          lucidity: updatedStatus.current,
        },
      },
    };
  }
};

export const handleRescueUpdate: EventHandler = (event, context, appendMessage) => {
  const rescueData = event.data as {
    status?: string;
    current_lcd?: number;
    message?: string;
    [key: string]: unknown;
  };

  if (rescueData.status === 'delirium') {
    context.setIsDelirious(true);
    if (rescueData.message) {
      appendMessage(
        sanitizeChatMessageForState({
          text: rescueData.message,
          timestamp: event.timestamp,
          messageType: 'system',
          channel: 'system',
          isHtml: false,
        })
      );
    }
    logger.info('systemHandlers', 'Delirium status detected from rescue_update', {
      current_lcd: rescueData.current_lcd,
    });
  }
};

function parseMythosHour(mythosDatetime: string | undefined): number | null {
  if (!mythosDatetime) {
    return null;
  }
  try {
    return new Date(mythosDatetime).getUTCHours();
  } catch (error) {
    logger.error('systemHandlers', 'Failed to parse mythos_datetime for clock chime', {
      error: error instanceof Error ? error.message : String(error),
      mythos_datetime: mythosDatetime,
    });
    return null;
  }
}

function appendHourChime(
  context: Parameters<EventHandler>[1],
  appendMessage: NonNullable<Parameters<EventHandler>[2]>,
  payload: MythosTimePayload,
  timestamp: string,
  currentHour: number
): void {
  const previousHour = context.lastHourRef.current;
  if (previousHour !== null && previousHour !== currentHour) {
    const formattedClock = formatMythosTime12Hour(payload.mythos_clock);
    appendMessage(
      sanitizeChatMessageForState({
        text: `[Time] The clock chimes ${formattedClock} Mythos`,
        timestamp,
        messageType: 'system',
        channel: 'system',
        isHtml: false,
      })
    );
  }
  context.lastHourRef.current = currentHour;
}

function appendDaypartChange(
  context: Parameters<EventHandler>[1],
  appendMessage: NonNullable<Parameters<EventHandler>[2]>,
  daypart: string,
  timestamp: string
): void {
  const previousDaypart = context.lastDaypartRef.current;
  if (previousDaypart && previousDaypart !== daypart) {
    const description = DAYPART_MESSAGES[daypart] ?? `The Mythos clock shifts into the ${daypart} watch.`;
    appendMessage(
      sanitizeChatMessageForState({
        text: `[Time] ${description}`,
        timestamp,
        messageType: 'system',
        channel: 'system',
        isHtml: false,
      })
    );
  }
  context.lastDaypartRef.current = daypart;
}

export const handleMythosTimeUpdate: EventHandler = (event, context, appendMessage) => {
  const payload = event.data as unknown as MythosTimePayload;
  if (!payload?.mythos_clock) {
    return;
  }
  const nextState = buildMythosTimeState(payload);
  context.setMythosTime(nextState);
  const currentHour = parseMythosHour(payload.mythos_datetime);
  if (currentHour !== null) {
    appendHourChime(context, appendMessage, payload, event.timestamp, currentHour);
  }
  appendDaypartChange(context, appendMessage, nextState.daypart, event.timestamp);
};

export const handleIntentionalDisconnect: EventHandler = (event, context, appendMessage) => {
  const message = (event.data as { message?: string }).message || 'You have disconnected from the game.';

  // Add message to chat
  appendMessage(
    sanitizeChatMessageForState({
      text: message,
      timestamp: event.timestamp,
      messageType: 'system',
      channel: 'system',
      isHtml: false,
    })
  );

  // Mark as intentional disconnect to prevent reconnection
  // Trigger logout which will disconnect and prevent auto-reconnect
  if (context.onLogout) {
    logger.info('systemHandlers', 'Intentional disconnect received, triggering logout', {
      message,
    });
    // Use setTimeout to allow the message to be displayed before logout
    // The logout will clear auth state and prevent reconnection
    setTimeout(() => {
      context.onLogout?.();
    }, 500);
  } else {
    logger.warn('systemHandlers', 'Intentional disconnect received but onLogout not available');
  }
};
