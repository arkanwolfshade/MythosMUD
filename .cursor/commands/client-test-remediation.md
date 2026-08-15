# Client Test Remediation

Fixes failing React/TypeScript test suite runs.

**Subagent integration:** can delegate to the **Test Suite Analyzer** subagent
(`.cursor/agents/test-analyzer.md`) for coverage/gap analysis when the failures are widespread
rather than a handful of isolated breaks.

## Entry point

Run `make test-client` from the project root. If it passes, stop; nothing to do.

## Priority

| Tier | Category | Example |
|---|---|---|
| 🔴 Critical | TypeScript compilation errors, JSX syntax errors, missing imports, hook rule violations | build-breaking |
| 🟡 High | Component rendering failures, prop validation errors, context provider issues, query failures | UI broken |
| 🟢 Medium | Hook dependency warnings, async timeouts, mock isolation, type mismatches | flaky/DX |
| 🔵 Low | Coverage below threshold, ESLint warnings, non-critical perf | polish |

## Fix-verify loop

1. `cd client && npx tsc --noEmit --strict` — fix ALL TypeScript errors first, they block
   everything downstream
2. `make test-client` — run the suite
3. `cd client && npm run lint` — confirm no new lint violations
4. Repeat per tier

## Never

- Fix a test by changing the assertion to match broken behavior instead of fixing the behavior
- Use `screen.getByText(...)` when `screen.getByRole(...)` would be more reliable — prefer role
  queries for interactive elements

## Fix patterns by tier

### 🔴 Critical — TypeScript/rendering errors

```typescript
// Missing/incomplete props interface
interface Props {
  title: string;
  count: number;
}
const Component: React.FC<Props> = ({ title, count }) => (
  <div>{title}: {count}</div>
);
```

### 🟡 High — component issues

```typescript
// Context provider wrapper for tests
const TestWrapper = ({ children }: { children: React.ReactNode }) => (
  <ContextProvider value={mockValue}>{children}</ContextProvider>
);

// Reliable element queries
const button = screen.getByRole('button', { name: /submit/i }); // not getByText('Button')
```

### 🟢 Medium — hook/async issues

```typescript
// Include ALL dependencies actually used
useEffect(() => {
  fetchData(dependency1, dependency2);
}, [dependency1, dependency2]);

// Await async assertions
test('handles async data', async () => {
  render(<AsyncComponent />);
  await waitFor(() => {
    expect(screen.getByText('Data loaded')).toBeInTheDocument();
  });
});
```

## Debugging when a fix doesn't take

```bash
cd client && npx tsc --noEmit           # syntax/type errors only
cd client && npx tsc --noEmit --strict  # full strict pass
cd client && npm run lint
```
