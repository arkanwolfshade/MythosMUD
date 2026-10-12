import React, { useMemo, useState } from 'react';
import { ALL_MESSAGES_CHANNEL, CHAT_CHANNEL_OPTIONS, DEFAULT_CHANNEL } from '../../../config/channels';
import { useChatGrainPreference } from '../../../contexts/hooks/useThemeContext';
import { decayMessageText } from '../../../utils/corruptionDecay';
import { SafeHtml } from '../../common/SafeHtml';
import { ChannelSelector, EldritchIcon, MythosIcons, TerminalButton } from '../primitives';
import type { ChatMessage } from '../types';
import { getMessageCategoryClass, isPlainRegisterCategory } from '../utils/messageCategoryStyle';

interface ChatHistoryPanelProps {
  messages: ChatMessage[];
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  /** #804: the viewer's own corruption stat (0-100), driving the chat pane's perceptual filter.
   * A global filter on the viewer's own value only, per ADR-025 -- never per-message. */
  corruption?: number;
}

/** Category routing: the Chat panel shows chat.* only; every other category lives in Game Info. */
function isChatCategory(category: string): boolean {
  return category.startsWith('chat.');
}

function matchesSelectedChannel(
  message: ChatMessage,
  normalizedSelectedChannel: string,
  isAllChannelSelected: boolean
): boolean {
  if (isAllChannelSelected) return true;
  // The selector filters on conversation identity (message.channel); the category suffix only supplies a fallback.
  const categoryChannel = message.channel || message.category.slice('chat.'.length);
  return categoryChannel === normalizedSelectedChannel;
}

function filterChatHistoryMessages(
  messages: ChatMessage[],
  normalizedSelectedChannel: string,
  isAllChannelSelected: boolean
): ChatMessage[] {
  return messages.filter(
    message =>
      isChatCategory(message.category) &&
      matchesSelectedChannel(message, normalizedSelectedChannel, isAllChannelSelected)
  );
}

function getCategorizedMessageClass(category: string): string | undefined {
  const categoryClass = getMessageCategoryClass(category);
  if (!categoryClass) return undefined;
  // #804/ADR-025: the corruption tint reaches only the plain (speech/ambient) register; alert,
  // private, action, meta and heading lines keep their semantic color. The register is a static
  // property of the category, so this stays a global filter on the viewer's own corruption value.
  // #714: no branch here may depend on anything but the category -- a hallucinated message carries
  // the same category as the real one and must not look different.
  return isPlainRegisterCategory(category) ? `${categoryClass} mythos-corruption-text` : categoryClass;
}

function getMessageClass(message: ChatMessage): string {
  // #714: styling depends on the category alone -- a hallucinated message carries the same category as the
  // real one and must not look different.
  return getCategorizedMessageClass(message.category) ?? 'mythos-corruption-text';
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

function ChatHistoryMessageList(props: { messages: ChatMessage[]; corruption: number }) {
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
        <ChatHistoryMessageRow key={index} message={message} index={index} corruption={props.corruption} />
      ))}
    </div>
  );
}

export const ChatHistoryPanel: React.FC<ChatHistoryPanelProps> = props => {
  const { messages, onClearMessages, onDownloadLogs, disabled = false, isConnected = true, corruption = 0 } = props;
  const [isHistoryVisible, setIsHistoryVisible] = useState(false);
  const [currentChannel, setCurrentChannel] = useState<string>(ALL_MESSAGES_CHANNEL.id);
  const { chatGrain } = useChatGrainPreference();

  const normalizedSelectedChannel = currentChannel ?? DEFAULT_CHANNEL;
  const isAllChannelSelected = normalizedSelectedChannel === ALL_MESSAGES_CHANNEL.id;

  const filteredMessages = useMemo(
    () => filterChatHistoryMessages(messages, normalizedSelectedChannel, isAllChannelSelected),
    [messages, normalizedSelectedChannel, isAllChannelSelected]
  );

  const historyEligibleMessages = useMemo(
    () => messages.filter(message => !message.category.startsWith('system.')),
    [messages]
  );
  const visibleMessages = isHistoryVisible ? historyEligibleMessages : filteredMessages;

  // #804: one CSS custom property, derived from the viewer's own corruption stat, drives both the
  // text-color filter (.mythos-corruption-text) and the grain overlay -- a single wire value, no
  // new event type (SUBSYSTEM_CORRUPTION_DESIGN.md §4).
  const corruptionIntensity = Math.max(0, Math.min(1, corruption / 100));

  return (
    <div
      className="h-full flex flex-col font-mono"
      data-testid="chat-history-panel"
      style={{ '--corruption-intensity': corruptionIntensity } as React.CSSProperties}
    >
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
        className={`flex-1 overflow-auto p-3 bg-mythos-terminal-background${chatGrain ? ' mythos-corruption-grain' : ''}`}
        role="log"
        aria-label="Chat Messages"
        style={{ minHeight: '200px' }}
      >
        <ChatHistoryMessageList messages={visibleMessages} corruption={corruption} />
      </div>
    </div>
  );
};

function AliasChainBlock({ chain }: { chain: NonNullable<ChatMessage['aliasChain']> }): React.ReactElement {
  return (
    <div className="mb-3 p-2 bg-mythos-terminal-background border border-mythos-terminal-primary/50 rounded text-xs">
      <div className="flex items-center gap-2 mb-2">
        <EldritchIcon name={MythosIcons.move} size={12} variant="warning" />
        <span className="text-mythos-terminal-warning font-bold">Alias Expansion:</span>
      </div>
      <div className="space-y-1">
        {chain.map((alias, chainIndex) => (
          <div key={chainIndex} className="flex items-center gap-2">
            <span className="text-mythos-terminal-warning font-bold">{alias.original}</span>
            <EldritchIcon name={MythosIcons.exit} size={10} variant="primary" />
            <span className="text-mythos-terminal-success italic">{alias.expanded}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function ChatHistoryMessageBody({
  message,
  corruption,
}: {
  message: ChatMessage;
  corruption: number;
}): React.ReactElement {
  if (message.isHtml) return <SafeHtml html={message.text} />;
  // #804: decay is scoped to plain text only -- corrupting arbitrary sanitized HTML text nodes
  // would need DOM-tree-aware processing, out of proportion for a decorative effect.
  const bodyText = decayMessageText(message.rawText ?? message.text, corruption, message.timestamp);
  return <span style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>{bodyText}</span>;
}

function ChatHistoryMessageRow({
  message,
  index,
  corruption,
}: {
  message: ChatMessage;
  index: number;
  corruption: number;
}) {
  const chain = message.aliasChain;
  return (
    <div
      key={index}
      className="message p-3 bg-mythos-terminal-surface border border-gray-700 rounded transition-all duration-300 hover:border-mythos-terminal-primary/30"
    >
      {chain && chain.length > 0 ? <AliasChainBlock chain={chain} /> : null}
      <div className="mb-2">
        <span className="text-xs text-mythos-terminal-text-secondary font-mono">
          {formatTimestamp(message.timestamp)}
        </span>
      </div>
      <div
        className={`text-sm leading-relaxed ${getMessageClass(message)}`}
        data-message-text={message.rawText ?? message.text}
      >
        <ChatHistoryMessageBody message={message} corruption={corruption} />
      </div>
    </div>
  );
}
