import React, { useEffect, useRef } from 'react';
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';
import { TerminalButton } from '../ui/TerminalButton';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

interface ChatPanelProps {
  messages: ChatMessage[];
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
}

export const ChatPanel: React.FC<ChatPanelProps> = ({ messages, onClearMessages, onDownloadLogs }) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const getMessageClass = (messageType?: string): string => {
    switch (messageType) {
      case 'emote':
        return 'text-mythos-terminal-primary italic';
      case 'system':
        return 'text-mythos-terminal-warning font-bold';
      case 'error':
        return 'text-mythos-terminal-error font-bold';
      case 'whisper':
        return 'text-mythos-terminal-secondary italic';
      case 'shout':
        return 'text-mythos-terminal-warning font-bold';
      default:
        return 'text-mythos-terminal-text';
    }
  };

  const formatTimestamp = (timestamp: string): string => {
    try {
      const date = new Date(timestamp);
      return date.toLocaleTimeString('en-US', {
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
      });
    } catch {
      return timestamp;
    }
  };

  return (
    <div className="h-full flex flex-col font-mono">
      {/* Chat Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center gap-2">
          <EldritchIcon name={MythosIcons.chat} size={20} variant="primary" />
          <h3 className="text-mythos-terminal-primary font-bold">Chat Log ({messages.length} messages)</h3>
        </div>
        <div className="flex items-center gap-2">
          {onClearMessages && (
            <TerminalButton variant="secondary" size="sm" onClick={onClearMessages} className="p-2 h-8 w-8">
              <EldritchIcon name={MythosIcons.clear} size={14} variant="error" />
            </TerminalButton>
          )}
          {onDownloadLogs && (
            <TerminalButton variant="secondary" size="sm" onClick={onDownloadLogs} className="p-2 h-8 w-8">
              <EldritchIcon name={MythosIcons.download} size={14} variant="primary" />
            </TerminalButton>
          )}
        </div>
      </div>

      {/* Messages Area */}
      <div className="flex-1 overflow-auto p-3 bg-mythos-terminal-background border border-gray-700 rounded">
        {messages.length === 0 ? (
          <div className="flex items-center justify-center h-full">
            <div className="text-center space-y-2">
              <EldritchIcon name={MythosIcons.chat} size={32} variant="secondary" className="mx-auto opacity-50" />
              <p className="text-mythos-terminal-text-secondary text-sm">
                No messages yet. Connect to the game to see chat activity.
              </p>
            </div>
          </div>
        ) : (
          <div className="space-y-3">
            {messages.map((message, index) => (
              <div
                key={index}
                className="p-3 bg-mythos-terminal-surface border border-gray-700 rounded transition-all duration-200 hover:border-mythos-terminal-primary/30"
              >
                {/* Alias Expansion Information */}
                {message.aliasChain && message.aliasChain.length > 0 && (
                  <div className="mb-3 p-2 bg-mythos-terminal-background border border-mythos-terminal-primary/50 rounded text-xs">
                    <div className="flex items-center gap-2 mb-2">
                      <EldritchIcon name={MythosIcons.move} size={12} variant="warning" />
                      <span className="text-mythos-terminal-warning font-bold">Alias Expansion:</span>
                    </div>
                    <div className="space-y-1">
                      {message.aliasChain.map((alias, chainIndex) => (
                        <div key={chainIndex} className="flex items-center gap-2">
                          <span className="text-mythos-terminal-warning font-bold">{alias.original}</span>
                          <EldritchIcon name={MythosIcons.exit} size={10} variant="primary" />
                          <span className="text-mythos-terminal-success italic">{alias.expanded}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Message Timestamp */}
                <div className="mb-2">
                  <span className="text-xs text-mythos-terminal-text-secondary font-mono">
                    {formatTimestamp(message.timestamp)}
                  </span>
                </div>

                {/* Message Content */}
                <div
                  className={`text-sm leading-relaxed ${getMessageClass(message.messageType)}`}
                  dangerouslySetInnerHTML={{
                    __html: message.isHtml
                      ? message.isCompleteHtml
                        ? message.text
                        : ansiToHtmlWithBreaks(message.text)
                      : message.text,
                  }}
                />
              </div>
            ))}
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>

      {/* Chat Footer */}
      <div className="p-2 border-t border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center justify-between text-xs text-mythos-terminal-text-secondary">
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-1">
              <div className="w-2 h-2 bg-mythos-terminal-success rounded-full"></div>
              <span>Connected</span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.chat} size={12} variant="secondary" />
              <span>{messages.length} messages</span>
            </div>
          </div>
          <div className="text-xs opacity-75">MythosMUD Terminal</div>
        </div>
      </div>
    </div>
  );
};
