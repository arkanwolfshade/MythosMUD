import { create } from 'zustand';
import { devtools } from 'zustand/middleware';

export interface CommandHistoryEntry {
  command: string;
  timestamp: number;
  success: boolean;
  result?: string;
}

export interface CommandAlias {
  [alias: string]: string;
}

export interface CommandTrigger {
  id: string;
  pattern: string;
  action: string;
  enabled: boolean;
  caseSensitive?: boolean;
  regex?: boolean;
}

export interface CommandState {
  // Command input
  currentCommand: string;
  commandIndex: number;

  // Command execution
  isExecuting: boolean;
  lastExecutedCommand: string | null;

  // Command history
  commandHistory: CommandHistoryEntry[];

  // Command queue
  commandQueue: string[];

  // Aliases and triggers
  aliases: CommandAlias;
  triggers: CommandTrigger[];
}

export interface CommandActions {
  // Command input management
  setCurrentCommand: (command: string) => void;
  clearCurrentCommand: () => void;
  appendToCommand: (text: string) => void;

  // Command history
  addToHistory: (command: string, success?: boolean, result?: string) => void;
  clearHistory: () => void;

  // Command navigation
  navigateHistory: (direction: number) => void;

  // Command execution
  setExecuting: (executing: boolean) => void;
  setLastExecutedCommand: (command: string | null) => void;
  executeCommand: (command: string) => void;

  // Command queue
  addToQueue: (command: string) => void;
  processNextCommand: () => string | null;
  clearQueue: () => void;

  // Aliases
  addAlias: (alias: string, command: string) => void;
  removeAlias: (alias: string) => void;
  expandAliases: (command: string) => string;
  clearAliases: () => void;

  // Triggers
  addTrigger: (trigger: CommandTrigger) => void;
  removeTrigger: (id: string) => void;
  toggleTrigger: (id: string) => void;
  findMatchingTriggers: (text: string) => CommandTrigger[];
  clearTriggers: () => void;

  // State management
  reset: () => void;
}

export interface CommandSelectors {
  // Computed properties
  getRecentCommands: (count: number) => CommandHistoryEntry[];
  getSuccessfulCommands: () => CommandHistoryEntry[];
  getCommandStatistics: () => {
    totalCommands: number;
    successfulCommands: number;
    failedCommands: number;
    successRate: number;
    mostUsedCommand: string;
    commandCounts: Record<string, number>;
  };
}

type CommandStore = CommandState & CommandActions & CommandSelectors;

/**
 * **Zustand Store Usage Patterns:**
 *
 * **CORRECT Usage Examples:**
 *
 * ```tsx
 * // ✅ GOOD: Using selectors with shallow comparison for arrays
 * import { shallow } from 'zustand/shallow';
 *
 * function CommandHistory() {
 *   const commandHistory = useCommandStore(state => state.commandHistory, shallow);
 *   const executeCommand = useCommandStore(state => state.executeCommand);
 *
 *   return <div>{commandHistory.map(cmd => <div key={cmd.timestamp}>{cmd.command}</div>)}</div>;
 * }
 *
 * // ✅ GOOD: Using selectors for specific fields
 * function CommandInput() {
 *   const currentCommand = useCommandStore(state => state.currentCommand);
 *   const setCurrentCommand = useCommandStore(state => state.setCurrentCommand);
 *   return <input value={currentCommand} onChange={e => setCurrentCommand(e.target.value)} />;
 * }
 * ```
 *
 * **INCORRECT Usage Examples (Anti-patterns):**
 *
 * ```tsx
 * // ❌ BAD: Subscribing to entire store
 * function MyComponent() {
 *   const commandState = useCommandStore(); // Don't do this!
 *   return <div>{commandState.currentCommand}</div>;
 * }
 *
 * // ❌ BAD: Calling selector functions inside selectors
 * function MyComponent() {
 *   const recent = useCommandStore(state => state.getRecentCommands(10)); // Don't do this!
 *   // Instead, use: const history = useCommandStore(state => state.commandHistory, shallow);
 *   // Then compute: const recent = useMemo(() => history.slice(-10), [history]);
 * }
 * ```
 *
 * **Note on Selector Functions:**
 * - Selector functions like `getRecentCommands()`, `getSuccessfulCommands()`, `getCommandStatistics()`
 *   are kept for backward compatibility but should NOT be called inside component selectors.
 * - Instead, access the underlying state directly and compute derived values in components using `useMemo`.
 */

const MAX_COMMAND_HISTORY = 100;
const MAX_COMMAND_QUEUE = 50; // Limit command queue to prevent unbounded growth (Task 5: Zustand Store Cleanup)

const createInitialState = (): CommandState => ({
  currentCommand: '',
  commandIndex: -1,
  isExecuting: false,
  lastExecutedCommand: null,
  commandHistory: [],
  commandQueue: [],
  aliases: {},
  triggers: [],
});

function computeNavigateHistoryState(state: CommandState, direction: number): Partial<CommandState> | CommandState {
  if (state.commandHistory.length === 0) {
    return state;
  }
  const maxIndex = state.commandHistory.length - 1;
  let newIndex = state.commandIndex + direction;
  if (state.commandIndex === -1 && direction < 0) {
    newIndex = maxIndex;
  }
  newIndex = Math.max(0, Math.min(maxIndex, newIndex));
  return {
    commandIndex: newIndex,
    currentCommand: state.commandHistory[newIndex]?.command || '',
  };
}

function findMatchingTriggersInState(triggers: CommandTrigger[], text: string): CommandTrigger[] {
  return triggers.filter(trigger => {
    if (!trigger.enabled) return false;

    if (trigger.regex) {
      try {
        if (trigger.pattern.length > 200) {
          return false;
        }
        const dangerousPatterns = /\([^)]*\+\)\+|\([^)]*\*\)\*|\([^)]*\?\)\?/;
        if (dangerousPatterns.test(trigger.pattern)) {
          return false;
        }
        // nosemgrep: javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp
        const regex = new RegExp(trigger.pattern, trigger.caseSensitive ? 'g' : 'gi');
        const startTime = performance.now();
        const result = regex.test(text);
        const executionTime = performance.now() - startTime;
        if (executionTime > 100) {
          console.warn('Regex execution took too long, potential ReDoS attack:', trigger.pattern);
          return false;
        }
        return result;
      } catch {
        return false;
      }
    }

    const searchText = trigger.caseSensitive ? text : text.toLowerCase();
    const searchPattern = trigger.caseSensitive ? trigger.pattern : trigger.pattern.toLowerCase();
    return searchText.includes(searchPattern);
  });
}

type CommandStoreSet = (
  partial: CommandStore | Partial<CommandStore> | ((state: CommandStore) => CommandStore | Partial<CommandStore>),
  replace?: false,
  action?: string
) => void;
type CommandStoreGet = () => CommandStore;

function createCommandQueueAndAliasActions(
  set: CommandStoreSet,
  get: CommandStoreGet
): Pick<
  CommandStore,
  | 'addToQueue'
  | 'processNextCommand'
  | 'clearQueue'
  | 'addAlias'
  | 'removeAlias'
  | 'expandAliases'
  | 'clearAliases'
  | 'addTrigger'
  | 'removeTrigger'
  | 'toggleTrigger'
  | 'findMatchingTriggers'
  | 'clearTriggers'
  | 'reset'
  | 'getRecentCommands'
  | 'getSuccessfulCommands'
  | 'getCommandStatistics'
> {
  return {
    addToQueue: (command: string) =>
      set(state => ({ commandQueue: [...state.commandQueue, command].slice(-MAX_COMMAND_QUEUE) }), false, 'addToQueue'),
    processNextCommand: () => {
      let nextCommand: string | null = null;
      set(
        state => {
          if (state.commandQueue.length === 0) return state;
          const [next, ...rest] = state.commandQueue;
          nextCommand = next;
          return { commandQueue: rest };
        },
        false,
        'processNextCommand'
      );
      return nextCommand;
    },
    clearQueue: () => set({ commandQueue: [] }, false, 'clearQueue'),
    addAlias: (alias: string, command: string) =>
      set(state => ({ aliases: { ...state.aliases, [alias]: command } }), false, 'addAlias'),
    removeAlias: (alias: string) =>
      set(
        state => {
          const newAliases = { ...state.aliases };
          delete newAliases[alias];
          return { aliases: newAliases };
        },
        false,
        'removeAlias'
      ),
    expandAliases: (command: string) => {
      const state = get();
      return command
        .split(' ')
        .map(word => state.aliases[word] || word)
        .join(' ');
    },
    clearAliases: () => set({ aliases: {} }, false, 'clearAliases'),
    addTrigger: (trigger: CommandTrigger) =>
      set(state => ({ triggers: [...state.triggers, trigger] }), false, 'addTrigger'),
    removeTrigger: (id: string) =>
      set(state => ({ triggers: state.triggers.filter(trigger => trigger.id !== id) }), false, 'removeTrigger'),
    toggleTrigger: (id: string) =>
      set(
        state => ({
          triggers: state.triggers.map(trigger =>
            trigger.id === id ? { ...trigger, enabled: !trigger.enabled } : trigger
          ),
        }),
        false,
        'toggleTrigger'
      ),
    findMatchingTriggers: (text: string) => findMatchingTriggersInState(get().triggers, text),
    clearTriggers: () => set({ triggers: [] }, false, 'clearTriggers'),
    reset: () => set(createInitialState(), false, 'reset'),
    getRecentCommands: (count: number) => get().commandHistory.slice(-count),
    getSuccessfulCommands: () => get().commandHistory.filter(entry => entry.success),
    getCommandStatistics: () => {
      const state = get();
      const totalCommands = state.commandHistory.length;
      const successfulCommands = state.commandHistory.filter(entry => entry.success).length;
      const failedCommands = totalCommands - successfulCommands;
      const successRate = totalCommands > 0 ? successfulCommands / totalCommands : 0;
      const commandCounts: Record<string, number> = {};
      state.commandHistory.forEach(entry => {
        commandCounts[entry.command] = (commandCounts[entry.command] || 0) + 1;
      });
      const mostUsedCommand = Object.entries(commandCounts).sort(([, a], [, b]) => b - a)[0]?.[0] || '';
      return { totalCommands, successfulCommands, failedCommands, successRate, mostUsedCommand, commandCounts };
    },
  };
}

function createCommandStoreSlice(set: CommandStoreSet, get: CommandStoreGet): CommandStore {
  return {
    ...createInitialState(),
    setCurrentCommand: (command: string) => set({ currentCommand: command }, false, 'setCurrentCommand'),
    clearCurrentCommand: () => set({ currentCommand: '', commandIndex: -1 }, false, 'clearCurrentCommand'),
    appendToCommand: (text: string) =>
      set(state => ({ currentCommand: state.currentCommand + text }), false, 'appendToCommand'),
    addToHistory: (command: string, success = true, result?: string) =>
      set(
        state => {
          const newEntry: CommandHistoryEntry = { command, timestamp: Date.now(), success, result };
          return {
            commandHistory: [...state.commandHistory, newEntry].slice(-MAX_COMMAND_HISTORY),
            commandIndex: -1,
          };
        },
        false,
        'addToHistory'
      ),
    clearHistory: () => set({ commandHistory: [], commandIndex: -1 }, false, 'clearHistory'),
    navigateHistory: (direction: number) =>
      set(state => computeNavigateHistoryState(state, direction), false, 'navigateHistory'),
    setExecuting: (executing: boolean) => set({ isExecuting: executing }, false, 'setExecuting'),
    setLastExecutedCommand: (command: string | null) =>
      set({ lastExecutedCommand: command }, false, 'setLastExecutedCommand'),
    executeCommand: (command: string) =>
      set(
        state => {
          const expandedCommand = get().expandAliases(command);
          return {
            isExecuting: true,
            lastExecutedCommand: expandedCommand,
            currentCommand: '',
            commandIndex: -1,
            commandHistory: [
              ...state.commandHistory,
              { command: expandedCommand, timestamp: Date.now(), success: true },
            ].slice(-MAX_COMMAND_HISTORY),
          };
        },
        false,
        'executeCommand'
      ),
    ...createCommandQueueAndAliasActions(set, get),
  };
}

export const useCommandStore = create<CommandStore>()(
  devtools(createCommandStoreSlice, {
    name: 'command-store',
    enabled: import.meta.env.MODE === 'development',
    partialize: (state: CommandStore) => ({
      commandHistory: state.commandHistory,
      aliases: state.aliases,
      triggers: state.triggers,
    }),
  })
);
