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

export const handleMythosTimeUpdate: EventHandler = (event, context, appendMessage) => {
  const payload = event.data as unknown as MythosTimePayload;
  if (payload && payload.mythos_clock) {
    const nextState = buildMythosTimeState(payload);
    context.setMythosTime(nextState);

    // Extract current hour from mythos_datetime for clock chime messages
    let currentHour: number | null = null;
    if (payload.mythos_datetime) {
      try {
        const mythosDate = new Date(payload.mythos_datetime);
        currentHour = mythosDate.getUTCHours();
      } catch (error) {
        logger.error('systemHandlers', 'Failed to parse mythos_datetime for clock chime', {
          error: error instanceof Error ? error.message : String(error),
          mythos_datetime: payload.mythos_datetime,
        });
      }
    }

    // Create clock chime message on hourly tick
    if (currentHour !== null) {
      const previousHour = context.lastHourRef.current;
      if (previousHour !== null && previousHour !== currentHour) {
        const formattedClock = formatMythosTime12Hour(payload.mythos_clock);
        appendMessage(
          sanitizeChatMessageForState({
            text: `[Time] The clock chimes ${formattedClock} Mythos`,
            timestamp: event.timestamp,
            messageType: 'system',
            channel: 'system',
            isHtml: false,
          })
        );
      }
      context.lastHourRef.current = currentHour;
    }

    // Create daypart change message
    const previousDaypart = context.lastDaypartRef.current;
    if (previousDaypart && previousDaypart !== nextState.daypart) {
      const description =
        DAYPART_MESSAGES[nextState.daypart] ?? `The Mythos clock shifts into the ${nextState.daypart} watch.`;
      appendMessage(
        sanitizeChatMessageForState({
          text: `[Time] ${description}`,
          timestamp: event.timestamp,
          messageType: 'system',
          channel: 'system',
          isHtml: false,
        })
      );
    }
    context.lastDaypartRef.current = nextState.daypart;
  }
};

export const handleGameTick: EventHandler = (event, _context, appendMessage) => {
  const tickNumber = typeof event.data.tick_number === 'number' ? event.data.tick_number : 0;

  // Display every 10th received tick message (10 seconds)
  // Server broadcasts every 10 ticks (1 second), so we display every 100th tick (10 seconds)
  if (tickNumber % 100 === 0 && tickNumber >= 0) {
    appendMessage(
      sanitizeChatMessageForState({
        text: `[Tick ${tickNumber}]`,
        timestamp: event.timestamp,
        messageType: 'system',
        channel: 'system',
        isHtml: false,
      })
    );
  }
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
