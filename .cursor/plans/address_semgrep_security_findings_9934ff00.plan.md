---
name: Address Semgrep Security Findings
overview: "Fix 73 semgrep security findings across the codebase. Most findings are already suppressed with nosemgrep comments (68 instances), but 5 legitimate security issues need attention: shell spawn vulnerability, non-literal RegExp in test fixtures, SQL injection concerns, unsafe format strings, and missing suppressions for test code."
todos:
  - id: shell-spawn-fix
    content: Fix shell spawn vulnerability in client/scripts/run-playwright-tests.js - evaluate necessity and add validation or nosemgrep comment
    status: completed
  - id: regexp-suppression
    content: Add nosemgrep comment to non-literal RegExp in client/tests/e2e/runtime/fixtures/multiplayer.ts
    status: completed
  - id: sql-injection-review
    content: Review and add nosemgrep comments to all Python SQL injection flagged locations (6 files)
    status: completed
  - id: format-strings-suppression
    content: Add nosemgrep comments to unsafe format string instances in console.log/error/warn calls (10+ files)
    status: completed
  - id: missing-suppressions
    content: Add missing nosemgrep comments to useCommandHandlers.ts HTTP requests and documentation example
    status: completed
  - id: python36-suppression
    content: Add nosemgrep comment for Python 3.6 compatibility warnings in run_test_ci.py
    status: completed
  - id: verify-fixes
    content: Re-run semgrep scan and verify all legitimate issues are addressed
    status: completed
---

# Semgrep Security Findings Remediation Plan

## Summary

- **Total Findings**: 73
- **Already Suppressed**: 68 (intentional via nosemgrep comments)
- **Require Action**: 5 categories of legitimate issues

## Findings Categories

### 1. Already Suppressed (68 instances) ✓

These findings have explicit `nosemgrep` comments and are intentional:

- HTTP insecure requests to localhost (debug logging endpoints)
- JWT tokens in test files
- Most non-literal RegExp instances (with validation)
- Insecure WebSocket in some test files
- XSS-related findings in test files

### 2. Shell Spawn Security Issue (1 instance) - HIGH PRIORITY

**File**: `client/scripts/run-playwright-tests.js`

**Issue**: `spawn()` with `shell: isWindows` allows shell injection

**Location**: Line 23-27

**Current Code**:

```javascript
const playwright = spawn('npx', ['playwright', 'test'], {
  stdio: 'inherit',
  shell: isWindows, // Use shell on Windows to resolve npx from PATH
  cwd: clientRoot,
});
```

**Action**:

- Investigate if `shell: true` is necessary on Windows
- If required, add input validation or use safer alternatives
- Add `nosemgrep` comment with justification if unavoidable

### 3. Non-literal RegExp in Test Fixtures (1 instance) - MEDIUM PRIORITY

**File**: `client/tests/e2e/runtime/fixtures/multiplayer.ts`

**Issue**: Dynamic RegExp construction could be vulnerable to ReDoS

**Location**: Line 86

**Current Code**:

```typescript
const patternRegex = new RegExp(source, flags);
```

**Action**:

- Add `nosemgrep` comment with justification (test fixture, source is controlled)
- OR validate pattern complexity to prevent ReDoS

### 4. Unsafe Format Strings (10+ instances) - LOW PRIORITY

**Files**: Multiple utility files with console.log/error/warn

- `client/src/hooks/useComponentLifecycleTracking.ts` (line 45)
- `client/src/utils/clientMetricsCollector.ts` (lines 66, 82)
- `client/src/utils/memoryLeakDetector.ts` (lines 100, 106, 125, 198, 201)
- `client/src/utils/memoryMonitor.ts` (lines 270, 288, 306, 313)
- `client/src/utils/performanceTester.ts` (lines 56, 74)
- `client/tests/e2e/di-migration-validation.spec.ts` (line 72)

**Issue**: String interpolation in console.log could forge log messages if attacker controls input

**Action**:

- Add `nosemgrep` comments with justification (internal logging, input is trusted)
- OR refactor to use structured logging without format strings

### 5. Python SQL Injection Concerns (6 instances) - HIGH PRIORITY

**Files**:

- `scripts/init_npc_database.py` (lines 130, 145) - Uses `sqlalchemy.text()` with parameterized queries (safe, but flagged)
- `scripts/load_world_seed.py` (line 149) - Already has nosemgrep comment but multiple rules flag it
- `scripts/populate_test_npc_databases.py` (lines 167, 184) - Uses `sqlalchemy.text()` with parameterized queries
- `server/container_persistence/container_persistence.py` (line 676) - Uses parameterized queries but flagged
- `server/persistence/repositories/experience_repository.py` (line 222) - Uses `sqlalchemy.text()` with parameterized queries

**Analysis**:

- All instances use parameterized queries or trusted input
- Semgrep flags `text()` usage as potentially unsafe, but these are false positives
- Some already have security comments

**Action**:

- Review each instance to confirm parameterization is correct
- Add appropriate `nosemgrep` comments with justification
- For `load_world_seed.py`, ensure all semgrep rules are suppressed

### 6. Python 3.6 Compatibility Warnings (2 instances) - INFORMATIONAL

**File**: `scripts/run_test_ci.py`

**Issue**: `errors` and `encoding` arguments to Popen only available on Python 3.6+

**Location**: Lines 680-636

**Action**:

- Add version check or `nosemgrep` comment (project requires Python 3.12+, so safe)

### 7. Missing Suppressions (2 instances) - LOW PRIORITY

**Files**:

- `client/src/components/ui-v2/hooks/useCommandHandlers.ts` (lines 19, 68) - HTTP requests missing nosemgrep
- `docs/archive/DUAL_CONNECTION_TROUBLESHOOTING_GUIDE.md` (line 90) - Example WebSocket code

**Action**:

- Add `nosemgrep` comments (localhost debug endpoint, example documentation)

## Implementation Steps

### Phase 1: Critical Security Issues (High Priority)

1. **Fix shell spawn vulnerability** in `run-playwright-tests.js`

   - Evaluate if `shell: true` is necessary
   - If yes, add validation or use safer method
   - Add `nosemgrep` comment with detailed justification

2. **Review and fix SQL injection concerns**

   - Audit each Python SQL usage
   - Confirm parameterization is correct
   - Add appropriate `nosemgrep` comments

### Phase 2: Medium Priority

3. **Add suppression for test fixture RegExp**

   - Add `nosemgrep` comment with justification

4. **Add missing suppressions**

   - Add `nosemgrep` to useCommandHandlers.ts HTTP requests
   - Add comment to documentation example

### Phase 3: Low Priority / Cleanup

5. **Add suppressions for unsafe format strings**

   - Add `nosemgrep` comments to all console.log instances
   - Document why each is safe (internal logging, trusted input)

6. **Add Python 3.6 compatibility suppression**

   - Add `nosemgrep` comment (Python 3.12+ required)

## Verification

After fixes:

- Re-run semgrep: `.\scripts\semgrep-autofix.ps1 --verbose`
- Verify all legitimate issues are addressed
- Ensure no new issues introduced
- Confirm all `nosemgrep` comments have clear justifications

## Files to Modify

1. `client/scripts/run-playwright-tests.js` - Shell spawn fix
2. `client/tests/e2e/runtime/fixtures/multiplayer.ts` - RegExp suppression
3. `scripts/init_npc_database.py` - SQL suppression
4. `scripts/populate_test_npc_databases.py` - SQL suppression
5. `server/container_persistence/container_persistence.py` - SQL suppression
6. `server/persistence/repositories/experience_repository.py` - SQL suppression
7. `scripts/run_test_ci.py` - Python 3.6 compatibility suppression
8. `client/src/components/ui-v2/hooks/useCommandHandlers.ts` - HTTP suppression
9. Multiple utility files - Format string suppressions (10 files)

## Notes

- Most findings (68/73) are already suppressed and intentional
- Focus on legitimate security issues, not false positives
- All `nosemgrep` comments should include clear justification
- Follow existing patterns for suppression comments in the codebase
