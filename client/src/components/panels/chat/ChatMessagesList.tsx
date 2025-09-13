import React from 'react';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { ChatMessage } from './ChatMessage';

interface ChatMessagesListProps {
  messages: Array<{
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
  }>;
}

export const ChatMessagesList: React.FC<ChatMessagesListProps> = ({ messages }) => {
  if (messages.length === 0) {
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
      {messages.map((message, index) => (
        <ChatMessage key={index} message={message} index={index} />
      ))}
    </div>
  );
};
