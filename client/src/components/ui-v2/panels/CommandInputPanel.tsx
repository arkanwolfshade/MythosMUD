import React, { useEffect, useRef, useState } from 'react';
import { ALL_MESSAGES_CHANNEL, CHAT_CHANNEL_OPTIONS, DEFAULT_CHANNEL } from '../../../config/channels';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';
import { TerminalInput } from '../../ui/TerminalInput';

interface CommandInputPanelProps {
  onSendCommand: (command: string) => void;
  disabled?: boolean;
  isConnected?: boolean;
  placeholder?: string;
  selectedChannel?: string;
}

// Simplified command input panel without logout button (moved to header)
// Based on findings from "Command Interface Design" - Dr. Armitage, 1928
export const CommandInputPanel: React.FC<CommandInputPanelProps> = ({
  onSendCommand,
  disabled = false,
  isConnected = true,
  placeholder = "Enter game command (e.g., 'look', 'inventory', 'go north')...",
  selectedChannel = DEFAULT_CHANNEL,
}) => {
  const [commandInput, setCommandInput] = useState('');
  const inputRef = useRef<HTMLInputElement>(null);

  // Focus input on mount
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleCommandSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!commandInput.trim() || disabled || !isConnected) return;

    let command = commandInput.trim();

    // List of standalone system commands that should never have channel shortcuts prepended
    const standaloneCommands = [
      'admin',
      'alias',
      'aliases',
      'attack',
      'emote',
      'go',
      'goto',
      'help',
      'hit',
      'inventory',
      'kick',
      'look',
      'logout',
      'me',
      'mute',
      'party',
      'pose',
      'punch',
      'quit',
      'smack',
      'status',
      'strike',
      'teleport',
      'thump',
      'unalias',
      'unmute',
      'w',
      'whisper',
      'who',
    ];
    const firstWord = command.split(/\s+/)[0].toLowerCase();
    const isStandaloneCommand = standaloneCommands.includes(firstWord);

    const effectiveChannel = selectedChannel === ALL_MESSAGES_CHANNEL.id ? 'say' : selectedChannel;

    // If the command doesn't start with a slash and we're not on the 'say' channel,
    // prepend the channel command ONLY if it's not a standalone command
    if (
      !command.startsWith('/') &&
      effectiveChannel !== 'say' &&
      effectiveChannel !== 'local' &&
      effectiveChannel !== 'party' &&
      !isStandaloneCommand
    ) {
      const channel = CHAT_CHANNEL_OPTIONS.find(c => c.id === effectiveChannel);
      const commandLower = command.toLowerCase();
      const channelName = channel?.id || '';
      const alreadyHasChannelPrefix = commandLower.startsWith(channelName + ' ') || commandLower === channelName;

      if (channel?.shortcut && !alreadyHasChannelPrefix) {
        command = `/${channel.shortcut} ${command}`;
      }
    }
    if (!command.startsWith('/') && effectiveChannel === 'party' && command.trim()) {
      const commandLower = command.toLowerCase();
      if (!commandLower.startsWith('party ')) {
        command = `party ${command}`;
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

  return (
    <div
      className="h-full flex flex-col bg-mythos-terminal-surface border border-gray-700 rounded"
      data-testid="command-input-panel"
    >
      {/* Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-background">
        <div className="flex items-center space-x-2">
          <EldritchIcon name={MythosIcons.command} size={20} className="text-mythos-terminal-primary" />
          <span className="text-sm font-bold text-mythos-terminal-primary">Commands</span>
        </div>
      </div>

      {/* Command Input */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-background">
        <form onSubmit={handleCommandSubmit} className="space-y-2">
          <TerminalInput
            ref={inputRef}
            value={commandInput}
            onChange={e => {
              setCommandInput(e.target.value);
            }}
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
    </div>
  );
};
