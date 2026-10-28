/**
 * Server log-file reading helpers for E2E tests.
 *
 * Reads the E2E environment's structured log files directly (logs/e2e_test/<category>.log,
 * matching LOGGING_ENVIRONMENT=e2e_test and DEFAULT_LOG_CATEGORIES in
 * server/structured_logging/logging_file_categories.py) so a spec can assert that a game
 * action actually produced a server-side log line, not just a client-visible message.
 *
 * New pattern for this suite (#688) -- no existing spec reads a server log file. Reuse this
 * for other log categories rather than re-implementing offset/poll/rotation handling per spec.
 */

import * as fs from 'fs';
import * as path from 'path';
import { E2E_PROJECT_ROOT } from '../../../../src/test/e2e-bootstrap';

const LOG_DIR = path.join(E2E_PROJECT_ROOT, 'logs', 'e2e_test');

function logPath(category: string): string {
  return path.join(LOG_DIR, `${category}.log`);
}

/** Current byte size of a category's log file (0 if it doesn't exist yet). */
export function logOffset(category: string): number {
  try {
    return fs.statSync(logPath(category)).size;
  } catch {
    return 0;
  }
}

/**
 * Poll a category's log file for a line matching `pattern`, starting from `sinceOffset`.
 *
 * If the file has shrunk below `sinceOffset` (rotated since the offset was captured), reads
 * from the start instead. Throws with the tail read so far if no match appears before timeout.
 */
export async function waitForLogLine(
  category: string,
  sinceOffset: number,
  pattern: RegExp,
  timeoutMs: number = 10000
): Promise<string> {
  const file = logPath(category);
  const pollIntervalMs = 250;
  const deadline = Date.now() + timeoutMs;
  let lastTail = '';

  while (Date.now() < deadline) {
    let size: number;
    try {
      size = fs.statSync(file).size;
    } catch {
      size = 0;
    }
    const start = size < sinceOffset ? 0 : sinceOffset;
    if (size > start) {
      const fd = fs.openSync(file, 'r');
      try {
        const length = size - start;
        const buffer = Buffer.alloc(length);
        fs.readSync(fd, buffer, 0, length, start);
        lastTail = buffer.toString('utf-8');
        const match = lastTail.split('\n').find(line => pattern.test(line));
        if (match) {
          return match;
        }
      } finally {
        fs.closeSync(fd);
      }
    }
    await new Promise(resolve => setTimeout(resolve, pollIntervalMs));
  }

  throw new Error(
    `Timed out after ${timeoutMs}ms waiting for ${category}.log to match ${pattern}. ` +
      `Tail read since offset ${sinceOffset}:\n${lastTail || '(nothing read)'}`
  );
}
