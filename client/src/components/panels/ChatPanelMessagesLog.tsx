/**
 * Chat message list: memoized rows, stable ref for search scroll, reduced-motion scroll.
 * Agent-readable: split from ChatPanelRuntimeViewParts to keep module size under Lizard NLOC limits.
 */
import type { MouseEvent } from 'react';
import { memo, useCallback, useLayoutEffect, useRef } from 'react';
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';
import { SafeHtml } from '../common/SafeHtml';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import {
  buildChatSearchHighlightHtml,
  chatPanelMessageRowKey,
  escapeForChatHighlight,
  formatChatTimestampUtc,
  getChatPanelMessageClass,
  type ChatPanelMessage,
} from './chatPanelRuntimeUtils';

const fontSizeClass = 'text-sm';

function preventChatRowContextMenu(e: MouseEvent<HTMLDivElement>) {
  e.preventDefault();
}

type ChatPanelMessageRowProps = {
  message: ChatPanelMessage;
  index: number;
  totalVisible: number;
  isHistoryVisible: boolean;
  searchQuery: string;
  currentSearchIndex: number;
  /** When set, wires the row root element for search scroll targeting (single highlighted row). */
  setRowElement?: (el: HTMLDivElement | null) => void;
};

function chatPanelMessageRowPropsEqual(prev: ChatPanelMessageRowProps, next: ChatPanelMessageRowProps): boolean {
  return (
    prev.message === next.message &&
    prev.index === next.index &&
    prev.totalVisible === next.totalVisible &&
    prev.isHistoryVisible === next.isHistoryVisible &&
    prev.searchQuery === next.searchQuery &&
    prev.currentSearchIndex === next.currentSearchIndex &&
    prev.setRowElement === next.setRowElement
  );
}

const ChatPanelMessageRow = memo(function ChatPanelMessageRow({
  message,
  index,
  totalVisible,
  isHistoryVisible,
  searchQuery,
  currentSearchIndex,
  setRowElement,
}: ChatPanelMessageRowProps) {
  const shouldAnimate = !isHistoryVisible && !searchQuery && index >= totalVisible - 10;
  const animationClass = shouldAnimate ? 'animate-fade-in' : '';
  const animationDelay = shouldAnimate ? `${(index - (totalVisible - 10)) * 40}ms` : '0ms';
  const isHighlighted = currentSearchIndex === index && Boolean(searchQuery);

  return (
    <div
      className={
        `message p-3 bg-mythos-terminal-surface border rounded transition-[border-color,box-shadow,opacity] duration-300 ` +
        `hover:border-mythos-terminal-primary/30 hover:shadow-lg ${animationClass} ` +
        (isHighlighted
          ? 'border-mythos-terminal-warning border-2 shadow-lg shadow-mythos-terminal-warning/50'
          : 'border-mythos-terminal-border')
      }
      style={{ animationDelay }}
      data-testid="chat-message"
      ref={setRowElement}
    >
      {message.aliasChain && message.aliasChain.length > 0 && (
        <div className="mb-3 p-2 bg-mythos-terminal-background border border-mythos-terminal-primary/50 rounded text-xs">
          <div className="flex items-center gap-2 mb-2">
            <EldritchIcon name={MythosIcons.move} size={12} variant="warning" aria-hidden />
            <span className="text-mythos-terminal-warning font-bold">Alias Expansion:</span>
          </div>
          <div className="space-y-1">
            {message.aliasChain.map((alias, chainIndex) => (
              <div key={chainIndex} className="flex items-center gap-2">
                <span className="text-mythos-terminal-warning font-bold">{alias.original}</span>
                <EldritchIcon name={MythosIcons.exit} size={10} variant="primary" aria-hidden />
                <span className="text-mythos-terminal-success italic">{alias.expanded}</span>
              </div>
            ))}
          </div>
        </div>
      )}
      <div className="mb-2">
        <span className="text-xs text-mythos-terminal-text-secondary font-mono">
          {formatChatTimestampUtc(message.timestamp)}
        </span>
      </div>
      <div
        className={`message-text min-w-0 ${fontSizeClass} leading-relaxed ${getChatPanelMessageClass(message)}`}
        data-message-text={message.rawText ?? message.text}
        onContextMenu={preventChatRowContextMenu}
      >
        {message.isHtml ? (
          <SafeHtml
            html={message.isCompleteHtml ? message.text : ansiToHtmlWithBreaks(message.text)}
            tag="div"
            className="wrap-anywhere"
          />
        ) : (
          <SafeHtml
            html={
              searchQuery
                ? buildChatSearchHighlightHtml(message.rawText ?? message.text, searchQuery)
                : escapeForChatHighlight(message.rawText ?? message.text)
            }
            tag="div"
            className="wrap-anywhere"
            style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}
          />
        )}
      </div>
    </div>
  );
}, chatPanelMessageRowPropsEqual);

export type ChatPanelMessagesLogProps = {
  visibleMessages: ChatPanelMessage[];
  isHistoryVisible: boolean;
  searchQuery: string;
  currentSearchIndex: number;
};

export function ChatPanelMessagesLog({
  visibleMessages,
  isHistoryVisible,
  searchQuery,
  currentSearchIndex,
}: ChatPanelMessagesLogProps) {
  const activeRowRef = useRef<HTMLDivElement | null>(null);
  const bindActiveRowRef = useCallback((el: HTMLDivElement | null) => {
    activeRowRef.current = el;
  }, []);
  const total = visibleMessages.length;

  useLayoutEffect(() => {
    if (currentSearchIndex < 0 || !searchQuery.trim()) return;
    const el = activeRowRef.current;
    if (!el) return;
    const reduceMotion = typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    el.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
  }, [currentSearchIndex, searchQuery]);

  if (total === 0) {
    return (
      <div className="flex h-full items-center justify-center">
        <div className="space-y-2 text-center">
          <EldritchIcon
            name={MythosIcons.chat}
            size={32}
            variant="secondary"
            className="mx-auto opacity-50"
            aria-hidden
          />
          <p className="text-sm text-mythos-terminal-text-secondary">
            No messages yet. Start chatting to see messages here.
          </p>
        </div>
      </div>
    );
  }
  return (
    <div className="space-y-3">
      {visibleMessages.map((message, index) => (
        <ChatPanelMessageRow
          key={`${chatPanelMessageRowKey(message)}\x1f${index}`}
          message={message}
          index={index}
          totalVisible={total}
          isHistoryVisible={isHistoryVisible}
          searchQuery={searchQuery}
          currentSearchIndex={currentSearchIndex}
          setRowElement={index === currentSearchIndex ? bindActiveRowRef : undefined}
        />
      ))}
    </div>
  );
}
