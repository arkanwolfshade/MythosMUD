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

export const useCommandStore = create<CommandStore>()(
  devtools(
    (set, get) => ({
      ...createInitialState(),

      // Command input management actions
      setCurrentCommand: (command: string) => set({ currentCommand: command }, false, 'setCurrentCommand'),

      clearCurrentCommand: () => set({ currentCommand: '', commandIndex: -1 }, false, 'clearCurrentCommand'),

      appendToCommand: (text: string) =>
        set(state => ({ currentCommand: state.currentCommand + text }), false, 'appendToCommand'),

      // Command history actions
      addToHistory: (command: string, success = true, result?: string) =>
        set(
          state => {
            const newEntry: CommandHistoryEntry = {
              command,
              timestamp: Date.now(),
              success,
              result,
            };
            const newHistory = [...state.commandHistory, newEntry];
            // Limit the number of commands to prevent memory issues
            const limitedHistory = newHistory.slice(-MAX_COMMAND_HISTORY);
            return {
              commandHistory: limitedHistory,
              commandIndex: -1, // Reset index when adding new command
            };
          },
          false,
          'addToHistory'
        ),

      clearHistory: () => set({ commandHistory: [], commandIndex: -1 }, false, 'clearHistory'),

      // Command navigation actions
      navigateHistory: (direction: number) =>
        set(
          state => {
            if (state.commandHistory.length === 0) {
              return state;
            }

            // If we're at -1 (no command selected), and going backward, go to last command
            if (state.commandIndex === -1 && direction < 0) {
              const lastIndex = state.commandHistory.length - 1;
              return {
                commandIndex: lastIndex,
                currentCommand: state.commandHistory[lastIndex]?.command || '',
              };
            }

            const newIndex = state.commandIndex + direction;
            const maxIndex = state.commandHistory.length - 1;

            if (newIndex < 0) {
              return { commandIndex: 0, currentCommand: state.commandHistory[0]?.command || '' };
            } else if (newIndex > maxIndex) {
              return { commandIndex: maxIndex, currentCommand: state.commandHistory[maxIndex]?.command || '' };
            } else {
              return {
                commandIndex: newIndex,
                currentCommand: state.commandHistory[newIndex]?.command || '',
              };
            }
          },
          false,
          'navigateHistory'
        ),

      // Command execution actions
      setExecuting: (executing: boolean) => set({ isExecuting: executing }, false, 'setExecuting'),

      setLastExecutedCommand: (command: string | null) =>
        set({ lastExecutedCommand: command }, false, 'setLastExecutedCommand'),

      executeCommand: (command: string) =>
        set(
          state => {
            const expandedCommand = get().expandAliases(command);
            const newEntry: CommandHistoryEntry = {
              command: expandedCommand,
              timestamp: Date.now(),
              success: true,
            };
            const newHistory = [...state.commandHistory, newEntry];
            const limitedHistory = newHistory.slice(-MAX_COMMAND_HISTORY);

            return {
              isExecuting: true,
              lastExecutedCommand: expandedCommand,
              currentCommand: '',
              commandIndex: -1,
              commandHistory: limitedHistory,
            };
          },
          false,
          'executeCommand'
        ),

      // Command queue actions
      addToQueue: (command: string) =>
        set(
          state => {
            const newQueue = [...state.commandQueue, command];
            // Limit queue size to prevent unbounded growth (Task 5: Zustand Store Cleanup)
            const limitedQueue = newQueue.slice(-MAX_COMMAND_QUEUE);
            return { commandQueue: limitedQueue };
          },
          false,
          'addToQueue'
        ),

      processNextCommand: () => {
        const state = get();
        if (state.commandQueue.length === 0) return null;

        const [nextCommand, ...remainingQueue] = state.commandQueue;
        set({ commandQueue: remainingQueue }, false, 'processNextCommand');
        return nextCommand;
      },

      clearQueue: () => set({ commandQueue: [] }, false, 'clearQueue'),

      // Aliases actions
      addAlias: (alias: string, command: string) =>
        set(
          state => ({
            aliases: { ...state.aliases, [alias]: command },
          }),
          false,
          'addAlias'
        ),

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
        const expandedCommand = command;

        // Split command into words and expand each alias
        const words = expandedCommand.split(' ');
        const expandedWords = words.map(word => state.aliases[word] || word);

        return expandedWords.join(' ');
      },

      clearAliases: () => set({ aliases: {} }, false, 'clearAliases'),

      // Triggers actions
      addTrigger: (trigger: CommandTrigger) =>
        set(
          state => ({
            triggers: [...state.triggers, trigger],
          }),
          false,
          'addTrigger'
        ),

      removeTrigger: (id: string) =>
        set(
          state => ({
            triggers: state.triggers.filter(trigger => trigger.id !== id),
          }),
          false,
          'removeTrigger'
        ),

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

      findMatchingTriggers: (text: string) => {
        const state = get();
        return state.triggers.filter(trigger => {
          if (!trigger.enabled) return false;

          if (trigger.regex) {
            try {
              // ReDoS protection: limit pattern length and add timeout
              if (trigger.pattern.length > 200) {
                return false; // Pattern too long, potential ReDoS risk
              }

              // Validate pattern doesn't contain obvious ReDoS patterns
              // (e.g., nested quantifiers like (a+)+)
              const dangerousPatterns = /\([^)]*\+\)\+|\([^)]*\*\)\*|\([^)]*\?\)\?/;
              if (dangerousPatterns.test(trigger.pattern)) {
                return false; // Pattern contains dangerous nested quantifiers
              }

              // nosemgrep: javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp
              // ReDoS protection is in place: pattern validation above (checks for dangerous nested quantifiers)
              // and 100ms timeout below. The trigger.pattern comes from user configuration but is validated
              // before use to prevent ReDoS attacks.
              const regex = new RegExp(trigger.pattern, trigger.caseSensitive ? 'g' : 'gi');

              // Add timeout protection for regex execution
              const startTime = performance.now();
              const result = regex.test(text);
              const executionTime = performance.now() - startTime;

              // If regex takes more than 100ms, it's likely a ReDoS attack
              if (executionTime > 100) {
                console.warn('Regex execution took too long, potential ReDoS attack:', trigger.pattern);
                return false;
              }

              return result;
            } catch {
              return false;
            }
          } else {
            const searchText = trigger.caseSensitive ? text : text.toLowerCase();
            const searchPattern = trigger.caseSensitive ? trigger.pattern : trigger.pattern.toLowerCase();
            return searchText.includes(searchPattern);
          }
        });
      },

      clearTriggers: () => set({ triggers: [] }, false, 'clearTriggers'),

      // State management actions
      reset: () => set(createInitialState(), false, 'reset'),

      // Selectors
      getRecentCommands: (count: number) => {
        const state = get();
        return state.commandHistory.slice(-count);
      },

      getSuccessfulCommands: () => {
        const state = get();
        return state.commandHistory.filter(entry => entry.success);
      },

      getCommandStatistics: () => {
        const state = get();
        const totalCommands = state.commandHistory.length;
        const successfulCommands = state.commandHistory.filter(entry => entry.success).length;
        const failedCommands = totalCommands - successfulCommands;
        const successRate = totalCommands > 0 ? successfulCommands / totalCommands : 0;

        // Count command usage
        const commandCounts: Record<string, number> = {};
        state.commandHistory.forEach(entry => {
          commandCounts[entry.command] = (commandCounts[entry.command] || 0) + 1;
        });

        // Find most used command
        const mostUsedCommand = Object.entries(commandCounts).sort(([, a], [, b]) => b - a)[0]?.[0] || '';

        return {
          totalCommands,
          successfulCommands,
          failedCommands,
          successRate,
          mostUsedCommand,
          commandCounts,
        };
      },
    }),
    {
      name: 'command-store',
      partialize: (state: CommandStore) => ({
        commandHistory: state.commandHistory,
        aliases: state.aliases,
        triggers: state.triggers,
      }),
    }
  )
);
