import React, { useEffect, useRef, useState } from 'react';
import { AVAILABLE_CHANNELS, DEFAULT_CHANNEL } from '../../config/channels';
import { ChannelSelector } from '../ui/ChannelSelector';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';
import { TerminalInput } from '../ui/TerminalInput';

interface CommandPanelProps {
  commandHistory: string[];
  onSendCommand: (command: string) => void;
  onClearHistory?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  placeholder?: string;
  selectedChannel?: string;
  onChannelSelect?: (channelId: string) => void;
}

export const CommandPanel: React.FC<CommandPanelProps> = ({
  commandHistory,
  onSendCommand,
  onClearHistory,
  disabled = false,
  isConnected = true,
  placeholder = "Enter game command (e.g., 'look', 'inventory', 'go north')...",
  selectedChannel = DEFAULT_CHANNEL,
  onChannelSelect,
}) => {
  const [commandInput, setCommandInput] = useState('');
  const [historyIndex, setHistoryIndex] = useState(-1);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [currentChannel, setCurrentChannel] = useState(selectedChannel);
  const inputRef = useRef<HTMLInputElement>(null);

  // Focus input on mount
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  // Update current channel when prop changes
  useEffect(() => {
    setCurrentChannel(selectedChannel);
  }, [selectedChannel]);

  const handleCommandSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!commandInput.trim() || disabled) return;

    let command = commandInput.trim();

    // If the command doesn't start with a slash and we're not on the 'say' channel,
    // prepend the channel command
    if (!command.startsWith('/') && currentChannel !== 'say') {
      const channel = AVAILABLE_CHANNELS.find(c => c.id === currentChannel);
      if (channel?.shortcut) {
        command = `/${channel.shortcut} ${command}`;
      }
    }

    onSendCommand(command);
    setCommandInput('');
    setHistoryIndex(-1);
    setShowSuggestions(false);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (historyIndex < commandHistory.length - 1) {
        const newIndex = historyIndex + 1;
        setHistoryIndex(newIndex);
        setCommandInput(commandHistory[commandHistory.length - 1 - newIndex]);
      }
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex > 0) {
        const newIndex = historyIndex - 1;
        setHistoryIndex(newIndex);
        setCommandInput(commandHistory[commandHistory.length - 1 - newIndex]);
      } else if (historyIndex === 0) {
        setHistoryIndex(-1);
        setCommandInput('');
      }
    } else if (e.key === 'Tab') {
      e.preventDefault();
      // Auto-complete logic could be added here
    }
  };

  const handleHistoryClick = (command: string) => {
    setCommandInput(command);
    inputRef.current?.focus();
  };

  const handleChannelSelect = (channelId: string) => {
    setCurrentChannel(channelId);
    onChannelSelect?.(channelId);
  };

  const formatTimestamp = (index: number) => {
    const timeAgo = commandHistory.length - index;
    if (timeAgo === 1) return 'Just now';
    if (timeAgo < 60) return `${timeAgo} commands ago`;
    return `${Math.floor(timeAgo / 60)}m ago`;
  };

  const getChannelQuickCommands = () => {
    const channel = AVAILABLE_CHANNELS.find(c => c.id === currentChannel);
    if (!channel) return [];

    const baseCommands = [
      { command: 'look', icon: MythosIcons.look, description: 'Look around' },
      { command: 'inventory', icon: MythosIcons.inventory, description: 'Check inventory' },
      { command: 'help', icon: MythosIcons.help, description: 'Get help' },
      { command: 'who', icon: MythosIcons.character, description: 'Who is online' },
      { command: 'n', icon: MythosIcons.exit, description: 'Go north' },
      { command: 's', icon: MythosIcons.exit, description: 'Go south' },
      { command: 'e', icon: MythosIcons.exit, description: 'Go east' },
      { command: 'w', icon: MythosIcons.exit, description: 'Go west' },
      { command: 'up', icon: MythosIcons.exit, description: 'Go up' },
      { command: 'down', icon: MythosIcons.exit, description: 'Go down' },
      { command: 'status', icon: MythosIcons.stats, description: 'Check status' },
      { command: 'get', icon: MythosIcons.inventory, description: 'Get item' },
    ];

    // Add channel-specific commands
    if (channel.shortcut) {
      const channelCommands = [`/${channel.shortcut} Hello!`, `/${channel.shortcut} How is everyone?`];

      channelCommands.forEach(channelCommand => {
        baseCommands.unshift({
          command: channelCommand,
          icon: channel.icon,
          description: `${channel.name} channel message`,
        });
      });
    }

    return baseCommands;
  };

  const quickCommands = getChannelQuickCommands();

  const commonCommands = [
    'look',
    'inventory',
    'help',
    'who',
    'n',
    's',
    'e',
    'w',
    'ne',
    'nw',
    'se',
    'sw',
    'up',
    'down',
    'get',
    'drop',
    'wear',
    'remove',
    'cast',
    'attack',
    'flee',
    'status',
    'stats',
  ];

  const getSuggestions = (input: string) => {
    if (!input.trim()) return [];
    return commonCommands.filter(cmd => cmd.toLowerCase().startsWith(input.toLowerCase())).slice(0, 5);
  };

  const suggestions = getSuggestions(commandInput);

  return (
    <div className="h-full flex flex-col font-mono">
      {/* Command Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center gap-2">
          <EldritchIcon name={MythosIcons.search} size={20} variant="primary" />
          <h3 className="text-mythos-terminal-primary font-bold">Commands</h3>
        </div>
        <div className="flex items-center gap-2">
          {onClearHistory && (
            <TerminalButton variant="secondary" size="sm" onClick={onClearHistory} className="p-2 h-8 w-8">
              <EldritchIcon name={MythosIcons.clear} size={14} variant="error" />
            </TerminalButton>
          )}
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={() => setShowSuggestions(!showSuggestions)}
            className="p-2 h-8 w-8"
          >
            <EldritchIcon name={MythosIcons.help} size={14} variant="primary" />
          </TerminalButton>
        </div>
      </div>

      {/* Channel Selector */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center gap-2">
          <span className="text-sm text-mythos-terminal-text-secondary">Channel:</span>
          <ChannelSelector
            channels={AVAILABLE_CHANNELS}
            selectedChannel={currentChannel}
            onChannelSelect={handleChannelSelect}
            disabled={disabled || !isConnected}
          />
        </div>
      </div>

      {/* Command Input Area */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <form onSubmit={handleCommandSubmit} className="space-y-3">
          <div className="flex gap-2">
            <div className="flex-1 relative">
              <TerminalInput
                // ref={inputRef}
                value={commandInput}
                onChange={setCommandInput}
                onKeyDown={handleKeyDown}
                placeholder={placeholder}
                disabled={disabled || !isConnected}
                className="w-full"
                onFocus={() => setShowSuggestions(true)}
              />
              {suggestions.length > 0 && showSuggestions && (
                <div className="absolute top-full left-0 right-0 mt-1 bg-mythos-terminal-surface border border-gray-700 rounded shadow-lg z-10">
                  {suggestions.map((suggestion, index) => (
                    <div
                      key={index}
                      className="px-3 py-2 hover:bg-mythos-terminal-background cursor-pointer text-sm"
                      onClick={() => {
                        setCommandInput(suggestion);
                        setShowSuggestions(false);
                        inputRef.current?.focus();
                      }}
                    >
                      <span className="text-mythos-terminal-primary">{suggestion}</span>
                    </div>
                  ))}
                </div>
              )}
            </div>
            <TerminalButton
              type="submit"
              variant="primary"
              disabled={!commandInput.trim() || disabled || !isConnected}
              className="px-4"
            >
              <EldritchIcon name={MythosIcons.chat} size={16} className="mr-2" />
              Send
            </TerminalButton>
          </div>
        </form>
      </div>

      {/* Command History */}
      <div className="flex-1 flex flex-col">
        <div className="flex items-center justify-between p-2 border-b border-gray-700 bg-mythos-terminal-background">
          <span className="text-sm text-mythos-terminal-text-secondary">Command History ({commandHistory.length})</span>
          <div className="flex items-center gap-1">
            <EldritchIcon name={MythosIcons.clock} size={12} variant="secondary" />
            <span className="text-xs text-mythos-terminal-text-secondary">Use ↑↓ to navigate</span>
          </div>
        </div>

        <div className="flex-1 overflow-auto bg-mythos-terminal-background border border-gray-700 rounded">
          {commandHistory.length === 0 ? (
            <div className="flex items-center justify-center h-full p-4">
              <div className="text-center space-y-2">
                <EldritchIcon name={MythosIcons.search} size={32} variant="secondary" className="mx-auto opacity-50" />
                <p className="text-mythos-terminal-text-secondary text-sm">No command history yet.</p>
                <p className="text-mythos-terminal-text-secondary text-xs">Start typing commands to see them here.</p>
              </div>
            </div>
          ) : (
            <div className="space-y-1 p-2">
              {commandHistory
                .slice()
                .reverse()
                .map((command, index) => (
                  <div
                    key={index}
                    onClick={() => handleHistoryClick(command)}
                    className="p-2 bg-mythos-terminal-surface border border-gray-700 rounded cursor-pointer hover:border-mythos-terminal-primary/30 transition-colors duration-200"
                  >
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="text-sm text-mythos-terminal-text font-mono">&gt; {command}</div>
                        <div className="text-xs text-mythos-terminal-text-secondary mt-1">{formatTimestamp(index)}</div>
                      </div>
                      <EldritchIcon name={MythosIcons.exit} size={12} variant="secondary" className="opacity-50" />
                    </div>
                  </div>
                ))}
            </div>
          )}
        </div>
      </div>

      {/* Quick Commands */}
      <div className="p-3 border-t border-gray-700 bg-mythos-terminal-surface">
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <EldritchIcon name={MythosIcons.move} size={14} variant="primary" />
            <span className="text-sm text-mythos-terminal-text-secondary font-bold">
              {AVAILABLE_CHANNELS.find(c => c.id === currentChannel)?.name} Channel:
            </span>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
            {quickCommands.map(({ command, icon }) => (
              <TerminalButton
                key={command}
                variant="secondary"
                size="sm"
                onClick={() => {
                  setCommandInput(command);
                  inputRef.current?.focus();
                }}
                disabled={disabled || !isConnected}
                className="flex items-center gap-2 text-xs"
              >
                <EldritchIcon name={icon} size={12} variant="primary" />
                <span>{command}</span>
              </TerminalButton>
            ))}
          </div>

          <div className="text-xs text-mythos-terminal-text-secondary">
            <span className="font-bold">Tip:</span> Use Tab for auto-completion, ↑↓ for history navigation
          </div>
        </div>
      </div>

      {/* Command Statistics */}
      <div className="p-2 border-t border-gray-700 bg-mythos-terminal-background">
        <div className="flex items-center justify-between text-xs text-mythos-terminal-text-secondary">
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.stats} size={12} variant="secondary" />
              <span>{commandHistory.length} commands</span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.connection} size={12} variant="secondary" />
              <span>Ready</span>
            </div>
          </div>
          <div className="text-xs opacity-75">MythosMUD Terminal</div>
        </div>
      </div>
    </div>
  );
};
