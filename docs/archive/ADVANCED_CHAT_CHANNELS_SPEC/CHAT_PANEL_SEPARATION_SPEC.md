# Chat Panel Separation Specification

## Overview

This specification outlines the separation of chat and channel functionality from the current CommandPanel into a dedicated "Chat" panel, while maintaining the command input functionality in the existing "Commands" panel.

## Current State Analysis

### Existing Structure

**CommandPanel**: Currently contains both command input AND chat functionality

- Channel selector for chat channels
- Command input field
- Command history
- Quick commands (both game commands and channel-specific commands)
- Chat message routing logic

**ChatPanel** (to be renamed to "Game Log"): Currently displays all game messages

- Message display with timestamps
- Message type styling (chat, system, error, etc.)
- Clear/download functionality
- No input capabilities
- Displays ALL game events (chat, system messages, room updates, etc.)

### Current Integration Points

Channel selection is handled in CommandPanel

- Chat message routing logic is embedded in CommandPanel
- Both panels receive messages from the same source (GameTerminalWithPanels)

## Proposed Changes

### 1. Enhanced ChatPanel (New Chat Input Panel)

#### New Features to Add

**Chat Input Section**: Add command input specifically for chat messages

**Channel Selector**: Move channel selection from CommandPanel to ChatPanel

**Chat History**: Display recent chat messages with better organization
- **Quick Chat Commands**: Channel-specific quick commands
- **Chat Statistics**: Message counts, channel activity, etc.

#### Enhanced ChatPanel Interface

```typescript
interface EnhancedChatPanelProps {
  messages: ChatMessage[];
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  selectedChannel?: string;
  onChannelSelect?: (channelId: string) => void;
}
```

#### ChatPanel Layout Structure

```
┌─────────────────────────────────────┐
│ Chat Panel Header                   │
│ [Chat Icon] Chat                    │
├─────────────────────────────────────┤
│ Channel Selector                    │
│ [Dropdown] Say /say                 │
├─────────────────────────────────────┤
│ Chat Input Area                     │
│ [Input Field] [Send Button]         │
├─────────────────────────────────────┤
│ Quick Chat Commands                 │
│ [Say Hello] [Local Greeting]        │
├─────────────────────────────────────┤
│ Chat Statistics                     │
│ Messages: 42 | Channel: Say         │
└─────────────────────────────────────┘
```

### 2. Renamed Game Log Panel (Formerly ChatPanel)

#### Purpose and Functionality

**Game Log Display**: Shows ALL game events and messages

**Message Types**: Chat messages, system messages, room updates, player events, etc.

**Comprehensive Logging**: Complete game activity history
- **No Input Capabilities**: Read-only display of game events

#### Game Log Panel Layout Structure

```
┌─────────────────────────────────────┐
│ Game Log Panel Header               │
│ [Log Icon] Game Log                 │
├─────────────────────────────────────┤
│ Game Messages Display               │
│ [Chat Message] [Timestamp]          │
│ [System Message] [Timestamp]        │
│ [Room Update] [Timestamp]           │
│ [Player Event] [Timestamp]          │
│ ...                                 │
├─────────────────────────────────────┤
│ Game Log Statistics                 │
│ Total Messages: 156 | Connected     │
└─────────────────────────────────────┘
```

### 3. Simplified CommandPanel

#### Features to Remove

Channel selector

- Chat message routing logic
- Channel-specific quick commands
- Chat-related command processing

#### Features to Keep

Command input for game commands

- Command history
- Game-specific quick commands
- Command suggestions/auto-completion
- Command statistics

#### Simplified CommandPanel Interface

```typescript
interface SimplifiedCommandPanelProps {
  commandHistory: string[];
  onSendCommand: (command: string) => void;
  onClearHistory?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  placeholder?: string;
}
```

#### CommandPanel Layout Structure

```
┌─────────────────────────────────────┐
│ Commands Panel Header               │
│ [Search Icon] Commands              │
├─────────────────────────────────────┤
│ Command Input Area                  │
│ [Input Field] [Send Button]         │
├─────────────────────────────────────┤
│ Command History                     │
│ [Command 1] [Timestamp]             │
│ [Command 2] [Timestamp]             │
│ ...                                 │
├─────────────────────────────────────┤
│ Quick Game Commands                 │
│ [Look] [Inventory] [Help] [Who]     │
├─────────────────────────────────────┤
│ Command Statistics                  │
│ Commands: 15 | Ready               │
└─────────────────────────────────────┘
```

## Technical Implementation

### 1. Component Refactoring

#### ChatPanel.tsx Enhancements (New Chat Input Panel)

Add chat input section with channel selector

- Implement chat message sending logic
- Add quick chat commands
- Add chat-specific statistics
- Focus on chat input and channel management

#### GameLogPanel.tsx (Renamed from ChatPanel.tsx)

Rename component from ChatPanel to GameLogPanel

- Update header to show "Game Log" instead of "Chat Log"
- Enhance message display for all game event types
- Add game log statistics
- Maintain read-only functionality for comprehensive game logging

#### CommandPanel.tsx Simplifications

Remove channel selector and related logic

- Remove chat message routing
- Simplify command processing to focus on game commands
- Update quick commands to be game-focused only

### 2. Message Routing Logic

#### Current Logic (in CommandPanel)

```typescript
// Current logic determines if command should be routed to chat
const gameCommands = ['look', 'inventory', 'help', ...];
const isGameCommand = gameCommands.includes(firstWord);
if (!command.startsWith('/') && !isGameCommand) {
  finalCommand = `/${channel.shortcut} ${command}`;
}
```

#### New Logic Distribution

**ChatPanel**: Handle all chat-related commands (say, local, global, whisper, etc.)

**GameLogPanel**: Display all game events and messages (read-only)

**CommandPanel**: Handle all game commands (look, inventory, movement, etc.)
- **GameTerminalWithPanels**: Route commands to appropriate panel based on command type

### 3. State Management

#### New State Structure

```typescript
interface ChatState {
  selectedChannel: string;
  chatHistory: ChatMessage[];
  channelActivity: Record<string, number>;
}

interface GameLogState {
  gameMessages: ChatMessage[];
  messageCounts: Record<string, number>;
  totalMessages: number;
}

interface CommandState {
  commandHistory: string[];
  commandSuggestions: string[];
}
```

#### State Distribution

Chat-related state moves to ChatPanel

- Game log state moves to GameLogPanel
- Command-related state stays in CommandPanel
- Shared state (connection status) remains in GameTerminalWithPanels

### 4. Event Handling

#### Command Routing Logic

```typescript
const handleCommandSubmit = (command: string) => {
  const chatCommands = ['say', 'local', 'global', 'whisper', 'reply'];
  const firstWord = command.split(' ')[0].toLowerCase();

  if (chatCommands.includes(firstWord) || command.startsWith('/')) {
    // Route to ChatPanel
    onSendChatMessage(command, selectedChannel);
  } else {
    // Route to CommandPanel
    onSendGameCommand(command);
  }
};
```

## UI/UX Considerations

### 1. Visual Distinction

**ChatPanel**: Use chat-themed icons and colors (message bubbles, etc.)

**GameLogPanel**: Use log-themed icons and colors (document, list, etc.)

**CommandPanel**: Use command-themed icons and colors (terminal, search, etc.)
- Clear visual separation between chat, game log, and command functionality

### 2. Panel Positioning

**ChatPanel**: Default position on left side (typical chat placement)

**GameLogPanel**: Default position on center-left (comprehensive game activity view)

**CommandPanel**: Default position on right side (typical command placement)
- All panels should be draggable and resizable

### 3. Responsive Design

Panels should adapt to different screen sizes

- Mobile-friendly layouts for smaller screens
- Collapsible sections for space efficiency

### 4. Accessibility

Proper ARIA labels for screen readers

- Keyboard navigation support
- High contrast mode support
- Focus management between panels

## Implementation Phases

### Phase 1: Core Separation

1. Create enhanced ChatPanel with input capabilities
2. Rename existing ChatPanel to GameLogPanel and update functionality
3. Simplify CommandPanel by removing chat functionality
4. Update GameTerminal to use all three panels
5. Implement basic command routing

### Phase 2: Enhanced Features

1. Add chat history and statistics to ChatPanel
2. Implement quick chat commands
3. Add channel activity indicators
4. Enhance GameLogPanel with better message categorization
5. Add game log filtering and search capabilities

### Phase 3: Polish and Optimization

1. Improve visual design and theming
2. Add advanced chat features (emotes, formatting)
3. Implement chat search and filtering
4. Add chat export functionality

### Phase 4: Testing and Refinement

1. Comprehensive testing of both panels
2. Performance optimization
3. User feedback integration
4. Documentation updates

## Testing Strategy

### Unit Tests

Test ChatPanel input functionality

- Test GameLogPanel display functionality
- Test CommandPanel simplification
- Test command routing logic
- Test state management

### Integration Tests

Test panel interaction between all three panels

- Test message flow between panels
- Test channel switching in ChatPanel
- Test game log updates in GameLogPanel
- Test command execution in CommandPanel

### User Acceptance Tests

Test chat functionality in ChatPanel

- Test game log display in GameLogPanel
- Test game commands in CommandPanel
- Test panel resizing and positioning
- Test responsive design

## Migration Considerations

### Backward Compatibility

Existing command functionality should continue to work

- No breaking changes to the API
- Gradual migration path for users

### Data Migration

Existing chat messages should be preserved

- Command history should be maintained
- User preferences should be migrated

### Performance Impact

Minimal performance impact from separation

- Efficient state management
- Optimized rendering for both panels

## Success Criteria

### Functional Requirements

[ ] Chat functionality completely separated into ChatPanel

- [ ] Game log functionality properly implemented in GameLogPanel
- [ ] Command functionality focused in CommandPanel
- [ ] All three panels work independently and together
- [ ] Command routing works correctly
- [ ] Channel selection works in ChatPanel
- [ ] Game log displays all game events properly

### Non-Functional Requirements

[ ] No performance degradation

- [ ] Maintained accessibility standards
- [ ] Responsive design preserved
- [ ] User experience improved
- [ ] Code maintainability enhanced

### User Experience Requirements

[ ] Clear visual distinction between all three panels

- [ ] Intuitive interaction patterns
- [ ] Efficient workflow for chat, game log, and commands
- [ ] Consistent theming and styling
- [ ] Smooth transitions and animations

## Risk Assessment

### Technical Risks

**State Management Complexity**: Mitigated by clear separation of concerns

**Command Routing Errors**: Mitigated by comprehensive testing

**Performance Issues**: Mitigated by efficient component design

### User Experience Risks

**User Confusion**: Mitigated by clear visual design and intuitive layout

**Workflow Disruption**: Mitigated by maintaining existing functionality

**Learning Curve**: Mitigated by gradual introduction and documentation

### Implementation Risks

**Scope Creep**: Mitigated by phased implementation approach

**Integration Issues**: Mitigated by comprehensive testing strategy

**Timeline Delays**: Mitigated by clear milestones and deliverables

## Conclusion

This specification provides a comprehensive plan for separating chat functionality into its own dedicated panel while renaming the existing ChatPanel to GameLogPanel to better reflect its purpose of displaying all game events. The approach ensures improved user experience, better code organization, and enhanced maintainability while preserving all existing functionality.

The three-panel system (Chat, Game Log, Commands) provides clear separation of concerns:
**Chat Panel**: Dedicated to chat input and channel management

**Game Log Panel**: Comprehensive display of all game events and messages

**Commands Panel**: Focused on game command execution

The phased implementation approach allows for gradual migration and testing, ensuring a smooth transition for users and developers alike.
