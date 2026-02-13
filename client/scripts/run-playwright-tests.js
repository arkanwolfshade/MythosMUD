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

// In CI, check if backend server is available (E2E tests require it)
async function checkBackendServer() {
  if (process.env.CI === 'true') {
    try {
      const response = await fetch('http://localhost:54731/v1/monitoring/health', {
        signal: AbortSignal.timeout(2000),
      });
      if (!response.ok) {
        console.log('Backend server not available - skipping E2E tests in CI');
        console.log('This is expected in frontend-only CI jobs');
        process.exit(0);
      }
    } catch {
      // Backend server not available - this is expected in frontend-only CI jobs
      console.log('Backend server not available - skipping E2E tests in CI');
      console.log('This is expected in frontend-only CI jobs');
      process.exit(0);
    }
  }
}

// Run backend check before starting tests
await checkBackendServer();

// Run Playwright tests
// On Windows, we need shell: true to resolve npx from PATH
// On Unix systems, we can use shell: false for better security
const isWindows = process.platform === 'win32';
// Shell is only enabled on Windows to resolve npx from PATH. The command ('npx') and
// arguments (['playwright', 'test']) are hardcoded constants with no user input, so
// shell injection is not possible. This is a build script, not user-facing code.
// nosemgrep: javascript.lang.security.audit.spawn-shell-true.spawn-shell-true
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
