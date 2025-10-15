# MythosMUD Client

React + TypeScript + Vite frontend for MythosMUD.

## Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## Testing

### Unit Tests (Vitest)

```bash
# Run unit tests
npm run test:unit

# Run with coverage
npm run test:coverage

# Watch mode
npm run test:unit:watch
```

### E2E Tests (Playwright)

#### Automated E2E Runtime Tests

Automated single-player E2E tests that run in CI/CD:

```bash
# Run all automated E2E tests
npm run test:e2e:runtime

# Run in headed mode (see browser)
npm run test:e2e:runtime:headed

# Run in debug mode (step through tests)
npm run test:e2e:runtime:debug

# Run in UI mode (interactive)
npm run test:e2e:runtime:ui
```

**Test Coverage:**

- 114 automated tests across 10 scenarios
- Error handling, accessibility, integration testing
- Runs in <5 minutes
- Full CI/CD integration

**See**: [E2E Testing Guide](../docs/E2E_TESTING_GUIDE.md) for detailed information.

#### Multiplayer MCP Scenarios

For multi-player scenarios requiring AI Agent coordination:

**See**: [Multiplayer Test Rules](../e2e-tests/MULTIPLAYER_TEST_RULES.md)

## Code Quality

```bash
# Lint code
npm run lint

# Format code
npm run format
```

## Tech Stack

- **Framework**: React 19
- **Language**: TypeScript 5.9
- **Build Tool**: Vite 7
- **Styling**: TailwindCSS 4
- **State**: Zustand
- **Testing**: Vitest + Playwright
- **Linting**: ESLint + Prettier

## Project Structure

```
client/
├── src/
│   ├── components/     # React components
│   ├── hooks/          # Custom React hooks
│   ├── contexts/       # React contexts
│   ├── services/       # API services
│   ├── types/          # TypeScript types
│   ├── utils/          # Utility functions
│   └── App.tsx         # Main app component
├── tests/
│   ├── e2e/
│   │   ├── runtime/    # Automated E2E tests
│   │   │   ├── fixtures/         # Test fixtures
│   │   │   ├── error-handling/   # Error tests
│   │   │   ├── accessibility/    # Accessibility tests
│   │   │   ├── admin/            # Admin tests
│   │   │   └── integration/      # Integration tests
│   │   └── playwright.runtime.config.ts
│   └── unit/           # Vitest unit tests
├── public/             # Static assets
└── package.json
```

## Environment Variables

Create a `.env` file in the client directory:

```env
VITE_API_URL=http://localhost:54731
VITE_WS_URL=ws://localhost:54731/ws
```

## Contributing

See [DEVELOPMENT.md](../DEVELOPMENT.md) for development guidelines.

## License

See [LICENSE](../LICENSE) for licensing information.
