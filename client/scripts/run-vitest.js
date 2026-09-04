#!/usr/bin/env node

import { spawn } from 'child_process';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const clientRoot = join(__dirname, '..');

// Avoid "NO_COLOR is ignored due to FORCE_COLOR" warning: when NO_COLOR is set,
// omit FORCE_COLOR so Node respects the no-color preference.
const env = { ...process.env };
if ('NO_COLOR' in process.env) {
  delete env.FORCE_COLOR;
}

const args = process.argv.slice(2);
const vitestBin = join(clientRoot, 'node_modules', 'vitest', 'vitest.mjs');
const vitest = spawn(process.execPath, [vitestBin, ...args], {
  stdio: 'inherit',
  cwd: clientRoot,
  env: {
    ...env,
    NODE_OPTIONS: [env.NODE_OPTIONS, '--max-old-space-size=4096'].filter(Boolean).join(' ').trim() || undefined,
  },
});

vitest.on('close', code => {
  process.exit(code ?? 0);
});

vitest.on('error', error => {
  console.error('Error running Vitest:', error);
  process.exit(1);
});
