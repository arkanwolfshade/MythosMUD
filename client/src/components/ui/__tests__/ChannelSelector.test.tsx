import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { vi } from 'vitest';
import { Channel, ChannelSelector } from '../ChannelSelector';
import { MythosIcons } from '../EldritchIcon';

// Mock the EldritchIcon component
vi.mock('../EldritchIcon', () => ({
  EldritchIcon: ({
    name,
    size,
    variant,
    className,
  }: {
    name: string;
    size?: string;
    variant?: string;
    className?: string;
  }) => (
    <div data-testid={`icon-${name}`} data-size={size} data-variant={variant} className={className}>
      {name}
    </div>
  ),
  MythosIcons: {
    chat: 'chat',
    local: 'local',
    global: 'global',
    whisper: 'whisper',
    system: 'system',
    exit: 'exit',
    connection: 'connection',
  },
}));

const mockChannels: Channel[] = [
  {
    id: 'say',
    name: 'Say',
    description: 'Speak to players in the same room',
    icon: MythosIcons.chat,
    color: 'text-mythos-terminal-text',
    shortcut: 'say',
  },
  {
    id: 'local',
    name: 'Local',
    description: 'Chat with players in the same sub-zone',
    icon: MythosIcons.local,
    color: 'text-mythos-terminal-primary',
    shortcut: 'l',
  },
  {
    id: 'global',
    name: 'Global',
    description: 'Chat with all players on the server',
    icon: MythosIcons.global,
    color: 'text-mythos-terminal-warning',
    shortcut: 'g',
  },
  {
    id: 'whisper',
    name: 'Whisper',
    description: 'Private message to a specific player',
    icon: MythosIcons.whisper,
    color: 'text-mythos-terminal-secondary',
    shortcut: 'w',
    disabled: true,
  },
];

describe('ChannelSelector', () => {
  const defaultProps = {
    channels: mockChannels,
    selectedChannel: 'say',
    onChannelSelect: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders the selected channel correctly', () => {
    render(<ChannelSelector {...defaultProps} />);

    expect(screen.getByText('Say')).toBeInTheDocument();
    expect(screen.getByText('/say')).toBeInTheDocument();
    expect(screen.getByTestId('icon-chat')).toBeInTheDocument();
  });

  it('shows dropdown when clicked', async () => {
    render(<ChannelSelector {...defaultProps} />);

    const button = screen.getByRole('button');
    fireEvent.click(button);

    await waitFor(() => {
      expect(screen.getByText('Local')).toBeInTheDocument();
      expect(screen.getByText('Global')).toBeInTheDocument();
      expect(screen.getByText('Whisper')).toBeInTheDocument();
    });
  });

  it('calls onChannelSelect when a channel is selected', async () => {
    const onChannelSelect = vi.fn();
    render(<ChannelSelector {...defaultProps} onChannelSelect={onChannelSelect} />);

    const button = screen.getByRole('button');
    fireEvent.click(button);

    await waitFor(() => {
      const localButton = screen.getByText('Local');
      fireEvent.click(localButton);
    });

    expect(onChannelSelect).toHaveBeenCalledWith('local');
  });

  it('closes dropdown after selecting a channel', async () => {
    const onChannelSelect = vi.fn();
    render(<ChannelSelector {...defaultProps} onChannelSelect={onChannelSelect} />);

    const button = screen.getByRole('button');
    fireEvent.click(button);

    await waitFor(() => {
      const localButton = screen.getByText('Local');
      fireEvent.click(localButton);
    });

    // Verify dropdown is closed after selection
    await waitFor(() => {
      expect(screen.queryByText('Global')).not.toBeInTheDocument();
      expect(screen.queryByText('Whisper')).not.toBeInTheDocument();
    });
  });

  it('closes dropdown when clicking outside', async () => {
    render(<ChannelSelector {...defaultProps} />);

    const button = screen.getByRole('button');
    fireEvent.click(button);

    await waitFor(() => {
      expect(screen.getByText('Local')).toBeInTheDocument();
    });

    // Click the backdrop to close the dropdown
    const backdrop = screen.getByTestId('dropdown-backdrop');
    fireEvent.click(backdrop);

    await waitFor(() => {
      expect(screen.queryByText('Local')).not.toBeInTheDocument();
    });
  });

  it('disables the selector when disabled prop is true', () => {
    render(<ChannelSelector {...defaultProps} disabled={true} />);

    const button = screen.getByRole('button');
    expect(button).toBeDisabled();
  });

  it('shows disabled channels as disabled in dropdown', async () => {
    render(<ChannelSelector {...defaultProps} />);

    const button = screen.getByRole('button');
    fireEvent.click(button);

    await waitFor(() => {
      const whisperButton = screen.getByText('Whisper').closest('button');
      expect(whisperButton).toBeDisabled();
    });
  });

  it('displays channel descriptions in dropdown', async () => {
    render(<ChannelSelector {...defaultProps} />);

    const button = screen.getByRole('button');
    fireEvent.click(button);

    await waitFor(() => {
      expect(screen.getByText('Speak to players in the same room')).toBeInTheDocument();
      expect(screen.getByText('Chat with players in the same sub-zone')).toBeInTheDocument();
      expect(screen.getByText('Chat with all players on the server')).toBeInTheDocument();
    });
  });

  it('highlights the selected channel in dropdown', async () => {
    render(<ChannelSelector {...defaultProps} selectedChannel="local" />);

    const button = screen.getByRole('button');
    fireEvent.click(button);

    await waitFor(() => {
      // Find the Local button in the dropdown (not the main button)
      const dropdownButtons = screen.getAllByRole('button');
      const localDropdownButton = dropdownButtons.find(
        btn => btn.textContent?.includes('Local') && btn.textContent?.includes('Chat with players in the same sub-zone')
      );
      expect(localDropdownButton).toHaveClass('bg-mythos-terminal-primary/20');
    });
  });

  it('rotates the dropdown arrow when open', async () => {
    render(<ChannelSelector {...defaultProps} />);

    const button = screen.getByRole('button');
    fireEvent.click(button);

    await waitFor(() => {
      const arrow = screen.getByTestId('icon-exit');
      expect(arrow).toHaveClass('rotate-90');
    });
  });

  it('applies custom className', () => {
    render(<ChannelSelector {...defaultProps} className="custom-class" />);

    const container = screen.getByRole('button').parentElement;
    expect(container).toHaveClass('custom-class');
  });

  it('handles empty channels array', () => {
    render(<ChannelSelector {...defaultProps} channels={[]} />);

    const button = screen.getByRole('button');
    expect(button).toBeInTheDocument();

    fireEvent.click(button);

    // Should not show any dropdown items
    expect(screen.queryByRole('button', { name: /Local/ })).not.toBeInTheDocument();
  });

  it('handles channel without shortcut', () => {
    const channelsWithoutShortcut = [
      {
        id: 'custom',
        name: 'Custom',
        description: 'Custom channel',
        icon: MythosIcons.chat,
        color: 'text-mythos-terminal-text',
      },
    ];

    render(<ChannelSelector {...defaultProps} channels={channelsWithoutShortcut} selectedChannel="custom" />);

    expect(screen.getByText('Custom')).toBeInTheDocument();
    expect(screen.queryByText('/custom')).not.toBeInTheDocument();
  });
});
