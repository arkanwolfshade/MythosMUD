import { vi } from 'vitest';

export type ChatPanelTestMessage = {
  text: string;
  timestamp: string;
  isHtml: boolean;
  messageType: string;
  channel?: string;
  aliasChain?: Array<{ original: string; expanded: string; alias_name: string }>;
};

export const mockMessages: ChatPanelTestMessage[] = [
  {
    text: '[local] Player1 says: Hello everyone!',
    timestamp: '2024-01-01T10:00:00Z',
    isHtml: false,
    messageType: 'chat',
    channel: 'local',
  },
  {
    text: '[whisper] Player2 whispers: Secret message',
    timestamp: '2024-01-01T10:01:00Z',
    isHtml: false,
    messageType: 'chat',
    channel: 'whisper',
  },
  {
    text: 'System: Welcome to the game!',
    timestamp: '2024-01-01T10:02:00Z',
    isHtml: false,
    messageType: 'system',
  },
  {
    text: 'You move north.',
    timestamp: '2024-01-01T10:03:00Z',
    isHtml: false,
    messageType: 'command',
  },
];

export function createChatPanelDefaultProps() {
  return {
    messages: mockMessages,
    onSendChatMessage: vi.fn(),
    onClearMessages: vi.fn(),
    onDownloadLogs: vi.fn(),
    disabled: false,
    isConnected: true,
    selectedChannel: 'local',
    onChannelSelect: vi.fn(),
  };
}
