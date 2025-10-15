import React from 'react';
import { ansiToHtmlWithBreaks } from '../../../utils/ansiToHtml';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';

interface ChatMessageProps {
  message: {
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
  };
  index: number;
}

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

const getFontSizeClass = (): string => {
  // This would typically come from theme context
  return 'text-sm';
};

export const ChatMessage: React.FC<ChatMessageProps> = ({ message, index }) => {
  return (
    <div
      className="message p-3 bg-mythos-terminal-surface border border-gray-700 rounded transition-all duration-300 hover:border-mythos-terminal-primary/30 hover:shadow-lg animate-fade-in"
      style={{ animationDelay: `${index * 50}ms` }}
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
        className={`${getFontSizeClass()} leading-relaxed ${getMessageClass(message.messageType)}`}
        dangerouslySetInnerHTML={{
          __html: message.isHtml
            ? message.isCompleteHtml
              ? message.text
              : ansiToHtmlWithBreaks(message.text)
            : message.text,
        }}
        onContextMenu={e => {
          e.preventDefault();
          // Context menu functionality would go here
        }}
        title="Right-click to ignore user"
      />
    </div>
  );
};
