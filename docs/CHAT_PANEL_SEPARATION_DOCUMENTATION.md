# Chat Panel Separation System Documentation

## Overview

The Chat Panel Separation System is a comprehensive refactoring of the MythosMUD client interface that separates chat functionality from game commands, creating a more organized and user-friendly experience. The system consists of three distinct panels:

1. **Chat Panel** - Dedicated chat input and management
2. **Game Log Panel** - Display of all game messages and events
3. **Commands Panel** - Game command input and history

## Architecture

### Component Hierarchy

```
GameTerminalWithPanels
├── GameTerminal
│   ├── ChatPanel
│   │   ├── ChannelSelector
│   │   ├── ChatInput
│   │   ├── EmotePanel
│   │   ├── FormattingPanel
│   │   ├── SettingsPanel
│   │   └── ChatHistory
│   ├── GameLogPanel
│   │   ├── MessageFilters
│   │   ├── SearchInterface
│   │   ├── MessageGroups
│   │   └── MessageDisplay
│   └── CommandPanel
│       ├── CommandInput
│       ├── CommandHistory
│       ├── QuickCommands
│       └── CommonCommands
```

### State Management

Each panel maintains its own local state while sharing common state through props:

- **ChatPanel**: Chat input, channel selection, emotes, formatting, settings
- **GameLogPanel**: Message filtering, search, grouping, statistics
- **CommandPanel**: Command input, history, suggestions, quick commands

## Components

### ChatPanel

The ChatPanel is responsible for all chat-related functionality.

#### Features
- **Channel Selection**: Switch between local, global, and other chat channels
- **Chat Input**: Rich text input with emotes and formatting
- **Quick Commands**: Pre-defined chat phrases for common interactions
- **Activity Indicators**: Visual feedback for channel activity
- **Emotes**: Click-to-insert emoji and text emotes
- **Text Formatting**: Markdown-style formatting options
- **Settings Panel**: Font size, notifications, spam filtering, export options
- **Moderation**: User ignore list, spam detection, rate limiting
- **Export/Backup**: Export chat logs and backup settings

#### Props
```typescript
interface ChatPanelProps {
  messages: ChatMessage[];
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages: () => void;
  onDownloadLogs: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  selectedChannel?: string;
  onChannelSelect?: (channel: string) => void;
}
```

#### Usage
```tsx
<ChatPanel
  messages={chatMessages}
  onSendChatMessage={handleChatMessage}
  onClearMessages={clearChat}
  onDownloadLogs={downloadChatLogs}
  disabled={!isConnected}
  isConnected={isConnected}
  selectedChannel="local"
  onChannelSelect={setSelectedChannel}
/>
```

### GameLogPanel

The GameLogPanel displays all game messages with advanced filtering and search capabilities.

#### Features
- **Message Display**: All game messages with timestamps and categorization
- **Message Filtering**: Filter by type (chat, system, error, move)
- **Time Filtering**: Filter by time range (last 5 minutes, hour, day, etc.)
- **Search**: Full-text search with history
- **Message Grouping**: Group messages by time periods
- **Statistics**: Message counts and type breakdown
- **Export**: Download game logs in various formats

#### Props
```typescript
interface GameLogPanelProps {
  messages: GameMessage[];
  onClearMessages: () => void;
  onDownloadLogs: () => void;
}
```

#### Usage
```tsx
<GameLogPanel
  messages={gameMessages}
  onClearMessages={clearGameLog}
  onDownloadLogs={downloadGameLogs}
/>
```

### CommandPanel

The CommandPanel handles all game command input and history.

#### Features
- **Command Input**: Text input for game commands
- **Command History**: Navigable history of previous commands
- **Quick Commands**: Common game commands as clickable buttons
- **Command Suggestions**: Auto-completion based on history
- **Common Commands**: Categorized common commands (movement, actions)

#### Props
```typescript
interface CommandPanelProps {
  commandHistory: string[];
  onSendCommand: (command: string) => void;
  onClearHistory: () => void;
  disabled?: boolean;
  isConnected?: boolean;
}
```

#### Usage
```tsx
<CommandPanel
  commandHistory={commandHistory}
  onSendCommand={handleGameCommand}
  onClearHistory={clearCommandHistory}
  disabled={!isConnected}
  isConnected={isConnected}
/>
```

## Performance Optimizations

### Virtual Scrolling

The system includes a `VirtualizedMessageList` component for efficient rendering of large message lists:

```tsx
<VirtualizedMessageList
  messages={messages}
  itemHeight={60}
  containerHeight={400}
  renderItem={(message, index) => <MessageItem message={message} />}
  overscan={5}
/>
```

### Performance Monitoring

Built-in performance monitoring with the `usePerformanceMonitor` hook:

```tsx
const { startRender, endRender, getStats } = usePerformanceMonitor({
  componentName: 'ChatPanel',
  threshold: 16, // 16ms threshold
  onMetrics: (metrics) => console.log('Performance:', metrics),
});
```

### Memory Leak Detection

Automatic memory leak detection with the `useMemoryLeakDetector` hook:

```tsx
const { getStats, getSnapshots } = useMemoryLeakDetector('ChatPanel', {
  warningThreshold: 100, // 100MB
  criticalThreshold: 500, // 500MB
  checkInterval: 10000, // 10 seconds
});
```

### Message Batching

Network optimization with message batching:

```tsx
const { addMessage, flush, getBatchSize } = useMessageBatcher(
  (messages) => sendBatchToServer(messages),
  {
    maxBatchSize: 10,
    maxBatchDelay: 100, // 100ms
    maxBatchSizeBytes: 10240, // 10KB
  }
);
```

## User Feedback System

### Feedback Collection

The system includes a comprehensive feedback collection system:

```tsx
const { addFeedback, getStats, searchFeedback } = useFeedbackManager();

// Submit feedback
addFeedback({
  type: 'bug',
  title: 'Performance Issue',
  description: 'Chat panel is slow with many messages',
  priority: 'high',
  component: 'chat',
  userAgent: navigator.userAgent,
  timestamp: new Date().toISOString(),
});
```

### Feedback Form

The `FeedbackForm` component provides a user-friendly interface for submitting feedback:

```tsx
<FeedbackForm
  onSubmit={handleFeedbackSubmit}
  onCancel={closeFeedbackForm}
  isOpen={showFeedbackForm}
/>
```

## Testing

### Unit Tests

Comprehensive unit tests for each component:

- `chat-panel.spec.ts` - ChatPanel functionality tests
- `game-log-panel.spec.ts` - GameLogPanel functionality tests
- `command-panel.spec.ts` - CommandPanel functionality tests
- `game-terminal-integration.spec.ts` - Integration tests

### Performance Tests

Performance benchmarking with `performance.spec.ts`:

- Render performance tests
- Memory usage tests
- Large dataset handling tests
- Integration performance tests

### Running Tests

```bash
# Run all tests
npm test

# Run specific test file
npm test chat-panel.spec.ts

# Run performance tests
npm test performance.spec.ts

# Run with coverage
npm run test:coverage
```

## Configuration

### Channel Configuration

Channels are configured in `src/config/channels.ts`:

```typescript
export const AVAILABLE_CHANNELS = [
  { id: 'local', name: 'Local', shortcut: 'l' },
  { id: 'global', name: 'Global', shortcut: 'g' },
  // Add more channels as needed
];

export const DEFAULT_CHANNEL = 'local';
```

### Performance Configuration

Performance settings can be adjusted:

```typescript
// Performance monitoring
const performanceConfig = {
  threshold: 16, // ms
  enabled: process.env.NODE_ENV === 'development',
};

// Memory leak detection
const memoryConfig = {
  warningThreshold: 100, // MB
  criticalThreshold: 500, // MB
  checkInterval: 10000, // ms
};

// Message batching
const batchingConfig = {
  maxBatchSize: 10,
  maxBatchDelay: 100, // ms
  maxBatchSizeBytes: 10240, // bytes
};
```

## Accessibility

### ARIA Labels

All components include proper ARIA labels:

```tsx
<div role="region" aria-label="Channel Selection">
  <ChannelSelector />
</div>

<div role="region" aria-label="Chat Input">
  <ChatInput />
</div>

<div role="region" aria-label="Chat Messages">
  <ChatHistory />
</div>
```

### Keyboard Navigation

Full keyboard navigation support:

- Tab navigation between panels
- Arrow keys for command history
- Enter to submit messages
- Escape to close modals
- Ctrl+L to clear input

### High Contrast Mode

CSS support for high contrast mode:

```css
@media (prefers-contrast: high) {
  .mythos-terminal-primary {
    color: #ffffff !important;
    background-color: #000000 !important;
    border-color: #ffffff !important;
  }
}
```

## Responsive Design

### Mobile Support

Responsive design for mobile devices:

```tsx
// Mobile-optimized layout
<div className="flex-col sm:flex-row">
  <div className="w-full sm:w-auto">
    <ChannelSelector />
  </div>
</div>
```

### Breakpoints

- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px

## Security

### Input Validation

All user inputs are validated:

```typescript
// Command validation
const validateCommand = (command: string): boolean => {
  const trimmed = command.trim();
  return trimmed.length > 0 && trimmed.length <= 1000;
};

// Message validation
const validateMessage = (message: string): boolean => {
  const trimmed = message.trim();
  return trimmed.length > 0 && trimmed.length <= 500;
};
```

### Spam Protection

Built-in spam detection:

```typescript
const isSpamMessage = (message: string): boolean => {
  const repeatedChars = /(.)\1{4,}/;
  const excessiveCaps = /[A-Z]{10,}/;
  const spamPatterns = /\b(buy|sell|click|free|money|casino)\b/i;

  return repeatedChars.test(message) ||
         excessiveCaps.test(message) ||
         spamPatterns.test(message);
};
```

### Rate Limiting

Message rate limiting:

```typescript
const checkRateLimit = (): boolean => {
  const now = Date.now();
  const timeSinceLastMessage = now - lastMessageTime;
  const minInterval = (60 * 1000) / messageRateLimit;

  return timeSinceLastMessage >= minInterval;
};
```

## Deployment

### Build Process

```bash
# Install dependencies
npm install

# Run tests
npm test

# Build for production
npm run build

# Start development server
npm run dev
```

### Environment Variables

```bash
# Development
NODE_ENV=development
VITE_API_URL=http://localhost:8000

# Production
NODE_ENV=production
VITE_API_URL=https://api.mythosmud.com
```

## Troubleshooting

### Common Issues

1. **Performance Issues**
   - Check memory usage with `useMemoryLeakDetector`
   - Monitor render times with `usePerformanceMonitor`
   - Enable virtual scrolling for large message lists

2. **Connection Issues**
   - Verify WebSocket connection status
   - Check network connectivity
   - Review server logs

3. **UI Issues**
   - Clear browser cache
   - Check for CSS conflicts
   - Verify responsive breakpoints

### Debug Tools

```typescript
// Enable debug logging
localStorage.setItem('debug', 'mythosmud:*');

// Performance monitoring
const stats = usePerformanceMonitor({
  componentName: 'ChatPanel',
  enabled: true,
  onMetrics: console.log,
});

// Memory monitoring
const memoryStats = useMemoryLeakDetector('ChatPanel', {
  enabled: true,
});
```

## Future Enhancements

### Planned Features

1. **Advanced Search**
   - Regular expression search
   - Search within specific time ranges
   - Search by user or channel

2. **Message Encryption**
   - End-to-end encryption for private messages
   - Secure channel communication

3. **Custom Themes**
   - User-defined color schemes
   - Theme marketplace
   - Dark/light mode toggle

4. **Advanced Analytics**
   - Usage statistics
   - Performance metrics
   - User behavior analysis

### Contributing

To contribute to the Chat Panel Separation System:

1. Fork the repository
2. Create a feature branch
3. Write tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## Conclusion

The Chat Panel Separation System provides a robust, performant, and user-friendly interface for the MythosMUD client. With comprehensive testing, performance optimization, and accessibility features, it serves as a solid foundation for future enhancements and improvements.

For additional support or questions, please refer to the project documentation or submit an issue through the feedback system.
