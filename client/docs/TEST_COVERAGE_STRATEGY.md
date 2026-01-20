# Test Coverage Strategy

This document outlines our tiered approach to test coverage, focusing testing effort on the most critical code while
maintaining reasonable standards across the codebase.

## Coverage Targets by Category

### 🔴 Critical Code: 90%

#### Security, Authentication, Data Handling, Event Processing, and State Management

These files require high test coverage due to their critical role in application security, data integrity, and game
state management:

**Security and Authentication:**

- `src/utils/security.ts` - Security utilities and sanitization
- `src/utils/errorHandler.ts` - Error handling and reporting
- `src/utils/logoutHandler.ts` - Authentication and logout flows

**Connection Management:**

- `src/hooks/useGameConnection.ts` - Connection management
- `src/hooks/useWebSocketConnection.ts` - WebSocket connection handling
- `src/hooks/useSessionManagement.ts` - Session ID generation and management (uses cryptographic APIs)
- `src/stores/sessionStore.ts` - Session state management
- `src/stores/connectionStore.ts` - Connection state management

**Event Processing:**

- `src/components/ui-v2/eventHandlers/messageHandlers.ts` - Message event handling
- `src/components/ui-v2/eventHandlers/playerHandlers.ts` - Player event handling
- `src/components/ui-v2/eventHandlers/roomHandlers.ts` - Room event handling
- `src/components/ui-v2/eventHandlers/systemHandlers.ts` - System event handling
- `src/components/ui-v2/eventHandlers/combatHandlers.ts` - Combat event handling
- `src/components/ui-v2/hooks/useEventProcessing.ts` - Event queue processing and deduplication

**State Management Utilities:**

- `src/components/ui-v2/utils/stateUpdateUtils.ts` - Game state update utilities
- `src/components/ui-v2/utils/messageUtils.ts` - Message sanitization and processing
- `src/components/ui-v2/utils/roomMergeUtils.ts` - Room state merging logic

**Rationale**: These areas handle sensitive data, authentication, critical system state, event processing, and game
state management. Bugs here can lead to security vulnerabilities, data loss, system failures, or incorrect game state.

### 🟡 Core Business Logic: 85%+

#### Game State, Connections, and Stores

Core business logic that drives game functionality:

- `src/stores/gameStore.ts` - Game state management
- `src/stores/commandStore.ts` - Command processing
- `src/stores/containerStore.ts` - Container/inventory state
- `src/stores/stateNormalization.ts` - State normalization
- `src/hooks/useGameTerminal.ts` - Game terminal logic
- `src/hooks/useConnectionStateMachine.ts` - Connection state machine
- `src/contexts/GameTerminalContext.tsx` - Game terminal context
- `src/contexts/PanelContext.tsx` - Panel management context

**Rationale**: These files contain the core game logic. High coverage ensures game functionality works correctly and
state is managed properly.

### 🟢 UI Components: 70-80%

#### Focus on Behavior, Not Every Render Path

All files in:

- `src/components/**/*.tsx`
- `src/pages/**/*.tsx`

**Rationale**: UI components should be tested for user interactions and behavior, not every possible render path. Focus
on:

- User interactions (clicks, inputs, navigation)
- Component behavior (state changes, prop handling)
- Integration with hooks and contexts
- Accessibility features

**Not required**: Testing every CSS class combination, every conditional render branch, or visual styling.

### 🔵 Utilities: 60-70%

#### Test the Important Ones

All files in:

- `src/utils/**/*.ts` (except critical files listed above)
- `src/types/**/*.ts`
- `src/config/**/*.ts`

**Rationale**: Utility functions should be tested, but not every helper needs exhaustive coverage. Prioritize:

- Functions with complex logic
- Functions used in critical paths
- Functions with side effects
- Functions that transform or validate data

**Lower priority**: Simple getters, type definitions, configuration constants.

## Global Threshold

The global minimum threshold is set to **70%** for all metrics (statements, branches, functions, lines) to ensure
overall code quality while allowing flexibility for different code categories.

## Implementation

### Vitest Configuration

Per-file thresholds are configured in `vitest.config.ts` for critical and core business logic files. UI components and
utilities use the global threshold as a baseline.

**Note**: Vitest requires exact file paths for per-file thresholds (glob patterns are not supported). Critical and core
files are explicitly listed.

### Monitoring Coverage

Run coverage reports to monitor progress:

```bash
# Full coverage report

make test-client

# Coverage report only

cd client && npm run test:coverage
```

### Adding New Files

When adding new files:

1. **Critical code**: Add to the 90% threshold list in `vitest.config.ts` (security, auth, event handlers, state

   utilities)

2. **Core business logic**: Add to the 85% threshold list in `vitest.config.ts` (game state, stores, contexts)
3. **UI components**: Will use the global 70% threshold
4. **Utilities**: Will use the global 70% threshold (adjust if critical)

**Critical Path Definition**: Code is considered critical if it:

- Handles authentication, security, or sensitive data
- Processes game events that affect game state
- Manages WebSocket connections or session state
- Performs state updates or data merging
- Handles error recovery or cleanup

## Coverage Goals

**Overall**: Maintain 70%+ global coverage

**Critical**: Achieve and maintain 90% coverage

**Core**: Achieve and maintain 85%+ coverage

**UI/Utilities**: Maintain 60-80% coverage (focus on behavior)

## Rationale

This tiered approach:

1. **Focuses effort** on the most critical code
2. **Maintains quality** across the entire codebase
3. **Avoids over-testing** of low-risk code
4. **Provides flexibility** for different code types
5. **Ensures security** by requiring high coverage for security-sensitive code

## References

[Vitest Coverage Documentation](https://vitest.dev/guide/coverage.html)

- [Testing Best Practices](../.cursor/rules/vitest.mdc)
