#!/usr/bin/env node
/**
 * Apply patches using patch-package, but don't fail if patches are outdated.
 * This handles the case where patch files exist for older package versions.
 */

import { exec } from 'child_process';

exec('patch-package', (error, stdout, stderr) => {
  if (error) {
    // Patch failed - this is OK if patches are outdated
    console.log('patch-package completed with warnings (this is OK if patches are outdated)');
    if (stderr) {
      console.error(stderr);
    }
  } else {
    // Patches applied successfully
    if (stdout) {
      console.log(stdout);
    }
  }
  // Always exit successfully to not break npm install
  process.exit(0);
});
