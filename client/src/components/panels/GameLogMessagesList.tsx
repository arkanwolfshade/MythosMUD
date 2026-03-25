import React, { RefObject } from 'react';
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';
import { SafeHtml } from '../common/SafeHtml';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { formatGameLogTimestamp, getGameLogMessageClassName, getGameLogMessageRowClassName } from './gameLogPanelUtils';

export interface GameLogListMessage {
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

interface GameLogMessagesListProps {
  messages: GameLogListMessage[];
  messagesEndRef: RefObject<HTMLDivElement | null>;
}

export const GameLogMessagesList: React.FC<GameLogMessagesListProps> = ({ messages, messagesEndRef }) => (
  <div
    className="game-log-messages-scroll min-h-panel-md flex-1 overflow-y-auto bg-[linear-gradient(180deg,rgba(0,40,0,0.22)_0%,transparent_10rem)] p-3"
    style={{ minHeight: '300px' }}
  >
    {messages.length === 0 ? (
      <div className="flex flex-col items-center justify-center px-4 py-12 text-center">
        <EldritchIcon name={MythosIcons.log} size={40} className="mb-3 text-mythos-terminal-primary/35" aria-hidden />
        <p className="font-mono text-base font-semibold leading-snug tracking-wide text-mythos-terminal-text-secondary">
          The chronicle is silent
        </p>
        <p className="mt-2 max-w-[min(100%,65ch)] font-mono text-sm leading-relaxed text-mythos-terminal-text-secondary/90">
          System, combat, and room events will stream here as they occur.
        </p>
      </div>
    ) : (
      messages.map((message, index) => (
        <div
          key={index}
          className={`message message-item mb-1.5 last:mb-0 ${getGameLogMessageRowClassName(message.messageType)}`}
          data-testid="game-log-message"
        >
          <div className="flex items-start gap-2.5">
            <span className="game-log-timestamp w-19 shrink-0 pt-0.5 text-left font-mono text-xs tabular-nums leading-none tracking-tight text-mythos-terminal-success/80">
              {formatGameLogTimestamp(message.timestamp)}
            </span>
            <div
              className={`min-w-0 flex-1 font-mono text-base leading-[1.65] antialiased ${getGameLogMessageClassName(message.messageType)}`}
              data-message-text={message.text}
            >
              {message.isHtml ? (
                <SafeHtml html={message.isCompleteHtml ? message.text : ansiToHtmlWithBreaks(message.text)} tag="div" />
              ) : (
                <span>{message.text}</span>
              )}
            </div>
          </div>
          {message.aliasChain && message.aliasChain.length > 0 && (
            <div className="ml-4 mt-1.5 max-w-[65ch] font-mono text-sm leading-normal text-mythos-terminal-text-secondary">
              <span className="font-medium text-mythos-terminal-secondary/70">Alias:</span>{' '}
              <span>{message.aliasChain.map(alias => alias.alias_name).join(' → ')}</span>
            </div>
          )}
        </div>
      ))
    )}
    <div ref={messagesEndRef} />
  </div>
);
