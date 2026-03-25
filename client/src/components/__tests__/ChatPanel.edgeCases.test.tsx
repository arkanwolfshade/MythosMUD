import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import React from 'react';
import { afterAll, beforeEach, describe, expect, it, vi } from 'vitest';
import { ChatPanel } from '../panels/ChatPanel';
import { createChatPanelDefaultProps } from './chatPanelTestHelpers';
import { mockConsoleLog } from './chatPanelTestSetup';

describe('ChatPanel', () => {
  let defaultProps: ReturnType<typeof createChatPanelDefaultProps>;

  beforeEach(() => {
    defaultProps = createChatPanelDefaultProps();
    vi.clearAllMocks();
    mockConsoleLog.mockClear();
  });

  afterAll(() => {
    mockConsoleLog.mockRestore();
  });

  describe('Edge Cases and Error Handling', () => {
    it('should handle messages with missing properties gracefully', () => {
      const incompleteMessages = [
        {
          text: 'Message without timestamp',
          timestamp: '2024-01-01T10:00:00Z',
          isHtml: false,
          messageType: 'chat',
          channel: 'local',
        },
        {
          text: 'Message without text',
          timestamp: '2024-01-01T10:00:00Z',
          isHtml: false,
          messageType: 'chat',
          channel: 'local',
        },
      ];

      expect(() => {
        render(<ChatPanel {...defaultProps} messages={incompleteMessages} />);
      }).not.toThrow();
    });

    it('should handle very long messages', () => {
      const longMessage = 'a'.repeat(1000);
      const messagesWithLongText = [
        {
          text: longMessage,
          timestamp: '2024-01-01T10:00:00Z',
          isHtml: false,
          messageType: 'chat',
          channel: 'local',
        },
      ];

      render(<ChatPanel {...defaultProps} messages={messagesWithLongText} />);

      expect(screen.getByText(longMessage)).toBeInTheDocument();
    });

    it('should handle many messages efficiently', () => {
      const manyMessages = Array.from({ length: 100 }, (_, i) => ({
        text: `Message ${i + 1}`,
        timestamp: `2024-01-01T${10 + Math.floor(i / 60)}:${i % 60}:00Z`,
        isHtml: false,
        messageType: 'chat',
        channel: 'local',
      }));

      expect(() => {
        render(<ChatPanel {...defaultProps} messages={manyMessages} />);
      }).not.toThrow();
    });

    it('should handle messages with special characters', () => {
      const specialMessages = [
        {
          text: 'Message with "quotes" & <html> tags',
          timestamp: '2024-01-01T10:00:00Z',
          isHtml: false,
          messageType: 'chat',
          channel: 'local',
        },
        {
          text: 'Message with \n newlines and \t tabs',
          timestamp: '2024-01-01T10:01:00Z',
          isHtml: true,
          messageType: 'chat',
          channel: 'local',
        },
      ];

      render(<ChatPanel {...defaultProps} messages={specialMessages} />);

      expect(screen.getByText(/Message with "quotes" &/)).toBeInTheDocument();
      expect(screen.getByText(/tags/)).toBeInTheDocument();
    });
  });
});
