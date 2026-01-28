# Test Client Remediation Prompt - AI-Optimized Version

*"In the digital realm of the client-side, we learn that proper testing requires systematic component validation, comprehensive hook testing, and thorough interaction simulation. The path to reliable user interfaces lies not in quick fixes, but in methodical test remediation and validation."*

**SUBAGENT INTEGRATION:**

This command leverages the **Test Suite Analyzer** subagent for comprehensive test analysis:
- **Subagent**: `.cursor/agents/test-analyzer.md`
- **Purpose**: Test coverage analysis, test quality assessment, gap identification
- **When Used**: Automatically invoked for client test suite analysis and coverage reporting
- **Benefits**: Isolated context for test analysis, comprehensive coverage reports, actionable recommendations

## 🎯 MANDATORY AI EXECUTION PROTOCOL

**CRITICAL**: You MUST follow this exact sequence. Do not skip steps or deviate from the order.

### Phase 1: Initial Assessment (REQUIRED FIRST)

```bash
# Step 1: Run client tests to get current failure state

make test-client
```

**AI ACTION**: Capture the complete test output. If tests pass, STOP - no remediation needed.

### Phase 2: Categorize and Prioritize Failures

**AI DECISION TREE**: For each failure, categorize into ONE of these priority levels:

#### 🔴 CRITICAL (Fix First - Blocking Issues)

**TypeScript compilation errors** (prevents build)

**JSX syntax errors** (breaks rendering)

**Missing imports** (component crashes)
- **Hook rule violations** (React runtime errors)

#### 🟡 HIGH PRIORITY (Fix Second - Core Functionality)

**Component rendering failures** (UI broken)

**Props validation errors** (runtime crashes)

**Context provider issues** (state not available)
- **Element query failures** (tests can't find elements)

#### 🟢 MEDIUM PRIORITY (Fix Third - Enhancement)

**Hook dependency warnings** (performance issues)

**Async operation timeouts** (test reliability)

**Mock implementation issues** (test isolation)
- **Type mismatches** (development experience)

#### 🔵 LOW PRIORITY (Fix Last - Polish)

**Test coverage below thresholds** (quality metrics)

**ESLint warnings** (code style)

**Performance optimizations** (non-critical)

**AI RULE**: Fix ONE category at a time. Do not move to the next category until current one is resolved.

#### For Each Failure Category

1. **IDENTIFY**: Use specific tools to diagnose the issue
2. **ANALYZE**: Understand root cause before attempting fix
3. **FIX**: Apply targeted solution
4. **VERIFY**: Run tests to confirm fix works
5. **VALIDATE**: Ensure no regressions introduced

### Phase 3: Systematic Fixing Process

**AI RULE**: Fix ONE category at a time. Do not move to the next category until current one is resolved.

### Phase 4: Tool Selection Guide

**AI TOOL MAPPING**: Use these specific tools for each failure type:

#### TypeScript/Compilation Issues

```bash
# REQUIRED: Check TypeScript compilation

cd client && npx tsc --noEmit --strict
```

**AI ACTION**: Fix ALL TypeScript errors before proceeding to other issues.

#### Component Rendering Issues

```bash
# REQUIRED: Check for syntax errors

cd client && npx tsc --noEmit
```

**AI ACTION**: Use `read_file` to examine failing components, identify missing imports/props.

#### Hook Issues

**AI ACTION**: Use `grep` to find hook usage patterns, verify dependency arrays.

#### Testing Library Issues

**AI ACTION**: Use `read_file` to examine test files, check query methods and async handling.

### Phase 5: Fix Implementation Patterns

#### 🔴 CRITICAL FIXES - TypeScript Errors

```typescript
// Pattern 1: Fix missing imports
import { Component } from './Component'; // Add missing import

// Pattern 2: Fix type mismatches
interface Props {
  title: string;
  count: number;
}
const Component: React.FC<Props> = ({ title, count }) => {
  return <div>{title}: {count}</div>;
};

// Pattern 3: Fix JSX syntax
// BEFORE: <div>{title</div>  // Missing closing brace
// AFTER:  <div>{title}</div> // Proper JSX
```

#### 🟡 HIGH PRIORITY FIXES - Component Issues

```typescript
// Pattern 1: Fix missing props
interface Props {
  title: string;
  optional?: boolean;
}
const Component: React.FC<Props> = ({ title, optional = false }) => {
  return <div>{title}</div>;
};

// Pattern 2: Fix context provider issues
const TestWrapper = ({ children }: { children: React.ReactNode }) => (
  <ContextProvider value={mockValue}>
    {children}
  </ContextProvider>
);

// Pattern 3: Fix element queries
// BEFORE: screen.getByText('Button')  // May not find element
// AFTER:  screen.getByRole('button', { name: /submit/i }) // More reliable
```

#### 🟢 MEDIUM PRIORITY FIXES - Hook Issues

```typescript
// Pattern 1: Fix missing dependencies
useEffect(() => {
  fetchData(dependency1, dependency2);
}, [dependency1, dependency2]); // Include ALL dependencies

// Pattern 2: Fix async operations in tests
test('handles async data', async () => {
  render(<AsyncComponent />);
  await waitFor(() => {
    expect(screen.getByText('Data loaded')).toBeInTheDocument();
  });
});
```

### Phase 6: Verification Protocol

**AI MANDATORY CHECKS**: After each fix, run these commands in order:

```bash
# 1. Verify TypeScript compilation

cd client && npx tsc --noEmit

# 2. Run client tests

make test-client

# 3. Check ESLint

cd client && npm run lint
```

**AI RULE**: If ANY check fails, STOP and fix the issue before proceeding.

### Phase 7: Success Validation

**AI SUCCESS CRITERIA**: All of these must pass:

- [ ] `make test-client` exits with code 0
- [ ] TypeScript compilation passes without errors
- [ ] ESLint passes without errors
- [ ] No new test failures introduced
- [ ] All critical and high-priority issues resolved

## 🚨 AI ERROR HANDLING

### If Tests Still Fail After Fixes

1. **STOP** - Do not continue with more fixes
2. **ANALYZE** - Use `read_file` to examine the specific failing test
3. **INVESTIGATE** - Check if the fix introduced new issues
4. **REVERT** - If fix caused problems, revert and try different approach
5. **REPORT** - Document what was attempted and why it failed

### If Multiple Categories Have Failures

1. **PRIORITIZE** - Always fix CRITICAL first, then HIGH, then MEDIUM, then LOW
2. **ISOLATE** - Fix one category completely before moving to next
3. **VALIDATE** - Run verification protocol after each category
4. **DOCUMENT** - Keep track of what was fixed in each category

## 📋 AI EXECUTION CHECKLIST

**Before Starting:**

- [ ] Confirm you are in the project root directory
- [ ] Verify you have access to `make test-client` command
- [ ] Understand the priority system (CRITICAL → HIGH → MEDIUM → LOW)

**During Execution:**

- [ ] Follow the exact sequence: Assessment → Categorize → Fix → Verify
- [ ] Fix ONE category at a time
- [ ] Run verification protocol after each category
- [ ] Document what was fixed and why

**After Completion:**

- [ ] All success criteria met
- [ ] No regressions introduced
- [ ] All critical and high-priority issues resolved
- [ ] Client tests passing with `make test-client`

## 🔧 COMMON FIX TEMPLATES

### Template 1: Missing Import Fix

```typescript
// BEFORE: Component fails to render
const MyComponent = () => <div>Hello</div>;

// AFTER: Add missing import
import React from 'react';
const MyComponent = () => <div>Hello</div>;
```

### Template 2: Props Interface Fix

```typescript
// BEFORE: Props not defined
const Component = ({ title, count }) => <div>{title}: {count}</div>;

// AFTER: Define proper interface
interface Props {
  title: string;
  count: number;
}
const Component: React.FC<Props> = ({ title, count }) => <div>{title}: {count}</div>;
```

### Template 3: Hook Dependency Fix

```typescript
// BEFORE: Missing dependency warning
useEffect(() => {
  fetchData(userId);
}, []); // Missing userId dependency

// AFTER: Include all dependencies
useEffect(() => {
  fetchData(userId);
}, [userId]); // Include userId dependency
```

### Template 4: Test Query Fix

```typescript
// BEFORE: Unreliable query
const button = screen.getByText('Submit');

// AFTER: More reliable query
const button = screen.getByRole('button', { name: /submit/i });
```

## 🎯 AI SUCCESS METRICS

**Primary Success**: `make test-client` passes with exit code 0
**Secondary Success**: All TypeScript and ESLint checks pass
**Tertiary Success**: Test coverage meets minimum thresholds

**AI RULE**: Primary success is mandatory. Secondary and tertiary are preferred but not blocking.

---

**Remember**: This prompt focuses on investigating and fixing client-side test failures systematically. Always run tests after making changes and ensure no regressions are introduced in the React application.

**AI INSTRUCTION**: Follow the exact sequence outlined above. Do not skip steps or deviate from the priority order. Your success will be measured by the successful execution of `make test-client` with exit code 0.
