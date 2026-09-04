# Client Test Remediation — Reference

## Fix patterns by tier

### 🔴 Critical — TypeScript/rendering errors

```typescript
// Missing import
import { Component } from './Component';

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
// Optional props with a default
interface Props {
  title: string;
  optional?: boolean;
}
const Component: React.FC<Props> = ({ title, optional = false }) => <div>{title}</div>;

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
