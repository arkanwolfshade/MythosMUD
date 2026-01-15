#!/usr/bin/env node

import { spawn } from 'child_process';
import { existsSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const clientRoot = join(__dirname, '..');
const testsDir = join(clientRoot, 'tests');

// Check if tests directory exists
if (!existsSync(testsDir)) {
  console.log('No Playwright tests found - this is expected if tests directory does not exist');
  process.exit(0);
}

// Run Playwright tests
// On Windows, we need shell: true to resolve npx from PATH
// On Unix systems, we can use shell: false for better security
const isWindows = process.platform === 'win32';
const playwright = spawn('npx', ['playwright', 'test'], {
  stdio: 'inherit',
  shell: isWindows, // Use shell on Windows to resolve npx from PATH
  cwd: clientRoot,
});

playwright.on('close', code => {
  process.exit(code || 0);
});

playwright.on('error', error => {
  console.error('Error running Playwright:', error);
  process.exit(1);
});
