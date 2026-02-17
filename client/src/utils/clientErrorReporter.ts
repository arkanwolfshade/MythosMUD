/**
 * Client-side error reporting to server.
 * Sends structured error reports via WebSocket; server logs to errors.log.
 */

export const OCCUPANTS_PANEL_EMPTY_PLAYERS = 'occupants_panel_empty_players';

export type SendMessageFn = (type: string, data: Record<string, unknown>) => boolean;

/**
 * Report a client-detected error to the server.
 * Server logs to errors.log via structured logging aggregator.
 *
 * @param sendMessage - WebSocket send function (type, data) => boolean
 * @param errorType - Error type constant (e.g. OCCUPANTS_PANEL_EMPTY_PLAYERS)
 * @param message - Human-readable description
 * @param context - Optional additional context for debugging
 * @returns true if message was sent, false otherwise
 */
export function reportClientError(
  sendMessage: SendMessageFn,
  errorType: string,
  message: string,
  context?: Record<string, unknown>
): boolean {
  return sendMessage('client_error_report', {
    error_type: errorType,
    message,
    ...(context != null && Object.keys(context).length > 0 && { context }),
  });
}
