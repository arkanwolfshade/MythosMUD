import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { DraggablePanelTest } from './DraggablePanelTest';

// Mock all child components
vi.mock('./DraggablePanel', () => ({
  DraggablePanel: ({
    title,
    defaultPosition,
    defaultSize,
    onClose,
    onMinimize,
    onMaximize,
    children,
  }: {
    title: string;
    _variant?: string;
    defaultPosition: { x: number; y: number };
    defaultSize: { width: number; height: number };
    onClose: () => void;
    onMinimize: () => void;
    onMaximize: () => void;
    children: React.ReactNode;
  }) => (
    <div data-testid={`draggable-panel-${title.toLowerCase().replace(/\s+/g, '-')}`}>
      <div data-testid="panel-header">
        <h3 data-testid="panel-title">{title}</h3>
        <button onClick={onClose} data-testid="close-button">
          Close
        </button>
        <button onClick={onMinimize} data-testid="minimize-button">
          Minimize
        </button>
        <button onClick={onMaximize} data-testid="maximize-button">
          Maximize
        </button>
      </div>
      <div data-testid="panel-content">{children}</div>
      <div data-testid="panel-position">
        Position: ({defaultPosition.x}, {defaultPosition.y})
      </div>
      <div data-testid="panel-size">
        Size: {defaultSize.width} × {defaultSize.height}
      </div>
    </div>
  ),
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
    onChange: (value: string) => void;
    placeholder?: string;
    onKeyDown?: (event: React.KeyboardEvent) => void;
  }) => (
    <input
      value={value}
      onChange={e => { onChange(e.target.value); }}
      placeholder={placeholder}
      onKeyDown={onKeyDown}
      data-testid="terminal-input"
    />
  ),
}));

vi.mock('./ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, className }: { name: string; _size?: number; className?: string; _variant?: string }) => (
    <div data-testid={`eldritch-icon-${name}`} className={className}>
      {name}
    </div>
  ),
  MythosIcons: {
    maximize: 'maximize',
    clear: 'clear',
    chat: 'chat',
    settings: 'settings',
  },
}));

// Mock console.log
const mockConsoleLog = vi.fn();
Object.defineProperty(console, 'log', {
  value: mockConsoleLog,
  writable: true,
});

describe('DraggablePanelTest', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Initial Rendering', () => {
    it('should render the main title and description', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByText('DraggablePanel Test')).toBeInTheDocument();
      expect(screen.getByText(/Enhanced Mythos-themed draggable panels/)).toBeInTheDocument();
    });

    it('should render panel controls', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByTestId('mythos-panel-panel-controls')).toBeInTheDocument();
      expect(screen.getByText('Add New Panel')).toBeInTheDocument();
      expect(screen.getByText('Clear All Panels')).toBeInTheDocument();
    });

    it('should render initial panels', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByTestId('draggable-panel-chat-panel')).toBeInTheDocument();
      expect(screen.getByTestId('draggable-panel-command-panel')).toBeInTheDocument();
      expect(screen.getByTestId('draggable-panel-eldritch-panel')).toBeInTheDocument();
    });

    it('should display panel titles correctly', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByText('Chat Panel')).toBeInTheDocument();
      expect(screen.getByText('Command Panel')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Panel')).toBeInTheDocument();
    });

    it('should display panel positions and sizes', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByText('Position: (50, 50)')).toBeInTheDocument();
      expect(screen.getByText('Position: (400, 50)')).toBeInTheDocument();
      expect(screen.getByText('Position: (50, 500)')).toBeInTheDocument();
      expect(screen.getByText('Size: 300 × 400')).toBeInTheDocument();
      expect(screen.getByText('Size: 350 × 300')).toBeInTheDocument();
      expect(screen.getByText('Size: 400 × 300')).toBeInTheDocument();
    });
  });

  describe('Panel Management', () => {
    it('should add a new panel when Add New Panel button is clicked', async () => {
      render(<DraggablePanelTest />);

      const addButton = screen.getByText('Add New Panel');
      fireEvent.click(addButton);

      await waitFor(() => {
        expect(screen.getByTestId('draggable-panel-new-default-panel')).toBeInTheDocument();
      });
    });

    it('should add multiple panels with correct variants', async () => {
      render(<DraggablePanelTest />);

      const addButton = screen.getByText('Add New Panel');

      // Add first panel (should be Default)
      fireEvent.click(addButton);
      await waitFor(() => {
        expect(screen.getByText('New Default Panel')).toBeInTheDocument();
      });

      // Add second panel (should be Elevated)
      fireEvent.click(addButton);
      await waitFor(() => {
        expect(screen.getByText('New Elevated Panel')).toBeInTheDocument();
      });

      // Add third panel (should be Eldritch)
      fireEvent.click(addButton);
      await waitFor(() => {
        expect(screen.getByText('New Eldritch Panel')).toBeInTheDocument();
      });
    });

    it('should clear all panels when Clear All Panels button is clicked', async () => {
      render(<DraggablePanelTest />);

      const clearButton = screen.getByText('Clear All Panels');
      fireEvent.click(clearButton);

      await waitFor(() => {
        expect(screen.queryByTestId('draggable-panel-chat-panel')).not.toBeInTheDocument();
        expect(screen.queryByTestId('draggable-panel-command-panel')).not.toBeInTheDocument();
        expect(screen.queryByTestId('draggable-panel-eldritch-panel')).not.toBeInTheDocument();
      });
    });

    it('should close individual panels when close button is clicked', async () => {
      render(<DraggablePanelTest />);

      const closeButtons = screen.getAllByTestId('close-button');
      fireEvent.click(closeButtons[0]); // Close first panel

      await waitFor(() => {
        expect(screen.queryByTestId('draggable-panel-chat-panel')).not.toBeInTheDocument();
        expect(screen.getByTestId('draggable-panel-command-panel')).toBeInTheDocument();
        expect(screen.getByTestId('draggable-panel-eldritch-panel')).toBeInTheDocument();
      });
    });
  });

  describe('Panel Controls', () => {
    it('should call minimize function when minimize button is clicked', () => {
      render(<DraggablePanelTest />);

      const minimizeButtons = screen.getAllByTestId('minimize-button');
      fireEvent.click(minimizeButtons[0]);

      expect(mockConsoleLog).toHaveBeenCalledWith('Minimize panel:', '1');
    });

    it('should call maximize function when maximize button is clicked', () => {
      render(<DraggablePanelTest />);

      const maximizeButtons = screen.getAllByTestId('maximize-button');
      fireEvent.click(maximizeButtons[0]);

      expect(mockConsoleLog).toHaveBeenCalledWith('Maximize panel:', '1');
    });

    it('should call close function when close button is clicked', async () => {
      render(<DraggablePanelTest />);

      const closeButtons = screen.getAllByTestId('close-button');
      fireEvent.click(closeButtons[0]);

      await waitFor(() => {
        expect(screen.queryByTestId('draggable-panel-chat-panel')).not.toBeInTheDocument();
      });
    });
  });

  describe('Panel Content', () => {
    it('should render panel content with correct variants', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByText('Default Content')).toBeInTheDocument();
      expect(screen.getByText('Elevated Content')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Content')).toBeInTheDocument();
    });

    it('should display panel variant information', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByText('default')).toBeInTheDocument();
      expect(screen.getByText('elevated')).toBeInTheDocument();
      expect(screen.getByText('eldritch')).toBeInTheDocument();
    });

    it('should display panel IDs', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByText('1')).toBeInTheDocument();
      expect(screen.getByText('2')).toBeInTheDocument();
      expect(screen.getByText('3')).toBeInTheDocument();
    });

    it('should render input fields in panels', () => {
      render(<DraggablePanelTest />);

      const inputs = screen.getAllByPlaceholderText('Type something...');
      expect(inputs).toHaveLength(3);
    });

    it('should render action buttons in panels', () => {
      render(<DraggablePanelTest />);

      expect(screen.getAllByText('Action')).toHaveLength(3);
      expect(screen.getAllByText('Settings')).toHaveLength(3);
    });
  });

  describe('Instructions Panel', () => {
    it('should render instructions panel', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByTestId('mythos-panel-instructions')).toBeInTheDocument();
      expect(screen.getByText('Instructions')).toBeInTheDocument();
    });

    it('should display panel variants information', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByText('Panel Variants')).toBeInTheDocument();
      expect(screen.getByText(/Default:/)).toBeInTheDocument();
      expect(screen.getByText(/Elevated:/)).toBeInTheDocument();
      expect(screen.getByText(/Eldritch:/)).toBeInTheDocument();
    });

    it('should display controls information', () => {
      render(<DraggablePanelTest />);

      expect(screen.getByText('Controls')).toBeInTheDocument();
      expect(screen.getByText(/Drag:/)).toBeInTheDocument();
      expect(screen.getByText(/Resize:/)).toBeInTheDocument();
      expect(screen.getByText(/Minimize:/)).toBeInTheDocument();
      expect(screen.getByText(/Maximize:/)).toBeInTheDocument();
      expect(screen.getByText(/Close:/)).toBeInTheDocument();
      expect(screen.getByText(/Grid Snap:/)).toBeInTheDocument();
    });
  });

  describe('State Management', () => {
    it('should maintain panel state when adding panels', async () => {
      render(<DraggablePanelTest />);

      const addButton = screen.getByText('Add New Panel');

      // Add a panel
      fireEvent.click(addButton);
      await waitFor(() => {
        expect(screen.getByText('New Default Panel')).toBeInTheDocument();
      });

      // Add another panel
      fireEvent.click(addButton);
      await waitFor(() => {
        expect(screen.getByText('New Elevated Panel')).toBeInTheDocument();
      });

      // Should still have original panels
      expect(screen.getByText('Chat Panel')).toBeInTheDocument();
      expect(screen.getByText('Command Panel')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Panel')).toBeInTheDocument();
    });

    it('should handle panel removal correctly', async () => {
      render(<DraggablePanelTest />);

      // Initially should have 3 panels
      expect(screen.getByTestId('draggable-panel-chat-panel')).toBeInTheDocument();
      expect(screen.getByTestId('draggable-panel-command-panel')).toBeInTheDocument();
      expect(screen.getByTestId('draggable-panel-eldritch-panel')).toBeInTheDocument();

      // Remove one panel
      const closeButtons = screen.getAllByTestId('close-button');
      fireEvent.click(closeButtons[0]);

      await waitFor(() => {
        expect(screen.queryByTestId('draggable-panel-chat-panel')).not.toBeInTheDocument();
        expect(screen.getByTestId('draggable-panel-command-panel')).toBeInTheDocument();
        expect(screen.getByTestId('draggable-panel-eldritch-panel')).toBeInTheDocument();
      });
    });

    it('should handle clearing all panels', async () => {
      render(<DraggablePanelTest />);

      const clearButton = screen.getByText('Clear All Panels');
      fireEvent.click(clearButton);

      await waitFor(() => {
        expect(screen.queryByTestId('draggable-panel-chat-panel')).not.toBeInTheDocument();
        expect(screen.queryByTestId('draggable-panel-command-panel')).not.toBeInTheDocument();
        expect(screen.queryByTestId('draggable-panel-eldritch-panel')).not.toBeInTheDocument();
      });

      // Should still have control panel and instructions
      expect(screen.getByTestId('mythos-panel-panel-controls')).toBeInTheDocument();
      expect(screen.getByTestId('mythos-panel-instructions')).toBeInTheDocument();
    });
  });
});
