import React, { useEffect, useRef, useState } from 'react';
import { DEFAULT_CHANNEL } from '../../config/channels';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { LogoutButton } from '../ui/LogoutButton';
import { TerminalButton } from '../ui/TerminalButton';
import { TerminalInput } from '../ui/TerminalInput';
import { prepareCommandForSubmit } from './commandPanelSubmit';

export interface CommandPanelProps {
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

function logCommandPanelConnectionDebug(isConnected: boolean, disabled: boolean, commandInput: string): void {
  if (import.meta.env.PROD) return;
  console.debug('CommandPanel received isConnected prop', {
    isConnected,
    disabled,
    commandInputLength: commandInput.length,
    buttonDisabled: !commandInput.trim() || disabled || !isConnected,
    buttonDisabledReason: {
      noCommand: !commandInput.trim(),
      panelDisabled: disabled,
      notConnected: !isConnected,
    },
  });
}

function useCommandPanelEffects(params: {
  onLogout?: () => void;
  disabled: boolean;
  isConnected: boolean;
  inputRef: React.RefObject<HTMLInputElement | null>;
}): void {
  const { onLogout, disabled, isConnected, inputRef } = params;

  useEffect(() => {
    inputRef.current?.focus();
  }, [inputRef]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.ctrlKey && e.key === 'q' && onLogout && !disabled && isConnected) {
        e.preventDefault();
        onLogout();
      }
    };
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [onLogout, disabled, isConnected]);
}

function CommandPanelInput(props: {
  commandInput: string;
  setCommandInput: (value: string) => void;
  placeholder: string;
  disabled: boolean;
  isConnected: boolean;
  inputRef: React.RefObject<HTMLInputElement | null>;
  onSubmit: (e: React.FormEvent) => void;
}): React.ReactElement {
  const { commandInput, setCommandInput, placeholder, disabled, isConnected, inputRef, onSubmit } = props;
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      onSubmit(e);
    }
  };

  return (
    <>
      <div className="flex items-center justify-between p-3 border-b border-mythos-terminal-border bg-mythos-terminal-background">
        <EldritchIcon name={MythosIcons.command} size={20} className="text-mythos-terminal-primary" />
      </div>
      <div className="p-3 border-b border-mythos-terminal-border bg-mythos-terminal-background">
        <form onSubmit={onSubmit} className="space-y-2">
          <TerminalInput
            ref={inputRef}
            value={commandInput}
            onChange={e => setCommandInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder={placeholder}
            disabled={disabled || !isConnected}
            className="w-full"
            // Command entry is the primary control in this panel; intentional focus for keyboard play.
            // eslint-disable-next-line jsx-a11y/no-autofocus -- MUD command entry convenience
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
    </>
  );
}

function CommandPanelHistory(props: {
  commandHistory: string[];
  onClearHistory?: () => void;
  onSelectCommand: (command: string) => void;
}): React.ReactElement {
  return (
    <div className="min-h-panel-sm flex-1 overflow-y-auto space-y-1 p-3">
      <div className="flex items-center justify-between mb-2">
        <h4 className="text-sm font-bold text-mythos-terminal-primary">Recent Commands</h4>
        {props.onClearHistory && props.commandHistory.length > 0 && (
          <TerminalButton variant="secondary" size="sm" onClick={props.onClearHistory} className="px-2 py-1 text-xs">
            Clear
          </TerminalButton>
        )}
      </div>
      {props.commandHistory.length === 0 ? (
        <div className="text-center text-mythos-terminal-text-secondary py-4">
          <p className="text-xs">No commands yet</p>
        </div>
      ) : (
        <div className="space-y-1">
          {props.commandHistory
            .slice(-10)
            .reverse()
            .map((command, index) => (
              <button
                key={index}
                type="button"
                className="text-xs text-mythos-terminal-text-secondary cursor-pointer hover:text-mythos-terminal-text p-1 rounded hover:bg-mythos-terminal-background w-full text-left"
                onClick={() => props.onSelectCommand(command)}
              >
                {command}
              </button>
            ))}
        </div>
      )}
    </div>
  );
}

function CommandPanelFooter(props: {
  onLogout: () => void;
  disabled: boolean;
  isConnected: boolean;
  isLoggingOut: boolean;
}): React.ReactElement {
  return (
    <div className="p-3 border-t border-mythos-terminal-border bg-mythos-terminal-background">
      <LogoutButton
        onLogout={props.onLogout}
        disabled={props.disabled || !props.isConnected}
        isLoggingOut={props.isLoggingOut}
      />
    </div>
  );
}

export const CommandPanel: React.FC<CommandPanelProps> = props => {
  const {
    commandHistory,
    onSendCommand,
    onClearHistory,
    onLogout,
    disabled = false,
    isConnected = true,
    isLoggingOut = false,
    placeholder = "Enter game command (e.g., 'look', 'inventory', 'go north')...",
    selectedChannel = DEFAULT_CHANNEL,
    onChannelSelect,
  } = props;

  const [commandInput, setCommandInput] = useState('');
  const isControlled = onChannelSelect !== undefined;
  const [uncontrolledChannel] = useState(selectedChannel ?? DEFAULT_CHANNEL);
  const currentChannel = isControlled ? (selectedChannel ?? DEFAULT_CHANNEL) : uncontrolledChannel;
  const inputRef = useRef<HTMLInputElement>(null);

  logCommandPanelConnectionDebug(isConnected, disabled, commandInput);
  useCommandPanelEffects({ onLogout, disabled, isConnected, inputRef });

  const handleCommandSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!commandInput.trim() || disabled) return;
    onSendCommand(prepareCommandForSubmit(commandInput, currentChannel));
    setCommandInput('');
  };

  return (
    <div
      className="command-panel h-full flex flex-col bg-mythos-terminal-surface border border-mythos-terminal-border rounded"
      data-testid="command-panel"
    >
      <CommandPanelInput
        commandInput={commandInput}
        setCommandInput={setCommandInput}
        placeholder={placeholder}
        disabled={disabled}
        isConnected={isConnected}
        inputRef={inputRef}
        onSubmit={handleCommandSubmit}
      />
      <CommandPanelHistory
        commandHistory={commandHistory}
        onClearHistory={onClearHistory}
        onSelectCommand={command => {
          setCommandInput(command);
          inputRef.current?.focus();
        }}
      />
      {onLogout && (
        <CommandPanelFooter
          onLogout={onLogout}
          disabled={disabled}
          isConnected={isConnected}
          isLoggingOut={isLoggingOut}
        />
      )}
    </div>
  );
};
