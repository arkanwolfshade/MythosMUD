import React, { useMemo, useState } from 'react';
import { ALL_MESSAGES_CHANNEL, CHAT_CHANNEL_OPTIONS, DEFAULT_CHANNEL } from '../../../config/channels';
import { ansiToHtmlWithBreaks } from '../../../utils/ansiToHtml';
import { extractChannelFromMessage, isChatContent } from '../../../utils/messageTypeUtils';
import { SafeHtml } from '../../common/SafeHtml';
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

const TAG_MESSAGE_CLASSES: Record<string, string> = {
  hallucination: 'text-fuchsia-300 italic',
  'command-misfire': 'text-mythos-terminal-warning font-semibold',
  rescue: 'text-mythos-terminal-primary font-semibold',
};

const TYPE_MESSAGE_CLASSES: Record<string, string> = {
  emote: 'text-mythos-terminal-primary italic',
  system: 'text-mythos-terminal-warning font-bold',
  error: 'text-mythos-terminal-error font-bold',
  whisper: 'text-mythos-terminal-secondary italic',
  party: 'text-mythos-terminal-primary',
  shout: 'text-mythos-terminal-warning font-bold',
};

function isExcludedFromChatPanel(message: ChatMessage): boolean {
  return (
    message.channel === 'game-log' ||
    message.messageType === 'system' ||
    message.messageType === 'combat' ||
    message.messageType === 'command'
  );
}

function matchesSelectedChannel(
  message: ChatMessage,
  normalizedSelectedChannel: string,
  isAllChannelSelected: boolean
): boolean {
  if (isAllChannelSelected) return true;

  const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';

  if (message.messageType === 'error') {
    return messageChannel === normalizedSelectedChannel;
  }

  const isChatMessage = message.messageType === 'chat' || isChatContent(message.text);
  if (!isChatMessage) return false;

  if (messageChannel === 'whisper' || messageChannel === 'party') {
    return normalizedSelectedChannel === messageChannel;
  }

  return messageChannel === normalizedSelectedChannel;
}

function filterChatHistoryMessages(
  messages: ChatMessage[],
  normalizedSelectedChannel: string,
  isAllChannelSelected: boolean
): ChatMessage[] {
  return messages.filter(
    message =>
      !isExcludedFromChatPanel(message) &&
      matchesSelectedChannel(message, normalizedSelectedChannel, isAllChannelSelected)
  );
}

function getMessageClass(message: ChatMessage): string {
  for (const tag of message.tags ?? []) {
    const tagClass = TAG_MESSAGE_CLASSES[tag];
    if (tagClass) return tagClass;
  }
  return TYPE_MESSAGE_CLASSES[message.messageType ?? ''] ?? 'text-mythos-terminal-text';
}

function formatTimestamp(timestamp: string): string {
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
}

function ChatHistoryPanelToolbar(props: { onClearMessages?: () => void; onDownloadLogs?: () => void }) {
  return (
    <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
      <div className="flex items-center gap-2">
        <EldritchIcon name={MythosIcons.chat} size={20} variant="primary" />
        <h3 className="text-mythos-terminal-primary font-bold">Chat</h3>
      </div>
      <div className="flex items-center gap-2">
        {props.onClearMessages ? (
          <TerminalButton variant="secondary" size="sm" onClick={props.onClearMessages} className="p-2 h-8 w-8">
            <EldritchIcon name={MythosIcons.clear} size={14} variant="error" />
          </TerminalButton>
        ) : null}
        {props.onDownloadLogs ? (
          <TerminalButton variant="secondary" size="sm" onClick={props.onDownloadLogs} className="p-2 h-8 w-8">
            <EldritchIcon name={MythosIcons.download} size={14} variant="primary" />
          </TerminalButton>
        ) : null}
      </div>
    </div>
  );
}

function ChatHistoryChannelBar(props: {
  normalizedSelectedChannel: string;
  disabled: boolean;
  isConnected: boolean;
  onChannelSelect: (channel: string) => void;
}) {
  return (
    <div
      className="p-3 border-b border-gray-700 bg-mythos-terminal-surface"
      role="region"
      aria-label="Channel Selection"
    >
      <div className="flex flex-col sm:flex-row items-start sm:items-center gap-2">
        <span className="text-sm text-mythos-terminal-text-secondary font-mono">Channel:</span>
        <ChannelSelector
          channels={CHAT_CHANNEL_OPTIONS}
          selectedChannel={props.normalizedSelectedChannel}
          onChannelSelect={props.onChannelSelect}
          disabled={props.disabled || !props.isConnected}
          className="flex-1 w-full sm:w-auto"
        />
      </div>
    </div>
  );
}

function ChatHistoryScopeToggle(props: { isHistoryVisible: boolean; onToggle: () => void; visibleCount: number }) {
  return (
    <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background">
      <button className="text-xs text-mythos-terminal-primary" onClick={props.onToggle} type="button">
        {props.isHistoryVisible ? 'Current' : 'All'} Messages
      </button>
      <span className="ml-2 text-xs text-mythos-terminal-text-secondary">
        ({props.visibleCount} message{props.visibleCount === 1 ? '' : 's'})
      </span>
    </div>
  );
}

function ChatHistoryMessageList(props: { messages: ChatMessage[] }) {
  if (props.messages.length === 0) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center space-y-2">
          <EldritchIcon name={MythosIcons.chat} size={32} variant="secondary" className="mx-auto opacity-50" />
          <p className="text-mythos-terminal-text-secondary text-sm">
            No messages yet. Start chatting to see messages here.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {props.messages.map((message, index) => (
        <ChatHistoryMessageRow key={index} message={message} index={index} />
      ))}
    </div>
  );
}

export const ChatHistoryPanel: React.FC<ChatHistoryPanelProps> = props => {
  const { messages, onClearMessages, onDownloadLogs, disabled = false, isConnected = true } = props;
  const [isHistoryVisible, setIsHistoryVisible] = useState(false);
  const [currentChannel, setCurrentChannel] = useState<string>(ALL_MESSAGES_CHANNEL.id);

  const normalizedSelectedChannel = currentChannel ?? DEFAULT_CHANNEL;
  const isAllChannelSelected = normalizedSelectedChannel === ALL_MESSAGES_CHANNEL.id;

  const filteredMessages = useMemo(
    () => filterChatHistoryMessages(messages, normalizedSelectedChannel, isAllChannelSelected),
    [messages, normalizedSelectedChannel, isAllChannelSelected]
  );

  const historyEligibleMessages = useMemo(
    () => messages.filter(message => message.messageType !== 'system'),
    [messages]
  );
  const visibleMessages = isHistoryVisible ? historyEligibleMessages : filteredMessages;

  return (
    <div className="h-full flex flex-col font-mono" data-testid="chat-history-panel">
      <ChatHistoryPanelToolbar onClearMessages={onClearMessages} onDownloadLogs={onDownloadLogs} />
      <ChatHistoryChannelBar
        normalizedSelectedChannel={normalizedSelectedChannel}
        disabled={disabled}
        isConnected={isConnected}
        onChannelSelect={setCurrentChannel}
      />
      <ChatHistoryScopeToggle
        isHistoryVisible={isHistoryVisible}
        onToggle={() => setIsHistoryVisible(!isHistoryVisible)}
        visibleCount={visibleMessages.length}
      />
      <div
        className="flex-1 overflow-auto p-3 bg-mythos-terminal-background"
        role="log"
        aria-label="Chat Messages"
        style={{ minHeight: '200px' }}
      >
        <ChatHistoryMessageList messages={visibleMessages} />
      </div>
    </div>
  );
};

function ChatHistoryMessageRow({ message, index }: { message: ChatMessage; index: number }) {
  return (
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
          <SafeHtml html={message.isCompleteHtml ? message.text : ansiToHtmlWithBreaks(message.text)} />
        ) : (
          <span style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>{message.rawText ?? message.text}</span>
        )}
      </div>
    </div>
  );
}
