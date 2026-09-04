import React, { useEffect, useRef, useState } from 'react';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';
import { TerminalInput } from '../../ui/TerminalInput';

interface CommandInputPanelProps {
  onSendCommand: (command: string) => void;
  disabled?: boolean;
  isConnected?: boolean;
  placeholder?: string;
}

interface CommandInputFormProps {
  commandInput: string;
  setCommandInput: (value: string) => void;
  disabled: boolean;
  isConnected: boolean;
  placeholder: string;
  onSubmit: (e: React.FormEvent) => void;
}

function CommandInputForm(props: CommandInputFormProps) {
  const { commandInput, setCommandInput, disabled, isConnected, placeholder, onSubmit } = props;
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      onSubmit(e);
    }
  };

  return (
    <form onSubmit={onSubmit} className="space-y-2">
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
        // eslint-disable-next-line jsx-a11y/no-autofocus -- primary game command entry must capture keyboard when shown
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
  );
}

/**
 * Game command entry. Chat channel selection lives on Chat History; this panel must not rewrite
 * typed commands into /say /g /l prefixes.
 */
export function CommandInputPanel(props: CommandInputPanelProps) {
  const {
    onSendCommand,
    disabled = false,
    isConnected = true,
    placeholder = "Enter game command (e.g., 'look', 'inventory', 'go north')...",
  } = props;
  const [commandInput, setCommandInput] = useState('');

  const handleCommandSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const trimmed = commandInput.trim();
    if (!trimmed || disabled || !isConnected) return;
    onSendCommand(trimmed);
    setCommandInput('');
  };

  return (
    <div
      className="h-full flex flex-col bg-mythos-terminal-surface border border-gray-700 rounded"
      data-testid="command-input-panel"
    >
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-background">
        <div className="flex items-center space-x-2">
          <EldritchIcon name={MythosIcons.command} size={20} className="text-mythos-terminal-primary" />
          <span className="text-sm font-bold text-mythos-terminal-primary">Commands</span>
        </div>
      </div>

      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-background">
        <CommandInputForm
          commandInput={commandInput}
          setCommandInput={setCommandInput}
          disabled={disabled}
          isConnected={isConnected}
          placeholder={placeholder}
          onSubmit={handleCommandSubmit}
        />
      </div>
    </div>
  );
}
