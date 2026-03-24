import React from 'react';
import { ChatPanelRuntimeView } from './ChatPanelRuntimeView';
import { useChatPanelRuntime, type ChatPanelProps } from './useChatPanelRuntime';

export type { ChatPanelMessage } from './chatPanelRuntimeUtils';
export type { ChatPanelProps } from './useChatPanelRuntime';

export const ChatPanel: React.FC<ChatPanelProps> = props => {
  const viewProps = useChatPanelRuntime(props);
  return <ChatPanelRuntimeView {...viewProps} />;
};
