import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useCommandStore } from '../commandStore';

describe('Command Store', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    // Reset store state
    useCommandStore.getState().reset();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Initial State', () => {
    it('should have correct initial state', () => {
      const state = useCommandStore.getState();

      expect(state.commandHistory).toEqual([]);
      expect(state.currentCommand).toBe('');
      expect(state.commandIndex).toBe(-1);
      expect(state.isExecuting).toBe(false);
      expect(state.lastExecutedCommand).toBe(null);
      expect(state.commandQueue).toEqual([]);
      expect(state.aliases).toEqual({});
      expect(state.triggers).toEqual([]);
    });
  });

  describe('Command Input Management', () => {
    it('should set current command', () => {
      const { result } = renderHook(() => useCommandStore());
      const command = 'look around';

      act(() => {
        result.current.setCurrentCommand(command);
      });

      expect(result.current.currentCommand).toBe(command);
    });

    it('should clear current command', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.setCurrentCommand('test command');
        result.current.clearCurrentCommand();
      });

      expect(result.current.currentCommand).toBe('');
    });

    it('should append to current command', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.setCurrentCommand('look');
        result.current.appendToCommand(' around');
      });

      expect(result.current.currentCommand).toBe('look around');
    });
  });

  describe('Command History', () => {
    it('should add command to history', () => {
      const { result } = renderHook(() => useCommandStore());
      const command = 'look around';

      act(() => {
        result.current.addToHistory(command);
      });

      expect(result.current.commandHistory).toHaveLength(1);
      expect(result.current.commandHistory[0]).toEqual({
        command,
        timestamp: expect.any(Number),
        success: true,
      });
    });

    it('should add command with success status', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToHistory('look around', false);
      });

      expect(result.current.commandHistory[0].success).toBe(false);
    });

    it('should limit command history size', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        // Add more commands than the limit (assuming limit is 100)
        for (let i = 0; i < 150; i++) {
          result.current.addToHistory(`command ${i}`);
        }
      });

      // Should not exceed the maximum number of commands
      expect(result.current.commandHistory.length).toBeLessThanOrEqual(100);
    });

    it('should clear command history', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToHistory('command 1');
        result.current.addToHistory('command 2');
        result.current.clearHistory();
      });

      expect(result.current.commandHistory).toEqual([]);
    });
  });

  describe('Command Navigation', () => {
    it('should navigate through command history', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToHistory('command 1');
        result.current.addToHistory('command 2');
        result.current.addToHistory('command 3');
      });

      // Navigate to previous command (should go to last command)
      act(() => {
        result.current.navigateHistory(-1);
      });

      expect(result.current.commandIndex).toBe(2); // Last command
      expect(result.current.currentCommand).toBe('command 3');

      // Navigate to previous command
      act(() => {
        result.current.navigateHistory(-1);
      });

      expect(result.current.commandIndex).toBe(1);
      expect(result.current.currentCommand).toBe('command 2');

      // Navigate to next command
      act(() => {
        result.current.navigateHistory(1);
      });

      expect(result.current.commandIndex).toBe(2);
      expect(result.current.currentCommand).toBe('command 3');
    });

    it('should not navigate beyond history bounds', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToHistory('command 1');
        result.current.navigateHistory(-1);
        result.current.navigateHistory(-1); // Try to go beyond
      });

      expect(result.current.commandIndex).toBe(0); // Should stay at first command

      act(() => {
        result.current.navigateHistory(1);
        result.current.navigateHistory(1); // Try to go beyond
      });

      expect(result.current.commandIndex).toBe(0); // Should stay at first command
    });

    it('should reset command index when adding new command', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToHistory('command 1');
        result.current.navigateHistory(-1);
        result.current.addToHistory('command 2');
      });

      expect(result.current.commandIndex).toBe(-1); // Should reset to -1
    });
  });

  describe('Command Execution', () => {
    it('should set executing state', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.setExecuting(true);
      });

      expect(result.current.isExecuting).toBe(true);
    });

    it('should set last executed command', () => {
      const { result } = renderHook(() => useCommandStore());
      const command = 'look around';

      act(() => {
        result.current.setLastExecutedCommand(command);
      });

      expect(result.current.lastExecutedCommand).toBe(command);
    });

    it('should execute command and add to history', () => {
      const { result } = renderHook(() => useCommandStore());
      const command = 'look around';

      act(() => {
        result.current.executeCommand(command);
      });

      expect(result.current.isExecuting).toBe(true);
      expect(result.current.lastExecutedCommand).toBe(command);
      expect(result.current.commandHistory).toHaveLength(1);
      expect(result.current.commandHistory[0].command).toBe(command);
    });
  });

  describe('Command Queue', () => {
    it('should add command to queue', () => {
      const { result } = renderHook(() => useCommandStore());
      const command = 'look around';

      act(() => {
        result.current.addToQueue(command);
      });

      expect(result.current.commandQueue).toHaveLength(1);
      expect(result.current.commandQueue[0]).toBe(command);
    });

    it('should add multiple commands to queue', () => {
      const { result } = renderHook(() => useCommandStore());
      const commands = ['look around', 'go north', 'inventory'];

      act(() => {
        commands.forEach(command => result.current.addToQueue(command));
      });

      expect(result.current.commandQueue).toEqual(commands);
    });

    it('should process next command from queue', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToQueue('command 1');
        result.current.addToQueue('command 2');
        result.current.addToQueue('command 3');
      });

      act(() => {
        const nextCommand = result.current.processNextCommand();
        expect(nextCommand).toBe('command 1');
      });

      expect(result.current.commandQueue).toEqual(['command 2', 'command 3']);
    });

    it('should return null when queue is empty', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        const nextCommand = result.current.processNextCommand();
        expect(nextCommand).toBe(null);
      });
    });

    it('should clear command queue', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToQueue('command 1');
        result.current.addToQueue('command 2');
        result.current.clearQueue();
      });

      expect(result.current.commandQueue).toEqual([]);
    });
  });

  describe('Aliases', () => {
    it('should add alias', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addAlias('l', 'look around');
      });

      expect(result.current.aliases).toEqual({
        l: 'look around',
      });
    });

    it('should add multiple aliases', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addAlias('l', 'look around');
        result.current.addAlias('n', 'go north');
        result.current.addAlias('s', 'go south');
      });

      expect(result.current.aliases).toEqual({
        l: 'look around',
        n: 'go north',
        s: 'go south',
      });
    });

    it('should remove alias', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addAlias('l', 'look around');
        result.current.removeAlias('l');
      });

      expect(result.current.aliases).toEqual({});
    });

    it('should expand alias in command', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addAlias('l', 'look around');
      });

      const expandedCommand = result.current.expandAliases('l');
      expect(expandedCommand).toBe('look around');
    });

    it('should expand multiple aliases in command', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addAlias('l', 'look');
        result.current.addAlias('a', 'around');
      });

      const expandedCommand = result.current.expandAliases('l a');
      expect(expandedCommand).toBe('look around');
    });

    it('should not expand unknown aliases', () => {
      const { result } = renderHook(() => useCommandStore());

      const expandedCommand = result.current.expandAliases('unknown command');
      expect(expandedCommand).toBe('unknown command');
    });

    it('should clear all aliases', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addAlias('l', 'look around');
        result.current.addAlias('n', 'go north');
        result.current.clearAliases();
      });

      expect(result.current.aliases).toEqual({});
    });
  });

  describe('Triggers', () => {
    it('should add trigger', () => {
      const { result } = renderHook(() => useCommandStore());
      const trigger = {
        id: 'trigger-1',
        pattern: 'You see:',
        action: 'look around',
        enabled: true,
      };

      act(() => {
        result.current.addTrigger(trigger);
      });

      expect(result.current.triggers).toHaveLength(1);
      expect(result.current.triggers[0]).toEqual(trigger);
    });

    it('should add multiple triggers', () => {
      const { result } = renderHook(() => useCommandStore());
      const triggers = [
        {
          id: 'trigger-1',
          pattern: 'You see:',
          action: 'look around',
          enabled: true,
        },
        {
          id: 'trigger-2',
          pattern: 'A monster attacks!',
          action: 'attack monster',
          enabled: true,
        },
      ];

      act(() => {
        triggers.forEach(trigger => result.current.addTrigger(trigger));
      });

      expect(result.current.triggers).toEqual(triggers);
    });

    it('should remove trigger', () => {
      const { result } = renderHook(() => useCommandStore());
      const trigger = {
        id: 'trigger-1',
        pattern: 'You see:',
        action: 'look around',
        enabled: true,
      };

      act(() => {
        result.current.addTrigger(trigger);
        result.current.removeTrigger('trigger-1');
      });

      expect(result.current.triggers).toEqual([]);
    });

    it('should toggle trigger enabled state', () => {
      const { result } = renderHook(() => useCommandStore());
      const trigger = {
        id: 'trigger-1',
        pattern: 'You see:',
        action: 'look around',
        enabled: true,
      };

      act(() => {
        result.current.addTrigger(trigger);
        result.current.toggleTrigger('trigger-1');
      });

      expect(result.current.triggers[0].enabled).toBe(false);
    });

    it('should find matching triggers', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addTrigger({
          id: 'trigger-1',
          pattern: 'You see:',
          action: 'look around',
          enabled: true,
        });
        result.current.addTrigger({
          id: 'trigger-2',
          pattern: 'A monster attacks!',
          action: 'attack monster',
          enabled: true,
        });
      });

      const matchingTriggers = result.current.findMatchingTriggers('You see: a door');
      expect(matchingTriggers).toHaveLength(1);
      expect(matchingTriggers[0].id).toBe('trigger-1');
    });

    it('should not find disabled triggers', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addTrigger({
          id: 'trigger-1',
          pattern: 'You see:',
          action: 'look around',
          enabled: false,
        });
      });

      const matchingTriggers = result.current.findMatchingTriggers('You see: a door');
      expect(matchingTriggers).toHaveLength(0);
    });

    it('should clear all triggers', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addTrigger({
          id: 'trigger-1',
          pattern: 'You see:',
          action: 'look around',
          enabled: true,
        });
        result.current.addTrigger({
          id: 'trigger-2',
          pattern: 'A monster attacks!',
          action: 'attack monster',
          enabled: true,
        });
        result.current.clearTriggers();
      });

      expect(result.current.triggers).toEqual([]);
    });
  });

  describe('State Reset', () => {
    it('should reset all state to initial values', () => {
      const { result } = renderHook(() => useCommandStore());

      // Modify state
      act(() => {
        result.current.addToHistory('command 1');
        result.current.setCurrentCommand('test command');
        result.current.setExecuting(true);
        result.current.addToQueue('queued command');
        result.current.addAlias('l', 'look around');
        result.current.addTrigger({
          id: 'trigger-1',
          pattern: 'You see:',
          action: 'look around',
          enabled: true,
        });
      });

      // Reset state
      act(() => {
        result.current.reset();
      });

      expect(result.current.commandHistory).toEqual([]);
      expect(result.current.currentCommand).toBe('');
      expect(result.current.commandIndex).toBe(-1);
      expect(result.current.isExecuting).toBe(false);
      expect(result.current.lastExecutedCommand).toBe(null);
      expect(result.current.commandQueue).toEqual([]);
      expect(result.current.aliases).toEqual({});
      expect(result.current.triggers).toEqual([]);
    });
  });

  describe('Selectors', () => {
    it('should provide recent commands selector', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToHistory('command 1');
        result.current.addToHistory('command 2');
        result.current.addToHistory('command 3');
        result.current.addToHistory('command 4');
        result.current.addToHistory('command 5');
      });

      const recentCommands = result.current.getRecentCommands(3);
      expect(recentCommands).toHaveLength(3);
      expect(recentCommands[0].command).toBe('command 3'); // Most recent
      expect(recentCommands[2].command).toBe('command 5'); // Oldest of the 3
    });

    it('should provide successful commands selector', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToHistory('command 1', true);
        result.current.addToHistory('command 2', false);
        result.current.addToHistory('command 3', true);
        result.current.addToHistory('command 4', false);
      });

      const successfulCommands = result.current.getSuccessfulCommands();
      expect(successfulCommands).toHaveLength(2);
      expect(successfulCommands[0].command).toBe('command 1');
      expect(successfulCommands[1].command).toBe('command 3');
    });

    it('should provide command statistics selector', () => {
      const { result } = renderHook(() => useCommandStore());

      act(() => {
        result.current.addToHistory('look', true);
        result.current.addToHistory('go north', true);
        result.current.addToHistory('look', true);
        result.current.addToHistory('invalid command', false);
      });

      const stats = result.current.getCommandStatistics();

      expect(stats).toEqual({
        totalCommands: 4,
        successfulCommands: 3,
        failedCommands: 1,
        successRate: 0.75,
        mostUsedCommand: 'look',
        commandCounts: {
          look: 2,
          'go north': 1,
          'invalid command': 1,
        },
      });
    });
  });
});
