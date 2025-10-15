import React, { useEffect, useRef, useState } from 'react';
import { AVAILABLE_CHANNELS, DEFAULT_CHANNEL } from '../../config/channels';
import { ChannelSelector } from '../ui/ChannelSelector';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { LogoutButton } from '../ui/LogoutButton';
import { TerminalButton } from '../ui/TerminalButton';
import { TerminalInput } from '../ui/TerminalInput';

interface CommandPanelProps {
  commandHistory: string[];
  onSendCommand: (command: string) => void;
  onClearHistory?: () => void;
  onLogout?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  isLoggingOut?: boolean;
  placeholder?: string;
  selectedChannel?: string;
  onChannelSelect?: (channelId: string) => void;
}

export const CommandPanel: React.FC<CommandPanelProps> = ({
  commandHistory,
  onSendCommand,
  onClearHistory,
  onLogout,
  disabled = false,
  isConnected = true,
  isLoggingOut = false,
  placeholder = "Enter game command (e.g., 'look', 'inventory', 'go north')...",
  selectedChannel = DEFAULT_CHANNEL,
  // onChannelSelect removed - not used in current implementation
}) => {
  const [commandInput, setCommandInput] = useState('');

  // Debug logging for isConnected prop
  if (process.env.NODE_ENV === 'development') {
    console.debug('CommandPanel received isConnected prop', {
      isConnected,
      disabled,
      commandInputLength: commandInput?.length || 0,
      buttonDisabled: !commandInput?.trim() || disabled || !isConnected,
      buttonDisabledReason: {
        noCommand: !commandInput?.trim(),
        panelDisabled: disabled,
        notConnected: !isConnected,
      },
    });
  }
  // historyIndex removed - not used in current implementation
  // showSuggestions removed - not used in current implementation
  const [currentChannel, setCurrentChannel] = useState(selectedChannel);
  const inputRef = useRef<HTMLInputElement>(null);

  // Focus input on mount
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  // Handle keyboard shortcuts
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Handle Ctrl+Q for logout
      if (e.ctrlKey && e.key === 'q' && onLogout && !disabled && isConnected) {
        e.preventDefault();
        onLogout();
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [onLogout, disabled, isConnected]);

  // Update current channel when prop changes
  useEffect(() => {
    setCurrentChannel(selectedChannel);
  }, [selectedChannel]);

  const handleCommandSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!commandInput.trim() || disabled) return;

    let command = commandInput.trim();

    // List of standalone system commands that should never have channel shortcuts prepended
    const standaloneCommands = [
      'admin',
      'alias',
      'aliases',
      'emote',
      'go',
      'goto',
      'help',
      'inventory',
      'look',
      'logout',
      'me',
      'mute',
      'pose',
      'quit',
      'status',
      'teleport',
      'unalias',
      'unmute',
      'w',
      'whisper',
      'who',
    ];
    const firstWord = command.split(/\s+/)[0].toLowerCase();
    const isStandaloneCommand = standaloneCommands.includes(firstWord);

    // If the command doesn't start with a slash and we're not on the 'say' channel,
    // prepend the channel command ONLY if:
    // 1. The command doesn't already start with the channel name
    // 2. The command is NOT a standalone system command
    if (!command.startsWith('/') && currentChannel !== 'say' && !isStandaloneCommand) {
      const channel = AVAILABLE_CHANNELS.find(c => c.id === currentChannel);
      // Don't prepend if command already starts with the channel name
      const commandLower = command.toLowerCase();
      const channelName = channel?.id || '';
      const alreadyHasChannelPrefix = commandLower.startsWith(channelName + ' ') || commandLower === channelName;

      if (channel?.shortcut && !alreadyHasChannelPrefix) {
        command = `/${channel.shortcut} ${command}`;
      }
    }

    onSendCommand(command);
    setCommandInput('');
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleCommandSubmit(e);
    }
  };

  // handleKeyDown removed - not used in current implementation
  // TODO: Implement keyboard navigation for command history

  // handleHistoryClick removed - not used in current implementation
  // TODO: Implement clickable command history

  // handleChannelSelect removed - not used in current implementation
  // TODO: Implement channel selection callback

  // formatTimestamp removed - not used in current implementation
  // TODO: Implement timestamp formatting for command history

  // getChannelQuickCommands removed - not used in current implementation
  // TODO: Implement channel-specific quick commands

  // quickCommands removed - not used in current implementation
  // TODO: Implement quick command buttons

  // commonCommands removed - not used in current implementation
  // TODO: Implement command suggestions with common commands

  // getSuggestions removed - not used in current implementation
  // TODO: Implement command suggestions

  // suggestions removed - not used in current implementation
  // TODO: Implement command suggestions

  return (
    <div
      className="command-panel h-full flex flex-col bg-mythos-terminal-surface border border-gray-700 rounded"
      data-testid="command-panel"
    >
      {/* Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-background">
        <div className="flex items-center space-x-2">
          <EldritchIcon name={MythosIcons.command} size={20} className="text-mythos-terminal-primary" />
          <span className="text-sm font-bold text-mythos-terminal-primary">Commands</span>
        </div>
        <div className="flex items-center space-x-2">
          <ChannelSelector
            channels={AVAILABLE_CHANNELS}
            selectedChannel={currentChannel}
            onChannelSelect={setCurrentChannel}
            disabled={disabled || !isConnected}
          />
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={() => onClearHistory?.()}
            className="px-2 py-1 text-xs"
          >
            Clear
          </TerminalButton>
        </div>
      </div>

      {/* Command Input */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-background">
        <form onSubmit={handleCommandSubmit} className="space-y-2">
          <TerminalInput
            ref={inputRef}
            value={commandInput}
            onChange={e => setCommandInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder={placeholder}
            disabled={disabled || !isConnected}
            className="w-full"
            autoFocus
            data-testid="command-input"
          />
          <TerminalButton
            type="submit"
            variant="primary"
            disabled={!commandInput.trim() || disabled || !isConnected}
            className="w-full"
          >
            Send Command
          </TerminalButton>
        </form>
      </div>

      {/* Command History */}
      <div className="flex-1 overflow-y-auto p-3 space-y-1 min-h-[150px]" style={{ minHeight: '150px' }}>
        <h4 className="text-sm font-bold text-mythos-terminal-primary mb-2">Recent Commands</h4>
        {commandHistory.length === 0 ? (
          <div className="text-center text-mythos-terminal-text-secondary py-4">
            <EldritchIcon name={MythosIcons.command} size={24} className="mx-auto mb-2 opacity-50" />
            <p className="text-xs">No commands yet</p>
          </div>
        ) : (
          <div className="space-y-1">
            {commandHistory
              .slice(-10)
              .reverse()
              .map((command, index) => (
                <div
                  key={index}
                  className="text-xs text-mythos-terminal-text-secondary cursor-pointer hover:text-mythos-terminal-text p-1 rounded hover:bg-mythos-terminal-background"
                  onClick={() => {
                    setCommandInput(command);
                    inputRef.current?.focus();
                  }}
                >
                  {command}
                </div>
              ))}
          </div>
        )}
      </div>

      {/* Quick Commands */}
      <div className="p-3 border-t border-gray-700 bg-mythos-terminal-background">
        <h4 className="text-sm font-bold text-mythos-terminal-primary mb-2">Quick Commands</h4>
        <div className="grid grid-cols-2 gap-2">
          {['look', 'inventory', 'health', 'status'].map(cmd => (
            <TerminalButton
              key={cmd}
              variant="secondary"
              size="sm"
              onClick={() => {
                setCommandInput(cmd);
                inputRef.current?.focus();
              }}
              className="text-xs"
            >
              {cmd}
            </TerminalButton>
          ))}
        </div>
      </div>

      {/* Logout Button */}
      {onLogout && (
        <div className="p-3 border-t border-gray-700 bg-mythos-terminal-background">
          <LogoutButton onLogout={onLogout} disabled={disabled || !isConnected} isLoggingOut={isLoggingOut} />
        </div>
      )}
    </div>
  );
};
