import React, { useMemo, useState } from 'react';
import { ALL_MESSAGES_CHANNEL, CHAT_CHANNEL_OPTIONS, DEFAULT_CHANNEL } from '../../../config/channels';
import { ansiToHtmlWithBreaks } from '../../../utils/ansiToHtml';
import { extractChannelFromMessage, isChatContent } from '../../../utils/messageTypeUtils';
import { ChannelSelector } from '../../ui/ChannelSelector';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';
import type { ChatMessage } from '../types';

interface ChatHistoryPanelProps {
  messages: ChatMessage[];
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
}

// Simplified chat history panel without channel activity indicators
// Based on findings from "Communication Interfaces in Non-Euclidean Spaces" - Dr. Armitage, 1928
export const ChatHistoryPanel: React.FC<ChatHistoryPanelProps> = ({
  messages,
  onClearMessages,
  onDownloadLogs,
  disabled = false,
  isConnected = true,
}) => {
  const [isHistoryVisible, setIsHistoryVisible] = useState(false);
  const [currentChannel, setCurrentChannel] = useState<string>(ALL_MESSAGES_CHANNEL.id);

  const normalizedSelectedChannel = currentChannel ?? DEFAULT_CHANNEL;
  const isAllChannelSelected = normalizedSelectedChannel === ALL_MESSAGES_CHANNEL.id;

  const filteredMessages = useMemo(() => {
    return messages.filter(message => {
      if (message.channel === 'game-log') {
        return false;
      }

      if (message.messageType === 'system') {
        return false;
      }

      // Exclude combat messages - they belong in Game Info panel only
      if (message.messageType === 'combat') {
        return false;
      }

      // Exclude command messages - they belong in Game Info panel only
      // This must be checked before isAllChannelSelected to prevent command messages
      // from appearing in Chat panel even when "All Messages" is selected
      if (message.messageType === 'command') {
        return false;
      }

      if (isAllChannelSelected) {
        return true;
      }

      const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';

      if (message.messageType === 'error') {
        return messageChannel === normalizedSelectedChannel;
      }

      const isChatMessage = message.messageType === 'chat' || isChatContent(message.text);
      if (!isChatMessage) {
        return false;
      }

      if (messageChannel === 'whisper') {
        return normalizedSelectedChannel === 'whisper';
      }

      return messageChannel === normalizedSelectedChannel;
    });
  }, [messages, normalizedSelectedChannel, isAllChannelSelected]);

  const historyEligibleMessages = useMemo(
    () => messages.filter(message => message.messageType !== 'system'),
    [messages]
  );
  const visibleMessages = isHistoryVisible ? historyEligibleMessages : filteredMessages;

  const handleChannelSelect = (channelId: string) => {
    setCurrentChannel(channelId);
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

  const getMessageClass = (message: ChatMessage): string => {
    if (message.tags?.includes('hallucination')) {
      return 'text-fuchsia-300 italic';
    }

    if (message.tags?.includes('command-misfire')) {
      return 'text-mythos-terminal-warning font-semibold';
    }

    if (message.tags?.includes('rescue')) {
      return 'text-mythos-terminal-primary font-semibold';
    }

    switch (message.messageType) {
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

  return (
    <div className="h-full flex flex-col font-mono">
      {/* Chat Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center gap-2">
          <EldritchIcon name={MythosIcons.chat} size={20} variant="primary" />
          <h3 className="text-mythos-terminal-primary font-bold">Chat</h3>
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

      {/* Channel Selector - Simplified (no activity indicators) */}
      <div
        className="p-3 border-b border-gray-700 bg-mythos-terminal-surface"
        role="region"
        aria-label="Channel Selection"
      >
        <div className="flex flex-col sm:flex-row items-start sm:items-center gap-2">
          <span className="text-sm text-mythos-terminal-text-secondary font-mono">Channel:</span>
          <ChannelSelector
            channels={CHAT_CHANNEL_OPTIONS}
            selectedChannel={normalizedSelectedChannel}
            onChannelSelect={handleChannelSelect}
            disabled={disabled || !isConnected}
            className="flex-1 w-full sm:w-auto"
          />
        </div>
      </div>

      {/* Simplified Chat History Toggle */}
      <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background">
        <button
          className="text-xs text-mythos-terminal-primary"
          onClick={() => setIsHistoryVisible(!isHistoryVisible)}
          type="button"
        >
          {isHistoryVisible ? 'Current' : 'All'} Messages
        </button>
        <span className="ml-2 text-xs text-mythos-terminal-text-secondary">
          ({visibleMessages.length} message{visibleMessages.length === 1 ? '' : 's'})
        </span>
      </div>

      {/* Chat Messages Display */}
      <div
        className="flex-1 overflow-auto p-3 bg-mythos-terminal-background"
        role="log"
        aria-label="Chat Messages"
        style={{ minHeight: '200px' }}
      >
        {visibleMessages.length === 0 ? (
          <div className="flex items-center justify-center h-full">
            <div className="text-center space-y-2">
              <EldritchIcon name={MythosIcons.chat} size={32} variant="secondary" className="mx-auto opacity-50" />
              <p className="text-mythos-terminal-text-secondary text-sm">
                No messages yet. Start chatting to see messages here.
              </p>
            </div>
          </div>
        ) : (
          <div className="space-y-3">
            {visibleMessages.map((message, index) => (
              <div
                key={index}
                className="message p-3 bg-mythos-terminal-surface border border-gray-700 rounded transition-all duration-300 hover:border-mythos-terminal-primary/30"
              >
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

                <div className="mb-2">
                  <span className="text-xs text-mythos-terminal-text-secondary font-mono">
                    {formatTimestamp(message.timestamp)}
                  </span>
                </div>

                <div
                  className={`text-sm leading-relaxed ${getMessageClass(message)}`}
                  data-message-text={message.rawText ?? message.text}
                >
                  {message.isHtml ? (
                    <span
                      dangerouslySetInnerHTML={{
                        __html: message.isCompleteHtml ? message.text : ansiToHtmlWithBreaks(message.text),
                      }}
                    />
                  ) : (
                    <span style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
                      {message.rawText ?? message.text}
                    </span>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
