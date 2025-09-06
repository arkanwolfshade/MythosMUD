import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { ChatPanelTest } from './ChatPanelTest';

// Mock all child components
vi.mock('./panels/ChatPanel', () => ({
  ChatPanel: ({
    messages,
    onClearMessages,
    onDownloadLogs,
  }: {
    messages: Array<Record<string, unknown>>;
    onClearMessages: () => void;
    onDownloadLogs: () => void;
  }) => (
    <div data-testid="chat-panel">
      <div data-testid="message-count">{messages.length} messages</div>
      <button onClick={onClearMessages} data-testid="clear-messages">
        Clear Messages
      </button>
      <button onClick={onDownloadLogs} data-testid="download-logs">
        Download Logs
      </button>
    </div>
  ),
}));

vi.mock('./ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, className }: { name: string; _size?: number; className?: string; _variant?: string }) => (
    <div data-testid={`eldritch-icon-${name}`} className={className}>
      {name}
    </div>
  ),
  MythosIcons: {
    chat: 'chat',
    move: 'move',
    clock: 'clock',
    download: 'download',
    clear: 'clear',
    connection: 'connection',
  },
}));

vi.mock('./ui/MythosPanel', () => ({
  MythosPanel: ({
    title,
    children,
    className,
  }: {
    title?: string;
    children: React.ReactNode;
    _variant?: string;
    _size?: string;
    className?: string;
  }) => (
    <div data-testid={`mythos-panel-${title?.toLowerCase().replace(/\s+/g, '-')}`} className={className}>
      {title && <h3 data-testid="panel-title">{title}</h3>}
      {children}
    </div>
  ),
}));

vi.mock('./ui/TerminalButton', () => ({
  TerminalButton: ({
    children,
    onClick,
    disabled,
    className,
  }: {
    children: React.ReactNode;
    onClick?: () => void;
    _variant?: string;
    _size?: string;
    disabled?: boolean;
    className?: string;
  }) => (
    <button onClick={onClick} disabled={disabled} className={className} data-testid="terminal-button">
      {children}
    </button>
  ),
}));

vi.mock('./ui/TerminalInput', () => ({
  TerminalInput: ({
    value,
    onChange,
    placeholder,
    onKeyDown,
  }: {
    value: string;
    onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
    placeholder?: string;
    onKeyDown?: (event: React.KeyboardEvent) => void;
  }) => (
    <input
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      onKeyDown={onKeyDown}
      data-testid="terminal-input"
    />
  ),
}));

// Mock global objects
const mockClick = vi.fn();
const mockCreateObjectURL = vi.fn();
const mockRevokeObjectURL = vi.fn();

// Mock URL methods
Object.defineProperty(URL, 'createObjectURL', {
  value: mockCreateObjectURL,
  writable: true,
});

Object.defineProperty(URL, 'revokeObjectURL', {
  value: mockRevokeObjectURL,
  writable: true,
});

describe('ChatPanelTest', () => {
  beforeEach(() => {
    vi.clearAllMocks();

    // Mock document.createElement for specific tests that need it
    const originalCreateElement = document.createElement;
    document.createElement = vi.fn((tagName: string) => {
      if (tagName === 'a') {
        return {
          href: '',
          download: '',
          click: mockClick,
        } as unknown as HTMLAnchorElement;
      }
      return originalCreateElement.call(document, tagName);
    });

    mockCreateObjectURL.mockReturnValue('mock-url');
  });

  describe('Initial Rendering', () => {
    it('should render the main title and description', () => {
      render(<ChatPanelTest />);

      expect(screen.getByText('Enhanced Chat Panel')).toBeInTheDocument();
      expect(screen.getByText(/Mythos-themed chat interface/)).toBeInTheDocument();
    });

    it('should render panel sections', () => {
      render(<ChatPanelTest />);

      expect(screen.getByTestId('mythos-panel-chat-interface')).toBeInTheDocument();
      expect(screen.getByTestId('mythos-panel-message-controls')).toBeInTheDocument();
      expect(screen.getByTestId('mythos-panel-sample-messages')).toBeInTheDocument();
      expect(screen.getByTestId('mythos-panel-statistics')).toBeInTheDocument();
    });

    it('should render initial messages', () => {
      render(<ChatPanelTest />);

      // Check that the chat panel shows the initial message count
      expect(screen.getByTestId('message-count')).toHaveTextContent('13 messages');
    });
  });

  describe('Message Controls', () => {
    it('should render message type selector', () => {
      render(<ChatPanelTest />);

      expect(screen.getByText('Message Type:')).toBeInTheDocument();
      expect(screen.getByRole('combobox')).toBeInTheDocument();
      expect(screen.getByText('Chat')).toBeInTheDocument();
    });

    it('should render message input', () => {
      render(<ChatPanelTest />);

      expect(screen.getByPlaceholderText('Type your message...')).toBeInTheDocument();
    });

    it('should handle message type changes', () => {
      render(<ChatPanelTest />);

      const select = screen.getByRole('combobox');
      fireEvent.change(select, { target: { value: 'whisper' } });

      expect(select).toHaveValue('whisper');
    });

    it('should handle message input changes', () => {
      render(<ChatPanelTest />);

      const input = screen.getByPlaceholderText('Type your message...');
      fireEvent.change(input, { target: { value: 'Test message' } });

      expect(input).toHaveValue('Test message');
    });
  });

  describe('Message Functions', () => {
    it('should add new message when send button is clicked', async () => {
      render(<ChatPanelTest />);

      const input = screen.getByPlaceholderText('Type your message...');
      const sendButton = screen.getByText('Send Message');

      // Initially disabled
      expect(sendButton).toBeDisabled();

      // Type a message
      fireEvent.change(input, { target: { value: 'Test message' } });

      // Now enabled
      expect(sendButton).not.toBeDisabled();

      // Send the message
      fireEvent.click(sendButton);

      await waitFor(() => {
        expect(screen.getByTestId('message-count')).toHaveTextContent('14 messages');
      });

      // Input should be cleared
      expect(input).toHaveValue('');
    });

    it('should not add empty messages', () => {
      render(<ChatPanelTest />);

      const sendButton = screen.getByText('Send Message');

      // Should be disabled initially
      expect(sendButton).toBeDisabled();

      // Try to send empty message
      fireEvent.click(sendButton);

      // Message count should remain the same
      expect(screen.getByTestId('message-count')).toHaveTextContent('13 messages');
    });

    it('should clear messages when clear button is clicked', async () => {
      render(<ChatPanelTest />);

      const clearButton = screen.getByTestId('clear-messages');
      fireEvent.click(clearButton);

      await waitFor(() => {
        expect(screen.getByTestId('message-count')).toHaveTextContent('0 messages');
      });
    });

    it('should download logs when download button is clicked', () => {
      render(<ChatPanelTest />);

      const downloadButton = screen.getByTestId('download-logs');
      fireEvent.click(downloadButton);

      expect(document.createElement).toHaveBeenCalledWith('a');
      expect(mockCreateObjectURL).toHaveBeenCalled();
      expect(mockClick).toHaveBeenCalled();
      expect(mockRevokeObjectURL).toHaveBeenCalled();
    });
  });

  describe('Sample Messages', () => {
    it('should render sample message buttons', () => {
      render(<ChatPanelTest />);

      expect(screen.getByText('Add System Message')).toBeInTheDocument();
      expect(screen.getByText('Add Emote')).toBeInTheDocument();
      expect(screen.getByText('Add Whisper')).toBeInTheDocument();
      expect(screen.getByText('Add Error')).toBeInTheDocument();
      expect(screen.getByText('Add Alias Expansion')).toBeInTheDocument();
    });

    it('should add sample system message', async () => {
      render(<ChatPanelTest />);

      const addSystemButton = screen.getByText('Add System Message');
      fireEvent.click(addSystemButton);

      await waitFor(() => {
        expect(screen.getByTestId('message-count')).toHaveTextContent('14 messages');
      });
    });

    it('should add sample emote message', async () => {
      render(<ChatPanelTest />);

      const addEmoteButton = screen.getByText('Add Emote');
      fireEvent.click(addEmoteButton);

      await waitFor(() => {
        expect(screen.getByTestId('message-count')).toHaveTextContent('14 messages');
      });
    });

    it('should add sample whisper message', async () => {
      render(<ChatPanelTest />);

      const addWhisperButton = screen.getByText('Add Whisper');
      fireEvent.click(addWhisperButton);

      await waitFor(() => {
        expect(screen.getByTestId('message-count')).toHaveTextContent('14 messages');
      });
    });

    it('should add sample error message', async () => {
      render(<ChatPanelTest />);

      const addErrorButton = screen.getByText('Add Error');
      fireEvent.click(addErrorButton);

      await waitFor(() => {
        expect(screen.getByTestId('message-count')).toHaveTextContent('14 messages');
      });
    });

    it('should add alias expansion message', async () => {
      render(<ChatPanelTest />);

      const addAliasButton = screen.getByText('Add Alias Expansion');
      fireEvent.click(addAliasButton);

      await waitFor(() => {
        expect(screen.getByTestId('message-count')).toHaveTextContent('14 messages');
      });
    });
  });

  describe('Keyboard Shortcuts', () => {
    it('should handle Enter key press to send message', async () => {
      render(<ChatPanelTest />);

      const input = screen.getByPlaceholderText('Type your message...');

      // Type a message
      fireEvent.change(input, { target: { value: 'Test message' } });

      // Press Enter
      fireEvent.keyDown(input, { key: 'Enter' });

      await waitFor(() => {
        expect(screen.getByTestId('message-count')).toHaveTextContent('14 messages');
      });

      // Input should be cleared
      expect(input).toHaveValue('');
    });

    it('should not send message on other key presses', () => {
      render(<ChatPanelTest />);

      const input = screen.getByPlaceholderText('Type your message...');

      // Type a message
      fireEvent.change(input, { target: { value: 'Test message' } });

      // Press Space
      fireEvent.keyDown(input, { key: ' ' });

      // Message count should remain the same
      expect(screen.getByTestId('message-count')).toHaveTextContent('13 messages');

      // Input should still have the value
      expect(input).toHaveValue('Test message');
    });
  });

  describe('Statistics', () => {
    it('should display message statistics', () => {
      render(<ChatPanelTest />);

      expect(screen.getByText('Total Messages:')).toBeInTheDocument();
      expect(screen.getByText('13')).toBeInTheDocument(); // Total messages
      expect(screen.getByText('System Messages:')).toBeInTheDocument();
      expect(screen.getByText('Chat Messages:')).toBeInTheDocument();
      expect(screen.getByText('Whispers:')).toBeInTheDocument();
      expect(screen.getByText('Emotes:')).toBeInTheDocument();
      expect(screen.getByText('Errors:')).toBeInTheDocument();
      expect(screen.getByText('With Aliases:')).toBeInTheDocument();
    });
  });
});
