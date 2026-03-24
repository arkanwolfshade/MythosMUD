import { ChatPanelRuntimeViewInner } from './ChatPanelRuntimeViewParts';
import type { ChatPanelRuntimeViewProps } from './chatPanelRuntimeViewTypes';

export function ChatPanelRuntimeView(props: ChatPanelRuntimeViewProps) {
  return <ChatPanelRuntimeViewInner {...props} />;
}

export type { ChatPanelRuntimeViewProps } from './chatPanelRuntimeViewTypes';
