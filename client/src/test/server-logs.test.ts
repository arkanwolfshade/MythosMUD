import * as fs from 'fs';
import * as path from 'path';
import { afterEach, describe, expect, it } from 'vitest';

import { logOffset, waitForLogLine } from '../../tests/e2e/runtime/fixtures/server-logs';
import { E2E_PROJECT_ROOT } from './e2e-bootstrap';

// Unique category name so this never collides with a real DEFAULT_LOG_CATEGORIES file.
const CATEGORY = 'test_server_logs_helper';
const LOG_FILE = path.join(E2E_PROJECT_ROOT, 'logs', 'e2e_test', `${CATEGORY}.log`);

function writeLog(content: string): void {
  fs.mkdirSync(path.dirname(LOG_FILE), { recursive: true });
  fs.writeFileSync(LOG_FILE, content, 'utf-8');
}

afterEach(() => {
  fs.rmSync(LOG_FILE, { force: true });
});

describe('server-logs fixture', () => {
  it('logOffset returns 0 when the category file does not exist', () => {
    expect(logOffset(CATEGORY)).toBe(0);
  });

  it('logOffset returns the current byte size of an existing file', () => {
    writeLog('hello\n');
    expect(logOffset(CATEGORY)).toBe(Buffer.byteLength('hello\n'));
  });

  it('waitForLogLine finds a matching line already present after the given offset', async () => {
    writeLog("event='first'\n");
    const line = await waitForLogLine(CATEGORY, 0, /event='first'/, 1000);
    expect(line).toContain("event='first'");
  });

  it('waitForLogLine ignores lines at or before sinceOffset', async () => {
    writeLog("event='before'\n");
    const offset = logOffset(CATEGORY);
    fs.appendFileSync(LOG_FILE, "event='after'\n");
    const line = await waitForLogLine(CATEGORY, offset, /event=/, 1000);
    expect(line).toContain("event='after'");
  });

  it('waitForLogLine reads from the start when the file has rotated (shrunk) below sinceOffset', async () => {
    writeLog("event='long-line-before-rotation'\n");
    const staleOffset = logOffset(CATEGORY);
    // Simulate rotation: file replaced with a shorter one.
    writeLog("event='after-rotation'\n");
    const line = await waitForLogLine(CATEGORY, staleOffset, /event='after-rotation'/, 1000);
    expect(line).toContain("event='after-rotation'");
  });

  it('waitForLogLine throws with the tail it saw when no match appears before the timeout', async () => {
    writeLog("event='irrelevant'\n");
    await expect(waitForLogLine(CATEGORY, 0, /event='nonexistent'/, 300)).rejects.toThrow(
      /Timed out after 300ms.*irrelevant/s
    );
  });

  it('waitForLogLine throws mentioning "(nothing read)" when the file never gains matching content', async () => {
    await expect(waitForLogLine(CATEGORY, 0, /event='nonexistent'/, 300)).rejects.toThrow(/\(nothing read\)/);
  });
});
