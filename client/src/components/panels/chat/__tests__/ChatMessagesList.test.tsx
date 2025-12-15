/**
 * Tests for ChatMessagesList component.
 */

import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { ChatMessagesList } from '../ChatMessagesList';

// Mock ChatMessage
vi.mock('../ChatMessage', () => ({
  ChatMessage: ({ message }: { message: { text: string } }) => <div>{message.text}</div>,
}));

// Mock EldritchIcon
vi.mock('../../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name }: { name: string }) => <span data-testid={`icon-${name}`}>icon</span>,
  MythosIcons: {
    chat: 'chat',
  },
}));

describe('ChatMessagesList', () => {
  const mockMessages = [
    {
      text: 'First message',
      timestamp: '2024-01-01T12:00:00Z',
      isHtml: false,
    },
    {
      text: 'Second message',
      timestamp: '2024-01-01T12:00:01Z',
      isHtml: false,
    },
    {
      text: 'Third message',
      timestamp: '2024-01-01T12:00:02Z',
      isHtml: false,
    },
  ];

  it('should render all messages', () => {
    render(<ChatMessagesList messages={mockMessages} />);
    expect(screen.getByText('First message')).toBeInTheDocument();
    expect(screen.getByText('Second message')).toBeInTheDocument();
    expect(screen.getByText('Third message')).toBeInTheDocument();
  });

  it('should render empty state when no messages', () => {
    render(<ChatMessagesList messages={[]} />);
    expect(screen.getByText(/No messages yet/i)).toBeInTheDocument();
    expect(screen.getByText(/Start chatting to see messages here/i)).toBeInTheDocument();
  });

  it('should have correct test id', () => {
    const { container } = render(<ChatMessagesList messages={mockMessages} />);
    const listElement = container.querySelector('[data-testid="chat-messages-list"]');
    expect(listElement).toBeInTheDocument();
  });

  it('should render messages with HTML content', () => {
    const htmlMessages = [
      {
        text: '<b>Bold message</b>',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: true,
      },
    ];
    render(<ChatMessagesList messages={htmlMessages} />);
    // ChatMessage component will handle HTML rendering
    expect(screen.getByText(/Bold message/i)).toBeInTheDocument();
  });

  it('should render messages with different message types', () => {
    const mixedMessages = [
      {
        text: 'System message',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        messageType: 'system',
      },
      {
        text: 'Emote message',
        timestamp: '2024-01-01T12:00:01Z',
        isHtml: false,
        messageType: 'emote',
      },
    ];
    render(<ChatMessagesList messages={mixedMessages} />);
    expect(screen.getByText('System message')).toBeInTheDocument();
    expect(screen.getByText('Emote message')).toBeInTheDocument();
  });

  it('should render messages with alias chains', () => {
    const messagesWithAlias = [
      {
        text: 'You say hello',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        aliasChain: [
          {
            original: 'say hello',
            expanded: 'say hello to everyone',
            alias_name: 'greet',
          },
        ],
      },
    ];
    render(<ChatMessagesList messages={messagesWithAlias} />);
    expect(screen.getByText('You say hello')).toBeInTheDocument();
  });
});
