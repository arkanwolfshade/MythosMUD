# MythosMUD UI Component Library

This directory contains a comprehensive UI component library for the MythosMUD client, built with React, TypeScript, and Tailwind CSS. The library follows consistent patterns and provides reusable components for building the game interface.

## Design Principles

### 1. Consistency

All components follow consistent naming conventions, prop patterns, and styling approaches.

### 2. Composability

Components are designed to be composable, allowing for flexible and reusable UI patterns.

### 3. Accessibility

All components include proper ARIA attributes and keyboard navigation support.

### 4. Performance

Components are optimized for performance with proper memoization and efficient rendering.

### 5. Type Safety

Full TypeScript support with comprehensive type definitions and interfaces.

## Component Categories

### Compound Components

Complex components that use the compound pattern for flexible composition:

- **StatusPanel**: Displays player status information with sub-components
- **RoomInfo**: Shows room details with modular information sections

### Basic UI Components

Fundamental building blocks for the interface:

- **TerminalButton**: Styled button component with variants
- **TerminalInput**: Text input with terminal styling
- **TerminalCard**: Container component with consistent styling
- **EldritchIcon**: Icon component with themed variants
- **ChannelSelector**: Dropdown for chat channel selection
- **MythosPanel**: Base panel component with theming

### Specialized Components

Purpose-built components for specific functionality:

- **FeedbackForm**: User feedback collection form
- **VirtualizedMessageList**: High-performance message list

## Usage Patterns

### Importing Components

```typescript
// Import individual components
import { TerminalButton, TerminalInput } from '../ui';

// Import compound components
import { StatusPanel, ConnectionStatus, PlayerName } from '../ui';

// Import types
import type { StatusPanelProps } from '../ui';
```

### Compound Component Usage

```typescript
// Using compound components
<StatusPanel
  player={player}
  isConnected={isConnected}
  playerName={playerName}
  messagesCount={messagesCount}
  commandsCount={commandsCount}
>
  <ConnectionStatus />
  <PlayerName />
  <HealthStat />
  <SanityStat />
  <CoreAttributes />
  <HorrorStats />
  <MessagesCount />
  <CommandsCount />
</StatusPanel>

// Or use the AllStats convenience component
<StatusPanel {...props}>
  <AllStats />
</StatusPanel>
```

### Basic Component Usage

```typescript
// Terminal button with variants
<TerminalButton variant="primary" size="md" onClick={handleClick}>
  Click Me
</TerminalButton>

// Terminal input with validation
<TerminalInput
  value={value}
  onChange={setValue}
  placeholder="Enter command..."
  disabled={!isConnected}
/>
```

## Styling System

### CSS Classes

Components use Tailwind CSS classes with custom MythosMUD theme extensions:

- `bg-mythos-terminal-background`: Primary background color
- `text-mythos-terminal-text`: Primary text color
- `border-mythos-terminal-border`: Border color
- `text-mythos-terminal-primary`: Accent color
- `text-mythos-terminal-success`: Success state color
- `text-mythos-terminal-error`: Error state color
- `text-mythos-terminal-warning`: Warning state color

### Variants

Many components support variants for different visual states:

- **Button variants**: `primary`, `secondary`, `error`, `success`, `warning`
- **Size variants**: `sm`, `md`, `lg`
- **State variants**: `default`, `hover`, `active`, `disabled`

## Testing

All components include comprehensive test suites:

```bash
# Run component tests
npm run test:unit:run -- src/components/ui/__tests__/

# Run specific component tests
npm run test:unit:run -- src/components/ui/__tests__/StatusPanel.test.tsx
```

### Test Patterns

- **Unit tests**: Test individual component behavior
- **Integration tests**: Test component interactions
- **Accessibility tests**: Verify ARIA attributes and keyboard navigation
- **Visual regression tests**: Ensure consistent styling

## Contributing

### Adding New Components

1. Create the component file in the appropriate directory
2. Add comprehensive TypeScript types
3. Include accessibility attributes
4. Write comprehensive tests
5. Update the index.ts file
6. Add documentation to this README

### Component Template

```typescript
import React from 'react';

export interface ComponentNameProps {
  // Define props with JSDoc comments
  /** Description of the prop */
  propName: string;
  /** Optional prop with default */
  optionalProp?: boolean;
}

export const ComponentName: React.FC<ComponentNameProps> = ({
  propName,
  optionalProp = false,
  ...props
}) => {
  return (
    <div
      className="component-base-classes"
      {...props}
    >
      {/* Component content */}
    </div>
  );
};
```

## Performance Considerations

- Use `React.memo` for components that receive stable props
- Implement proper `useCallback` and `useMemo` for expensive operations
- Consider virtualization for large lists
- Optimize re-renders with proper dependency arrays

## Accessibility Guidelines

- Include proper ARIA labels and roles
- Support keyboard navigation
- Ensure sufficient color contrast
- Provide alternative text for images
- Test with screen readers

## Future Enhancements

- Animation system integration
- Dark/light theme switching
- Component playground/storybook
- Automated accessibility testing
- Performance monitoring
- Bundle size optimization
