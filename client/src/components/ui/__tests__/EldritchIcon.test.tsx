import { render } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { EldritchIcon, MythosIcons } from '../EldritchIcon';

// Mock lucide-react
vi.mock('lucide-react', () => {
  const createMockIcon = (name: string) => {
    const MockIcon = ({ size, className }: { size?: number; className?: string }) => (
      <svg data-testid={`icon-${name}`} data-size={size} className={className} />
    );
    MockIcon.displayName = name;
    return MockIcon;
  };

  return {
    MessageCircle: createMockIcon('MessageCircle'),
    ArrowUp: createMockIcon('ArrowUp'),
    Download: createMockIcon('Download'),
    Trash2: createMockIcon('Trash2'),
    Wifi: createMockIcon('Wifi'),
    Minus: createMockIcon('Minus'),
    Maximize: createMockIcon('Maximize'),
    Minimize2: createMockIcon('Minimize2'),
    X: createMockIcon('X'),
    Clock: createMockIcon('Clock'),
    FileText: createMockIcon('FileText'),
    Lightbulb: createMockIcon('Lightbulb'),
    Heart: createMockIcon('Heart'),
    Sparkles: createMockIcon('Sparkles'),
    Eye: createMockIcon('Eye'),
    EyeOff: createMockIcon('EyeOff'),
    Star: createMockIcon('Star'),
    Moon: createMockIcon('Moon'),
    Square: createMockIcon('Square'),
    Play: createMockIcon('Play'),
    Settings: createMockIcon('Settings'),
    Layout: createMockIcon('Layout'),
    RotateCw: createMockIcon('RotateCw'),
    HelpCircle: createMockIcon('HelpCircle'),
    BarChart3: createMockIcon('BarChart3'),
    Search: createMockIcon('Search'),
    Package: createMockIcon('Package'),
    User: createMockIcon('User'),
    ArrowRight: createMockIcon('ArrowRight'),
    WifiOff: createMockIcon('WifiOff'),
    Loader2: createMockIcon('Loader2'),
    Sword: createMockIcon('Sword'),
    Home: createMockIcon('Home'),
    Skull: createMockIcon('Skull'),
    Globe: createMockIcon('Globe'),
    MapPin: createMockIcon('MapPin'),
    MessageSquare: createMockIcon('MessageSquare'),
    Users: createMockIcon('Users'),
    Megaphone: createMockIcon('Megaphone'),
    CircleDot: createMockIcon('CircleDot'),
  };
});

describe('EldritchIcon', () => {
  describe('Basic rendering', () => {
    it('should render an icon with default props', () => {
      const { container } = render(<EldritchIcon name="chat" />);
      const icon = container.querySelector('svg');
      expect(icon).toBeInTheDocument();
      expect(icon).toHaveAttribute('data-size', '16');
    });

    it('should render with custom size', () => {
      const { container } = render(<EldritchIcon name="chat" size={24} />);
      const icon = container.querySelector('svg');
      expect(icon).toHaveAttribute('data-size', '24');
    });

    it('should render with custom className', () => {
      const { container } = render(<EldritchIcon name="chat" className="custom-class" />);
      const icon = container.querySelector('svg');
      expect(icon).toHaveClass('custom-class');
    });
  });

  describe('Icon variants', () => {
    it('should apply primary variant classes', () => {
      const { container } = render(<EldritchIcon name="chat" variant="primary" />);
      const icon = container.querySelector('svg');
      expect(icon).toHaveClass('text-mythos-terminal-primary');
    });

    it('should apply secondary variant classes', () => {
      const { container } = render(<EldritchIcon name="chat" variant="secondary" />);
      const icon = container.querySelector('svg');
      expect(icon).toHaveClass('text-mythos-terminal-secondary');
    });

    it('should apply warning variant classes', () => {
      const { container } = render(<EldritchIcon name="chat" variant="warning" />);
      const icon = container.querySelector('svg');
      expect(icon).toHaveClass('text-mythos-terminal-warning');
    });

    it('should apply error variant classes', () => {
      const { container } = render(<EldritchIcon name="chat" variant="error" />);
      const icon = container.querySelector('svg');
      expect(icon).toHaveClass('text-mythos-terminal-error');
    });

    it('should apply success variant classes', () => {
      const { container } = render(<EldritchIcon name="chat" variant="success" />);
      const icon = container.querySelector('svg');
      expect(icon).toHaveClass('text-mythos-terminal-success');
    });
  });

  describe('Icon mapping', () => {
    it('should render correct icon for chat', () => {
      const { container } = render(<EldritchIcon name="chat" />);
      const icon = container.querySelector('[data-testid="icon-MessageCircle"]');
      expect(icon).toBeInTheDocument();
    });

    it('should render correct icon for move', () => {
      const { container } = render(<EldritchIcon name="move" />);
      const icon = container.querySelector('[data-testid="icon-ArrowUp"]');
      expect(icon).toBeInTheDocument();
    });

    it('should render correct icon for download', () => {
      const { container } = render(<EldritchIcon name="download" />);
      const icon = container.querySelector('[data-testid="icon-Download"]');
      expect(icon).toBeInTheDocument();
    });

    it('should render correct icon for help', () => {
      const { container } = render(<EldritchIcon name="help" />);
      const icon = container.querySelector('[data-testid="icon-HelpCircle"]');
      expect(icon).toBeInTheDocument();
    });

    it('should render correct icon for portal', () => {
      const { container } = render(<EldritchIcon name="portal" />);
      const icon = container.querySelector('[data-testid="icon-CircleDot"]');
      expect(icon).toBeInTheDocument();
    });
  });

  describe('MythosIcons constant', () => {
    it('should have all expected icon names', () => {
      expect(MythosIcons.chat).toBe('chat');
      expect(MythosIcons.move).toBe('move');
      expect(MythosIcons.download).toBe('download');
      expect(MythosIcons.help).toBe('help');
      expect(MythosIcons.portal).toBe('portal');
    });

    it('should have all icon names as string literals', () => {
      Object.values(MythosIcons).forEach(iconName => {
        expect(typeof iconName).toBe('string');
        expect(iconName.length).toBeGreaterThan(0);
      });
    });
  });

  describe('Combined props', () => {
    it('should combine variant, size, and className correctly', () => {
      const { container } = render(<EldritchIcon name="chat" variant="error" size={32} className="my-custom-class" />);
      const icon = container.querySelector('svg');
      expect(icon).toHaveClass('text-mythos-terminal-error');
      expect(icon).toHaveClass('my-custom-class');
      expect(icon).toHaveAttribute('data-size', '32');
    });
  });
});
