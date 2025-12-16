/**
 * Tests for ChatMessage component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { ChatMessage } from '../ChatMessage';

// Mock ansiToHtmlWithBreaks
vi.mock('../../../utils/ansiToHtml', () => ({
  ansiToHtmlWithBreaks: (text: string) => `<span>${(text)}</span>`,
}));

// Mock inputSanitizer
vi.mock('../../../utils/security', () => ({
  inputSanitizer: {
    sanitizeIncomingHtml: (html: string) => html,
  },
}));

// Mock EldritchIcon
vi.mock('../../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, variant }: { name: string; variant?: string }) => (
    <span data-testid={`icon-${name}-${variant || 'default'}`}>icon</span>
  ),
  MythosIcons: {
    move: 'move',
    exit: 'exit',
  },
}));

describe('ChatMessage', () => {
  const mockMessage = {
    text: 'Test message',
    timestamp: '2024-01-01T12:00:00Z',
    isHtml: false,
  };

  it('should render message text', () => {
    render(<ChatMessage message={mockMessage} index={0} />);
    expect(screen.getByText('Test message')).toBeInTheDocument();
  });

  it('should render timestamp', () => {
    render(<ChatMessage message={mockMessage} index={0} />);
    // Timestamp should be formatted and displayed
    const timestampElements = screen.getAllByText(/\d{1,2}:\d{2}:\d{2}/);
    expect(timestampElements.length).toBeGreaterThan(0);
  });

  it('should render HTML content when isHtml is true', () => {
    const htmlMessage = {
      ...mockMessage,
      text: '<b>Bold text</b>',
      isHtml: true,
    };
    render(<ChatMessage message={htmlMessage} index={0} />);
    expect(screen.getByText(/Bold text/i)).toBeInTheDocument();
  });

  it('should render complete HTML when isCompleteHtml is true', () => {
    const htmlMessage = {
      ...mockMessage,
      text: '<div>Complete HTML</div>',
      isHtml: true,
      isCompleteHtml: true,
    };
    render(<ChatMessage message={htmlMessage} index={0} />);
    // HTML should be rendered
    expect(screen.getByText(/Complete HTML/i)).toBeInTheDocument();
  });

  it('should apply correct CSS class for emote message type', () => {
    const emoteMessage = {
      ...mockMessage,
      messageType: 'emote',
    };
    const { container } = render(<ChatMessage message={emoteMessage} index={0} />);
    const messageElement = container.querySelector('.text-mythos-terminal-primary');
    expect(messageElement).toBeInTheDocument();
  });

  it('should apply correct CSS class for system message type', () => {
    const systemMessage = {
      ...mockMessage,
      messageType: 'system',
    };
    const { container } = render(<ChatMessage message={systemMessage} index={0} />);
    const messageElement = container.querySelector('.text-mythos-terminal-warning');
    expect(messageElement).toBeInTheDocument();
  });

  it('should apply correct CSS class for error message type', () => {
    const errorMessage = {
      ...mockMessage,
      messageType: 'error',
    };
    const { container } = render(<ChatMessage message={errorMessage} index={0} />);
    const messageElement = container.querySelector('.text-mythos-terminal-error');
    expect(messageElement).toBeInTheDocument();
  });

  it('should apply correct CSS class for whisper message type', () => {
    const whisperMessage = {
      ...mockMessage,
      messageType: 'whisper',
    };
    const { container } = render(<ChatMessage message={whisperMessage} index={0} />);
    const messageElement = container.querySelector('.text-mythos-terminal-secondary');
    expect(messageElement).toBeInTheDocument();
  });

  it('should apply correct CSS class for shout message type', () => {
    const shoutMessage = {
      ...mockMessage,
      messageType: 'shout',
    };
    const { container } = render(<ChatMessage message={shoutMessage} index={0} />);
    const messageElement = container.querySelector('.text-mythos-terminal-warning');
    expect(messageElement).toBeInTheDocument();
  });

  it('should render alias chain when present', () => {
    const messageWithAlias = {
      ...mockMessage,
      aliasChain: [
        {
          original: 'say hello',
          expanded: 'say hello to everyone',
          alias_name: 'greet',
        },
      ],
    };
    render(<ChatMessage message={messageWithAlias} index={0} />);
    expect(screen.getByText(/Alias Expansion:/i)).toBeInTheDocument();
    expect(screen.getByText('say hello')).toBeInTheDocument();
    expect(screen.getByText('say hello to everyone')).toBeInTheDocument();
  });

  it('should render multiple alias chain entries', () => {
    const messageWithMultipleAliases = {
      ...mockMessage,
      aliasChain: [
        {
          original: 'say hello',
          expanded: 'say hello to everyone',
          alias_name: 'greet',
        },
        {
          original: 'look',
          expanded: 'look around',
          alias_name: 'observe',
        },
      ],
    };
    render(<ChatMessage message={messageWithMultipleAliases} index={0} />);
    expect(screen.getByText('say hello')).toBeInTheDocument();
    expect(screen.getByText('say hello to everyone')).toBeInTheDocument();
    expect(screen.getByText('look')).toBeInTheDocument();
    expect(screen.getByText('look around')).toBeInTheDocument();
  });

  it('should not render alias chain when absent', () => {
    render(<ChatMessage message={mockMessage} index={0} />);
    expect(screen.queryByText(/Alias Expansion:/i)).not.toBeInTheDocument();
  });

  it('should handle context menu event', () => {
    const messageWithAlias = {
      ...mockMessage,
      aliasChain: [],
    };
    const { container } = render(<ChatMessage message={messageWithAlias} index={0} />);
    const messageContent = container.querySelector('[title="Right-click to ignore user"]');
    expect(messageContent).toBeInTheDocument();

    if (messageContent) {
      const contextMenuEvent = new MouseEvent('contextmenu', {
        bubbles: true,
        cancelable: true,
      });
      const preventDefaultSpy = vi.spyOn(contextMenuEvent, 'preventDefault');
      fireEvent(messageContent, contextMenuEvent);
      expect(preventDefaultSpy).toHaveBeenCalled();
    }
  });

  it('should handle invalid timestamp gracefully', () => {
    const messageWithInvalidTimestamp = {
      ...mockMessage,
      timestamp: 'invalid-date',
    };
    render(<ChatMessage message={messageWithInvalidTimestamp} index={0} />);
    // Should not throw error, should display "Invalid Date" when date parsing fails
    // formatTimestamp catches the error and returns timestamp, but new Date('invalid-date')
    // creates an Invalid Date, and toLocaleTimeString() on Invalid Date returns "Invalid Date"
    expect(screen.getByText('Invalid Date')).toBeInTheDocument();
  });

  it('should use rawText when provided for non-HTML messages', () => {
    const messageWithRawText = {
      ...mockMessage,
      text: 'Processed text',
      rawText: 'Raw text',
      isHtml: false,
    };
    render(<ChatMessage message={messageWithRawText} index={0} />);
    expect(screen.getByText('Raw text')).toBeInTheDocument();
    expect(screen.queryByText('Processed text')).not.toBeInTheDocument();
  });

  it('should have correct test id', () => {
    const { container } = render(<ChatMessage message={mockMessage} index={0} />);
    const messageElement = container.querySelector('[data-testid="chat-message"]');
    expect(messageElement).toBeInTheDocument();
  });

  it('should apply animation delay based on index', () => {
    const { container } = render(<ChatMessage message={mockMessage} index={5} />);
    const messageElement = container.querySelector('[style*="animation-delay"]');
    expect(messageElement).toBeInTheDocument();
    expect(messageElement?.getAttribute('style')).toContain('250ms'); // 5 * 50ms
  });
});
